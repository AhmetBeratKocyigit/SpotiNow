# SpotiNow

**Spotinow** is a web application that lets users display their currently playing track from Spotify on a personalized URL (e.g., `spotinow.com/ahmet`).  
Built with Python (backend) and HTML/CSS/JavaScript (frontend).

## 🎯 Features

- Connects to the Spotify API to fetch the currently playing track.  
- Provides a personalized public URL for each user (e.g., `spotinow.com/{username}`).  
- Displays track information in real‑time: track name, artist, album art, etc.  
- Simple, clean interface built with HTML, CSS & JavaScript.  
- Backend written in Python (Flask/Django—adjust if needed).  
- User authentication via Spotify OAuth.  
- Easy to deploy and customize for your brand or personal use.

## 🧩 Architecture

- **Backend**: Python (Flask or Django)  
  - Handles Spotify OAuth authentication.  
  - Provides API endpoints for frontend to get current track data.  
  - Manages user sessions and personalized URLs.  
- **Frontend**: HTML / CSS / JavaScript  
  - Responsive UI to display track details.  
  - Connects to backend API to pull data and update UI live.  
- **Database / Storage**  
  - Stores user tokens, refresh tokens (e.g., `tokens.db`).  
  - Tracks user metadata (username, custom URL slug, linked Spotify account).  

## 🚀 Getting Started

### Prerequisites

- Python 3.x  
- A Spotify Developer account and registered application (Client ID & Secret)  
- A web server or hosting environment (can be local for testing)  
- Optional: domain name for the personalized URLs (e.g., spotinow.com)

### Installation

```bash
git clone https://github.com/AhmetBeratKocyigit/SpotiNow.git
cd SpotiNow
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

1. Rename `.env.example` to `.env` (or create a config file) and set:  
   ```
   SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID  
   SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET  
   REDIRECT_URI=YOUR_REDIRECT_URI  
   ```

2. (If applicable) Set up the database (e.g., SQLite) and apply migrations.

3. Run the app:  
   ```bash
   python app.py    # or manage.py runserver if Django
   ```

4. Visit `http://localhost:5000` (or your server address) and register/login via Spotify.

### Usage

- After linking your Spotify account, you’ll receive a unique URL like `spotinow.com/yourname`.  
- When you listen to a track on Spotify, the page will update in near‑real time to show:  
  - Track title  
  - Artist  
  - Album cover  
  - Link to Spotify  
- You can share this URL on social media, your website, or bio.

## 🛠 Customization

- Update the frontend styles (CSS) to match your brand or theme.  
- Add features like:  
  - Dark mode toggle  
  - Track history carousel  
  - Embeddable widget for blogs  
- For self‑hosting: Configure NGINX/Apache, SSL (HTTPS), and custom domain routing.

## 🧭 Roadmap / Future Improvements

- Support multiple streaming services (e.g., YouTube Music, Apple Music).  
- Mobile app version (React Native or Flutter).  
- Analytics dashboard: how many people visited your URL, top tracks.  
- Webhook support: notify when a track changes.  
- Premium features: custom URL aliasing, themes, privacy settings.

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your‑feature`).  
3. Make your changes, commit (`git commit -m "Add awesome feature"`).  
4. Push to your branch and open a Pull Request.  
5. Ensure code is well‑formatted and documented.

Please read CONTRIBUTING.md (if available) for guidelines.

## 📝 License

This project is licensed under the **MIT License** (or whichever you choose).  
See the LICENSE file for details.

