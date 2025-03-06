from random import randint as ri
import string,random
# TODO Step 0.a Copy your classes here from Project 3 here! 
class SerializeMixin:
    """Provides basic serialization and deserialization"""
    delimiter = "|" #delimiter to use when serializing

    def serialize(self):
        """Subclasses should overwrite this but do something similar!"""
        return self.create_string_for_serialize([])

    @staticmethod
    def deserialize(encoded):
        """Subclasses should overwrite this but do something similar!"""
        list_of_attributes = SerializeMixin.get_deserialized_list(encoded)
        # construct the specific class using these attributes!
        pass

    def create_string_for_serialize(self,attributes_to_serialize):
        """Given a list of attributes, ensures they are all strings, and returns a list of them"""
        list_of_string = [str(obj) if obj is not None else '' for obj in attributes_to_serialize]
        return SerializeMixin.delimiter.join(list_of_string)
    @staticmethod
    def get_deserialized_list(encoded_string):
        """Given a string, returns a list of strings split by the delimiter. 
            If the element is the empty string replace with None.
        """
        return [val if val else None for val in encoded_string.split(SerializeMixin.delimiter)]



class Track(SerializeMixin):
    """A song on an album"""
    def __init__(self,title,artist,album):
        """Initialize the Track"""
        self.title = title
        self.artist = artist
        self.album = album

        self.popularity = -1
        self.url = None
        self._id = None

    def set_popularity(self,popularity):
        """Sets the popularity"""
        self.popularity = popularity

    def set_id(self,id):
        """Sets the id"""
        self._id = id

    def get_id(self):
        """Gets the id"""
        return self._id

    def serialize(self):
        """Converts this object to something we can write to a file"""
        artist_s = self.artist._id if self.artist else ""
        album_s = self.album._id if self.album else ""
        return self.create_string_for_serialize([self._id,self.title,self.popularity,self.url,artist_s,album_s])

    @staticmethod
    def deserialize(encoded):
        """Creates a Track w/ Artist and Album from the encoded string"""
        try:
            attributes = SerializeMixin.get_deserialized_list(encoded)
            _id         = attributes[0]
            title       = attributes[1]
            popularity  = attributes[2]
            url         = attributes[3]
            artist_id   = attributes[4]
            album_id    = attributes[5]

            artist = None 
            if artist_id:
                artist = Artist(None)
                artist._id = artist_id
            album = None 
            if album_id:
                album = Album(None,artist)
                album._id = album_id
            t = Track(title,artist,album)
            t.set_id(_id)
            t.set_popularity(popularity)
            t.url = url

            return t
        except Exception as e:
            print(f"Could not deserialize {encoded}. Error:{e}")
            return None

    def __str__(self):
        """Title and popularity"""
        if self.popularity != -1:
            return f"{self.title} has popularity {self.popularity}"
        else:
            return f"{self.title}"
class Album(SerializeMixin):
    """An aggretation of songs"""
    def __init__(self,title,artist):
        """Initialize the Album"""
        self.title = title
        self.artist = artist
        self.tracks = []

        self.release_date = None
        self.url = None
        self._id = None

    def add_track(self,track):
        """Adds a track to the album"""
        self.tracks.append(track)

    def set_id(self,id):
        """Sets the id"""
        self._id = id
    def get_id(self):
        """Gets the id"""
        return self._id

    def set_release_date(self,date):
        """Sets the id"""
        self.release_date = date

    def __str__(self):
        """Title and release_date or number of tracks"""
        if self.release_date:
            return f"{self.title} was released {self.release_date}"
        else:
            return f"{self.title} has {len(self.tracks)} tracks"

    def serialize(self):
        """Converts this object to something we can write to a file"""
        artist_s = self.artist._id if self.artist else ""
        return self.create_string_for_serialize([self._id,self.title,self.release_date,self.url,artist_s])

    @staticmethod
    def deserialize(encoded):
        """Creates a Track w/ Artist and Album from the encoded string"""
        try:
            attributes = SerializeMixin.get_deserialized_list(encoded)
            _id         = attributes[0]
            title       = attributes[1]
            release_date  = attributes[2]
            url         = attributes[3]
            artist_id   = attributes[4]

            artist = None 
            if artist_id:
                artist = Artist(None)
                artist._id = artist_id
            album = Album(title,artist)
            album.set_id(_id)
            album.set_release_date(release_date)
            album.url = url
            album._id = _id

            return album
        except Exception as e:
            print(f"Could not deserialize {encoded}. Error:{e}")
            return None



class Artist(SerializeMixin):
    """A musician that makes albums with songs"""
    def __init__(self,name):
        """Initialize the Album"""
        self.name = name
        self.albums = []

        self.url = None
        self._id = None

    def add_album(self,album):
        """Adds a album to the artist"""
        self.albums.append(album)

    def set_id(self,id):
        """Sets the id"""
        self._id = id
    def get_id(self):
        """Gets the id"""
        return self._id

    def __str__(self):
        """Title and popularity"""
        return f"{self.name} has {len(self.albums)} albums"

    def serialize(self):
        """Converts this object to something we can write to a file"""
        return self.create_string_for_serialize([self._id,self.name,self.url])

    @staticmethod
    def deserialize(encoded):
        """Creates a Track w/ Artist and Album from the encoded string"""
        try:
            attributes = SerializeMixin.get_deserialized_list(encoded)
            _id         = attributes[0]
            title       = attributes[1]
            url         = attributes[2]

            artist = Artist(title)
            artist.set_id(_id)
            artist.url = url

            return artist
        except Exception as e:
            print(f"Could not deserialize {encoded}. Error:{e}")
            return None
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

    bryson_tiller = Artist("Bryson Tiller")
    bryson_tiller.set_id(ri(1,10000000))
    bryson_tiller._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album1 = Album("Trapsoul", bryson_tiller)
    album1.set_id(ri(1,10000000))
    album1._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    track1 = Track("Don't", bryson_tiller, album1)
    track1.set_id(ri(1,10000000))
    track1._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album1.add_track(track1)
    bryson_tiller.add_album(album1)

    drake = Artist("Drake")
    drake.set_id(ri(1,10000000))
    drake._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album2 = Album("Take Care", drake)
    album2.set_id(ri(1,10000000))
    album2._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    track2 = Track("Headlines", drake, album2)
    track2.set_id(ri(1,10000000))
    track2._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album2.add_track(track2)
    drake.add_album(album2)

    artists = [bryson_tiller,drake]
    for artist in artists:
        print(artist)
        for i,album in enumerate(artist.albums):
            print(f"\t{i+1}.",album)
            for j, track in enumerate(album.tracks):
                print(f"\t\t{j+1}:",track)

    # Serializing a few things
    print(f"{'Artists':*^30}")
    for artist in artists:
        encoded = artist.serialize()
        print(encoded)
    print(f"{'Albums':*^30}")
    for artist in artists:
        for album in artist.albums:
            encoded = album.serialize()
            print(encoded)
    print(f"{'Tracks':*^30}")
    for artist in artists:
        for album in artist.albums:
            for track in album.tracks:
                encoded = track.serialize()
            print(encoded)
