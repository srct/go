/**
 *
 *  const APISubmission = {
          destination: targetURL,
          short: shortcode,
          date_expires: expires
        };

 * Bind API errors on field submissions to local Formik fields.
 * @param {object} apiResponse
 */
const ParseAPIErrors = apiResponse => {
  const parsedAPIErrors = {};

  if (apiResponse.short) {
    if (apiResponse.short.length > 0) {
      parsedAPIErrors.shortcode = apiResponse.short[0];
    } else {
      parsedAPIErrors.shortcode = apiResponse.short;
    }
  }
  if (apiResponse.destination) {
    parsedAPIErrors.targetURL = apiResponse.targetURL;
  }
  if (apiResponse.date_expires) {
    parsedAPIErrors.expires = apiResponse.date_expires;
  }

  return parsedAPIErrors;
};

export default ParseAPIErrors;
