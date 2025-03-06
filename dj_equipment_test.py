import unittest
from dj_equipment import Artist,Album,Track
# TODO Step 0.b Copy your test classes here from Project 3 here! 
class TestTrack(unittest.TestCase):
    """"
    I am going to write these tests
    1. Test 1: Test what __str__ returns
    2. Test 2: After constructing an Album, the title and artist instance attributes are set to what was passed as params 
    3. Test 3: After constructing an Album, release_date, url, and _id are set to None
    4. Test 4: After calling add_track(...) with some track, the tracks list contains the track 
    """
    def test_constructor(self):
        """Ensures the params from the cstr are set on the instance"""
        title = "some title"
        artist = Artist("me")
        album = Album("album title",artist)

        t = Track(title,artist,album)
        self.assertEqual(t.title,title)
        self.assertEqual(t.artist,artist)
        self.assertEqual(t.album,album)

        self.assertEqual(t.popularity,-1)
        self.assertEqual(t.url,None)
        self.assertEqual(t._id,None)

    def test_str(self):
        """Ensures a Track prints out the name and possibly the popularity"""
        title = "some title"
        artist = Artist("me")
        album = Album("album title",artist)

        t = Track(title,artist,album)
        self.assertEqual(str(t),f"{t.title}")

        t.set_popularity(100)
        self.assertEqual(str(t),f"{title} has popularity 100")

    def test_set_populatiry(self):
        """Ensures set_popularity """
        title = "some title"
        artist = Artist("me")
        album = Album("album title",artist)

        t = Track(title,artist,album)
        t.set_popularity(99)
        self.assertEqual(t.popularity,99)
    def test_get_id(self):
        """Gets the id"""
        title = "some title"
        artist = Artist("me")
        album = Album("album title",artist)

        t = Track(title,artist,album)
        t.set_id("88")
        self.assertEqual(t.get_id,"88")
    def test_set_id(self):
        """Ensures set id sets an id"""
        title = "some title"
        artist = Artist("me")
        album = Album("album title",artist)

        t = Track(title,artist,album)
        t.set_id("88")
        self.assertEqual(t._id,"88")

class TestAlbum(unittest.TestCase):
    """"
    I am going to write these tests
    1. Test 1: Test what __str__ returns
    2. Test 2: After constructing an Album, the title and artist instance attributes are set to what was passed as params 
    3. Test 3: After constructing an Album, release_date, url, and _id are set to None
    4. Test 4: After calling add_track(...) with some track, the tracks list contains the track 
    """
    def test_constructor(self):
        """Ensures the params from the cstr are set on the instance"""
        title = "some title"
        artist = Artist("me")

        album = Album(title,artist)

        self.assertEqual(album.title,title)
        self.assertEqual(album.artist,artist)

        self.assertEqual(album.tracks,[])
        self.assertEqual(album.release_date,None)
        self.assertEqual(album.url,None)
        self.assertEqual(album._id,None)


    def test_str(self):
        """Ensures an Album prints out the title and possibly the release date"""
        title = "some title"
        artist = Artist("me")

        album = Album(title,artist)

        self.assertEqual(str(album),f"{album.title}")

        album.release_date = "10/10/2024"
        self.assertEqual(str(album),f"{album.title} was released {album.release_date}")

    def test_add_track(self):
        """Ensures tracks are added properly """
        title = "some title"
        artist = Artist("me")

        album = Album(title,artist)

        t = Track("t title",artist,album)
        album.add_track(t)
        self.assertIn(t,album.tracks)
    def test_get_id(self):
        """Ensures tracks have good ids"""
        title = "some title"
        artist = Artist("me")

        album = Album(title,artist)
        album.set_id("22")
        self.assertEqual("22",album.get_id())

    def test_set_release_date(self):
        """Ensures release date is set properly"""
        album = Album("some title", Artist("me"))
        album.set_release_date("10/10/2024")

        self.assertEqual(album.release_date,"10/10/2024")

class TestArtist(unittest.TestCase):
    """"
    I am going to write these tests
    1. Test 1: Test what __str__ returns
    2. Test 2: After constructing an Album, the title and artist instance attributes are set to what was passed as params 
    3. Test 3: After constructing an Album, release_date, url, and _id are set to None
    4. Test 4: After calling add_track(...) with some track, the tracks list contains the track 
    """
    def test_constructor(self):
        """Ensures the params from the cstr are set on the instance #score(0)"""
        name = "singer"
        artist = Artist(name)

        self.assertEqual(artist.name,name)

        self.assertEqual(artist.albums,[])
        self.assertEqual(artist.url,None)
        self.assertEqual(artist._id,None)

    def test_str(self):
        """Ensures an Artist prints out the name and the number of albums #score(0)"""
        name = "singer"
        artist = Artist(name)

        self.assertEqual(str(artist),f"{name} has 0 albums")

        a = Album("t",artist)
        b = Album("t",artist)
        c = Album("t",artist)
        artist.add_album(a)
        artist.add_album(b)
        artist.add_album(c)
        self.assertEqual(str(artist),f"{name} has 3 albums")

    def test_add_album(self):
        """Ensures add album adds an ablum! #score(0)"""
        name = "singer"
        artist = Artist(name)
        artist.add_album(Album("t",artist))
        self.assertEqual(str(artist),f"{name} has 1 albums")
        artist.add_album(Album("t",artist))
        self.assertEqual(str(artist),f"{name} has 2 albums")
        artist.add_album(Album("t",artist))
        self.assertEqual(str(artist),f"{name} has 3 albums")

    def test_set_id(self):
        """Ensures set id sets an id #score(0)"""
        name = "singer"
        artist = Artist(name)
        artist.set_id("1111")
        self.assertEqual(artist._id,"1111")
    def test_get_id(self):
        """Ensures get id gets an id #score(0)"""
        name = "singer"
        artist = Artist(name)
        artist.set_id("1111")
        self.assertEqual(artist.get_id(),"1111")

if __name__ == "__main__":
    unittest.main()
