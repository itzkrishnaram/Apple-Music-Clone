// src/components/TopBar.js
import React from 'react';
import '../styles/TopBar.css';

const TopBar = () => {
  return (
    <div className="topbar">
      <div className="playback-controls">
        <button><i className="fas fa-random"></i></button>
        <button><i className="fas fa-step-backward"></i></button>
        <button><i className="fas fa-play"></i></button>
        <button><i className="fas fa-step-forward"></i></button>
        <button><i className="fas fa-redo"></i></button>
      </div>
      <div className="volume-controls">
        <button><i className="fas fa-volume-up"></i></button>
        <input type="range" className="volume-slider" min="0" max="100" />
      </div>
      <button className="sign-in-btn">Sign In</button>
    </div>
  );
};

export default TopBar;