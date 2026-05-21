async function searchBook() {
  const input = document.getElementById("searchInput");
  const query = input.value;
  input.value = "";
  const res = await fetch("/search", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query})
  });
  const data = await res.json();
  document.getElementById("results").innerText = data.output;
}