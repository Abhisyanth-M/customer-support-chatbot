import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle
import numpy as np

# Sample training data (customer support questions)
train_data = {
    'text': [
        'where is my order', 'track my package', 'order status', 'shipping time', 'delivery date',
        'cancel my order', 'how to cancel', 'stop my order', 'dont want order',
        'return item', 'refund request', 'money back', 'exchange product',
        'reset password', 'forgot password', 'change password', 'login problem',
        'account help', 'profile issue', 'my account'
    ] * 50,  # Repeat 50x = 1000 training examples
    
    'intent': [
        'track_order', 'track_order', 'track_order', 'track_order', 'track_order',
        'cancel_order', 'cancel_order', 'cancel_order', 'cancel_order',
        'return_refund', 'return_refund', 'return_refund', 'return_refund',
        'password_reset', 'password_reset', 'password_reset', 'password_reset',
        'account_help', 'account_help', 'account_help'
    ] * 50
}

# Create table from data
df = pd.DataFrame(train_data)

# Build ML Pipeline (text → numbers → predict intent)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=100, stop_words='english')),
    ('clf', LogisticRegression())
])

# TRAIN the ML model
pipeline.fit(df['text'], df['intent'])

# SAVE trained brain to file
pickle.dump(pipeline, open('chatbot_model.pkl', 'wb'))

print("✅ ML Model trained & saved!")
print("🧠 Your chatbot brain is ready in 'chatbot_model.pkl'")