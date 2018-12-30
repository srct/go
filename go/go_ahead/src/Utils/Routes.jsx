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

class Routes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      authToken: null
    };
  }

  componentDidMount() {
    fetch("/auth/token")
      .then(res => res.json())
      .then(
        result => {
          this.setState({
            authToken: result.token
          });
        },
        error => {
          this.setState({
            error
          });
        }
      );
  }

  render() {
    const { authToken } = this.state;
    return (
      <div>
        <NavBarWithRouter />
        <Route
          path="/"
          exact
          render={props => <HomePage {...props} authToken={authToken} />}
        />
        <Route
          path="/dhaynes"
          render={props => <DhaynesPage {...props} authToken={authToken} />}
        />
        <Route
          path="/about"
          render={props => <AboutPage {...props} authToken={authToken} />}
        />
        <Route
          path="/debug"
          render={props => <DebugCRUD {...props} authToken={authToken} />}
        />
      </div>
    );
  }
}

export default Routes;
