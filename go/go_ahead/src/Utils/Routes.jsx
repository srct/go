import React from "react";
import { Route, withRouter } from "react-router-dom";
import {
  HomePage,
  AboutPage,
  DhaynesPage,
  DebugCRUD,
  NavBar
} from "Components";

const NavBarWithRouter = withRouter(props => <NavBar {...props} />);

const Routes = () => (
  <div>
    <NavBarWithRouter />
    <Route path="/" exact component={HomePage} />
    <Route path="/dhaynes" component={DhaynesPage} />
    <Route path="/about" component={AboutPage} />
    <Route path="/debug" component={DebugCRUD} />
  </div>
);

export default Routes;
