import React, { useState } from "react";
import {
  Container,
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  NavbarToggler,
  Collapse
} from "reactstrap";
import { AuthButton } from "../";

const NavBar = props => {
  const [collapsed, setCollapsed] = useState(true);
  const { pathname } = props.location;

  return (
    <Navbar dark color="dark" expand="md">
      <Container>
        <NavbarBrand href="#/">
          <img
            src="static/go.svg"
            className="d-inline-block align-top"
            width="42"
            height="42"
            alt="SRCT Go"
          />
        </NavbarBrand>
        <NavbarToggler
          onClick={() => setCollapsed(!collapsed)}
          className="ml-auto"
        />
        <Collapse isOpen={!collapsed} navbar>
          <Nav className="mx-auto" navbar>
            <NavItem>
              <NavLink href="#/dhaynes" active={pathname == "/dhaynes"}>
                Dhaynes
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="#/about" active={pathname == "/about"}>
                About
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="#/debug" active={pathname == "/debug"}>
                Debug
              </NavLink>
            </NavItem>
          </Nav>
          <AuthButton className="ml-auto" />
        </Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
