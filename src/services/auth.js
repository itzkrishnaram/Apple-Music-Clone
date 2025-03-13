import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}/login`, 
      new URLSearchParams({
        username: credentials.email,
        password: credentials.password
      }), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
    return response.data;
  } catch (error) {
    throw error;
  }
};
