def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def clean_text(text):
    import re
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip()

def preprocess_data(data):
    data['cleaned_text'] = data['content'].apply(clean_text)
    return data

def tokenize_text(data):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['cleaned_text'])
    return X, vectorizer

def preprocess(file_path):
    data = load_data(file_path)
    data = preprocess_data(data)
    X, vectorizer = tokenize_text(data)
    y = data['label']
    return X, y, vectorizer