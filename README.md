# Project

SMS Smishing and Phishing Detection Suite

A lightweight collection of scripts, models and a small web UI for classifying SMS messages as Smishing or Not Smishing, plus a separate set of tools and models for phishing detection. The work is organized into a primary Python/Flask app for quick testing, and a second “new model” folder containing additional explainability and modeling utilities.

What’s included (high level)
- A Flask-based web UI under Smishing/ for interactive classification.
- Pre-trained vectorizers and classifiers (for Smishing) in Smishing/vectorizer.pkl and Smishing/model.pkl.
- A separate phishing model and related artifacts at the root (phishing_rf_model.pkl and other assets).
- A larger set of model and training utilities in new model/, including explainability scripts and additional features.
- Datasets and templates used to drive and display results (templates/, Smishing/spam.csv, etc.).
- A conventional .gitignore to keep environment- and build-specific files out of version control.

Quick start

Prerequisites
- Python 3.x
- pip

Initial setup
- Install root dependencies:
  - pip install -r requirements.txt
- If you’ll run the Smishing web UI, also install the Smishing-specific requirements:
  - cd Smishing
  - pip install -r requirements.txt

Running the Smishing web UI
- Change to the Smishing directory and start the app:
  - cd Smishing
  - python app.py
- Open http://127.0.0.1:5000 in your browser.
- How it works at a glance:
  - The app loads a pre-trained vectorizer from vectorizer.pkl and a pre-trained model from model.pkl (both located in Smishing/).
  - It preprocesses input text, vectorizes it, and predicts Smishing vs Not Smishing.
  - NLTK data is downloaded programmatically at startup (punkt and stopwords).

Notes on data and models
- Smishing UI artifacts
  - Smishing/app.py (Flask app)
  - Smishing/vectorizer.pkl (vectorizer used by the Smishing model)
  - Smishing/model.pkl (classifier used by the Smishing model)
  - Smishing/spam.csv (example dataset content)
  - Smishing/templates/index.html (UI)
  - Smishing/templates/phishing.html and other templates for UI
  - Smishing/train.py, Smishing/learned artifacts and related files for model training
  - Smishing/nltk.txt and Smishing/nltk data handling in code
- Root-level phishing model
  - phishing_rf_model.pkl (random-forest based phishing model)
  - Additional artifacts as part of the phishing workflow
- New model folder (additional models and utilities)
  - new model/Model/ and related files (structure and scripts for alternative models)
  - new model/explain.py, new model/visualize.py, new model/predict.py (explanation, visualization and prediction helpers)
  - new model/feature_extractor.py, new model/feature_columns.pkl (feature extraction and feature space)
  - new model/README.md and related readme/help content
  - new model/shap_background.pkl (SHAP background data for explainability)
- Top-level app.py (alternative/auxiliary entry point)
  - Root app.py imports and uses a vectorizer and model as well, offering a separate quick-start path
- Resources and dependencies
  - Smishing/requirements.txt (specific dependencies for the Smishing app)
  - new model/requirements.txt (dependencies for the second-model workflow)
  - .gitignore (ignore patterns for common Python/virtualenv outputs)
  - Smishing/nltk.txt (minimal reference to NLTK resources)

Directory layout (quick map)
- Smishing/
  - app.py (Flask web UI for Smishing classification)
  - model.pkl, vectorizer.pkl (pre-trained Smishing model artifacts)
  - nltk.txt, templates/, spam.csv, train.py, etc. (data, training, and UI assets)
  - requirements.txt (Smishing-specific Python dependencies)
- new model/
  - explain.py, feature_extractor.py, predict.py, visualize.py (explainability, features, and predictions)
  - feature_columns.pkl, shap_background.pkl (model feature space and SHAP background)
  - Model/ (subfolders with additional model artifacts)
  - README.md (documentation for the new model suite)
  - requirements.txt (dependencies for the new model suite)
- root
  - app.py (alternative entry point)
  - phishing_rf_model.pkl (phishing model artifact)
  - catboost_phishing_model.pkl (additional model artifact, if present)
  - shap_background.pkl (SHAP background data for other models)
  - phishing-related data and templates
  - requirements.txt (root dependencies)
- templates/
  - index.html, phishing.html, smishing.html (UI templates)
- .gitignore
  - Ignores environment, caches, venvs, etc.

Model details (summary)
- Smishing
  - A small pipeline using a vectorizer and a classifier stored under Smishing/.
  - Primary UI at Smishing/app.py to input a message and receive a Smishing/Not Smishing result.
  - The training and data artifacts are included to reproduce or extend the model locally.
- Phishing
  - A dedicated binary classifier and related assets are included at root (phishing_rf_model.pkl, etc.).
  - The new model folder also contains an extended set of tools for experimentation and explainability with SHAP.

Usage notes
- The repository includes large binary artifacts (models and datasets). When cloning or pulling, ensure you have sufficient storage and bandwidth.
- For explainability and experimentation, explore new model/ to examine feature extractors and SHAP-based explanations, then adapt as needed for your data.

Contributing
- If you extend or replace models, keep the existing directory structure and document changes in the respective README files (Smishing/README.md, new model/README.md).
- Ensure any new requirements are added to the appropriate requirements.txt files to keep environment setup straightforward.

License
- See LICENSE (if present) for licensing information.

If you need a focused start guide for a specific component (Smishing UI, root phishing model, or the new model suite), I can tailor a step-by-step setup.
