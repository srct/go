import React from "react";
import * as Yup from "yup";
import { GetCSRFToken } from "../../Utils";
import { Formik, Field, Form, ErrorMessage } from "formik";

const DebugDeleteYup = Yup.object().shape({
  short: Yup.string()
    .required("Required")
    .max(20, "Too Long!")
});

const DebugDelete = () => (
  <div>
    <Formik
      initialValues={{ short: "" }}
      validationSchema={DebugDeleteYup}
      onSubmit={(values, { setSubmitting }) => {
        const deleteURL = "/api/golinks/" + values.short;
        fetch(deleteURL, {
          method: "delete",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": GetCSRFToken()
          }
        })
          .then(response => console.log(response))
          .then(setSubmitting(false));
      }}
      render={({ isSubmitting }) => (
        <Form>
          {"Short: "}
          <Field name="short" />
          <ErrorMessage name="short" />
          <br />
          <button type="submit" disabled={isSubmitting}>
            Submit
          </button>
        </Form>
      )}
    />
  </div>
);

export default DebugDelete;
