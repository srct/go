import React from "react";
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

class NavBar extends React.Component {
  constructor(props) {
    super(props);

    this.toggleNavbar = this.toggleNavbar.bind(this);
    this.state = {
      collapsed: true
    };
  }

  toggleNavbar() {
    this.setState({
      collapsed: !this.state.collapsed
    });
  }

  render() {
    const { page } = this.props;
    return (
      <Navbar dark color="dark" expand="md">
        <Container>
          <NavbarBrand href="#/">
            <img
              src="static/go.svg"
              className="d-inline-block align-top"
              width="30"
              height="30"
              alt="SRCT Go"
            />
            Go
          </NavbarBrand>
          <NavbarToggler onClick={this.toggleNavbar} className="mr-2" />
          <Collapse isOpen={!this.state.collapsed} navbar>
            <Nav className="ml-auto" navbar>
              <NavItem>
                <NavLink href="#/dhaynes" active={page == "dhaynes"}>
                  Dhaynes
                </NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="#/about" active={page == "about"}>
                  About
                </NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="#/debug" active={page == "debug"}>
                  Debug
                </NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Container>
      </Navbar>
    );
  }
}

export default NavBar;
