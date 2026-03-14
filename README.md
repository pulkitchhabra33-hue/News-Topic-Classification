# News Topic Classification using NLP and Deep Learning

This project builds an **automated News Topic Classification system** using **Natural Language Processing (NLP)** and **Deep Learning**.

The model predicts the category of a news headline among the following topics:

- 🌍 World
- ⚽ Sports
- 💰 Business
- 🤖 Sci/Tech

The system is deployed using **Streamlit**, allowing users to interactively classify news headlines.

---

# Project Overview

News websites generate thousands of articles daily. Automatically categorizing news articles helps organize content and improve information retrieval.

In this project, we build a **Deep Learning-based classifier** that learns patterns from news headlines and predicts the correct category.

---

# Model Architecture

The classification model uses the following architecture:

Embedding Layer  
→ Bidirectional LSTM  
→ Dropout  
→ Bidirectional LSTM  
→ Dense (ReLU)  
→ Dense (Softmax)

### Explanation

- **Embedding Layer** converts words into dense vectors.
- **Bidirectional LSTM** captures context from both directions in text.
- **Dropout** helps reduce overfitting.
- **Dense + Softmax** outputs the final class probabilities.

---

# Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- Natural Language Processing

---

# Model Performance

| Metric | Value |
|------|------|
| Test Accuracy | ~85% |

The model performs well for short news headlines and general news topics.

---

# Project Structure

News Topic Classification
│
├── app.py
├── news_classifier.h5
├── tokenizer.pkl
├── news_topic_classification.ipynb
├── requirements.txt
└── data/


---

# How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/pulkitchhabra33-hue/news-topic-classifier.git
cd news-topic-classifier
```

2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run app.py
4️⃣ Enter a news headline

Example:

NASA launches new satellite to study climate change

Prediction:

Sci/Tech
Example Predictions
Headline	Prediction
NASA discovers new exoplanet	Sci/Tech
Apple stock rises after earnings report	Business
Barcelona wins Champions League final	Sports
Russia launches missile strike on Ukraine	World
Future Improvements

Possible improvements include:

Using pre-trained embeddings (GloVe, Word2Vec)

Training with larger datasets

Implementing Transformer-based models like BERT

Deploying the model with Docker or cloud services

# Author

Pulkit Chhabra
Aspiring Data Scientist passionate about Machine Learning, NLP, and AI-driven applications.