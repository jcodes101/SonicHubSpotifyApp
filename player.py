
def menu(sonic_hub):
    while True:
        print("\nChoose an action:")
        print("1. List Albums")
        print("2. List Tracks")
        print("3. List Artists")
        print("4. Search Albums")
        print("5. Search Artists")
        print("6. Search Tracks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            albums = sonic_hub.get_cached_albums()
            print(f"\tFound {len(albums)} Albums!")
            for album in albums:
                print('\t',album)
        elif choice == '2':
            tracks = sonic_hub.get_cached_tracks()
            print(f"\tFound {len(tracks)} Tracks!")
            for track in tracks:
                print('\t',track)
        elif choice == '3':
            artists = sonic_hub.get_cached_artists()
            print(f"\tFound {len(artists)} Artists!")
            for artist in artists:
                print('\t',artist)
        elif choice == '4':
            album_title = input("Enter album title to search: ")
            albums = sonic_hub.get_albums_by_title(album_title)
            if albums:
                print(f"\tFound {len(albums)}")
                for album in albums:
                    print('\t',album)
                    print(f"\t\tListen here: {album.url}")
            else:
                print("No albums not found.")
        elif choice == '5':
            artist_name = input("Enter artist name to search: ")
            artists = sonic_hub.get_artists_by_name(artist_name)
            if artists:
                print(f"\tFound {len(artists)}")
                for artist in artists:
                    print('\t',artist)
                    print(f"\t\tListen here: {artist.url}")
            else:
                print("No artists not found.")
        elif choice == '6':
            track_title = input("Enter track title to search: ")
            tracks = sonic_hub.get_tracks_by_title(track_title)
            if tracks:
                print(f"\tFound {len(tracks)}")
                for track in tracks:
                    print('\t',track)
                    print(f"\t\tListen here: {track.url}")
            else:
                print("No tracks not found.")
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
