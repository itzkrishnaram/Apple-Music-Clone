import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';  // Import axios
import '../styles/song.css';

function Songs() {
  const navigate = useNavigate();
  
  // State to hold the song data
  const [songs, setSongs] = useState([]);
  const [loading, setLoading] = useState(true);  // Track loading state
  const [error, setError] = useState(null);  // Track any errors

  // Fetch songs with durations greater than 5 minutes
  useEffect(() => {
    const fetchSongs = async () => {
      try {
        const response = await fetch('http://localhost:8000/songs-duration-greater-than-5');
        if (!response.ok) {
          throw new Error('Failed to fetch songs');
        }
        const data = await response.json();
        setSongs(data.songs_duration_greater_than_5); // Ensure the key matches what the API returns
      } catch (error) {
        setError(error.message);
      }
    };

    fetchSongs();
  }, []);

return (
    <div className="songs-page">
      <button className="back-button" onClick={() => navigate('/')}>
        Back to Home
      </button>
      <div className="songs-content">
        <h1>Songs List (Duration > 5 minutes)</h1>
        <div className="songs-list">
          {songs.map((song) => (
            <div key={song.id} className="song-item">
              <h3>{song.name}</h3>
              <p>{song.duration} seconds</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Songs;