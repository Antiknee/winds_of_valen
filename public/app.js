async function callAPI(endpoint) {
  const url = `/api/${endpoint}`;

  const container = document.getElementById("tableContainer");
  container.innerHTML = "<p>Loading...</p>";

  try {
    const response = await fetch(url);
    const data = await response.json();
    renderAnyJSON(data);
  } catch (err) {
    container.innerHTML = `<p class="error">Error calling ${endpoint}</p>`;
    console.error(err);
  }
}

function renderAnyJSON(data) {
  const container = document.getElementById("tableContainer");
  container.innerHTML = "";

  // If it's already a table-like structure
  if (Array.isArray(data.rows) && Array.isArray(data.columns)) {
    return renderTable(data.columns, data.rows);
  }

  // If it's an array of objects → convert to table
  if (Array.isArray(data) && typeof data[0] === "object") {
    const columns = Object.keys(data[0]);
    const rows = data.map(row => columns.map(col => row[col]));
    return renderTable(columns, rows);
  }

  // If it's a dict of lists → convert to table
  if (typeof data === "object") {
    const columns = Object.keys(data);
    const maxLen = Math.max(...columns.map(c => data[c].length || 1));
    const rows = [];

    for (let i = 0; i < maxLen; i++) {
      rows.push(columns.map(col => data[col][i] ?? ""));
    }

    return renderTable(columns, rows);
  }

  // Fallback: show raw JSON
  container.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

function renderTable(columns, rows) {
  const container = document.getElementById("tableContainer");
  const table = document.createElement("table");

  // Header
  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  columns.forEach(col => {
    const th = document.createElement("th");
    th.textContent = col;
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);
  table.appendChild(thead);

  // Body
  const tbody = document.createElement("tbody");
  rows.forEach(row => {
    const tr = document.createElement("tr");
    row.forEach(cell => {
      const td = document.createElement("td");
      td.textContent = cell;
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  container.innerHTML = "";
  container.appendChild(table);
}

// Bind buttons
document.querySelectorAll("button[data-endpoint]").forEach(btn => {
  btn.onclick = () => callAPI(btn.dataset.endpoint);
});
