import React from "react";
import * as Yup from "yup";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { GetCSRFToken } from "../../Utils";

const DebugUpdateYup = Yup.object().shape({
  destination: Yup.string()
    .url()
    .max(1000, "Too Long!"),
  oldshort: Yup.string()
    .required("Required")
    .max(20, "Too Long!"),
  newshort: Yup.string()
    .required("Required")
    .max(20, "Too Long!")
  // expires: Yup.date()
  //   .nullable()
  //   .min(new Date(new Date().getTime() + 24 * 60 * 60 * 1000))
});

const DebugUpdate = () => (
  <div>
    <Formik
      initialValues={{
        oldshort: "",
        newshort: "",
        newdestination: "",
        expires: null
      }}
      validationSchema={DebugUpdateYup}
      onSubmit={(
        { newshort, oldshort, expires, destination },
        { setSubmitting }
      ) => {
        const updateURL = "/api/golinks/" + oldshort + "/";
        const payload = {
          short: newshort,
          destination: destination,
          expires: expires
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
      render={({ isSubmitting }) => (
        <Form>
          {"Old Short: "}
          <Field name="oldshort" />
          <ErrorMessage name="oldshort" />

          {"New Destination: "}
          <Field name="destination" placeholder="https://longwebsitelink.com" />
          <ErrorMessage name="destination" component="div" />

          {"New Short: "}
          <Field name="newshort" />
          <ErrorMessage name="newshort" />

          {"New Expires: "}
          <Field type="select" name="expires" placeholder="leave blank" />
          <ErrorMessage name="expires" />
          <button type="submit" disabled={isSubmitting}>
            Submit
          </button>
        </Form>
      )}
    />
  </div>
);
export default DebugUpdate;
