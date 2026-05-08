import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const fetchArticles = async (limit = 50, offset = 0, source = null) => {
  try {
    const params = { limit, offset };
    if (source) {
      params.source = source;
    }
    const response = await api.get('/articles', { params });
    return response.data;
  } catch (error) {
    console.error('Error fetching articles:', error);
    throw error;
  }
};

export const fetchSources = async () => {
  try {
    const response = await api.get('/sources');
    return response.data;
  } catch (error) {
    console.error('Error fetching sources:', error);
    throw error;
  }
};

export const refreshFeeds = async () => {
  try {
    const response = await api.post('/refresh');
    return response.data;
  } catch (error) {
    console.error('Error refreshing feeds:', error);
    throw error;
  }
};

export default api;
