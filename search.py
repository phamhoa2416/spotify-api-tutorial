from requests import get
import json
import auth

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={artist_name}&type=artist&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("artists", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No artist found")
        return None
    
    return json_result[0]

def search_for_album(token, album_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token) 
    
    query = f"q={album_name}&type=album&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("albums", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No album found")
        return None
    
    return json_result[0]

def search_for_track(token, track_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={track_name}&type=track&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("tracks", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No track found")
        return None
    
def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={playlist_name}&type=playlist&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("playlists", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No playlist found")
        return None
    
def search_for_show(token, show_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={show_name}&type=show&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("shows", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No show found")
        return None 
    
def search_for_episode(token, episode_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={episode_name}&type=episode&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("episodes", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No show found")
        return None 
    
def search_for_audiobook(token, audiobook_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth.get_auth_headers(token)
    
    query = f"q={audiobook_name}&type=audiobook&limit=20"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content).get("audiobooks", {}).get("items", [])
    
    if len(json_result) == 0:
        print("No show found")
        return None 