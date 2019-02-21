import React, { useState, useEffect } from "react";

/**
 * Hook to get whether or not the currently logged in user is registered.
 */
const useRegistrationCheck = () => {
  const [isRegistered, setIsRegistered] = useState(null);
  const [registeredLoaded, setRegisteredLoaded] = useState(false);

  const getRegistrationStatus = async () => {
    let response = await fetch("/auth/status/", {
      headers: {
        "Content-Type": "application/json"
      }
    });
    let data = await response.json();
    setIsRegistered(data.is_registered);
    setRegisteredLoaded(true);
  };

  useEffect(() => {
    getRegistrationStatus();
  }, []);

  return { isRegistered, registeredLoaded };
};

export default useRegistrationCheck;
