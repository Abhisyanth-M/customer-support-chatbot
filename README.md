# Customer Support Chatbot

A Machine Learning powered customer support chatbot that handles order tracking, cancellations, refunds, password resets and account help using intent classification.

## Live Demo
https://huggingface.co/spaces/Abhisyanth-M/customer-support-chatbot

## Problem Statement
Customer support teams spend most of their time answering the same repetitive questions repeatedly. This wastes time and increases operational costs for businesses.

## Solution
An ML-powered chatbot that automatically handles common customer queries, detects multiple intents in a single message, and dynamically looks up order details.

## Features
- Intent classification for 25+ customer support topics
- Unknown intent handler with proper fallback message
- Multi-intent detection for combined queries like "cancel and refund"
- Dynamic order lookup by order number with real address and status
- Help menu showing all supported topics
- Session state chat history

## Tech Stack
- Python
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit

## ML Model
- Algorithm: Logistic Regression
- Vectorization: TF-IDF
- Intents: 25+ customer support categories
- Accuracy: 92% on test queries

## How to Run Locally
```bash
git clone https://github.com/Abhisyanth-M/customer-support-chatbot
cd customer-support-chatbot
pip install -r requirements.txt
streamlit run app.py
```

## Limitations
- Scoped to customer support workflows only — order tracking, cancellations, refunds, password reset and account help
- Conversations outside this scope receive a fallback message
- Order database contains sample data only — not connected to a real backend

## GitHub
https://github.com/Abhisyanth-M/customer-support-chatbot
``
