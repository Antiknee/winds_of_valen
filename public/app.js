async function callAPI(endpoint) {
  const url = `/api/${endpoint}`;

  const table = document.getElementById("tableContainer");
  const forest = document.getElementById("forestOutput");
  const debug = document.getElementById("debugOutput");

  table.innerHTML = "";
  forest.innerHTML = "";
  debug.innerHTML = "Loading...";

  try {
    const response = await fetch(url);
    const data = await response.json();

    // Show debug info
    debug.innerHTML = JSON.stringify(data, null, 2);

    // If backend returned text (forest)
    if (data.text) {
      forest.innerHTML = data.text;
      return;
    }

    // If backend returned a table-like structure
    if (data.return_value && typeof data.return_value === "object") {
      renderAnyJSON(data.return_value);
      return;
    }

  } catch (err) {
    debug.innerHTML = `Frontend error: ${err}`;
  }
}


function renderAnyJSON(data) {
  const container = document.getElementById("tableContainer");
  container.innerHTML = "";

  if (Array.isArray(data.rows) && Array.isArray(data.columns)) {
    return renderTable(data.columns, data.rows);
  }

  if (Array.isArray(data) && typeof data[0] === "object") {
    const columns = Object.keys(data[0]);
    const rows = data.map(row => columns.map(col => row[col]));
    return renderTable(columns, rows);
  }

  if (typeof data === "object") {
    const columns = Object.keys(data);
    const maxLen = Math.max(...columns.map(c => data[c].length || 1));
    const rows = [];

    for (let i = 0; i < maxLen; i++) {
      rows.push(columns.map(col => data[col][i] ?? ""));
    }

    return renderTable(columns, rows);
  }

  container.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

function renderTable(columns, rows) {
  const container = document.getElementById("tableContainer");
  const table = document.createElement("table");

  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  columns.forEach(col => {
    const th = document.createElement("th");
    th.textContent = col;
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);
  table.appendChild(thead);

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

// Forest button
document.getElementById("forestBtn").onclick = () => callAPI("print_global_forest");
