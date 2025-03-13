import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMusic } from '@fortawesome/free-solid-svg-icons';
import { useNavigate } from 'react-router-dom';
import '../styles/MainContents.css';

function MainContent() {
    const navigate = useNavigate();

  const handleSignIn = () => {
    navigate('/login');
  };

  const handleTryItFree = () => {
    navigate('/signup');
  };
  
  
  
  
  
    return (
    <div className="main-content">
      <div className="header">
        <img src="applumusic.png" alt="Apple Music" className="header-logo" />
        <button className="sign-in" onClick={handleSignIn}>Sign In</button>
      </div>
      <div className="hero-section">
        <div className="apple-music-logo">
          <img src="/applemiddle.png" alt="Apple Music" />
        </div>
        <h1>Discover new<br />music every day.</h1>
        <div className="music-icon">
          <FontAwesomeIcon icon={faMusic} />
        </div>
        <p>Get playlists and albums inspired by the artists and<br />genres you're listening to. 1 month free, then<br />$10.99/month.</p>
        <button className="try-free" onClick={handleTryItFree}>Try It Free</button>
        
        <a href="#" className="learn-more">Learn More ›</a>
      </div>
    </div>
  );
}

export default MainContent;
