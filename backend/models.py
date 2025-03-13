from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_f_name = Column(String(50))  # Specify length here, e.g., 50 characters
    user_l_name = Column(String(50))  # Specify length here, e.g., 50 characters
    email = Column(String(100), unique=True, index=True)  # Specify length for email
    password = Column(String(100))  # Specify length for password

    # Relationships
    subscription = relationship("Subscription", back_populates="user", uselist=False)
    playlists = relationship("Playlist", back_populates="user")
    devices = relationship("Device", back_populates="user")


class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String(50))
    price = Column(Integer)
    duration = Column(Integer)

    # Foreign key
    user_id = Column(Integer, ForeignKey("users.user_id"))

    # Relationships
    user = relationship("User", back_populates="subscription")


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    bio = Column(String(500), nullable=True)  # Optional biography of the artist

    # Relationships
    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="artist")
    genres = relationship("ArtistGenre", back_populates="artist")


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Specify length for VARCHAR
    release_date = Column(Date)

    # Foreign key
    artist_id = Column(Integer, ForeignKey("artists.id"))

    # Relationships
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    duration = Column(Integer, nullable=False)  # Duration in seconds

    # Foreign keys
    album_id = Column(Integer, ForeignKey("albums.id"), nullable=True)  # Album ID (optional)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)  # Artist ID
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=True)  # Genre ID (optional)

    # Relationships
    album = relationship("Album", back_populates="songs")
    artist = relationship("Artist", back_populates="songs")
    genre = relationship("Genre", back_populates="songs")
    playlists = relationship("PlaylistSong", back_populates="song")


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)

    # Relationships
    songs = relationship("Song", back_populates="genre")
    artist_genres = relationship("ArtistGenre", back_populates="genre")


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True, index=True)  # Playlist ID
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)  # Weak entity relationship
    name = Column(String(255), nullable=False)
    creation_date = Column(Date)

    # Relationships
    user = relationship("User", back_populates="playlists")
    songs = relationship("PlaylistSong", back_populates="playlist")


class Device(Base):
    __tablename__ = 'devices'

    device_id = Column(Integer, primary_key=True, index=True)
    device_type = Column(String(50))
    device_name = Column(String(100))
    last_active = Column(Date)

    # Foreign key
    user_id = Column(Integer, ForeignKey("users.user_id"))

    # Relationship
    user = relationship("User", back_populates="devices")


class PlaylistSong(Base):
    __tablename__ = 'playlist_songs'

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for the entry
    playlist_id = Column(Integer, ForeignKey("playlists.id"), nullable=False)  # Playlist ID
    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False)  # Song ID

    # Relationships
    playlist = relationship("Playlist", back_populates="songs")
    song = relationship("Song", back_populates="playlists")


class ArtistGenre(Base):
    __tablename__ = 'artist_genres'

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for the entry
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)  # Artist ID
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)  # Genre ID

    # Relationships
    artist = relationship("Artist", back_populates="genres")
    genre = relationship("Genre", back_populates="artist_genres")