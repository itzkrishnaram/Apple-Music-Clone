import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/SideBar.css';

function Sidebar() {
  const navigate = useNavigate();
  return (
    <div className="sidebar">
      <div className="logo">
        <img src="/sidebard.png" alt="Apple Music" />
      </div>
      <div className="search-bar">
        <input type="text" placeholder="Search" />
      </div>
      <nav className="nav-menu">
        <ul>
        <li onClick={() => navigate('/')}>Home</li>
          <li onClick={() => navigate('/new')}>New</li>
          <li>Radio</li>
        </ul>
      </nav>
    </div>
  );
}

export default Sidebar;
