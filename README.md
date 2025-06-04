# 🎬 Sentiment Analysis on IMDB Reviews

This project classifies movie reviews as positive or negative using a custom feedforward neural network built in PyTorch. It processes 50,000 IMDB reviews through tokenization, filtering, and vectorization.

---

## 📁 Project Structure

```
sentiment_analysis/
├── model.ipynb            # Model definition, training, and evaluation
├── tokenizing.ipynb       # Data extraction and tokenization
├── data/                  # Contains train/test CSV data
├── word_counts.json       # Raw word frequency dictionary
├── final_tokens.json      # Filtered and cleaned token list
├── model.pth              # Trained PyTorch model weights
```

---

## ⚙️ How to Run

1. **Extract & Process Data**
   - Place `aclImdb_v1.tar.gz` in the root directory.
   - Run `tokenizing.ipynb` to extract text, count words, and save cleaned tokens to JSON.

2. **Train Model**
   - Make sure `data/` contains the `.csv.gzip` files.
   - Run `model.ipynb` to split data, train the model, and save it as `model.pth`.

---

## 🧠 Model Architecture

- Fully connected feedforward network:
  - Input layer → Linear(256) → ReLU → BatchNorm
  - → Linear(512) → Dropout(0.5) → ReLU → BatchNorm
  - → Linear(256) → ReLU → BatchNorm
  - → Output layer → Sigmoid

---

## 🧪 Notes

- Uses token frequency vectors (not word embeddings).
- Negative word combinations (e.g., `not_good`) are handled explicitly.
- Stopwords, HTML tags, and generic movie terms are filtered out.
