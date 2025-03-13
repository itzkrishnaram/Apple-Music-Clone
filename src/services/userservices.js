import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000/users"; // Corrected the URL

// Function to register a new user
export const registerUser = async (userData) => {
  try {
    console.log("userData", userData)
    const response = await axios.post(API_BASE_URL + "/signup", userData); // Removed extra `/users/` from the URL
    return response.data;
  } catch (error) {
    console.error("Error during registration:", error.response?.data || error.message);
    throw error;
  }
};