from requests import get
import json
from auth import get_auth_headers

class Artist:
    BASE_URL = "https://api.spotify.com/v1/artists/"
    
    def __init__(self, token):
        self.token = token
        self.headers = get_auth_headers(token)            
        
    def _get_artist_data(self, artist_id):
        url = f"{self.BASE_URL}{artist_id}"
        response = get(url, headers=self.headers)
        
        if response.status_code == 429:
            raise Exception("Rate limited. Try again later.")
        if response.status_code != 200:
            raise Exception(f"Failed to fetch artist data: {response.status_code} {response.text}")
        
        try:
            return response.json()
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response.")
         
    def get_name(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return json_result.get("name", "")
    
    def get_external_urls(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return json_result.get("external_urls", {})
    
    def get_number_of_followers(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return json_result.get("followers", {}).get("total", 0)
    
    def get_genres(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return json_result.get("genres", [])
    
    def get_images(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return [image.get("url", "") for image in json_result.get("images", [])]
    
    def get_popularity(self, artist_id):
        json_result = self._get_artist_data(artist_id)
        return json_result.get("popularity", 0)
    
    def get_albums_by_artist(self, artist_id):
        url = f"{self.BASE_URL}{artist_id}/albums"
        response = get(url, headers=self.headers)
        
        json_result = response.json().get("items", [])
        return json_result
    
    def get_top_tracks_by_artist(self, artist_id):
        url = f"{self.BASE_URL}{artist_id}/top-tracks"
        response = get(url, headers=self.headers)
                       
        json_result = response.json().get("tracks", [])
        return json_result
    
    def get_related_artists(self, artist_id):
        url = f"{self.BASE_URL}{artist_id}/related-artists"
        response = get(url, headers=self.headers)
                       
        json_result = response.json().get("artists", [])
        return json_result
        
    