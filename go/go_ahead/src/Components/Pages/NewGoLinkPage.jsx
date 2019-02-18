import React from "react";
import AuthedPageTemplate from "../Templates/AuthedPageTemplate";
import NewGolinkForm from "../Organisms/NewGoLinkForm";
import { Row, Col } from "reactstrap";

const NewGoLinkPage = props => {
  return (
    <AuthedPageTemplate {...props}>
      <Row>
        <Col>
          <h2 className="mt-4 font-weight-light">Create a new Go link</h2>
        </Col>
      </Row>
      <Row>
        <Col>
          <p className="text-muted">
            A Go link is composed of the original "target" URL, and the unique
            "shortcode" to be used in the Go link.
          </p>
          <legend />
        </Col>
      </Row>
      <NewGolinkForm {...props} />
    </AuthedPageTemplate>
  );
};

export default NewGoLinkPage;
