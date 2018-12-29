import React from "react";
import { Navbar, NavbarBrand, Nav, NavItem, NavLink } from "reactstrap";

const NavBar = props => (
  <div>
    <Navbar color="dark" dark expand="md">
      <NavbarBrand href="#">Go</NavbarBrand>

      <Nav className="ml-auto" navbar>
        <NavItem>
          <NavLink href="#/dhaynes" active={props.page == "dhaynes"}>
            Dhaynes
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink href="#/about" active={props.page == "about"}>
            About
          </NavLink>
        </NavItem>
      </Nav>
    </Navbar>
  </div>
);

export default NavBar;
