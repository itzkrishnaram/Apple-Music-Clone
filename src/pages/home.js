// src/pages/home.js
import React from 'react';
import Sidebar from '../components/SideBar';
import TopBar from '../components/TopBar';
import MainContent from '../components/MainContents';
import '../styles/home.css';

const Home = () => {
  return (
    <div className="home">
      <Sidebar />
      <div className="main-wrapper">
        <TopBar />
        <MainContent />
      </div>
    </div>
  );
};

export default Home;