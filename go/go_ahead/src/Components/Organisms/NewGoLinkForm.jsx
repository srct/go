import React, { useState } from "react";
import NewGoLinkValidator from "../Molecules/NewGoLinkValidator";
import { Formik, Field, Form } from "formik";
import { GetCSRFToken } from "../../Utils/GetCSRFToken";
import { SingleDatePicker } from "react-dates";
import moment from "moment";
import {
  FormGroup,
  Button,
  Label,
  FormText,
  Row,
  Col,
  InputGroup,
  InputGroupAddon,
  InputGroupText
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
  var today = new Date();
  var tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);

  return (
    <Formik
      //
      initialValues={{
        shortcode: "",
        targetURL: ""
        // willExpire: false,
        // expires: moment(tomorrow)
      }}
      //
      validationSchema={NewGoLinkValidator}
      //
      onSubmit={({ targetURL }, { setSubmitting }) => {
        console.log("submitting..");
        console.log(targetURL);
        setSubmitting(false);
      }}
      //
      render={({
        values,
        isSubmitting,
        setFieldValue,
        errors,
        touched,
        handleBlur,
        handleChange
      }) => (
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
              <Button
                type="submit"
                disabled={isSubmitting}
                outline
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
