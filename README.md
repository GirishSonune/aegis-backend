# Project

- This repository contains a Python-based project that combines phishing and smishing detection with a web interface and supporting utilities.
- It includes a root application (app.py) along with verification and startup scripts, as well as HTML templates used by the UI.
- The project ships with pre-trained models and feature extractors housed in a Smishing directory and a separate new model folder containing updated artifacts.
- Multiple scripts handle training, prediction, explanation, and visualization, along with utilities to verify the setup.
- Templates for the UI are provided in the templates directory (and there is a Smishing subdirectory with its own templates).
- Several pickle models and feature files are included to enable phishing and smishing predictions.

- Top-level files:
  - app.py, predict.py, explain.py, visualize.py, verify_setup.py, startup.sh, templates/
  - requirements.txt
- Directories containing ML artifacts:
  - Smishing/ (model.pkl, vectorizer.pkl, nltk.txt, spam.csv, train.py, templates/, etc.)
  - new model/ (Model/, read me, README.md, explain.py, feature_extractor.py, predict.py, requirements.txt, visualize.py, etc.)
- Templates and UI:
  - templates/index.html, templates/phishing.html, templates/smishing.html
- Models and features:
  - phishing_rf_model.pkl, catboost_phishing_model.pkl, Smishing/model.pkl, Smishing/vectorizer.pkl, smishing_model.pkl, smishing_vectorizer.pkl
- Additional utilities:
  - explain.py, visualize.py, verify_setup.py

- Ensure Python is installed on your system (preferably a supported Python 3.x environment).
- Install dependencies from the repository requirements:
  - pip install -r requirements.txt
- If you plan to work with the updated models in the new model folder, install its dependencies as well:
  - pip install -r new model/requirements.txt
- Make startup script executable and (optionally) run it to initialize the environment:
  - chmod +x startup.sh
  - ./startup.sh
- The project includes multiple components; the files listed under ML artifacts (Smishing/ and new model/) are loaded by the application as needed.

- Start the main entry point to run the web application:
  - python app.py
- If you want to examine the Smishing-specific component, there is a Smishing/app.py entry point as well:
  - python Smishing/app.py
- The UI relies on templates located in the templates directory (index.html, phishing.html, smishing.html).

- The repository ships with pre-trained models and feature extractors used for phishing and smishing detection:
  - Smishing/model.pkl, Smishing/vectorizer.pkl, Smishing/nltk.txt, Smishing/spam.csv, Smishing/train.py
  - phishing_rf_model.pkl, catboost_phishing_model.pkl
  - smishing_model.pkl, smishing_vectorizer.pkl
- Updated models and related artifacts are available under the new model/ directory (e.g., new model/Model/catboost_phishing_model.pkl, new model/Model/feature_columns.pkl, new model/Model/shap_background.pkl).
- Feature extractor and explanation utilities are present (feature_extractor.py, explain.py, new model/feature_extractor.py, new model/explain.py).

- HTML templates used by the web interface are located in the templates directory:
  - templates/index.html
  - templates/phishing.html
  - templates/smishing.html
- The Smishing-specific templates are also present under Smishing/templates/index.html.

- Prediction, explanation, and visualization utilities are provided:
  - predict.py, explain.py, visualize.py (root)
  - new model/predict.py, new model/explain.py, new model/visualize.py
- Setup verification is handled by verify_setup.py.

- The project includes multiple pre-trained artifacts in pickle format (e.g., model.pkl, vectorizer.pkl, catboost_phishing_model.pkl). Handle these artifacts in a secure environment.
- Additional model and utility files exist under the new model/ directory for updated workflows.
- UI relies on HTML templates for phishing and smishing interfaces.
