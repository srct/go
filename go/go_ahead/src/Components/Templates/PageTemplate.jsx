import React from "react";
import { NavBar } from "Components";
import { Container } from "reactstrap";

const PageTemplate = props => (
  <div>
    <NavBar page={props.page} />
    <Container>{props.children}</Container>
  </div>
);

export default PageTemplate;
