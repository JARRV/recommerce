import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000"
})


//Products 

export const getAllOriginalItems = async() =>
    await API.get(`/items/`);

export const getOriginalItemDetail = async (item_id) =>
    await API.get(`/items/${item_id}`);

export const getSimilarItems = async (item_id) =>
    await API.get(`/similar_items/${item_id}`);

export const getSimilarItemInfo = async (item_id) =>
    await API.get(`/similar_items/info/${item_id}`);



//User 

export const getUserList = async () => 
    await API.get(`/users/`);

export const getUserInfo = async(user_id) =>
    await API.get(`/users/${user_id}`);


//Purchase History

export const getAllPurchases = async () =>
    await API.get(`/purchase_history/`);

export const getPurchaseDetails = async(purchase_id) =>
    await API.get(`/purchase_history/${purchase_id}`)

export const getUserPurchaseHistory =async(user_id) =>
    await API.get(`/purchase_history/user/${user_id}`);

export const getItemPurchaseHistory = async(item_id) =>
    await API.get(`/purchase_history/item/${item_id}`)


