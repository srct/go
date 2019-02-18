import * as Yup from "yup";
import moment from "moment";

const NewGoLinkValidator = Yup.object().shape({
  targetURL: Yup.string()
    .required("You must submit a target URL!")
    .url("Not a valid URL!")
    .max(1000, "URL is too long!"),
  shortcode: Yup.string()
    .required("You must submit a shortcode!")
    .max(20, "Your shortcode is too long!"),
  expires: Yup.date()
    .nullable()
    .min(
      moment(new Date())
        .add(1, "days")
        .format(),
      "You cannot expire your Go link on that day."
    )
});

export default NewGoLinkValidator;
