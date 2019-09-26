import axios from 'axios';

export const http = axios.create({
  baseURL: 'http://192.168.88.9:8080/',
  headers: {
    Authorization: `Bearer ${localStorage.getItem('TOKEN')!}`,
  },
});
