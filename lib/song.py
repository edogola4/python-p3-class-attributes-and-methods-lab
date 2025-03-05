#!/usr/bin/env python3

class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Set instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes via class methods
        Song.add_song_to_count()
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        # Only add if this artist is not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        # Only add if this genre is not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the count for this genre; initialize if necessary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment the count for this artist; initialize if necessary
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
