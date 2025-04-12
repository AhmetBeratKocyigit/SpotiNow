import requests
from auth import get_user_tokens, refresh_token, save_tokens

def get_current_track(username):
    tokens = get_user_tokens(username)
    if not tokens:
        return None

    access_token = tokens['access_token']
    refresh = tokens['refresh_token']

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)

    # Token expired veya geçersizse yeniden deneyelim
    if response.status_code == 401:
        new_access_token = refresh_token(refresh)
        tokens['access_token'] = new_access_token
        save_tokens(username, tokens)
        headers["Authorization"] = f"Bearer {new_access_token}"
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)

    if response.status_code == 204 or not response.ok:
        return None

    data = response.json()
    item = data.get("item")
    if not item:
        return None

    track_name = item["name"]
    artists = ", ".join([artist["name"] for artist in item["artists"]])
    album_image = item["album"]["images"][0]["url"]
    progress_ms = data.get("progress_ms")
    duration_ms = item["duration_ms"]
    external_url = item["external_urls"]["spotify"]

    return {
        "track": track_name,
        "artists": artists,
        "album_image": album_image,
        "progress_ms": progress_ms,
        "duration_ms": duration_ms,
        "url": external_url
    }
