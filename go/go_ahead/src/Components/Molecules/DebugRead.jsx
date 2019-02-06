import React from "react";
import { GetAllGoLinks } from "../../Utils";
import { Button, Card, CardBody, CardTitle, Table } from "reactstrap";

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
        <Card>
          <CardBody>
            <CardTitle className="d-flex">
              Read{" "}
              <Button
                className="ml-auto"
                onClick={this.refreshGoLinks}
                outline
                color="primary"
              >
                Refresh
              </Button>
            </CardTitle>

            <Table>
              <thead>
                <tr>
                  <th>short</th>
                  <th>destination</th>
                  <th>expires</th>
                </tr>
              </thead>
              <tbody>
                {this.state.GoLinks.map(golink => (
                  <tr key={golink.short}>
                    <td>
                      <a href={`/${golink.short}`}> /{golink.short}</a>
                    </td>
                    <td>{golink.destination}</td>
                    <td>{golink.date_expires}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </CardBody>
        </Card>
      </div>
    );
  }
}

export default DebugRead;
