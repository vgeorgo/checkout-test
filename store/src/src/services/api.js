
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 500,
  headers: { 'Content-Type': 'application/json' },
  validateStatus: (status) => status >= 200 && status < 500,
});

const getItems = () => {
  return api.get('/items');
}

const createOrder = (payload) => {
  return api.post('/orders', payload);
}

export default {
  getItems,
  createOrder,
}