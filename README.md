# Project

Aegis Backend is a Python-based backend system designed to support phishing and smishing detection through a combination of machine learning models, lightweight web interfaces, and utility scripts. The repository includes training and evaluation tooling, pre-trained models and vectorizers, and simple web pages for demonstration.

Key components include:
- Backend logic and entry points (app.py and Smishing/app.py)
- Training and explainability helpers (train.py, explain.py)
- Pre-trained models and feature data (e.g., catboost_phishing_model.pkl, phishing_rf_model.pkl, smishing_model.pkl, vectorizers, and feature_columns.pkl)
- Lightweight web templates for quick demos (templates/index.html, templates/phishing.html, templates/smishing.html)
- Setup verification and startup utilities (verify_setup.py, startup.sh)
- A dedicated directory for experimental/model migrations (new model/)

This README describes the project structure, installation steps, usage guidance, and the data/models included in the repository.

The repository is organized to separate core server logic, ML assets, web templates, and model experimentation. A non-exhaustive map:
- Root: app.py, verify_setup.py, templates/, requirements.txt, startup.sh, visualize.py
- Smishing/: backend logic and data specific to smishing/phishing tasks (Smishing/app.py, Smishing/train.py, Smishing/vectorizer.pkl, Smishing/model.pkl, Smishing/spam.csv, Smishing/nltk.txt)
- New model/: experimental/model migration area (new model/Model/, new model/explain.py, new model/feature_extractor.py, new model/predict.py, new model/visualize.py, new model/requirements.txt)
- Models/Data: catboost_phishing_model.pkl, phishing_rf_model.pkl, smishing_model.pkl, shap_background.pkl, feature_columns.pkl, vectorizer.pkl, etc.
- Templates: index.html, phishing.html, smishing.html under templates/

This structure supports quick demos and experimentation while keeping production-like server code in a central place.

Install dependencies and prepare a local environment:
- Create and activate a virtual environment
  - macOS/Linux: python -m venv venv && source venv/bin/activate
  - Windows: python -m venv venv && venv\Scripts\activate
- Install root dependencies
  - pip install -r requirements.txt
- Install model-related dependencies (if separate requirements are used)
  - pip install -r new model/requirements.txt
- Optional: verify setup to ensure tools and paths are correct
  - python verify_setup.py

Run and interact with the backend:
- Basic server run
  - python app.py
- Alternative startup script
  - bash startup.sh
- Verify environment before running (optional but recommended)
  - python verify_setup.py
- Access the web interface or API endpoints as implemented by the app (default port may vary, commonly http://localhost:5000)

The repository includes templates for quick demo pages and a simple server for demonstration purposes.

This section catalogs the pre-trained models, vectorizers, and supporting data assets included in the repo. These artifacts enable quick inference and experimentation without retraining from scratch:
- catboost_phishing_model.pkl
- phishing_rf_model.pkl
- smishing_model.pkl
- Smishing/vectorizer.pkl
- vectorizer.pkl
- feature_columns.pkl
- shap_background.pkl
- new model artifacts in new model/ (e.g., new model/Model/catboost_phishing_model.pkl, new model/Model/shap_background.pkl, etc.)

Note: Some items are placed under a dedicated new-model directory to distinguish experimental artifacts from production-ready assets.

Model training and explanation utilities are provided to support experimentation and model introspection:
- train.py: training workflow and data handling
- explain.py: baseline explanations or feature importances
- new model/explain.py, new model/feature_extractor.py, new model/predict.py, new model/visualize.py: additional or migrated tooling for the experimental model suite

These scripts enable iterative development and evaluation of models beyond the initial production assets.

The repository includes simple HTML templates to demonstrate the models via a minimal web interface:
- templates/index.html
- templates/phishing.html
- templates/smishing.html

These pages provide lightweight front-ends to showcase model inferences or demo routes.

Contributions are welcome. If you plan to contribute, consider:
- Keeping changes isolated to new features or fixes
- Updating documentation and usage notes as needed
- Adding tests or validation scripts where feasible

For quick local testing, you can rely on the provided scripts (verify_setup.py, app.py, startup.sh) and the demo templates to exercise the backend.

This project is provided for local development and experimentation. The repository contains various ML artifacts and utility scripts. Users may apply their preferred license when distributing derivatives or deploying in production environments.
