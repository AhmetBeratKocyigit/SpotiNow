from flask import Flask, redirect, request, jsonify
from auth import get_auth_url, get_tokens, save_tokens
from spotify import get_current_track
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def home():
    return 'Spotinow API Çalışıyor 🚀'

@app.route('/login')
def login():
    return redirect(get_auth_url())

@app.route('/callback')
def callback():
    code = request.args.get('code')
    username = request.args.get('state')  # kullanıcı adı buradan alınabilir
    tokens = get_tokens(code)
    save_tokens(username, tokens)
    return f"{username} için bağlantı tamamlandı!"

@app.route('/track/<username>')
def track(username):
    track_info = get_current_track(username)
    if track_info:
        return jsonify(track_info)
    return jsonify({'error': 'Kullanıcı bağlı değil ya da şu an dinlemiyor.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
