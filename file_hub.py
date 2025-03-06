from dj_equipment import Artist,Album,Track
from hubs import BaseSonicHub
from player import menu

#TODO implement FileBasedSonicHub
class FileBasedSonicHub(BaseSonicHub):
    """derived FileBasedSonicHub class from BaseSonicHub class"""
    def __init__(self, name):
        """constructor for derived class FileBasedSonicHub"""
        BaseSonicHub.__init__(self, name)

    def populate_maps(self):
        
        with open('encoded/artists.txt', 'r') as file:
            for line in file:
                artist = Artist.deserialize(line.strip())
                self._artist_map[artist.get_id()] = artist

        with open('encoded/albums.txt', 'r') as file:
            for line in file:
                album = Album.deserialize(line.strip())
                self._album_map[album.get_id()] = album

        with open('encoded/tracks.txt', 'r') as file:
            for line in file:
                track = Track.deserialize(line.strip())
                self._track_map[track.get_id()] = track

if __name__ == "__main__":

    try:
        sonic_hub = FileBasedSonicHub("File Based Sonic Hub")
        print(sonic_hub)
        sonic_hub.populate_maps()
        print(sonic_hub)
        sonic_hub.cross_pollinate()

        menu(sonic_hub)

    except Exception as e:
        print("Could not run our program due to error",e)
