import React from "react";
import * as Yup from "yup";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { GetCSRFToken } from "../../Utils";

const DebugCreateYup = Yup.object().shape({
  destination: Yup.string()
    .url()
    .max(1000, "Too Long!"),
  short: Yup.string()
    .required("Required")
    .max(20, "Too Long!")
  // expires: Yup.date()
  //   .nullable()
  //   .min(new Date(new Date().getTime() + 24 * 60 * 60 * 1000))
});

const DebugCreate = () => (
  <div>
    <Formik
      initialValues={{ destination: "", short: "", expires: null }}
      validationSchema={DebugCreateYup}
      onSubmit={(values, { setSubmitting }) => {
        fetch("/api/golinks/", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": GetCSRFToken()
          },
          body: JSON.stringify(values)
        })
          .then(response => console.log(response))
          .then(setSubmitting(false));
      }}
      render={({ isSubmitting }) => (
        <Form>
          {"Destination: "}
          <Field name="destination" placeholder="https://longwebsitelink.com" />
          <ErrorMessage name="destination" component="div" />
          <br />
          {"Short: "}
          <Field name="short" />
          <ErrorMessage name="short" />
          <br />
          {"Expires: "}
          <Field type="select" name="expires" placeholder="leave blank" />
          <ErrorMessage name="expires" />
          <br />
          <button type="submit" disabled={isSubmitting}>
            Submit
          </button>
        </Form>
      )}
    />
  </div>
);

export default DebugCreate;
