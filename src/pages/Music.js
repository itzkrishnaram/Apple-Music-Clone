import React from 'react';
import '../styles/Music.css';

import { useNavigate } from 'react-router-dom'; // Make sure to import useNavigate

const MusicDashboard = () => {
  const navigate = useNavigate();

  // Example album data
  const albums = [
    { id: 1, name: "A-List Pop", averageDuration: 3.5, imageUrl: "avg1.png" },
    { id: 2, name: "Anirudh Hits", averageDuration: 4.2, imageUrl: "/avg2.png" },
    { id: 3, name: "Hip Hop Classics", averageDuration: 3.8, imageUrl: "/avg3.png" },
    { id: 4, name: "Summer Vibes", averageDuration: 3.2, imageUrl: "/avg4.png" },
    { id: 5, name: "Rock Legends", averageDuration: 5.1, imageUrl: "/avg5.png" },
    { id: 6, name: "Pop Party", averageDuration: 4.0, imageUrl: "/avg6.png" },
    { id: 7, name: "Indie Beats", averageDuration: 4.3, imageUrl: "/avg7.png" },
    { id: 8, name: "Chillwave Essentials", averageDuration: 3.6, imageUrl: "/avg8.png" },
    { id: 9, name: "90s Rock Anthems", averageDuration: 5.0, imageUrl: "/avg9.png" }
  ];

  return (
    <div className="music-dashboard">
      <h1>Music Dashboard</h1>
      <div className="albums-grid">
        {albums.map(album => (
          <div
            key={album.id}
            className="album-card"
            onClick={() => navigate(`/album/${album.id}`)}  // Navigate to album details page
          >
            <img src={album.imageUrl} alt={album.name} />
            <h3>{album.name}</h3>
            <div className="average-duration">
              <p>Avg Duration: {album.averageDuration} mins</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MusicDashboard;