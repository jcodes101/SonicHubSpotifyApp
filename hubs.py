class BaseSonicHub:
    """Provides common methods for sonic hubs"""
    _track_map = {} # track id to Track object 
    _album_map = {} # album id to Album object 
    _artist_map = {} # artist id to Artist object

    def __init__(self,name):
        """Store the name/nature of this SonicHub"""
        self.name = name

    def register_artist(self,artist):
        """Adds the Artist to the _artist_map, the artists Albums to the _album_map, and the 
           albums Tracks to the _track_map!"""
        self._artist_map[artist.get_id()] = artist 
        for album in artist.albums:
            self._album_map[album.get_id()] = album
            for track in album.tracks:
                self._track_map[track.get_id()] = track
    def cross_pollinate(self):
        """Tracks, Albums, and Aritsts may be created independently. This will add
           tracks to albums, albums to artists, and so forth."""
        for track_id,track in self._track_map.items():
 
            if track.album and track.album.get_id() in self._album_map:
                album = self._album_map[track.album.get_id()]

                if track not in album.tracks:
                    #print(f"Added track {track_id} to album {album.get_id()}")
                    album.add_track(track)
                track.album = album
            if track.artist and track.artist.get_id() in self._artist_map:
                artist = self._artist_map[track.artist.get_id()]
                track.arist = artist
       
        for album_id,album in self._album_map.items():
            if album.artist and album.artist.get_id() in self._artist_map:
                artist = self._artist_map[album.artist.get_id()]
                if album not in artist.albums:
                    #print(f"Added album {album_id} to artist {artist.get_id()}")
                    artist.add_album(album)
                album.arist = artist
      

    def __str__(self):
        return f"{self.name} has {len(self._track_map)} tracks,  {len(self._album_map)} albums,  {len(self._artist_map)} artists" 

    def get_cached_tracks(self):
        return self._track_map.values()
    def get_cached_albums(self):
        return self._album_map.values()
    def get_cached_artists(self):
        return self._artist_map.values()

    def get_tracks_by_title(self,track_title):
        """If we have a track with a title like this return it otherwise None"""
        tracks = []
        for track in self._track_map.values():
            if track_title.lower() in track.title.lower():
                tracks.append(track)
        return tracks
    def get_albums_by_title(self,album_title):
        """If we have an album with a title like this return it otherwise None"""
        albums = []
        for album in self._album_map.values():
            if album_title.lower() in album.title.lower():
                albums.append(album)
        return albums
    def get_artists_by_name(self,artist_name):
        """If we have an artist with a name like this return it otherwise None"""
        artists = []
        for artist in self._artist_map.values():
            if artist_name.lower() in artist.name.lower():
                artists.append(artist)
        return artists
    def populate_maps(self):
        """Derived classes should populate the maps when this is called!"""
        raise NotImplementedError("Dervied classes need to implement me!")

if __name__ == "__main__":
    hub = BaseSonicHub("Test Hub")
