import React from "react";
import { PageTemplate } from "Components";
import useAuthCheck from "../../Utils/useAuthCheck";
import RegisterPage from "../Pages/RegisterPage";
import useRegistrationCheck from "../../Utils/useRegistrationCheck";

const HomePage = () => {
  const { isLoggedIn, authLoaded } = useAuthCheck();
  const { isRegistered, registeredLoaded } = useRegistrationCheck();

  return (
    <div>
      {authLoaded && registeredLoaded ? (
        <div>
          {isLoggedIn ? (
            <div>
              {isRegistered ? (
                <PageTemplate>
                  <p>
                    You're logged in and looking at the homepage which means you
                    passed the auth check and we are now rendering the new
                    homepage for logged in users but we haven't written it so
                    you're looking at this sentence yeah.
                  </p>
                </PageTemplate>
              ) : (
                <PageTemplate>
                  <RegisterPage />
                </PageTemplate>
              )}
            </div>
          ) : (
            <PageTemplate>
              <p>
                You're not logged in and looking at the homepage which means you
                failed the auth check and we are now rendering the homepage for
                non logged in users but we haven't written it so you're looking
                at this sentence yeah.
              </p>
            </PageTemplate>
          )}
        </div>
      ) : (
        <div />
      )}
    </div>
  );
};

export default HomePage;
