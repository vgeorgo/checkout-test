
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 500,
  headers: { 'Content-Type': 'application/json' }
});

const getItems = () => {
  return api.get('/items');
}

const createOrder = () => {

}

export default {
  getItems,
  createOrder,
}