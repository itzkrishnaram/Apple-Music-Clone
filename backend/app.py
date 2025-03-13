from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import status
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship, Session,aliased
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from models import Subscription  # import the Subscription model
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
import models
import schemas
from models import User
from pydantic import BaseModel
from typing import List
from sqlalchemy import desc
# Ensure all models are imported so SQLAlchemy is aware of them
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User endpoints
class UserCreate(BaseModel):
    user_f_name: str
    user_l_name: str
    email: str
    password: str

class UserOut(BaseModel):
    user_id: int
    user_f_name: str
    user_l_name: str
    email: str

@app.post("/users/signup", response_model=UserOut, tags=["user"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
            logger.error(f"Email already exists: {user.email}")
            raise HTTPException(status_code=400, detail="Email already exists")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Find user by email
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    # Check password (plaintext comparison for now)
    if user.password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    
    # Login successful, return user data
    return {
        "status": "success",
        "user": {
            "user_id": user.user_id,
            "email": user.email,
            "user_f_name": user.user_f_name,
            "user_l_name": user.user_l_name
        }
    }

    

@app.get("/users/", response_model=list[UserOut], tags=["user"])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@app.post("/login", response_model=UserOut, tags=["user"])
def login_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@app.get("/users/{user_id}", response_model=UserOut, tags=["user"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=UserOut, tags=["user"])
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}", response_model=UserOut, tags=["user"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

# Subscription endpoints
@app.post("/subscriptions/", response_model=schemas.Subscription, tags=["subscription"])
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = models.Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@app.get("/subscriptions/{subscription_id}", response_model=schemas.Subscription, tags=["subscription"])
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription
    
@app.get("/subscriptions/", response_model=List[schemas.Subscription], tags=["subscription"])
def read_subscriptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subscriptions = db.query(models.Subscription).offset(skip).limit(limit).all()
    return subscriptions

@app.put("/subscriptions/{subscription_id}", response_model=schemas.Subscription, tags=["subscription"])
def update_subscription(subscription_id: int, subscription: schemas.SubscriptionUpdate, db: Session = Depends(get_db)):
    db_subscription = db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).first()
    if not db_subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    for key, value in subscription.dict(exclude_unset=True).items():
        setattr(db_subscription, key, value)
    
    db.commit()
    db.refresh(db_subscription)
    return db_subscription
@app.delete("/subscriptions/{subscription_id}", response_model=dict, tags=["subscription"])
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    db.delete(subscription)
    db.commit()
    return {"message": "Subscription deleted successfully"}



# Artist endpoints
@app.post("/artists/", response_model=schemas.Artist, tags=["artist"])
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

@app.get("/artists/", response_model=list[schemas.Artist], tags=["artist"])
def read_artists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Artist).offset(skip).limit(limit).all()

