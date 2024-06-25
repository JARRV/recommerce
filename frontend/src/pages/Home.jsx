 import React from 'react';
 import styled from 'styled-components';
 import HeaderImage from "/Users/roberttoribio/visa_hackathon/webscraping/frontend/src/utils/Images/Header.png";
 import LogoImg from "../utils/Images/Header.png"
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
  max-width: 1200px;

 `;
 const Home = () => {
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
     </Container>
   )
 }
 
 export default Home