import React, { useEffect, useState,useDispatch } from "react"; 
 import styled from 'styled-components';
 import HeaderImage from "../utils/Images/Header.png"
 import LogoImg from "../utils/Images/Header.png"
 import BlueMan from "../utils/Images/blue man.jpg"
 import BlueWoman from "../utils/Images/blue woman.jpg"
 import WaterHand from "../utils/Images/hand in water.jpg"
 import WaterDrop from "../utils/Images/water drop.jpg"
 import WaterWave from "../utils/Images/water wave.jpg"
 import SunglassWoman from "../utils/Images/sunglasses woman.jpg"
 import Jeans from "../utils/Images/jeans.jpg"
 import StandingMan from "../utils/Images/man standing.jpg"
 import ProductCard from "../components/cards/ProductCard";
 import { dummyProducts } from "../mockdata"; // Adjust the path as needed
 import { getOriginalItemDetail, getAllOriginalItems, getSimilarItems } from "../api";
 const Container = styled.div`
    padding: 20px 30px;
    padding-bottom: 200px;
    font-family: Arial, Helvetica, sans-serif;
    font-color: black;
    height:100%;
    display:flex;
    align-items:center;
    flex-direction:column;
    gap:30p; 
    @media (max-width:768px){
      padding:20px 12px;
    }
    background: ${({theme}) => theme.bg};
    
 `;
 //background: #f2f6fc;

 const Section = styled.div`
  max-width: 1400px;
  padding: 32px 16px;
  display: flex;
  flex-direction: column;
  gap: 0px;`;
  

 const Img = styled.img`
  width: 49%;
  height: 49%;

  `;

const ImgWrapper = styled.div`
  display: flex;
  gap:5px;
  @media (max-width: 750px) {
    gap: 5px;
  }
  
`;

const TextWrapper = styled.div`
  width: 107%;
  background: #5389a6;
  align-items: center;
  display: flex;
  @media (max-width: 750px) {
    gap: 5px;
  }
  
`;

const Column = styled.div`
  display: flex;
  flex-direction: column;
  gap:5px;
  @media (max-width: 750px) {
    gap: 5px;
  } 
`;

const Row = styled.div`
  display: flex;
  flex-direction: row;
  gap:5px;
  @media (max-width: 750px) {
    gap: 5px;
  } 
`;

  const Title = styled.div`
  font-size: 28px;
  font-weight: 500;
  display: flex;
  color: ${({ theme }) => theme.text_primary};
  margin-bottom: -20px;
  justify-content: ${({ center }) => (center ? "center" : "space-between")};
  align-items: center;
`;

const Quote = styled.div`
font-size: 30px;
padding: 100px 200px;
font-weight: 600;
color: white;

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
      console.log("ITEMS")
      console.log(items)
      const allItems = await fetchSimilarItems(items);
      
      console.log("HERE")
      
      const filteredItems = allItems.filter(item => item.similar_items.length > 0);
      const detailedFilteredItems = await calculatePercentage(filteredItems);
      setProducts(detailedFilteredItems);
      console.log(detailedFilteredItems);
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
          
          const updatedSimilarItems = item.similar_items.map(similarItem => {
            const percent_off = ((item.price - similarItem.price)/item.price) * 100
            const rounded_percent_off = Math.round(percent_off/5)*5;
            
            return {
              ...similarItem,
              percent_off: rounded_percent_off
            };
          });

          return {
            ...item,
            similar_items: updatedSimilarItems
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
          <ImgWrapper style={{marginLeft: '-50px', marginRight: '-50px'}}>
            <Row>
              <Column style={{width: '30%', height: '80%' }}>
                <img  src={BlueWoman} style={{ width: '100%', height: '70%' }} />
                <img  src={WaterWave} style={{ width: '100%', height: '30%' }}/>
              </Column>
              <Column style={{width: '70%', height: '80%'}}>
                
                <Row style={{ width: '100%', height:'100%' }}>
                  <Column >
                    <img  src={WaterDrop} style={{ width: '100%', height: '20%' }}/>
                    <img  src={SunglassWoman} style={{ width: '100%', height: '80%' }}/>
                  </Column>
                    <img  src={BlueMan} style={{ width: '35%', height: '100%' }}/>
                    <img  src={WaterHand} style={{  width: '35%', height: '100%' }}/>
                </Row>
                <Row style={{width: '100%', height: '40%'}}>
                  <img  src={Jeans} style={{ width: '70%', height: '100%' }}/>
                  <img src={StandingMan} style={{ width: '50%', height: '100%' }}/>
                </Row>
              </Column>
            </Row>
          </ImgWrapper>
       
          <TextWrapper>
            <Quote>
              "The fashion industry is the second largest consumer of water. Water is used for bleaching, dyeing, and growing cotton. 
              While water may have been considered en endless resource in the the early days od textile production, we now understand that clean water is precious and finite." 
             
            </Quote>
            
        </TextWrapper>
        
      </Section>

      <Section style={{width: '100%'}}>
        
        
      </Section>

      <Section>
        <Title>New Arrivals</Title>
        <p style={{height: '5px', color: '${({ theme }) => theme.text_secondary + 60}'}}><hr/></p>
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