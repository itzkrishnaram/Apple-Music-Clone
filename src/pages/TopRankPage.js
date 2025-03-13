import React from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
// TopRankPage.js
import '../styles/TopRankPage.css';

function SongPage() {
  const navigate = useNavigate();

  // Example song data
  const songs = [
    { id: 1, title: "STARBOY", artist: "WEEKEND", rank: 1 },
    { id: 2, title: "The Mountain", artist: "Shawn Mendes", rank: 2 },
    { id: 3, title: "Good News", artist: "Blackbear", rank: 3 },
    { id: 4, title: "In My Bag", artist: "FLO, Gunilla", rank: 4 },
    // Add more songs as needed
  ];

  // Function to navigate back to the previous page
  const goBack = () => {
    navigate(-1); // Go back to the previous page
  };

  return (
    <div className="song-page">
      <button className="back-button" onClick={goBack}>
        <FontAwesomeIcon icon={faChevronLeft} /> Back
      </button>
      <div className="content-area">
        <h1>Songs</h1>

        <div className="song-cards">
          {songs.map((song) => (
            <div key={song.id} className="song-card">
              <img src={song.imageUrl} alt={song.title} />
              <div className="song-info">
                <h2>{song.title}</h2>
                <p>{song.artist}</p>
                <p className="rank">Rank: {song.rank}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SongPage;