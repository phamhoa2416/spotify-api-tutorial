from auth import get_token
import artist
import search

def main():
    query = input("Which type do you want to search: ").lower()
    match query:
        case "artist":
            artist_name = input("Enter the artist name: ")
            token = get_token()
            
            artist_api = artist.Artist(token)
            artist_id = search.search_for_artist(token, artist_name)["id"]
            
            print("Artist Information:")
            
            name = artist_api.get_name(artist_id)
            print("Name:", name)
            
            external_urls = artist_api.get_external_urls(artist_id)
            print("External URLs:", external_urls)
            
            followers = artist_api.get_number_of_followers(artist_id)
            print("Number of Followers:", followers)
            
            genres = artist_api.get_genres(artist_id)
            print("Genres:", ", ".join(genres) if genres else "No genres found")
            
            images = artist_api.get_images(artist_id)
            if images:
                print("Images:")
                for idx, img_url in enumerate(images, start=1):
                    print(f"  {idx}. {img_url}")
            else:
                print("No images available")
                
            albums = artist_api.get_albums_by_artist(artist_id)
            if albums:
                print("Albums:")
                for idx, album in enumerate(albums, start=1):
                    print(f"  {idx}. {album['name']} (total tracks: {album["total_tracks"]}) (release date: {album['release_date']})")
            else:
                print("No albums found")
            
            top_tracks = artist_api.get_top_tracks_by_artist(artist_id)
            if top_tracks:
                print("Top tracks:")
                for idx, top_track in enumerate(top_tracks, start=1):
                    print(f"  {idx}. {top_track['name']} (featuring artists: {top_track["artists"][0]['name']}) (duration: {top_track["duration_ms"]}) ({top_track["external_urls"]})")
            else:
                print("No top tracks found")
                
            related_artists = artist_api.get_related_artists(artist_id)
            if related_artists:
                print("Related artists:")
                for idx, related_artist in enumerate(related_artists, start=1):
                    print(f"  {idx}. {related_artist['name']}")
            else:
                print("No related artist found")
        case "album":
            pass
        case "track":
            pass
        case "playlist":
            pass
        case "show":
            pass
        case "episode":
            pass
        case "audiobook":
            pass
if __name__ == "__main__":
    main()


