import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import HomePage from "./Pages/Hero";
import Hero from p
// import AboutPage from "./pages/AboutPage";
// import ContactPage from "./pages/ContactPage";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <HomePage />
        </Route>
        {/* <Route path="/about">
          <AboutPage />
        </Route>
        <Route path="/contact">
          <ContactPage />
        </Route> */}
      </Switch>
    </Router>
  );
}

export default App;
