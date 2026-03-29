import axios from 'axios';

const API_BASE_URL = 'http://localhost:8001';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const queryAgent = async (userInput, userProfile) => {
  try {
    const response = await apiClient.post('/query', {
      user_input: userInput,
      user_profile: userProfile,
    });
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export default apiClient;
