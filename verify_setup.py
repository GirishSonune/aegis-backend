import os
import sys

# Set CWD to backend/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

print(f"Running verification in {BASE_DIR}")

try:
    import app
    print("Successfully imported app.")
    
    # Check if models are loaded
    if app.SMISHING_AVAILABLE:
        print("Smishing models loaded successfully.")
    else:
        print("Smishing models FAILED to load.")

    # Check predict module
    try:
        import predict
        import joblib
        # Try loading new models
        model = joblib.load(predict.MODEL_PATH)
        print("New phishing model loaded successfully.")
    except Exception as e:
        print(f"Failed to load new phishing models: {e}")

except Exception as e:
    print(f"Verification failed: {e}")
