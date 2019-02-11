import React from "react";
import { Container } from "reactstrap";
import useAuthCheck from "../../Utils/useAuthCheck";

const AuthedPageTemplate = props => {
  const { isLoggedIn, loaded } = useAuthCheck();

  return (
    <div>
      {loaded ? (
        <div>
          {isLoggedIn ? (
            <Container>{props.children}</Container>
          ) : (
            <h1>You're not authed!</h1>
          )}
        </div>
      ) : (
        <div />
      )}
    </div>
  );
};

export default AuthedPageTemplate;
