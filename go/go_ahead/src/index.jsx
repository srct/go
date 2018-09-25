// Apply Global Masonstrap styling
import "masonstrap/build/css/masonstrap.min.css";
import "masonstrap/build/js/masonstrap.min.js";
import React from "react";
import ReactDOM from "react-dom";
import AuthButton from "./AuthButton.jsx";
import Golinkslist from "./GolinksList.jsx";

ReactDOM.render(
  <div>
    <AuthButton />
    <Golinkslist />
  </div>,
  document.getElementById("root")
);
