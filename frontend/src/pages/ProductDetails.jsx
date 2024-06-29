import React, { useEffect, useState } from 'react';
import styled from "styled-components"

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
    width: 100;
    padding: 12px;
    gap: 32px;
    @media (max-width; 750px) {
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
    overflow-y: auto;
    display: flex;
    gap: 18px;
    flex-direction: column;
    padding: 4px 10px;
    flex: 1;
`;

const Image = styled.img`
    height: 800px;
    @media (max-width; 750px) {
        flex-direction: column;
        justify-content: center;
        height: 400px;
    }
    `;

    const Title = styled.div`
        font-size: 30px;
        font-weight: 600;
        margin-bottom: 10px;
       
        `;

    const Brand = styled.div`
        font-size: 20px;
        font-weight: 400;
        margin-bottom: 20px;
        color: ${({ theme }) => theme.text_primary};
        text-transform: uppercase;
        `;

    const Desc = styled.div`
        font-size: 16px;
        font-weight: 400;
        color: ${({ theme }) => theme.text_primary};
        `;
    
    const Price = styled.div`
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 22px;
        font-weight: 500;
        color: ${({ theme }) => theme.text_primary};
        `;

    const Span = styled.div`
        font-size: 22px;
        font-weight: 500;
        padding: 0px 0px 0px 5px;
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
                    <div>
                        <Title>{product?.item_name}</Title>
                        <Brand>{product?.brand}</Brand>
                        <Span>{product?.price}</Span>
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

