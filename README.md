# Purpose
This package includes source code of similar keyword model training. It includes 3 models which are pre-trained word2vec model, word2vec model training, word2vecf model training.

# Deployment
After cloning source code to the machine, you can open notebooks for **word2vec** and **word2vecf** model training pipeline. 

# Usage
It includes data processing, model training and evaluation. Given raw data, it goes through the standard data processing step. After that, you can either use pre-trained word2vec or training a new model from word2vec or word2vecf model architecture. Finally, several evaluation metrics are implemented for different scenarios. 

# Requirements and Dependencies
Use the following command to install dependency libraries.
- pip install -r requirements.txt

# System Architecture
N/A.

# Codebase Organization
**keywordsforward**
- processing: Data processing step for model training/ inference.
- model: Includes 3 models which are pre-trained word2vec, word2vec model training and word2vecf model training.
- evaluation: Includes 3 evaluation methods which are token match, spearman correlation and token similarity.
- util: Common function or utils.

**notebooks**
2 models (word2vec and word2vecf) training pipeline

**scripts**
- evaluation: Packed script for model evaluation.
- processing: Packed script for data processing.
- training: Packed script for models (word2vec and word2vecf) training.
