import React from "react";
import { Button } from "reactstrap";

class AuthButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { error: null, is_auth: false };
  }

  componentDidMount() {
    fetch("/auth/status")
      .then(res => res.json())
      .then(
        result => {
          this.setState({
            is_auth: result.is_authenticated
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
    const { is_auth, error } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else {
      return (
        <div>
          {is_auth ? (
            <Button color="info" href="/auth/logout">
              Logout <i className="fas fa-sign-out-alt" />
            </Button>
          ) : (
            <Button color="info" href="/auth/login">
              Login <i className="fas fa-sign-in-alt" />
            </Button>
          )}
        </div>
      );
    }
  }
}

export default AuthButton;
