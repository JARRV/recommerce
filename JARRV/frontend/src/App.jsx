import styled, { ThemeProvider } from "styled-components"
import { lightTheme } from "./utils/Themes"
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import ShopListing from "./pages/ShoppingList"
import Favorite from "./pages/Favorite";
import Cart from "./pages/Cart"
import ProductDetails from "./pages/ProductDetails"

const Container = styled.div`
  width:100%;
  height:100vh
  flex-direction:column;
  background:${({theme})=> theme.bg}; 
  color:${({theme}) => theme.text_primary};
  overflow-x:hidden;
  over-flow-y:hidden;
  transition: all 0.2s ease;
`;
function App(){
  return <ThemeProvider theme={lightTheme}>
    <BrowserRouter>
      <Container>
        <Navbar/>
        <Routes>
          <Route path='/' exact element ={<Home/>}/> 
          <Route path="/shop/:item_id" exact element={<ProductDetails/>} />
          <Route path="/favorite" exact element={<Favorite />} />
          <Route path="/cart" exact element={<Cart />} />
        </Routes>
      </Container>
    </BrowserRouter>
  </ThemeProvider>
}
export default App
