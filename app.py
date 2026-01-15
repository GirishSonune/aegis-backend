import os
import sys

# Ensure we are running from the backend directory so relative paths work
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import predict  # Imports from backend/predict.py

# -------- NLTK Setup ----------
try:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print(f"Warning: NLTK download failed: {e}")

app = Flask(__name__)
# Configure CORS to allow requests from frontend
CORS(app, resources={r"/*": {"origins": "*"}})

# -------- Feature Map for UI ----------
FEATURE_MAP = {
    'length_url': "URL Length",
    'length_hostname': "Hostname Length",
    'ip': "Contains IP",
    'nb_dots': "Dots Count",
    'nb_hyphens': "Hyphens Count",
    'nb_at': "@ Symbol Count",
    'nb_qm': "? Symbol Count",
    'nb_and': "& Symbol Count",
    'nb_eq': "= Symbol Count",
    'nb_underscore': "_ Symbol Count",
    'nb_slash': "/ Symbol Count",
    'nb_percent': "% Symbol Count",
    'nb_colon': ": Symbol Count",
    'nb_www': "Contains www",
    'nb_com': "Contains .com",
    'nb_dslash': "Double Slash Count",
    'https_token': "HTTPS Token",
    'ratio_digits_url': "Ratio Digits (URL)",
    'ratio_digits_host': "Ratio Digits (Host)",
    'punycode': "Punycode",
    'port': "Port Defined",
    'tld_in_path': "TLD in Path",
    'tld_in_subdomain': "TLD in Subdomain",
    'abnormal_subdomain': "Abnormal Subdomain",
    'nb_subdomains': "Subdomain Count",
    'prefix_suffix': "Prefix/Suffix -",
    'random_domain': "Random Domain",
    'shortening_service': "Shortening Service",
    'path_extension': "Path Extension",
    'char_repeat': "Char Repeat",
    'phish_hints': "Phishing Hints"
}


# -------- Smishing Model / Logic ----------
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load Smishing models
try:
    tfidf = pickle.load(open('smishing_vectorizer.pkl', 'rb'))
    smishing_model = pickle.load(open('smishing_model.pkl', 'rb'))
    SMISHING_AVAILABLE = True
except Exception as e:
    print(f"Error loading smishing models: {e}")
    SMISHING_AVAILABLE = False


# -------- Routes ----------

# 1. Landing Page
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# 2. Phishing Page
@app.route("/phishing", methods=["GET"])
def phishing_page():
    return render_template("phishing.html", FEATURE_MAP=FEATURE_MAP)

# 3. Phishing UI Prediction
@app.route("/predict_ui", methods=["POST"])
def predict_ui():
    url = request.form.get("url", "").strip()
    if not url:
        return render_template("phishing.html", error="Please enter a URL", FEATURE_MAP=FEATURE_MAP)

    try:
        result = predict.predict_with_explain(url)
        
        # Mapping result
        prediction = result["prediction"] # "PHISHING" or "SAFE"
        if prediction == "SAFE":
            prediction = "Legitimate"
        else:
            prediction = "Phishing"

        # Parse shap explanation (it's text in the result, but we might want values for the chart)
        # predict_with_explain returns 'shap_explanation' as text.
        # But for the chart, we need raw values. 
        # Modification needed: We need access to raw shap values if we want to plot them.
        # predict.py's predict_with_explain currently returns text. 
        # Let's see if we can get raw values or if we should rely on the text list.
        # The new 'phishing.html' expects 'shap_values' as a dict {feature: value} for the chart.
        
        # We might need to call lower-level functions or parse the text if we can't change predict.py easily.
        # OR better: Update predict.py to return raw values too. 
        # For now, let's look at what predict_with_explain returns.
        # It calls: shap_vals = shap_explanation(explainer, features)
        # shap_vals is the raw array/list.
        # Then shap_to_text converts it.
        # It currently doesn't return the raw dictionary.
        
        # Workaround: Re-implement some logic here or update predict.py. 
        # I'll update predict.py to return raw values as well in next step if possible, 
        # but for now let's just pass empty dict if not available, or try to hack it.
        
        # Actually, let's just update `app.py` to be robust and maybe skip the chart if data is missing, 
        # OR better, since I am rewriting `app.py`, I can import `extract_features`, `model`, `explainer` here or from `predict` 
        # and do what's needed. BUT `predict.py` encapsulates a lot.
        
        # Let's check predict.py content again.
        # It creates explainer locally inside `predict_with_explain`.
        
        # I will assume for now I will rely on the text explanation for the UI list, 
        # and maybe disable the chart or update predict.py later.
        # But the user asked for "separate files", not "broken chart".
        
        # Quick fix: I will assume `predict.predict_with_explain` returns `shap_values` dict too?
        # No, I saw the code. It returns `shap_explanation` (text).
        
        # I will update `app.py` to try to use `predict.shap_explanation` text for the table, 
        # and maybe omit the chart for now or mock it? 
        # No, I should fix it properly. 
        
        # I will Modify `backend/predict.py` to return raw SHAP values too.
        
        return render_template(
            "phishing.html",
            url=url,
            prediction=prediction,
            confidence=f"{result['confidence']*100:.2f}%",
            features=predict.extract_features(url).iloc[0].to_dict(), 
            shap_values=result.get("shap_values", {}),
            FEATURE_MAP=FEATURE_MAP
        )

    except Exception as e:
        return render_template("phishing.html", error=f"Error: {e}", FEATURE_MAP=FEATURE_MAP)

# 4. Smishing Page
@app.route("/smishing", methods=["GET"])
def smishing_page():
    return render_template("smishing.html")

# 5. Smishing UI Prediction
@app.route("/smishing_ui", methods=["POST"])
def smishing_ui():
    if not SMISHING_AVAILABLE:
        return render_template("smishing.html", result="Error: Model not loaded")

    message = request.form.get("message", "").strip()
    if not message:
        return render_template("smishing.html", message=message, result="Error: No message")

    try:
        transformed_sms = transform_text(message)
        vector_input = tfidf.transform([transformed_sms])
        prediction = smishing_model.predict(vector_input)[0]
        result = "Smishing" if prediction == 1 else "Legitimate"
        
        return render_template("smishing.html", message=message, result=result)
    except Exception as e:
         return render_template("smishing.html", message=message, result=f"Error: {e}")


# -------- API Routes (Keep for extension/external) ----------
@app.route("/api/predict", methods=["POST"])
def api_predict_url():
    data = request.get_json() or {}
    url = data.get("url", "").strip()
    if not url:
        return jsonify({"error": "no url provided"}), 400

    try:
        result = predict.predict_with_explain(url)
        pred_label = result["prediction"].lower() # "phishing" or "safe"
        if pred_label == "safe":
            pred_label = "legitimate"
            
        return jsonify({
            "url": url,
            "prediction": pred_label,
            "riskScore": result["confidence"] * 100,
            "risk_level": result["risk_level"],
            "riskReasons": [result["shap_explanation"]], # Text
            "shap_values": {} # Placeholder
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/detect_smishing", methods=["POST"])
def api_predict_smishing():
    if not SMISHING_AVAILABLE:
        return jsonify({"error": "Smishing functionality unavailable"}), 503

    data = request.get_json() or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "no message provided"}), 400

    try:
        transformed_sms = transform_text(message)
        vector_input = tfidf.transform([transformed_sms])
        prediction = smishing_model.predict(vector_input)[0]
        result_label = "Smishing" if prediction == 1 else "Legitimate"
        return jsonify({
            "message": message,
            "prediction": result_label,
            "is_smishing": bool(prediction == 1)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
