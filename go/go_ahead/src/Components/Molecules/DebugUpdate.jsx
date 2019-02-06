import React from "react";
import * as Yup from "yup";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { GetCSRFToken } from "../../Utils";
import { FormGroup, Button, Card, CardBody, CardTitle } from "reactstrap";
import { SingleDatePicker } from "react-dates";
import moment from "moment";

const DebugUpdateYup = Yup.object().shape({
  destination: Yup.string()
    .url()
    .max(1000, "Too Long!"),
  oldshort: Yup.string()
    .required("Required")
    .max(20, "Too Long!"),
  newshort: Yup.string()
    .required("Required")
    .max(20, "Too Long!"),
  expires: Yup.date()
    .nullable()
    .min(new Date())
});

class DebugUpdate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      focused: false
    };
  }

  render() {
    return (
      <div>
        <Card>
          <CardBody>
            <CardTitle>Update</CardTitle>
            <Formik
              initialValues={{
                oldshort: "",
                newshort: "",
                newdestination: "",
                expires: moment(new Date())
              }}
              validationSchema={DebugUpdateYup}
              onSubmit={(
                { newshort, destination, expires },
                { setSubmitting }
              ) => {
                const updateURL = "/api/golinks/" + oldshort + "/";
                const payload = {
                  short: newshort,
                  destination: destination,
                  expires: expires.format()
                };
                fetch(updateURL, {
                  method: "put",
                  headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": GetCSRFToken()
                  },
                  body: JSON.stringify(payload)
                })
                  .then(response => console.log(response))
                  .then(setSubmitting(false));
              }}
              render={({ values, isSubmitting, setFieldValue }) => (
                <Form>
                  <FormGroup>
                    {"Old Short: "}
                    <Field className="form-control" name="oldshort" />
                    <ErrorMessage name="oldshort" />
                  </FormGroup>

                  <FormGroup>
                    {"New Destination: "}
                    <Field
                      className="form-control"
                      name="destination"
                      placeholder="https://longwebsitelink.com"
                    />
                    <ErrorMessage name="destination" component="div" />
                  </FormGroup>

                  <FormGroup>
                    {"New Short: "}
                    <Field className="form-control" name="newshort" />
                    <ErrorMessage name="newshort" />
                  </FormGroup>

                  <FormGroup>
                    {"Expires: "}
                    <br />
                    <SingleDatePicker
                      date={values["expires"]} // momentPropTypes.momentObj or null
                      onDateChange={date => setFieldValue("expires", date)} // PropTypes.func.isRequired
                      focused={this.state.focused} // PropTypes.bool
                      onFocusChange={({ focused }) =>
                        this.setState({ focused })
                      } // PropTypes.func.isRequired
                      id="expires" // PropTypes.string.isRequired,
                    />
                    <ErrorMessage name="expires" />
                  </FormGroup>
                  <Button
                    type="submit"
                    disabled={isSubmitting}
                    outline
                    color="primary"
                  >
                    Submit
                  </Button>
                </Form>
              )}
            />
          </CardBody>
        </Card>
      </div>
    );
  }
}
export default DebugUpdate;
