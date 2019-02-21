import React, { useState, useEffect } from "react";

const useAuthCheck = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(null);
  const [authLoaded, setAuthLoaded] = useState(false);

  const getAuthStatus = async () => {
    let response = await fetch("/auth/status/", {
      headers: {
        "Content-Type": "application/json"
      }
    });
    let data = await response.json();
    setIsLoggedIn(data.is_authenticated);
    setAuthLoaded(true);
  };

  useEffect(() => {
    getAuthStatus();
  }, []);

  return { isLoggedIn, authLoaded };
};

export default useAuthCheck;
