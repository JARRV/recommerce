import React, { useEffect, useState,useDispatch } from "react"; 
 import styled from 'styled-components';
 import HeaderImage from "../utils/Images/Header.png"
 import LogoImg from "../utils/Images/Header.png"
 import ProductCard from "../components/cards/ProductCard";
 import { dummyProducts } from "../mockdata"; // Adjust the path as needed
 import { getOriginalItemDetail, getAllOriginalItems, getSimilarItems } from "../api";
 const Container = styled.div`
    padding: 20px 30px;
    padding-bottom: 200px;
    font-family: Arial, Helvetica, sans-serif;
    font-color: black;
    height:100%;
    overflow-y:scroll;
    display:flex;
    align-items:center;
    flex-direction:column;
    gap:30px; 
    @media (max-width:768px){
      padding:20px 12px;
    }
    background: ${({theme}) => theme.bg};
 `;
 const Section = styled.div`
  max-width: 1400px;
  padding: 32px 16px;
  display: flex;
  flex-direction: column;
  gap: 28px;`;

 const Img = styled.img`
  width: 90%;
  height: 700px;
  object-fit: cover;
  max-width: 1200px;`;

  const Title = styled.div`
  font-size: 28px;
  font-weight: 500;
  display: flex;
  
  justify-content: ${({ center }) => (center ? "center" : "space-between")};
  align-items: center;
`;

const CardWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  justify-content: center;
  @media (max-width: 750px) {
    gap: 14px;
  }
`;

 const Home = () => {

   const [loading, setLoading] = useState(false);
   const [products, setProducts] = useState([]);
   

   const getAllItems = async () => {
     setLoading(true);
    try{
      const res = await getAllOriginalItems();
      const items = res.data;
      const allItems = await fetchSimilarItems(items);
      
      console.log("HERE")
      console.log(allItems)
      const filteredItems = allItems.filter(item => item.similar_items.length > 0);
      const detailedFilteredItems = await calculatePercentage(filteredItems);
      setProducts(detailedFilteredItems);
    }
    catch(error){
      console.log("Failed to fetch original items:", error);
    }
    finally{
      setLoading(false);
      
    }
   };
   const fetchSimilarItems = async (items) => {
    try{
      const allItems = await Promise.all(
        items.map(async (item) =>{
          const similarRes = await getSimilarItems(item.item_id)
          // console.log(similarRes.data)

          const pricedSimilarItems = similarRes.data.filter(similarItem =>{
            return similarItem.price !== "Unknown" && item.price > similarItem.price;
          });

          const sortedSimilarItems = pricedSimilarItems.sort((a,b) => a.price - b.price);
          return{
            ...item, //takes all properties of item and spread them into a new object
            similar_items: sortedSimilarItems
          };
        })
      );
      return allItems;
    }
    catch(error){
      console.log("Failed to fetch similar items:", error);
    }
  };

  const calculatePercentage = async (filteredItems) => {
    try{
      const allItems = await Promise.all(
        filteredItems.map(async (item) =>{

          let newPrice = item.similar_items[0].price;
          let origPrice = item.price;
          
          let percentageOff = ((origPrice - newPrice)/origPrice)* 100;
          let roundedPercentageOff = Math.round((percentageOff) / 5) * 5;
          return{
            ...item, //takes all properties of item and spread them into a new object
            percent_off: roundedPercentageOff
          };
        })
      );
      return allItems;
    }
    catch(error){
      console.log("Failed to get percentage:", error);
    }
  };

   useEffect(() => {
     getAllItems();
   }, []);
   console.log(products[0])
  //  for (var i = 0; i < itemids.length; i++) {
  //   console.log(itemids[i]);
  //  }

  if (loading) {
    return <div>Loading...</div>;
  }
   return (
     <Container>
      <Section
        style={{alignItems:"center",}}>
   
            <Img src={LogoImg}/>
            <div> 
              <p>
                  Save Water  
                  <br/>kdfdsgwgryfsgsgf
                  <br/>sdfsfsffdhdghdfdhfshs
                  <br/>dgsdgfdgsfgfsfgggs
              </p>
            </div>
       
      </Section>

      <Section>
        <Title>JARRV</Title>
        <p><hr/></p>
        
        <CardWrapper>
          {products.map((product) => (
            <ProductCard key={product.id} product={product}/>
          ))}
        </CardWrapper>
      </Section>
     
     </Container>
   )
 }
 
 export default Home