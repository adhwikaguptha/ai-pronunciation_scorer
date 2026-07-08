import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

export const analyzePronunciation = async (formData) => {
  const response = await api.post("/analyze", formData);

  return response.data;
};

export default api;