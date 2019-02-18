import React, { useState, useEffect } from "react";
import NewGoLinkValidator from "../Molecules/NewGoLinkValidator";
import { Formik, Field, Form } from "formik";
import GetCSRFToken from "../../Utils/GetCSRFToken";
import { SingleDatePicker } from "react-dates";
import ParseAPIErrors from "../../Utils/ParseAPIErrors";
import moment from "moment";
import {
  FormGroup,
  Button,
  Label,
  FormText,
  Row,
  Col,
  InputGroup,
  InputGroupAddon
} from "reactstrap";
import MasonstrappedFormInput from "../Molecules/MasonstrappedFormInput";

const divStyle = {
  display: "block"
};

const style2 = {
  borderTopLeftRadius: "0rem",
  borderBottomLeftRadius: "0rem"
};

const NewGoLinkForm = props => {
  const [focused, setFocused] = useState(false);
  const [expiresFieldDisabled, setexpiresFieldDisabled] = useState(true);
  var today = new Date();
  var tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);

  const toggleExpiresField = () => {
    setexpiresFieldDisabled(!expiresFieldDisabled);
  };

  return (
    <Formik
      // Init our form with some blank values
      initialValues={{
        shortcode: "",
        targetURL: "",
        expires: moment(tomorrow) // You must set a default date to start with
      }}
      // Yup client side validation
      validationSchema={NewGoLinkValidator}
      // Handle form submission
      onSubmit={(
        { targetURL, shortcode, expires },
        { setSubmitting, setErrors }
      ) => {
        if (expiresFieldDisabled) {
          expires = null;
        } else {
          expires = expires.format();
        }

        const APISubmission = {
          destination: targetURL,
          short: shortcode,
          date_expires: expires
        };

        fetch("/api/golinks/", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": GetCSRFToken()
          },
          body: JSON.stringify(APISubmission)
        }).then(response => {
          response.json().then(body => {
            if (!response.ok) {
              console.log(body);
              const parsedAPIErrors = ParseAPIErrors(body);
              setErrors(parsedAPIErrors);
            } else {
              props.history.push("/debug");
            }
          });
        });
        setSubmitting(false);
      }}
      // Render out our form
      render={({ values, isSubmitting, setFieldValue, errors }) => (
        <Form>
          <Row>
            <Col md="12">
              <FormGroup>
                <Label for="targetURL">Target URL</Label>
                <Field
                  name="targetURL"
                  type="text"
                  placeholder="https://longwebsitelink.com"
                  component={MasonstrappedFormInput}
                />
                <FormText>The URL that you would like to shorten.</FormText>
              </FormGroup>
            </Col>
          </Row>

          <Row>
            <Col>
              <FormGroup>
                <Label for="shortcode">Shortcode</Label>
                <InputGroup>
                  <InputGroupAddon addonType="prepend" style={divStyle}>
                    https://go.gmu.edu/
                  </InputGroupAddon>
                  <Field
                    name="shortcode"
                    type="text"
                    placeholder=""
                    className="form-control"
                    style={style2}
                    component={MasonstrappedFormInput}
                  />
                </InputGroup>
                <FormText>The unique address for your target URL.</FormText>
              </FormGroup>
            </Col>
          </Row>

          <legend />

          <Row>
            <Col>
              <h4 className="font-weight-light">
                (Optional) Expire your Go link.
              </h4>
            </Col>
          </Row>

          <Row>
            <Col>
              <p className="text-muted">
                A Go link may be set to expire on a specific date. When that
                happens, anyone who visits the Go link will not be redirected to
                the target URL and the shortcode will be freed up for other
                users to use. You cannot un-expire a Go link.
              </p>
            </Col>
          </Row>

          <Row>
            <Col>
              <div className="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  className="custom-control-input"
                  id="customCheck1"
                  onChange={toggleExpiresField}
                />
                <label className="custom-control-label" htmlFor="customCheck1">
                  Expire my Go link.
                </label>
              </div>
            </Col>
          </Row>

          <Row>
            <Col>
              <FormGroup>
                <Label className="mt-3" htmlFor="expires">
                  Date of Expiration
                </Label>{" "}
                <br />
                <SingleDatePicker
                  date={values["expires"]} // momentPropTypes.momentObj or null
                  onDateChange={date => setFieldValue("expires", date)} // PropTypes.func.isRequired
                  focused={focused} // PropTypes.bool
                  onFocusChange={({ focused }) => setFocused(focused)} // PropTypes.func.isRequired
                  id="expires" // PropTypes.string.isRequired,
                  disabled={expiresFieldDisabled}
                  readOnly={true}
                  showDefaultInputIcon={true}
                  numberOfMonths={1}
                />
                <FormText>
                  You cannot expire Go links on the same day (or before) they
                  are created.
                </FormText>
                {errors.expires ? <div>{errors.expires}</div> : null}
              </FormGroup>
            </Col>
          </Row>

          <legend />

          <Row>
            <Col>
              <h4 className="font-weight-light">
                (Optional) Force GMU login before redirect.
              </h4>
            </Col>
          </Row>

          <Row>
            <Col>
              <p className="text-muted">
                A Go link that forces login requires any user to first log in
                before being redirected to the target URL. This may be used to
                protect target URLs from non GMU users.
              </p>
            </Col>
          </Row>

          <Row>
            <Col>
              <div className="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  className="custom-control-input"
                  disabled={true}
                />
                <label className="custom-control-label">
                  Require GMU login.
                </label>
              </div>
            </Col>
          </Row>

          <legend />

          <Row>
            <Col>
              <h4 className="font-weight-light">
                (Optional) Self destruct your Go link.
              </h4>
            </Col>
          </Row>

          <Row>
            <Col>
              <p className="text-muted">
                A Go link that is set to self destruct will delete itself after
                a number of clicks. For example if a Go link is set to self
                destruct after 1 click, the moment after the first person vists
                the link, the Go link is deleted. This can be used as an
                alternative to date expiration if you know exactly how many
                times Go should process redirects for your Go link.
              </p>
            </Col>
          </Row>

          <Row>
            <Col>
              <div className="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  className="custom-control-input"
                  disabled={true}
                />
                <label className="custom-control-label">
                  Self destruct my Go link.
                </label>
              </div>
            </Col>
          </Row>

          <legend />

          <Row>
            <Col md="4">
              <Button
                type="submit"
                disabled={isSubmitting}
                outline
                block
                color="primary"
              >
                Submit
              </Button>
            </Col>
          </Row>
        </Form>
      )}
    />
  );
};

export default NewGoLinkForm;
