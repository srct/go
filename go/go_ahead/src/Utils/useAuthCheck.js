import React, { useState, useEffect } from "react";

const useAuthCheck = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(null);
  const [loaded, setLoaded] = useState(false);

  const getAuthStatus = async () => {
    let response = await fetch("/auth/status/", {
      headers: {
        "Content-Type": "application/json"
      }
    });
    let data = await response.json();
    setIsLoggedIn(data.is_authenticated);
    setLoaded(true);
  };

  useEffect(() => {
    getAuthStatus();
  }, []);

  return { isLoggedIn, loaded };
};

export default useAuthCheck;
