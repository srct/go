import React from "react";
import AuthedPageTemplate from "../Templates/AuthedPageTemplate";
import NewGolinkForm from "../Organisms/NewGoLinkForm";

const NewGoLinkPage = props => {
  return (
    <AuthedPageTemplate>
      <h2 className="mt-4 font-weight-light">Create a new Go link</h2>
      <p className="text-muted">
        A Go link is composed of the original "target" URL, and the shortcode to
        be used in the Go link.
      </p>
      <legend />
      <NewGolinkForm />
    </AuthedPageTemplate>
  );
};

export default NewGoLinkPage;
