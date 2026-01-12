Neville’s Remembrall Vault 🔐

A magical password vault inspired by Harry Potter, built with FastAPI (Python) and a sleek wizard-themed frontend. Store your passwords for different “common rooms” with hints, view them in a live proclamation, and clear all when needed.

Perfect for learning FastAPI, frontend-backend integration, and creating a polished interactive web app.

Features ✨

Add Passwords with Location, Hint, and Password

View Hints / Proclamation in real-time

Clear All Passwords with a single click

Persistent Storage in vault.json

Automatic Input Clearing and UI Notifications

Wizard-themed UI with hover effects, scrollable proclamation, and responsive design

Tech Stack 🛠️

Backend: Python 3 + FastAPI

Frontend: HTML, CSS, JavaScript

Storage: JSON file (vault.json)

Getting Started 🚀
Prerequisites

Python 3.10+ installed

Git (optional)

Installation & Run

Clone the repository (or download files):

git clone https://github.com/<your-username>/neville-remembrall.git
cd neville-remembrall


Create a virtual environment and activate it:

python -m venv venv
.\venv\Scripts\activate


Install dependencies:

pip install fastapi uvicorn


Run the server:

python -m uvicorn main:app --reload


Open the app in your browser:

http://127.0.0.1:8000

Folder Structure 📂
neville-remembrall/
│
├─ main.py          # FastAPI backend
├─ index.html       # Frontend UI
├─ vault.json       # Stores passwords (auto-created)
├─ README.md        # This file

Usage 🧙‍♂️

Enter Location, Hint, and Password, then click Store

See your hints appear instantly under Proclamation

Click Refresh to reload

Click Clear All Passwords to reset vault (confirmation required)

Notes 💡

The vault is stored in a simple JSON file for simplicity.

Perfect for small-scale personal use or learning projects.

Can be upgraded to Supabase or a database for production-level persistence.

License

This project is MIT Licensed — feel free to modify, learn, and use freely.
