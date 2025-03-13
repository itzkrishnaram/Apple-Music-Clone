// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/NavBar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <Link to="/" className="navbar-logo">Apple Music</Link>
      </div>
      <div className="navbar-center">
        <Link to="/" className="navbar-item">Home</Link>
        <Link to="/new" className="navbar-item">New</Link>
        <Link to="/radio" className="navbar-item">Radio</Link>
      </div>
      <div className="navbar-right">
        <input type="text" placeholder="Search" className="navbar-search" />
        <button className="navbar-button">Open in Music</button>
        <button className="navbar-button">Try Beta</button>
        <button className="navbar-button">Sign In</button>
      </div>
    </nav>
  );
};

export default Navbar;
