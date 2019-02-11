import React, { Suspense, lazy } from "react";
import { Route, withRouter, Switch } from "react-router-dom";
import { NavBar } from "Components";

const Home = lazy(() => import("../Components/Pages/HomePage"));
const Dhaynes = lazy(() => import("../Components/Pages/DhaynesPage"));
const About = lazy(() => import("../Components/Pages/AboutPage"));
const DebugCRUD = lazy(() => import("../Components/Pages/DebugCRUD"));

const NavBarWithRouter = withRouter(props => <NavBar {...props} />);

const Routes = () => (
  <div>
    <NavBarWithRouter />
    <Suspense fallback={<div>Loading...</div>}>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/dhaynes" component={Dhaynes} />
        <Route path="/about" component={About} />
        <Route path="/debug" component={DebugCRUD} />
        <Route render={() => <div>404</div>} />
      </Switch>
    </Suspense>
  </div>
);

export default Routes;
