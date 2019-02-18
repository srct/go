import React from "react";
import { Input, FormFeedback } from "reactstrap";

/**
 * https://codebrains.io/build-react-forms-validation-formik-reactstrap/
 */
const MasonstrappedFormInput = ({
  field,
  form: { touched, errors },
  ...props
}) => (
  <div>
    <Input
      invalid={!!(touched[field.name] && errors[field.name])}
      {...field}
      {...props}
    />
    {touched[field.name] && errors[field.name] && (
      <FormFeedback>{errors[field.name]}</FormFeedback>
    )}
  </div>
);

export default MasonstrappedFormInput;
