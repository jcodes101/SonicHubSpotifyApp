from dj_equipment import BaseSonicHub,Artist,Album,Track
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from player import menu

class SpotifySonicHub(BaseSonicHub):
    """Reads from Spotify!"""
    MAX_RETURN = 10 # max number of any results to return
    def __init__(self,name,client_id,client_secret):
        """Using the given cllient_id and client_secret create the spotify api so we can make web service calls!"""
        super().__init__(name)
        client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
        self.spotify_api = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def populate_maps(self):
        """
        Spotify has over 100MM tracks, 1.8M albums from 8MM artists, and . We can't store that in memory!
        so we'll pass!
        """
        pass
    def get_tracks_by_title(self,track_title):
        """Calls spotify for the track!"""
        tracks = []
        results = self.spotify_api.search(q=track_title, type='track', limit=SpotifySonicHub.MAX_RETURN)

        for result in results['tracks']['items']:

            album = self._get_album(result['album'])
            artist = album.artist if album else None

            track_id = result['id']
            track = self._track_map[track_id] if track_id in self._track_map else None
            if track is None:
                track = Track(result['name'], artist, album)
                track.set_id(track_id)
                track.url = result['external_urls']['spotify']
                track.set_popularity(result['popularity'])
                self._track_map[track_id] = track

                album.add_track(track)
            else:
                print(f"Reusing Track: {track.title}")

            tracks.append(track)
        return tracks

    def get_albums_by_title(self,album_title):
        """Calls spotify for the album!"""
        results = self.spotify_api.search(q=album_title, type='album', limit=SpotifySonicHub.MAX_RETURN)
        albums = self._get_albums(results['albums']['items'])
        return albums


    def get_artists_by_name(self,artist_name):
        """Calls spotify for the artist!"""
        results = self.spotify_api.search(q=artist_name, type='artist', limit=SpotifySonicHub.MAX_RETURN)
        artists = self._get_artists(results['artists']['items'])
        return artists

    def _get_artists(self,artists):
        """common logic to get artist from spotify results"""
        output = []
        if artists:
            for result_artist in artists:
                artist_id = result_artist['id']
                artist = self._artist_map[artist_id] if artist_id in self._artist_map else None
                if artist is None:
                    artist = Artist(result_artist['name'])
                    artist.set_id(result_artist['id'])
                    artist.url = result_artist['external_urls']['spotify']
                    self._artist_map[artist_id] = artist
                output.append(artist)
            return output

    def _get_albums(self,albums):
        """common logic to get albums from spotify results"""
        output = []
        if albums:
            for result_album in albums:
                album = self._get_album(result_album)
                output.append(album)
        return output

    def _get_album(self,result_album):
        """common logic to get albums from spotify results"""
        album = None
        if result_album:
            album_id = result_album['id']
            album = self._album_map[album_id] if album_id in self._album_map else None
            if album is None:
                artists = self._get_artists(result_album['artists'])
                artist = artists[0] if artists else None
                album = Album(result_album['name'], artist)
                album.set_id(album_id)
                album.url = result_album['external_urls']['spotify']
                album.release_date = result_album['release_date']

                self._album_map[album_id] = album
                artist.add_album(album)
            else:
                print(f"Reusing Album: {album.title}")
        return album

if __name__ == "__main__":
    """
    Expects 2 args, 1) client_id 2) client_secret 
    If they are missing, the user will be prompted for them. 
    """
    try:
        client_id = None
        client_secret = None


        if (len(sys.argv) > 2):
            client_id = sys.argv[1]
            client_secret = sys.argv[2]
            print("Looks like we got the client_id and client_secrety from the sys args. Cool")
        else:
            print("No arguments passed in so I must ask...")
            client_id = input("Client Id: ")
            client_secret = input("Client Secret: ")

        sonic_hub = SpotifySonicHub("Spotify Based Sonic Hub",client_id,client_secret)
        print(sonic_hub)
        sonic_hub.populate_maps()
        print(sonic_hub)
        sonic_hub.cross_pollinate()

        menu(sonic_hub)

    except Exception as e:
        print("Could not run our program due to error",e)
