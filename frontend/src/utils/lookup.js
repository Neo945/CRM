const URL = "http://localhost:8000";

// function JSONlookup(method, endpoint, parameters, data) {
//   return new Promise((resolve, reject) => {
//     fetch(`${URL}/api${endpoint}${parameters}`, {
//       method,
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(data),
//     })
//       .then((response) => response.json())
//       .then((json) => resolve(json))
//       .catch((error) => reject(error));
//   });
// }
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

async function JSONlookup(method, endpoint, parameters, data) {
  if (method === "GET") {
    const response = await fetch(`${URL}/api/v1${endpoint}${parameters}`, {
      method,
      credentials: "include",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });

    return { data: await response.json(), status: response.status };
  } else if (method === "POST") {
    const newData = { ...data, csrftoken: getCookie("csrftoken") };
    console.log(newData);
    const response = await fetch(`${URL}/api/v1${endpoint}`, {
      method,
      body: JSON.stringify(newData),
      credentials: "include",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
    });
    return { data: await response.json(), status: response.status };
  }
}

export default JSONlookup;
