import os
import base64
import requests
import sqlite3
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

SCOPES = "user-read-currently-playing user-read-playback-state"

def get_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "state": "testuser"  # ileride kullanıcıdan alacağımız kullanıcı adı
    }
    return "https://accounts.spotify.com/authorize?" + urlencode(params)

def get_tokens(code):
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

def refresh_token(refresh_token):
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

# Basit SQLite ile token kaydetme
def save_tokens(username, tokens):
    conn = sqlite3.connect('tokens.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
            username TEXT PRIMARY KEY,
            access_token TEXT,
            refresh_token TEXT
        )
    ''')
    cursor.execute('REPLACE INTO tokens (username, access_token, refresh_token) VALUES (?, ?, ?)',
                   (username, tokens['access_token'], tokens['refresh_token']))
    conn.commit()
    conn.close()

def get_user_tokens(username):
    conn = sqlite3.connect('tokens.db')
    cursor = conn.cursor()
    cursor.execute('SELECT access_token, refresh_token FROM tokens WHERE username=?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {'access_token': row[0], 'refresh_token': row[1]}
    return None
