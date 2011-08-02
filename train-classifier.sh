#!/bin/bash

python nltk-trainer/train_classifier.py data/$1 --filename data/classifiers/$1.pickle --classifier NaiveBayes