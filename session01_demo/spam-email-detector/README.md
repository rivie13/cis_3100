# Spam Email Detector

This project is a binary classification machine learning model designed to detect spam emails based on their content. The model takes email text as input and returns the probability of the email being spam.

## Project Structure

```
spam-email-detector
├── src
│   ├── data_preprocessing.py       # Functions for loading and preprocessing email data
│   ├── model_training.py            # Training the binary classification model
│   ├── model_evaluation.py          # Evaluating the model's performance
│   └── predict.py                   # Prediction logic for spam detection
├── data
│   └── emails.csv                   # Dataset of emails for training and testing
├── notebooks
│   └── exploratory_data_analysis.ipynb # Jupyter notebook for exploratory data analysis
├── requirements.txt                 # Python dependencies for the project
├── .gitignore                       # Files and directories to ignore by Git
└── README.md                        # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/spam-email-detector.git
   cd spam-email-detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Preprocess the email data using `data_preprocessing.py`.
2. Train the model using `model_training.py`.
3. Evaluate the model's performance with `model_evaluation.py`.
4. Use `predict.py` to input email content and get the probability of it being spam.

## License

This project is licensed under the MIT License.