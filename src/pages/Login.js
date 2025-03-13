import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { loginUser } from '../services/auth'

import '../styles/Login.css';

function Login() {
  // Define state variables using useState hook
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      // Call the login endpoint with form data
      const response = await axios.post('http://localhost:8000/login', 
        new URLSearchParams({
          username: formData.email,
          password: formData.password
        }), {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }
      );

      if (response.data) {
        localStorage.setItem('token', response.data.access_token);
        localStorage.setItem('user', JSON.stringify({
          id: response.data.user_id,
          email: response.data.email,
          firstName: response.data.user_f_name,
          lastName: response.data.user_l_name
        }));
        navigate('/new');
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  // Add handleChange function
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="login-container">
      <button className="back-button" onClick={() => navigate('/')}>
        <FontAwesomeIcon icon={faChevronLeft} /> Back
      </button>
      <div className="login-box">
        <img src="logo.png" alt="Apple Music" className="logo" />
        <h2>Sign in to Apple Music</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          <button 
            type="submit" 
            className="login-button"
            disabled={loading}
          >
            {loading ? 'Signing In...' : 'Sign In'}
          </button>
        </form>
        <p className="signup-link">
          Don't have an account? <Link to="/signup">Sign up</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
