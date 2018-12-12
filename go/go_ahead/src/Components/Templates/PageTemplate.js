import React from "react";

import { NavBar } from "Components";

const PageTemplate = props => (
  <div>
    <NavBar page={props.page} />
    <div>{props.children}</div>
  </div>
);

export default PageTemplate;
