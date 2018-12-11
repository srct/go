import React from "react";
import { Navbar, NavbarBrand, Nav, NavItem, NavLink } from "reactstrap";

export default class NavBar extends React.Component {
  render() {
    return (
      <div>
        <Navbar color="dark" dark expand="md">
          <NavbarBrand href="#">Go</NavbarBrand>

          <Nav className="ml-auto" navbar>
            <NavItem>
              <NavLink href="#/dhaynes" active={this.props.page == "dhaynes"}>
                Dhaynes
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="#/about" active={this.props.page == "about"}>
                About
              </NavLink>
            </NavItem>
          </Nav>
        </Navbar>
      </div>
    );
  }
}
