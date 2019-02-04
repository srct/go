import React from "react";
import { Container } from "reactstrap";

class AuthedPageTemplate extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isLoggedIn: null, loaded: false };
  }

  componentDidMount() {
    fetch("/auth/status/", {
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(r => r.json())
      .then(res =>
        this.setState({
          isLoggedIn: res.is_authenticated,
          loaded: true
        })
      );
  }

  render() {
    const { isLoggedIn, loaded } = this.state;
    return (
      <div>
        {loaded ? (
          <div>
            {isLoggedIn ? (
              <Container>{this.props.children}</Container>
            ) : (
              <h1>You're not authed!</h1>
            )}
          </div>
        ) : (
          <div />
        )}
      </div>
    );
  }
}

export default AuthedPageTemplate;
