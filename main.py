from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    return json.loads(result.content)

def search_for_artist(token, artist_name):
    """Search for an artist by name"""
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=10"
    
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    
    if len(json_result["artists"]["items"]) == 0:
        print(f"No artist found with name: {artist_name}")
        return None
    
    return json_result["artists"]["items"]

def search_for_track(token, track_name):
    """Search for a track by name"""
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={track_name}&type=track&limit=10"
    
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    
    if len(json_result["tracks"]["items"]) == 0:
        print(f"No track found with name: {track_name}")
        return None
    
    return json_result["tracks"]["items"]

def display_artist_info(artist_data):
    """Display artist information in a clean, formatted way"""
    print("\n" + "="*50)
    print(f"Artist: {artist_data['name']}")
    print(f"Popularity: {artist_data['popularity']}/100")
    print(f"Followers: {artist_data['followers']['total']:,}")
    print(f"Genres: {', '.join(artist_data['genres'])}")
    print(f"Spotify URL: {artist_data['external_urls']['spotify']}")
    print("="*50 + "\n")

def display_track_info(track):
    """Display track information in a clean, formatted way"""
    print("\n" + "-"*50)
    print(f"Track: {track['name']}")
    print(f"Artist: {', '.join([artist['name'] for artist in track['artists']])}")
    print(f"Album: {track['album']['name']}")
    print(f"Released: {track['album']['release_date']}")
    print(f"Duration: {round(track['duration_ms']/1000/60, 2)} minutes")
    print(f"Popularity: {track['popularity']}/100")
    print(f"Preview URL: {track['preview_url'] or 'Not available'}")
    print(f"Spotify URL: {track['external_urls']['spotify']}")
    print("-"*50 + "\n")

def interactive_search():
    """Interactive search function for artists and tracks"""
    token = get_token()
    
    while True:
        print("\n1. Search for an artist")
        print("2. Search for a track")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            artist_name = input("Enter artist name: ")
            artists = search_for_artist(token, artist_name)
            
            if artists:
                print(f"\nFound {len(artists)} artists:")
                for i, artist in enumerate(artists):
                    print(f"{i+1}. {artist['name']} (Popularity: {artist['popularity']}/100)")
                
                artist_choice = input("\nSelect an artist number (or press Enter to skip): ")
                if artist_choice.isdigit() and 1 <= int(artist_choice) <= len(artists):
                    selected_artist = artists[int(artist_choice) - 1]
                    display_artist_info(selected_artist)
        
        elif choice == '2':
            track_name = input("Enter track name: ")
            tracks = search_for_track(token, track_name)
            
            if tracks:
                print(f"\nFound {len(tracks)} tracks:")
                for i, track in enumerate(tracks):
                    artists = ', '.join([artist['name'] for artist in track['artists']])
                    print(f"{i+1}. {track['name']} by {artists}")
                
                track_choice = input("\nSelect a track number (or press Enter to skip): ")
                if track_choice.isdigit() and 1 <= int(track_choice) <= len(tracks):
                    selected_track = tracks[int(track_choice) - 1]
                    display_track_info(selected_track)
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

# Main execution
if __name__ == "__main__":
    interactive_search()