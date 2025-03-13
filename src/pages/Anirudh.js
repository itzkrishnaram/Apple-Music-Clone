import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Anirudh.css';

const Anirudh = () => {
  const navigate = useNavigate();

  const goBack = () => {
    navigate('/');
  };

  // List of songs with different genres
  const songs = [
    { id: 1, title: 'Minnale', artist: 'Anirudh', genre: 'Rock', image: '/top1.png' },
    { id: 2, title: 'Perfect', artist: 'Anirudh', genre: 'Pop', image: '/top2.png' },
    { id: 3, title: 'Closer', artist: 'Anirudh', genre: 'Jazz', image: '/top3.png' },
    { id: 4, title: 'Heat Waves', artist: 'Anirudh', genre: 'Classical', image: '/top4.png' },
    { id: 5, title: 'So High', artist: 'Anirudh', genre: 'Electronic', image: '/top5.png' },
    { id: 6, title: 'See you Again', artist: 'Anirudh', genre: 'Hip-Hop', image: '/top6.png' },
    { id: 7, title: 'Bla Bla', artist: 'Anirudh', genre: 'Reggae', image: '/top7.png' },
    { id: 8, title: 'Manjal Veyil', artist: 'Anirudh', genre: 'Blues', image: '/top8.png' },
    { id: 9, title: 'Anbe Sivam', artist: 'Anirudh', genre: 'R&B', image: '/top9.png' }
  ];

  return (
    <div className="anirudh-page">
      <button className="back-button" onClick={goBack}>
        Back
      </button>
      <div className="content-area">
        <h1>Anirudh - Song Collection</h1>
        <p>Explore the various genres of Anirudh's hits!</p>

        <div className="songs-grid">
          {songs.map((song) => (
            <div key={song.id} className="song-card">
              <img src={song.image} alt={song.title} className="song-image" />
              <div className="song-details">
                <h3>{song.title}</h3>
                <p>{song.artist}</p>
                <p>{song.genre}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Anirudh;