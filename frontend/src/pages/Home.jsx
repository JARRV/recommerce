import React, { useEffect, useState,useDispatch } from "react"; 
 import styled from 'styled-components';
 import HeaderImage from "/Users/roberttoribio/visa_hackathon/webscraping/frontend/src/utils/Images/Header.png";
 import LogoImg from "../utils/Images/Header.png"
 import ProductCard from "../components/ProductCard";
 import { dummyProducts } from "../mockdata"; // Adjust the path as needed

 const Container = styled.div`
    padding: 20px 30px;
    padding-bottom: 200px;
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
   const [products, setProducts] = useState([]);
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
        <Title center>JARRV</Title>
        <CardWrapper>
          {dummyProducts.map((product) => (
            <ProductCard product={product} />
          ))}
        </CardWrapper>
      </Section>
     
     </Container>
   )
 }
 
 export default Home