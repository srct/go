import React from "react";
import ReactDOM from "react-dom";
import { HashRouter } from "react-router-dom";

import { Routes } from "Utils";

// Apply Global Masonstrap styling
import "masonstrap/build/css/masonstrap.min.css";
import "masonstrap/build/js/masonstrap.min.js";

ReactDOM.render(
  <HashRouter>
    <Routes />
  </HashRouter>,
  document.getElementById("root")
);
