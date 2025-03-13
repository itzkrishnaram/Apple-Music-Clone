import React from 'react';
import Sidebar from './components/SideBar';
import MainContent from './components/MainContents';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import New from './pages/New';
import Subscription from './pages/Subscription';
import UsersWithPlans from './pages/UsersWithPlans';
import './styles/App.css';
import Songs from './pages/song';
import Anirudh from './pages/Anirudh'
import TopRankPage from './pages/TopRankPage';  
import Music from './pages/Music'; // Assuming MusicDashboard is in the 'pages' directory


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <div className="app">
            <Sidebar />
            <MainContent />
          </div>
        } />
        <Route path="/signup" element={<Signup />} />
        <Route path="/new" element={<New />} />
        <Route path="/" element={<New />} />
        <Route path="/music" element={<Music />} /> 
        <Route path="/anirudh" element={<Anirudh />} />
        
        <Route path="/songs" element={<Songs />} />  {/* Route for Songs page */}
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/toprank" element={<TopRankPage />} />
        
        {/* Add this route */}

        <Route path="/subscription" element={<Subscription />} />
        <Route path="/users-with-plans" element={<UsersWithPlans />} />
        
        
      </Routes>
    </Router>
  );
}

export default App;

