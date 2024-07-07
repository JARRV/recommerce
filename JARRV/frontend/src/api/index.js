import axios from "axios";

const API = axios.create({
    baseURL: "jarrv.onrender.com" || "http://localhost:8000"
})


//Products 

export const getAllOriginalItems = async() =>
    await API.get(`/items/`);

export const getOriginalItemDetail = async (item_id) =>
    await API.get(`/items/${item_id}`);

export const getSimilarItems = async (item_id) =>
    await API.get(`/similar_items/${item_id}`);