@app.get("/artists/{artist_id}", response_model=schemas.Artist, tags=["artist"])
def read_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@app.put("/artists/{artist_id}", response_model=schemas.Artist, tags=["artist"])
def update_artist(artist_id: int, artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    for key, value in artist.dict().items():
        setattr(db_artist, key, value)
    db.commit()
    db.refresh(db_artist)
    return db_artist

@app.delete("/artists/{artist_id}", response_model=schemas.Artist, tags=["artist"])
def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(db_artist)
    db.commit()
    return db_artist

# Album endpoints
@app.post("/albums/", response_model=schemas.Album, tags=["album"])
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

@app.get("/albums/", response_model=list[schemas.Album], tags=["album"])
def read_albums(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Album).offset(skip).limit(limit).all()

@app.get("/albums/{album_id}", response_model=schemas.Album, tags=["album"])
def read_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@app.put("/albums/{album_id}", response_model=schemas.Album, tags=["album"])
def update_album(album_id: int, album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")
    for key, value in album.dict().items():
        setattr(db_album, key, value)
    db.commit()
    db.refresh(db_album)
    return db_album

@app.delete("/albums/{album_id}", response_model=schemas.Album, tags=["album"])
def delete_album(album_id: int, db: Session = Depends(get_db)):
    db_album = db.query(models.Album).filter(models.Album.id == album_id).first()
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(db_album)
    db.commit()
    return db_album

# Genre endpoints
@app.post("/genres/", response_model=schemas.Genre, tags=["genre"])
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

@app.get("/genres/", response_model=list[schemas.Genre], tags=["genre"])
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Genre).offset(skip).limit(limit).all()

@app.get("/genres/{genre_id}", response_model=schemas.Genre, tags=["genre"])
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@app.put("/genres/{genre_id}", response_model=schemas.Genre, tags=["genre"])
def update_genre(genre_id: int, genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    for key, value in genre.dict().items():
        setattr(db_genre, key, value)
    db.commit()
    db.refresh(db_genre)
    return db_genre

@app.delete("/genres/{genre_id}", response_model=schemas.Genre, tags=["genre"])
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(db_genre)
    db.commit()
    return db_genre

# Song endpoints
@app.post("/songs/", response_model=schemas.Song, tags=["song"])
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song = models.Song(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

@app.get("/songs/", response_model=list[schemas.Song], tags=["song"])
def read_songs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Song).offset(skip).limit(limit).all()

@app.get("/songs/{song_id}", response_model=schemas.Song, tags=["song"])
def read_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.put("/songs/{song_id}", response_model=schemas.Song, tags=["song"])
def update_song(song_id: int, song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if not db_song:
        raise HTTPException(status_code=404, detail="Song not found")
    for key, value in song.dict().items():
        setattr(db_song, key, value)
    db.commit()
    db.refresh(db_song)
    return db_song

@app.delete("/songs/{song_id}", response_model=schemas.Song, tags=["song"])
def delete_song(song_id: int, db: Session = Depends(get_db)):
    db_song = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if not db_song:
        raise HTTPException(status_code=404, detail="Song not found")
    db.delete(db_song)
    db.commit()
    return db_song

# Playlist endpoints
@app.post("/playlists/", response_model=schemas.Playlist, tags=["playlist"])
def create_playlist(playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    db_playlist = models.Playlist(**playlist.dict())
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist

@app.get("/playlists/", response_model=list[schemas.Playlist], tags=["playlist"])
def read_playlists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Playlist).offset(skip).limit(limit).all()

@app.get("/playlists/{playlist_id}", response_model=schemas.Playlist, tags=["playlist"])
def read_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = db.query(models.Playlist).filter(models.Playlist.playlist_id == playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    return playlist

@app.put("/playlists/{playlist_id}", response_model=schemas.Playlist, tags=["playlist"])
def update_playlist(playlist_id: int, playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    db_playlist = db.query(models.Playlist).filter(models.Playlist.playlist_id == playlist_id).first()
    if not db_playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    for key, value in playlist.dict().items():
        setattr(db_playlist, key, value)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist

@app.delete("/playlists/{playlist_id}", response_model=schemas.Playlist, tags=["playlist"])
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    db_playlist = db.query(models.Playlist).filter(models.Playlist.playlist_id == playlist_id).first()
    if not db_playlist:
        raise HTTPException(status_code=404, detail="Playlist not found")
    db.delete(db_playlist)
    db.commit()
    return db_playlist

# Playlist_Song endpoints
@app.post("/playlist_songs/", response_model=schemas.PlaylistSong, tags=["playlist_song"])
def create_playlist_song(playlist_song: schemas.PlaylistSongCreate, db: Session = Depends(get_db)):
    db_playlist_song = models.Playlist_Song(**playlist_song.dict())
    db.add(db_playlist_song)
    db.commit()
    db.refresh(db_playlist_song)
    return db_playlist_song

@app.get("/playlist_songs/", response_model=list[schemas.PlaylistSong], tags=["playlist_song"])
def read_playlist_songs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Playlist_Song).offset(skip).limit(limit).all()

@app.get("/playlist_songs/{playlist_song_id}", response_model=schemas.PlaylistSong, tags=["playlist_song"])
def read_playlist_song(playlist_song_id: int, db: Session = Depends(get_db)):
    playlist_song = db.query(models.Playlist_Song).filter(models.Playlist_Song.playlist_song_id == playlist_song_id).first()
    if not playlist_song:
        raise HTTPException(status_code=404, detail="Playlist Song not found")
    return playlist_song

@app.delete("/playlist_songs/{playlist_song_id}", response_model=schemas.PlaylistSong, tags=["playlist_song"])
def delete_playlist_song(playlist_song_id: int, db: Session = Depends(get_db)):
    db_playlist_song = db.query(models.Playlist_Song).filter(models.Playlist_Song.playlist_song_id == playlist_song_id).first()
    if not db_playlist_song:
        raise HTTPException(status_code=404, detail="Playlist Song not found")
    db.delete(db_playlist_song)
    db.commit()
    return db_playlist_song

@app.post("/artist_genres/", response_model=schemas.ArtistGenre, tags=["artist_genre"])
def create_artist_genre(artist_genre: schemas.ArtistGenreCreate, db: Session = Depends(get_db)):
    db_artist_genre = models.Artist_Genre(**artist_genre.dict())
    db.add(db_artist_genre)
    db.commit()
    db.refresh(db_artist_genre)
    return db_artist_genre

@app.get("/artist_genres/", response_model=list[schemas.ArtistGenre], tags=["artist_genre"])
def read_artist_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Artist_Genre).offset(skip).limit(limit).all()

@app.get("/artist_genres/{artist_genre_id}", response_model=schemas.ArtistGenre, tags=["artist_genre"])
def read_artist_genre(artist_genre_id: int, db: Session = Depends(get_db)):
    artist_genre = db.query(models.Artist_Genre).filter(models.Artist_Genre.artist_genre_id == artist_genre_id).first()
    if not artist_genre:
        raise HTTPException(status_code=404, detail="Artist-Genre relationship not found")
    return artist_genre

@app.put("/artist_genres/{artist_genre_id}", response_model=schemas.ArtistGenre, tags=["artist_genre"])
def update_artist_genre(artist_genre_id: int, artist_genre: schemas.ArtistGenreCreate, db: Session = Depends(get_db)):
    db_artist_genre = db.query(models.Artist_Genre).filter(models.Artist_Genre.artist_genre_id == artist_genre_id).first()
    if not db_artist_genre:
        raise HTTPException(status_code=404, detail="Artist-Genre relationship not found")
    for key, value in artist_genre.dict().items():
        setattr(db_artist_genre, key, value)
    db.commit()
    db.refresh(db_artist_genre)
    return db_artist_genre

@app.delete("/artist_genres/{artist_genre_id}", response_model=schemas.ArtistGenre, tags=["artist_genre"])
def delete_artist_genre(artist_genre_id: int, db: Session = Depends(get_db)):
    db_artist_genre = db.query(models.Artist_Genre).filter(models.Artist_Genre.artist_genre_id == artist_genre_id).first()
    if not db_artist_genre:
        raise HTTPException(status_code=404, detail="Artist-Genre relationship not found")
    db.delete(db_artist_genre)
    db.commit()
    return db_artist_genre


@app.post("/devices/", response_model=schemas.DeviceOut, tags=["device"])
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@app.get("/devices/", response_model=list[schemas.DeviceOut], tags=["device"])
def read_devices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Device).offset(skip).limit(limit).all()

@app.get("/devices/{device_id}", response_model=schemas.DeviceOut, tags=["device"])
def read_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(models.Device).filter(models.Device.device_id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@app.put("/devices/{device_id}", response_model=schemas.DeviceOut, tags=["device"])
def update_device(device_id: int, device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.device_id == device_id).first()
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.dict().items():
        setattr(db_device, key, value)
    db.commit()
    db.refresh(db_device)
    return db_device

@app.delete("/devices/{device_id}", response_model=schemas.DeviceOut, tags=["device"])
def delete_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(models.Device).filter(models.Device.device_id == device_id).first()
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return db_device





#Set Membership (IN Query)
@app.get("/users-with-plans")
def get_users_with_plans(db: Session = Depends(get_db)):
    # Subquery to get user IDs with specific plans
    subquery = db.query(models.Subscription.user_id).filter(models.Subscription.plan_name.in_(['Individual', 'Family']))

    # Main query to get user details
    query = db.query(models.User.user_id, models.User.user_f_name, models.User.user_l_name, models.User.email).filter(models.User.user_id.in_(subquery)).all()

    return {"users_with_plans": [{"user_id": user.user_id, "user_f_name": user.user_f_name, "user_l_name": user.user_l_name, "email": user.email} for user in query]}

#Set Comparison (ANY Query)
@app.get("/songs-duration-greater-than-5")
def get_songs_duration_greater_than_5(db: Session = Depends(get_db)):
    # Subquery to get the duration of the song with id 5
    subquery = db.query(models.Song.duration).filter(models.Song.id == 5)

    # Main query to get songs with duration greater than or equal to the subquery value
    query = db.query(models.Song.id, models.Song.name, models.Song.duration).filter(models.Song.duration >= subquery).all()

    return {"songs_duration_greater_than_5": [{"id": song.id, "name": song.name, "duration": song.duration} for song in query]}


#Subqueries Using WITH Clause
@app.get("/artists-with-multiple-genres")
def get_artists_with_multiple_genres(db: Session = Depends(get_db)):
    # Define the subquery to count distinct genres per artist
    artist_genre_count_subquery = db.query(
        models.Song.artist_id,
        func.count(func.distinct(models.Song.genre_id)).label("genre_count")
    ).group_by(models.Song.artist_id).subquery()

    # Main query to get artists with more than one genre
    query = db.query(artist_genre_count_subquery.c.artist_id).filter(artist_genre_count_subquery.c.genre_count > 1).all()

    return {"artists_with_multiple_genres": [{"Anirudh,artist_id": row.artist_id} for row in query]}

#Advanced Aggregate Functions (AVG Query)
@app.get("/average-song-duration-per-album")
def get_avg_song_duration_per_album(db: Session = Depends(get_db)):
    # Query to calculate the average duration per album
    query = db.query(
        models.Song.album_id,
        func.avg(models.Song.duration).label("avg_duration")
    ).group_by(models.Song.album_id).all()

    return {"average_duration_per_album": [{"album_id": row.album_id, "avg_duration": row.avg_duration} for row in query]}


@app.get("/song-duration-rank-per-album")
def get_song_duration_rank_per_album(db: Session = Depends(get_db)):
    # Create an alias for the Song table if necessary (optional)
    songs = aliased(models.Song)

    # Create the query using SQLAlchemy
    query = db.query(
        songs.id,
        songs.name,
        songs.duration,
        songs.album_id,
        func.rank().over(
            partition_by=songs.album_id,
            order_by=desc(songs.duration)
        ).label("duration_rank")
    ).all()  # Executes the query

    # Return the results as a list of dictionaries
    return {"song_duration_rank": [{"id": song.id, "name": song.name, "duration": song.duration, "album_id": song.album_id, "duration_rank": song.duration_rank} for song in query]}


def row_to_dict(row, columns):
    """
    Convert a tuple row from query result to a dictionary
    """
    return {columns[i]: row[i] for i in range(len(columns))}

