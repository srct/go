import * as Yup from "yup";

var today = new Date();
var tomorrow = new Date();
tomorrow.setDate(today.getDate() + 1);

const NewGoLinkValidator = Yup.object().shape({
  targetURL: Yup.string()
    .required("You must submit a target URL!")
    .url("Not a valid URL!")
    .max(1000, "URL is too long!"),
  shortcode: Yup.string()
    .required("You must submit a shortcode!")
    .max(20, "Your shortcode is too long!")
});

export default NewGoLinkValidator;
