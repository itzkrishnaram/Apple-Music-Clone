import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Subscription.css';

function Subscription() {
  const navigate = useNavigate();

  const handleSubscribe = (plan) => {
    // Add subscription logic here
    navigate('/');
  };

  const goToUsersWithPlans = () => {
    // Navigate to the page showing users with plans
    navigate('/users-with-plans');
  };

  return (
    <div className="subscription-container">
      <div className="subscription-header">
        <img src="/apple-music-logo.png" alt="Apple Music" className="logo" />
        <h2>Choose Your Plan</h2>
      </div>
      
      <div className="plans-container">
        <div className="plan-card">
          <h3>Individual</h3>
          <p className="price">$10.99/month</p>
          <ul className="features">
            <li>Ad-free music listening</li>
            <li>Download to listen offline</li>
            <li>Original shows, concerts, and exclusives</li>
          </ul>
          <button onClick={() => handleSubscribe('individual')}>
            Try It Free
          </button>
        </div>

        <div className="plan-card featured">
          <h3>Family</h3>
          <p className="price">$16.99/month</p>
          <ul className="features">
            <li>All Individual features</li>
            <li>Up to 6 accounts</li>
            <li>Personal library for each member</li>
          </ul>
          <button onClick={() => handleSubscribe('family')}>
            Try It Free
          </button>
        </div>
      </div>
      {/* Button to go to the Users with Plans page */}
      <div className="users-plans-button">
        <button onClick={goToUsersWithPlans}>View Users with Plans</button>
      </div>
    </div>
  );
}

export default Subscription;
