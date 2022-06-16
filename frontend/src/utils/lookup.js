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
    const response = await fetch(`${URL}/api/v1${endpoint}`, {
      method,
      body: JSON.stringify(data),
      credentials: "include",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    return { data: await response.json(), status: response.status };
  }
}

export default JSONlookup;
