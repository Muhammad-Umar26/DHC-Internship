---
title: News Topic Classifier
emoji: 📰
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.38.0    # adjust to your actual version
python_version: 3.11   # ⬅️ critical! use 3.11 or 3.12
app_file: app.py
pinned: false
---

# News Topic Classifier

This app uses a fine-tuned BERT model to classify news headlines into 4 categories: World, Sports, Business, and Sci/Tech.

**Performance on AG News test set:**
- Accuracy: ~94.75%
- F1 Score: ~94.75%

Enter a headline and click "Classify" to see the magic!