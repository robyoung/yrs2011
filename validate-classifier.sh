#!/bin/bash

# Options to try:
# --ngrams 2 - including multi token features such as (not, happy) - NB. can only change this for validation, the classifier needs to support it.
# --classifier DecisionTree - trying out different classification algorithms, different ones have different strengths
# --filter-stopwords english - remove stopwords before classifying - NB. can only change this for validation, the classifier needs to support it.

# Options to try but not spend too much time on yet:
# --max_feats 1000 - only use the 1000 most 'useful' features
# --min_score 3 - only use features with a score greater than 3
python nltk-trainer/train_classifier.py data/$1 --classifier NaiveBayes --cross-fold 10