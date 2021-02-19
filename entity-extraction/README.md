# Entity and Relation Modeling

## 💾 `data/`

Contains translated menu data sets and results from previous semester of project work.  Also contains the resources for ongoing NER and relation extraction model training.

## 🐡 `seafood_model/`

Houses the code neccessary to load the custom spaCy model.

### Test Results

- Overall Model F-score: 77.329
- Label scores
  - `SEAFOOD`: 75.096
  - `SIDE`: 78.601
  - `METHOD`: 78.543
  - `LOCATION`: 84.848

These results will likely improve once time permits for additional model training.

## 🐍 Other Files

- `exploration.ipynb`: Initial analysis of translated menu data and data processing for model training.
