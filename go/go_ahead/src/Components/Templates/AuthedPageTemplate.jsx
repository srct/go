import React from "react";
import { Container } from "reactstrap";
import useAuthCheck from "../../Utils/useAuthCheck";
import useRegistrationCheck from "../../Utils/useRegistrationCheck";
import RegisterPage from "../Pages/RegisterPage";

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
                <Container>
                  <RegisterPage />
                </Container>
              )}
            </div>
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
