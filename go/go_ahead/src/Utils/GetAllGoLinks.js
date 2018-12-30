async function GetAllGoLinks(token) {
  let response = await fetch("/auth/token");
  let data = await response.json();
  return data;
}

export default GetAllGoLinks;
