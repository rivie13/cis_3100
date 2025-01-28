from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import pandas as pd
import joblib

def train_model(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Split the data into features and labels
    X = data['content']  # Assuming 'content' is the column with email text
    y = data['label']    # Assuming 'label' is the column with spam (1) or not spam (0)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline that combines CountVectorizer and Logistic Regression
    model = make_pipeline(CountVectorizer(), LogisticRegression())

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(model, 'spam_classifier_model.pkl')

if __name__ == "__main__":
    train_model('../data/emails.csv')  # Adjust the path as necessary