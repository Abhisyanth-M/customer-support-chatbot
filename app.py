import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="AI Support Assistant", layout="centered")

USER_DB = "users.json"

# ---------- FILE INIT ----------
if not os.path.exists(USER_DB):
    with open(USER_DB, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- AI ----------
def get_ai_response(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"""
You are a customer support assistant.

RULES:
- Max 2 lines
- No explanations
- No "Here is", "Sure"
- Natural reply

User: {prompt}
""",
                "stream": False
            }
        )

        text = res.json()["response"].strip()

        # clean unwanted words
        bad_words = ["Here", "Sure", "Revised", "Answer:", "Response:"]
        for w in bad_words:
            if w.lower() in text.lower():
                text = text.split("\n")[-1]

        return "\n".join(text.split("\n")[:2])

    except:
        return "⚠️ AI not responding"

# ---------- AUTH ----------
def login(email, password):
    users = load_users()
    if email in users and users[email]["password"] == password:
        st.session_state.logged_in = True
        st.session_state.user = email
        st.session_state.chat = users[email].get("chat", [])
        return True
    return False

def signup(email, password):
    users = load_users()
    if email in users:
        return False
    users[email] = {"password": password, "chat": []}
    save_users(users)
    return True

def save_chat():
    users = load_users()
    users[st.session_state.user]["chat"] = st.session_state.chat
    save_users(users)

# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:
    st.title("Login / Signup")

    option = st.radio("", ["Login", "Signup"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Login":
        if st.button("Login"):
            if login(email, password):
                st.success("Login success")
                st.rerun()
            else:
                st.error("Invalid")

    else:
        if st.button("Signup"):
            if signup(email, password):
                st.success("Account created")
            else:
                st.error("User exists")

# ---------- MAIN APP ----------
else:
    st.title("AI Support Assistant")

    st.write(f"Logged in as: {st.session_state.user}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.chat = []
        st.rerun()

    if st.button("Clear Chat"):
        st.session_state.chat = []
        save_chat()
        st.rerun()

    # show chat
    for msg in st.session_state.chat:
        if msg["role"] == "user":
            st.write(f"You: {msg['content']}")
        else:
            st.write(f"Bot: {msg['content']}")

    # input
    user_input = st.text_input("Type message")

    if st.button("Send") and user_input:
        st.session_state.chat.append({"role": "user", "content": user_input})

        reply = get_ai_response(user_input)

        st.session_state.chat.append({"role": "bot", "content": reply})

        save_chat()
        st.rerun()