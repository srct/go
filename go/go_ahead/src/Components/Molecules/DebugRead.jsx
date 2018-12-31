import React from "react";
import { GetAllGoLinks } from "../../Utils";
import { Button } from "reactstrap";

class DebugRead extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      GoLinks: [],
      error: null
    };
    // This binding is necessary to make `this` work in the callback
    this.refreshGoLinks = this.refreshGoLinks.bind(this);
  }

  async refreshGoLinks() {
    GetAllGoLinks()
      .then(data =>
        this.setState({
          GoLinks: data
        })
      )
      .catch(reason => this.setState({ error: reason }));
  }

  async componentDidMount() {
    this.refreshGoLinks();
  }

  render() {
    return (
      <div>
        <Button onClick={this.refreshGoLinks} color="primary">
          Refresh
        </Button>{" "}
        {this.state.GoLinks.map(golink => (
          <li key={golink.short}>
            <a href={`/${golink.short}`}> /{golink.short}</a> |{" "}
            {golink.destination}
          </li>
        ))}
      </div>
    );
  }
}

export default DebugRead;
