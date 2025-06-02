import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3001", // Change to production URL as needed
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
