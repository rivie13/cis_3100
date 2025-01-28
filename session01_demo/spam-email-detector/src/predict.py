def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_email(email_content):
    import re
    from sklearn.feature_extraction.text import CountVectorizer

    # Basic text cleaning
    email_content = re.sub(r'\W', ' ', email_content)
    email_content = email_content.lower()
    email_content = email_content.split()

    # Load the vectorizer
    vectorizer = joblib.load('src/vectorizer.pkl')
    email_content = vectorizer.transform([' '.join(email_content)])
    
    return email_content

def predict_spam(email_content, model_path='src/spam_model.pkl'):
    model = load_model(model_path)
    processed_email = preprocess_email(email_content)
    probability = model.predict_proba(processed_email)[:, 1]
    return probability[0]  # Return the probability of being spam

# Example usage:
# email_content = "Congratulations! You've won a lottery!"
# print(predict_spam(email_content))