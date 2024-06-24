import styled, { ThemeProvider } from "styled-components"
import { lightTheme } from "./utils/Themes"
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
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
        </Routes>
        Hi GFG   
      </Container>
    </BrowserRouter>
  </ThemeProvider>
}
export default App