import React from "react";
import { Route } from "react-router-dom";
import { HomePage, AboutPage, DhaynesPage, DebugCRUD } from "Components";

const Routes = () => (
  <div>
    <Route path="/" exact component={HomePage} />
    <Route path="/dhaynes" component={DhaynesPage} />
    <Route path="/about" component={AboutPage} />
    <Route path="/debug" component={DebugCRUD} />
  </div>
);

export default Routes;
