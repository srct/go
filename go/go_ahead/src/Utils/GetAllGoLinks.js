async function GetAllGoLinks() {
  let response = await fetch("/api/golinks/", {
    headers: {
      "Content-Type": "application/json"
    }
  });
  let data = await response.json();
  return data;
}

export default GetAllGoLinks;
