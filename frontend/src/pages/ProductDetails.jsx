import React, { useEffect, useState } from 'react';
import styled from "styled-components"
import BigWaterDropIcon from '../components/BigWaterDropIcon.jsx';
import RecommerceCard from '../components/cards/RecommerceCard.jsx'
import { useNavigate, useParams } from "react-router-dom";

<link href='https://fonts.googleapis.com/css?family=Inter' rel='stylesheet'></link>

import {
    getOriginalItemDetail
} from "../api/index.js";

//image wrapper on left
//details on right
const Container = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 90%;
    font-family: Arial, Helvetica, sans-serif;
    font-color: black;
    `;
const Wrapper = styled.div`
    flex: 1;
    max-width: 1200px;
    display: flex;
   
    flex-direction: row;
    width: 100;
    padding: 12px;
    gap: 32px;
    @media (max-width; 768px) {
        flex-direction: column;
        justify-content: center;
    }
    `;
const ImageWrapper = styled.div`
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    `;
const Details = styled.div`
    display: flex;
    gap: 18px;
    flex-direction: column;
    padding: 4px 10px;
    flex: 1;
`;

const DetailsWrapper = styled.div`
    overflow-y: scroll;
    display: flex;
    gap: 18px;
    flex-direction: column;
    padding: 4px 10px;
    flex: 1;
`;

const WaterWrapper = styled.div`
    display: flex;
    flex-direction: row;
    flex: 1;
    margin-bottom: 10px;
    margin-top: -2px;
    
`;

const Water = styled.div`
    padding: 3px 3px 0px 0px;
    font-size: 15px;
    font-weight: 600;
    color: ${({ theme }) => theme.text_primary};
    `;

//ensures that scrollbar doesn't show but the user can still scroll if there are more cards than sapce in div, detailsWrapper
const scrollbarStyle = `
    div::-webkit-scrollbar {
        display: none;
    }
`;

const Image = styled.img`
    height: 800px;
    @media (max-width; 750px) {
        flex-direction: column;
        justify-content: center;
        height: 400px;
    }
    `;

const Icon = styled.img`
    height: 50px;
    @media (max-width; 50px) {
        flex-direction: column;
        justify-content: center;
        height: 400px;
    }
    `;

    const Title = styled.div`
        font-size: 30px;
        font-weight: 600;
        margin-bottom: 0px;
       
        `;

    const Brand = styled.div`
        font-size: 20px;
        font-weight: 400;
        color: ${({ theme }) => theme.text_primary};
        text-transform: uppercase;
        `;

    const Desc = styled.div`
        font-size: 16px;
        font-weight: 400;
        color: ${({ theme }) => theme.text_primary};
        `;
    
    
    const Price = styled.div`
        font-size: 18px;
        font-weight: 500;
        padding: 0px 0px 0px 2px;
        margin-top: 15px;
      
        color:grey;
        text-decoration: line-through;
        text-decoration-color: grey;
        `;

    const CardWrapper = styled.div`
        height: 600px;
        justify-content: center;
       
        `;
    
    const Card = styled.div`
        width: 100%;
        border-top: 3px solid grey;
        padding: 10px 0px 0px 0px;
        height: 140px;
        flex-direction: column;
        
        gap: 16px;
        `;
    
    const Button = styled.div`
        display: flex;
        width: 30%;
        padding: 10px;
        flex-wrap: wrap;
        gap: 24px;
        justify-content: center;
        background: black;
        color: white
        `;
    
    const Top = styled.div`
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        background: red;
        `;
    
    const Menu = styled.div`
        width: 90%;
        position: absolute;
        z-index: 10;
        
        bottom: 20px;
        display: flex;
        gap: 12px;
        `;

    const Button1 = styled.div`
        width: 100%;
        padding: 12px 20px;
        background: white;
        text-align: center;
        font-weight: 500;
        
        `;

const ProductDetails = () => {
    const { item_id } = useParams();
    const gallons_saved = {"dress": 1550, "jeans": 1800, "t-shirt": 850, "hoodie": 1720, "sweatshirt": 1720}
    const navigate = useNavigate();
    const [product, setProduct] = useState();
    const [recommerceProducts, setRecommerceProducts] = useState([]);
    const getProduct = async () => {
        //await getOriginalItemDetail(item_id).then((res) => {
        const object = localStorage.getItem('product');
        const item = JSON.parse(object);
        setProduct(item);
        setRecommerceProducts(item.similar_items)
        //remove it from localstorage 
        };
    
    useEffect(() => {
        getProduct();
    }, []);

    return (

        <Container>
            <Wrapper>
                <ImageWrapper>
                    <Image src={product?.picture_link}></Image>
                </ImageWrapper>
                <DetailsWrapper>
                    <style>
                        {scrollbarStyle}
                    </style>
                    <div>
                        <Title>{product?.item_name}</Title>
                        <WaterWrapper>
                            <Water>{gallons_saved[product?.item_type]} gallons of water saved</Water>
                            <BigWaterDropIcon />
                        </WaterWrapper>
                        <Brand>{product?.brand}</Brand>
                        <Price>${product?.price}</Price>
                        
                    </div>
                    <CardWrapper>
                        {recommerceProducts.map((recommerceProduct) => (
                                <RecommerceCard key={recommerceProduct.item_id} recommerceProduct={recommerceProduct} />
                            ))}
                    </CardWrapper>
                </DetailsWrapper>
            </Wrapper>
        </Container>
        
    );
}
 

export default ProductDetails

