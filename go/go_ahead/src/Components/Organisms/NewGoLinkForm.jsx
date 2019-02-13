import React, { useState } from "react";
import NewGoLinkValidator from "../Molecules/NewGoLinkValidator";
import { Formik, Field, Form } from "formik";
import { GetCSRFToken } from "../../Utils/GetCSRFToken";
import { SingleDatePicker } from "react-dates";
import moment from "moment";
import { FormGroup, Button, Label, FormText } from "reactstrap";
import MasonstrappedFormInput from "../Molecules/MasonstrappedFormInput";

const NewGoLinkForm = props => {
  const [focused, setFocused] = useState(false);
  var today = new Date();
  var tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);

  return (
    <Formik
      //
      initialValues={{
        // shortcode: "",
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
          <FormGroup>
            <Label for="targetURL">Target URL</Label>
            <Field
              name="targetURL"
              type="text"
              placeholder="https://longwebsitelink.com"
              component={MasonstrappedFormInput}
            />
            <FormText>Example help text that remains unchanged.</FormText>
          </FormGroup>

          <Button type="submit" disabled={isSubmitting} outline color="primary">
            Submit
          </Button>
        </Form>
      )}
    />
  );
};

export default NewGoLinkForm;
