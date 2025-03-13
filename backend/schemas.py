from datetime import date,datetime
from pydantic import BaseModel
from typing import Optional, List


# Subscription Schemas
class SubscriptionBase(BaseModel):
    plan_name: str
    price: float
    duration: int

class SubscriptionCreate(SubscriptionBase):
    pass

# Schema for updating an existing subscription
class SubscriptionUpdate(BaseModel):
    plan_name: Optional[str] = None
    price: Optional[float] = None
    duration: Optional[int] = None

# Schema for reading subscription data
class Subscription(SubscriptionBase):
    subscription_id: int

    class Config:
        orm_mode = True
# User Schemas
class UserBase(BaseModel):
    user_f_name: str
    user_l_name: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int
    subscription: Optional[Subscription] = None  # Relationship to Subscription
    playlists: Optional[List["Playlist"]] = []  # Relationship to Playlist
    devices: Optional[List["Device"]] = []  # Relationship to Device

    class Config:
        orm_mode = True


# Artist Schemas
class ArtistBase(BaseModel):
    name: str
    bio: Optional[str] = None  # Optional field for bio

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int

    class Config:
        orm_mode = True


# Album Schemas
class AlbumBase(BaseModel):
    title: str
    release_date: Optional[date] = None  # Use Optional for nullable fields

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int
    artist_id: int  # Foreign key to Artist

    class Config:
        orm_mode = True


# Song Schemas
class SongBase(BaseModel):
    name: str
    duration: int  # Duration in seconds
    album_id: Optional[int] = None  # Optional Album ID
    artist_id: int  # Artist ID
    genre_id: Optional[int] = None  # Optional Genre ID

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        orm_mode = True


# Genre Schemas
class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


# Playlist Schemas
class PlaylistBase(BaseModel):
    user_id: int
    name: str

class PlaylistCreate(PlaylistBase):
    pass

class Playlist(PlaylistBase):
    id: int
    creation_date: date

    class Config:
        orm_mode = True

class DeviceCreate(BaseModel):
    device_type: str
    device_name: str
    last_active: datetime
    user_id: int

class DeviceOut(BaseModel):
    device_id: int
    device_type: str
    device_name: str
    last_active: datetime
    user_id: int

    class Config:
        orm_mode = True
# Device Schemas
#class DeviceBase(BaseModel):
 #   device_type: str
  #  device_name: str
   # last_active: date

#class DeviceCreate(DeviceBase):
    pass

#class Device(DeviceBase):
   # device_id: int
    #user_id: int  # Foreign key to User

    #lass Config:
     #   orm_mode = True


# PlaylistSong Schemas
class PlaylistSongBase(BaseModel):
    playlist_id: int
    song_id: int

class PlaylistSongCreate(PlaylistSongBase):
    pass

class PlaylistSong(PlaylistSongBase):
    id: int

    class Config:
        orm_mode = True


# ArtistGenre Schemas
class ArtistGenreBase(BaseModel):
    artist_id: int
    genre_id: int

class ArtistGenreCreate(ArtistGenreBase):
    pass

class ArtistGenre(ArtistGenreBase):
    id: int

    class Config:
        orm_mode = True