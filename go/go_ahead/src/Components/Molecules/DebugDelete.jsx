import React from "react";
import * as Yup from "yup";
import { GetCSRFToken } from "../../Utils";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { Button, Card, CardBody, CardTitle, FormGroup } from "reactstrap";

const DebugDeleteYup = Yup.object().shape({
  short: Yup.string()
    .required("Required")
    .max(20, "Too Long!")
});

const DebugDelete = () => (
  <div>
    <Card>
      <CardBody>
        <CardTitle>Delete</CardTitle>

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
              <FormGroup>
                {"Short: "}
                <Field className="form-control" name="short" />
                <ErrorMessage name="short" />
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

export default DebugDelete;
