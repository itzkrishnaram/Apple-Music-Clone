import React, { useState } from 'react';
import { registerUser } from '../services/userservices';
import { useNavigate, Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
import '../styles/SignUp.css';

function SignUp() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  
  const [error, setError] = useState(''); // [Added] To display error messages
  const [loading, setLoading] = useState(false);//new
  const navigate = useNavigate();
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // [Added] Reset error message
    setLoading(true);
    // [Added] Check if passwords match
    
    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    try {
      // [Added] Call the backend API to register the user
      const response = await registerUser({
        user_f_name: formData.firstName,  // Match FastAPI field name
      user_l_name: formData.lastName,   // Match FastAPI field name
      email: formData.email,
      password: formData.password
      });

      console.log(response);

      if (response?.user_id) {
        // Store user data if needed
        localStorage.setItem('user', JSON.stringify(response));
        // Remove the alert and directly navigate
        navigate('/subscription', { replace: true });
      }
    } catch (err) {
      // Handle specific error cases
      if (err.response?.status === 400 && err.response?.data?.detail === "Email already registered") {
        setError('This email is already registered. Please use a different email or sign in.');
      } else if (err.response?.status === 400) {
        setError(err.response?.data?.detail || 'Invalid input. Please check your details.');
      } else {
        setError('An error occurred. Please try again later.');
      }
    } finally {
      setLoading(false); // Stop loading
    }
  };

  return (
    <div className="signup-container">
        <button className="back-button" onClick={() => navigate('/')}>
        <FontAwesomeIcon icon={faChevronLeft} /> Back
      </button>
      <div className="signup-box">
        <div className="signup-header">
          <img src="logo.png" alt="Apple Music" className="logo" />
          <h2>Create Account</h2>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="form-group">
              <input
                type="text"
                name="firstName"
                placeholder="First Name"
                value={formData.firstName}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                name="lastName"
                placeholder="Last Name"
                value={formData.lastName}
                onChange={handleChange}
                required
              />
            </div>
          </div>

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

          <div className="form-group">
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit" className="signup-button">Create Account</button>
        </form>

        <div className="signup-footer">
          <p>Already have an account? <Link to="/login">Sign In</Link></p>
          <p className="terms">
            By creating an account, you agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default SignUp;
