import React from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
import '../styles/New.css';

function New() {
  const navigate = useNavigate();

  // Function to navigate to different pages
  const goToMusicPage = () => {
    navigate('/music'); // Navigate to the Music page
  };
  const goToAnirudhPage = () => {
    navigate('/anirudh'); // Navigate to the Anirudh page
  };
  const goToSongsPage = () => {
    navigate('/songs'); // Navigate to the Songs page
  };
  const goTotoprankPage = () => {
    navigate('/toprank');  // Navigate to the Top Ranked Songs page
  };
  return (
    <div className="new-page">
      <button className="back-button" onClick={() => navigate('/')}>
        <FontAwesomeIcon icon={faChevronLeft} /> Back
      </button>
      <div className="content-area">
        <h1>New</h1>

        <div className="featured-section">
          {/* Playlist Cards Row */}
          <div className="playlist-row">
            {/* Playlist Card 1 */}
            <div className="playlist-card" onClick={goToMusicPage}>
              <img src="/alistpop.png" alt="A-List Pop" />
              <h3>MUSIC DASHBOARD</h3>
              <h2>A-List Pop</h2>
              <p>Apple Music Pop</p>
            </div>

            {/* Playlist Card 2: Navigate to Anirudh Page */}
            <div className="playlist-card" onClick={goToAnirudhPage}>
              <img src="/ani.png" alt="Anirudh Hits" />
              <h3>ANIRUDH HITS</h3>
              <h2>Anirudh</h2>
              <p>Rock Hits</p>
            </div>

            {/* Playlist Card 3: Navigate to Songs Page */}
            <div className="playlist-card" onClick={goToSongsPage}>
              <img src="arr.png" alt="Dr. Dre Album" />
              <h2>LONG HITS</h2>
            </div>

            {/* Playlist Card 4: Navigate to Songs Page */}
            <div className="playlist-card" onClick={goTotoprankPage}>
              <img src="toprank.png" alt="Top Ranked Album" />
              <h2>TOP RANKED</h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default New;