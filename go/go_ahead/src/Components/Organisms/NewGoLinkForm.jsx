import React, { useState } from "react";
import NewGoLinkValidator from "../Molecules/NewGoLinkValidator";
import { Formik, Field, Form, ErrorMessage } from "formik";
import { GetCSRFToken } from "../../Utils/GetCSRFToken";
import { SingleDatePicker } from "react-dates";

const NewGoLinkForm = props => {
  const [focused, setFocused] = useState(false);

  return <div />;
};

export default NewGoLinkForm;
