import * as Yup from "yup";

const NewGoLinkValidator = Yup.object().shape({
  destination: Yup.string()
    .url()
    .max(1000, "Too Long!"),
  short: Yup.string()
    .required("Required")
    .max(20, "Too Long!"),
  expires: Yup.date()
    .nullable()
    .min(new Date())
});

export default NewGoLinkValidator;
