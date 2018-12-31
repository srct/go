import React from "react";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";
import { PageTemplate, DebugRead } from "Components";

const SignupSchema = Yup.object().shape({
  password: Yup.string()
    .min(2, "Too Short!")
    .max(50, "Too Long!"),
  email: Yup.string()
    .email("Invalid email")
    .required("Required")
});

class DebugCRUD extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <PageTemplate>
        <div>
          <h1>Debug CRUD Page</h1>

          <h3>Create</h3>
          <Formik
            initialValues={{ email: "", password: "" }}
            validationSchema={SignupSchema}
            onSubmit={(values, { setSubmitting }) => {
              setTimeout(() => {
                console.log(JSON.stringify(values, null, 2));
                setSubmitting(false);
              }, 400);
            }}
            render={({ isSubmitting }) => (
              <Form>
                <Field type="email" name="email" placeholder="Email" />
                <ErrorMessage name="email" component="div" />
                <Field type="password" name="password" />
                <ErrorMessage name="password" />
                <button type="submit" disabled={isSubmitting}>
                  Submit
                </button>
              </Form>
            )}
          />

          <h3>Read</h3>
          <DebugRead />

          <h3>Update</h3>
          <Formik
            initialValues={{ email: "", password: "" }}
            validationSchema={SignupSchema}
            onSubmit={(values, { setSubmitting }) => {
              setTimeout(() => {
                console.log(JSON.stringify(values, null, 2));
                setSubmitting(false);
              }, 400);
            }}
            render={({ isSubmitting }) => (
              <Form>
                <Field type="email" name="email" placeholder="Email" />
                <ErrorMessage name="email" component="div" />
                <Field type="password" name="password" />
                <ErrorMessage name="password" />
                <button type="submit" disabled={isSubmitting}>
                  Submit
                </button>
              </Form>
            )}
          />

          <h3>Delete</h3>
          <Formik
            initialValues={{ email: "", password: "" }}
            validationSchema={SignupSchema}
            onSubmit={(values, { setSubmitting }) => {
              setTimeout(() => {
                console.log(JSON.stringify(values, null, 2));
                setSubmitting(false);
              }, 400);
            }}
            render={({ isSubmitting }) => (
              <Form>
                <Field type="email" name="email" placeholder="Email" />
                <ErrorMessage name="email" component="div" />
                <Field type="password" name="password" />
                <ErrorMessage name="password" />
                <button type="submit" disabled={isSubmitting}>
                  Submit
                </button>
              </Form>
            )}
          />
        </div>
      </PageTemplate>
    );
  }
}

export default DebugCRUD;
