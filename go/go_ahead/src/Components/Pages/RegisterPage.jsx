import React from "react";
import { Row, Col } from "reactstrap";
import RegisterForm from "../Organisms/RegisterForm";

const RegisterPage = props => {
  return (
    <div>
      <Row>
        <Col>
          <h2 className="mt-4 font-weight-light">Register to use Go</h2>
        </Col>
      </Row>
      <Row>
        <Col>
          <p className="text-muted">
            In order to use Go you need to accept the terms of agreement.
          </p>
          <legend />
        </Col>
      </Row>
      <RegisterForm {...props} />
    </div>
  );
};

export default RegisterPage;
