import React from "react";
import { PageTemplate } from "Components";
import useAuthCheck from "../../Utils/useAuthCheck";

const HomePage = () => {
  const { isLoggedIn, loaded } = useAuthCheck();

  return (
    <div>
      {loaded ? (
        <div>
          {isLoggedIn ? (
            <PageTemplate>
              <p>
                You're logged in and looking at the homepage which means you
                passed the auth check and we are now rendering the new homepage
                for logged in users but we haven't written it so you're looking
                at this sentence yeah.
              </p>
            </PageTemplate>
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
