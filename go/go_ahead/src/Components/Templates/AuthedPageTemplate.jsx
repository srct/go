import React from "react";
import { Container } from "reactstrap";
import useAuthCheck from "../../Utils/useAuthCheck";
import useRegistrationCheck from "../../Utils/useRegistrationCheck";

const AuthedPageTemplate = props => {
  const { isLoggedIn, authLoaded } = useAuthCheck();
  const { isRegistered, registeredLoaded } = useRegistrationCheck();

  return (
    <div>
      {authLoaded && registeredLoaded ? (
        <div>
          {isLoggedIn ? (
            <div>
              {isRegistered ? (
                <Container>{props.children}</Container>
              ) : (
                <div>You are logged in but not registered!</div>
              )}
            </div>
          ) : (
            <h1>You're not authed!</h1>
          )}
        </div>
      ) : (
        <div>shits fucked my man</div>
      )}
    </div>
  );
};

export default AuthedPageTemplate;
