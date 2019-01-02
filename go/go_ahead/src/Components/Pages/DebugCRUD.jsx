import React from "react";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";
import { PageTemplate, DebugRead } from "Components";

const DebugCreate = Yup.object().shape({
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

class DebugCRUD extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  render() {
    return (
      <PageTemplate>
        <div>
          <h1>Debug CRUD Page</h1>

          <h3>Create</h3>
          <Formik
            initialValues={{ destination: "", short: "", expires: null }}
            validationSchema={DebugCreate}
            onSubmit={(values, { setSubmitting }) => {
              fetch("/api/golinks/", {
                method: "post",
                headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": this.getCookie("csrftoken")
                },
                body: JSON.stringify(values)
              }).then(response => console.log(response));
            }}
            render={({ isSubmitting }) => (
              <Form>
                <Field
                  name="destination"
                  placeholder="https://longwebsitelink.com"
                />{" "}
                <ErrorMessage name="destination" component="div" />
                <Field name="short" />
                <ErrorMessage name="short" />
                <Field type="select" name="expires" />
                <ErrorMessage name="expires" />
                <button type="submit" disabled={isSubmitting}>
                  Submit
                </button>
              </Form>
            )}
          />

          <h3>Read</h3>
          <DebugRead />

          <h3>Update</h3>
          <h3>Delete</h3>
        </div>
      </PageTemplate>
    );
  }
}

export default DebugCRUD;
