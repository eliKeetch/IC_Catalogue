const state = {
  components: [],
  selectedId: null,
  search: "",
  category: "",
};

const listEl = document.querySelector("#component-list");
const detailEl = document.querySelector("#detail");
const searchEl = document.querySelector("#search");
const categoryEl = document.querySelector("#category-filter");
const dialog = document.querySelector("#component-dialog");
const form = document.querySelector("#component-form");

const DIP_PIN_COUNTS = new Set([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]);

const PACKAGE_MODELS = {
  mosfet_to220_3pin: {
    path: "/images/ic_pinout_blank_models/svg/mosfet_to220_3pin_blank.svg",
    label: "3-pin TO-220 MOSFET",
    layout: "inline",
  },
  mosfet_to220_5pin: {
    path: "/images/ic_pinout_blank_models/svg/mosfet_to220_5pin_blank.svg",
    label: "5-pin TO-220 MOSFET",
    layout: "inline",
  },
  transistor_to92_3pin: {
    path: "/images/ic_pinout_blank_models/svg/transistor_to92_3pin_blank.svg",
    label: "3-pin TO-92 transistor",
    layout: "inline",
  },
};

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || "Request failed");
  return data;
}

function linesToArray(value) {
  return value
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
}

function parsePins(value) {
  return linesToArray(value).map((line) => {
    const match = line.match(/^([^:]+):\s*([^-]+)(?:-\s*(.*))?$/);
    if (!match) return { pin: "", name: line, description: "" };
    return {
      pin: match[1].trim(),
      name: match[2].trim(),
      description: (match[3] || "").trim(),
    };
  });
}

function pinsToText(pins = []) {
  return pins.map((pin) => `${pin.pin}: ${pin.name}${pin.description ? ` - ${pin.description}` : ""}`).join("\n");
}

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function load() {
  const params = new URLSearchParams();
  if (state.search) params.set("q", state.search);
  if (state.category) params.set("category", state.category);
  state.components = await api(`/api/components?${params}`);
  const categories = await api("/api/categories");
  renderCategories(categories);
  renderList();
  renderStats();
  if (state.selectedId && state.components.some((item) => item.id === state.selectedId)) {
    renderDetail(state.components.find((item) => item.id === state.selectedId));
  } else if (state.components.length) {
    selectComponent(state.components[0].id);
  } else {
    detailEl.innerHTML = `<div class="empty-detail">No components match the current filters.</div>`;
  }
}

function renderCategories(categories) {
  const current = categoryEl.value;
  categoryEl.innerHTML = `<option value="">All categories</option>`;
  for (const category of categories) {
    const option = document.createElement("option");
    option.value = category;
    option.textContent = category;
    categoryEl.append(option);
  }
  categoryEl.value = current;
}

function renderStats() {
  const totalParts = state.components.reduce((sum, item) => sum + item.quantity, 0);
  document.querySelector("#component-count").textContent = `${state.components.length} components`;
  document.querySelector("#part-count").textContent = `${totalParts} total parts`;
}

function renderList() {
  if (!state.components.length) {
    listEl.innerHTML = `<div class="empty-state">No components yet. Add your first component to start the catalogue.</div>`;
    return;
  }

  listEl.innerHTML = state.components
    .map(
      (item) => `
        <article class="component-card ${item.id === state.selectedId ? "active" : ""}" data-id="${item.id}">
          <div class="card-main">
            <div class="card-title">
              <span>${escapeHtml(item.name)}</span>
              <span class="chip">${escapeHtml(item.category)}</span>
              ${item.package ? `<span class="chip">${escapeHtml(item.package)}</span>` : ""}
            </div>
            <p class="card-summary">${escapeHtml(item.summary || "No summary yet.")}</p>
          </div>
          <div class="quantity">
            <strong>${item.quantity}</strong>
            <div class="qty-actions">
              <button class="icon-button" data-qty="-1" data-id="${item.id}" aria-label="Decrease quantity">-</button>
              <button class="icon-button" data-qty="1" data-id="${item.id}" aria-label="Increase quantity">+</button>
            </div>
          </div>
        </article>
      `
    )
    .join("");
}

function renderDetail(item) {
  detailEl.innerHTML = `
    <div class="detail-head">
      <div class="detail-title-row">
        <h2>${escapeHtml(item.name)}</h2>
        <button id="edit-component">Edit</button>
      </div>
      <div class="meta">
        <span>${escapeHtml(item.category)}</span>
        ${item.package ? `<span>${escapeHtml(item.package)}</span>` : ""}
        ${item.location ? `<span>${escapeHtml(item.location)}</span>` : ""}
        <span>${item.quantity} on hand</span>
      </div>
      <p>${escapeHtml(item.summary || "No summary yet.")}</p>
    </div>

    ${renderListSection("Common Uses", item.uses)}
    ${renderListSection("Project Ideas", item.project_ideas)}
    ${renderPinout(item.pins, item.model_type)}
    ${renderDocuments(item)}
    ${renderNotes(item.notes)}
  `;
  document.querySelector("#edit-component").addEventListener("click", () => openDialog(item));
}

function renderListSection(title, values = []) {
  if (!values.length) return "";
  return `
    <section class="detail-section">
      <h3>${title}</h3>
      <ul>${values.map((value) => `<li>${escapeHtml(value)}</li>`).join("")}</ul>
    </section>
  `;
}

function renderPinout(pins = [], modelType = "") {
  if (!pins.length) return "";
  return `
    <section class="detail-section">
      <h3>Pinout</h3>
      ${renderPackageDiagram(pins, modelType)}
      <table class="pin-table">
        <thead><tr><th>Pin</th><th>Name</th><th>Description</th></tr></thead>
        <tbody>
          ${pins
            .map(
              (pin) => `
                <tr>
                  <td>${escapeHtml(pin.pin)}</td>
                  <td>${escapeHtml(pin.name)}</td>
                  <td>${escapeHtml(pin.description)}</td>
                </tr>
              `
            )
            .join("")}
        </tbody>
      </table>
    </section>
  `;
}

function renderPackageDiagram(pins = [], modelType = "") {
  const model = resolvePackageModel(pins, modelType);
  if (!model) return "";
  if (model.layout === "dip") return renderDipDiagram(pins, model);
  return renderInlinePackageDiagram(pins, model);
}

function resolvePackageModel(pins = [], modelType = "") {
  const normalized = modelType.trim();
  if (PACKAGE_MODELS[normalized]) return PACKAGE_MODELS[normalized];
  if (DIP_PIN_COUNTS.has(pins.length)) return dipModel(pins.length);
  return null;
}

function dipModel(count) {
  return {
    path: `/images/ic_pinout_blank_models/svg/dip_${String(count).padStart(2, "0")}_blank.svg`,
    label: `${count}-pin DIP`,
    layout: "dip",
  };
}

function renderDipDiagram(pins = [], model) {
  const count = pins.length;
  if (!DIP_PIN_COUNTS.has(count)) return "";

  const half = count / 2;
  const leftPins = pins.slice(0, half);
  const rightPins = pins.slice(half).reverse();

  return `
    <div class="dip-pinout" style="--pin-rows: ${half};">
      <div class="dip-labels dip-labels-left">
        ${leftPins.map((pin) => renderPinLabel(pin)).join("")}
      </div>
      <div class="pinout-model dip-model" aria-label="${escapeHtml(model.label)} package model">
        <img src="${model.path}" alt="${escapeHtml(model.label)} blank pinout model">
        <span>${escapeHtml(model.label)}</span>
      </div>
      <div class="dip-labels dip-labels-right">
        ${rightPins.map((pin) => renderPinLabel(pin)).join("")}
      </div>
    </div>
  `;
}

function renderInlinePackageDiagram(pins = [], model) {
  return `
    <div class="inline-pinout" style="--inline-pins: ${pins.length};">
      <div class="pinout-model inline-model" aria-label="${escapeHtml(model.label)} package model">
        <img src="${model.path}" alt="${escapeHtml(model.label)} blank pinout model">
        <span>${escapeHtml(model.label)}</span>
      </div>
      <div class="inline-labels">
        ${pins.map((pin) => renderPinLabel(pin)).join("")}
      </div>
    </div>
  `;
}

function renderPinLabel(pin) {
  return `
    <div class="pin-label" title="${escapeHtml(pin.description || "")}">
      <span class="pin-number">${escapeHtml(pin.pin)}</span>
      <strong>${escapeHtml(pin.name)}</strong>
    </div>
  `;
}

function renderDocuments(item) {
  const docs = [...(item.documents || [])];
  if (item.datasheet_url) docs.unshift(item.datasheet_url);
  if (!docs.length) return "";
  return `
    <section class="detail-section">
      <h3>Documents</h3>
      <ul>
        ${docs
          .map((doc) => `<li><a href="${escapeHtml(doc)}" target="_blank" rel="noreferrer">${escapeHtml(doc)}</a></li>`)
          .join("")}
      </ul>
    </section>
  `;
}

function renderNotes(notes) {
  if (!notes) return "";
  return `
    <section class="detail-section">
      <h3>Notes</h3>
      <p>${escapeHtml(notes)}</p>
    </section>
  `;
}

function selectComponent(id) {
  state.selectedId = id;
  const item = state.components.find((component) => component.id === id);
  renderList();
  if (item) renderDetail(item);
}

function openDialog(item = null) {
  document.querySelector("#dialog-title").textContent = item ? "Edit Component" : "Add Component";
  document.querySelector("#component-id").value = item?.id || "";
  document.querySelector("#name").value = item?.name || "";
  document.querySelector("#category").value = item?.category || "";
  document.querySelector("#package").value = item?.package || "";
  document.querySelector("#quantity").value = item?.quantity || 0;
  document.querySelector("#location").value = item?.location || "";
  document.querySelector("#model_type").value = item?.model_type || "";
  document.querySelector("#datasheet_url").value = item?.datasheet_url || "";
  document.querySelector("#summary").value = item?.summary || "";
  document.querySelector("#uses").value = (item?.uses || []).join("\n");
  document.querySelector("#project_ideas").value = (item?.project_ideas || []).join("\n");
  document.querySelector("#pins").value = pinsToText(item?.pins || []);
  document.querySelector("#documents").value = (item?.documents || []).join("\n");
  document.querySelector("#notes").value = item?.notes || "";
  dialog.showModal();
}

async function saveComponent(event) {
  event.preventDefault();
  const id = document.querySelector("#component-id").value;
  const payload = {
    name: document.querySelector("#name").value,
    category: document.querySelector("#category").value,
    package: document.querySelector("#package").value,
    quantity: Number(document.querySelector("#quantity").value || 0),
    location: document.querySelector("#location").value,
    model_type: document.querySelector("#model_type").value,
    datasheet_url: document.querySelector("#datasheet_url").value,
    summary: document.querySelector("#summary").value,
    uses: linesToArray(document.querySelector("#uses").value),
    project_ideas: linesToArray(document.querySelector("#project_ideas").value),
    pins: parsePins(document.querySelector("#pins").value),
    documents: linesToArray(document.querySelector("#documents").value),
    notes: document.querySelector("#notes").value,
  };

  const saved = id
    ? await api(`/api/components/${id}`, { method: "PUT", body: JSON.stringify(payload) })
    : await api("/api/components", { method: "POST", body: JSON.stringify(payload) });
  state.selectedId = saved.id;
  dialog.close();
  await load();
}

listEl.addEventListener("click", async (event) => {
  const qtyButton = event.target.closest("[data-qty]");
  if (qtyButton) {
    event.stopPropagation();
    const id = Number(qtyButton.dataset.id);
    const delta = Number(qtyButton.dataset.qty);
    const updated = await api(`/api/components/${id}/quantity`, {
      method: "PATCH",
      body: JSON.stringify({ delta }),
    });
    state.components = state.components.map((item) => (item.id === id ? updated : item));
    renderList();
    renderStats();
    if (state.selectedId === id) renderDetail(updated);
    return;
  }

  const card = event.target.closest(".component-card");
  if (card) selectComponent(Number(card.dataset.id));
});

searchEl.addEventListener("input", () => {
  state.search = searchEl.value;
  load();
});

categoryEl.addEventListener("change", () => {
  state.category = categoryEl.value;
  load();
});

document.querySelector("#new-component").addEventListener("click", () => openDialog());
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());
form.addEventListener("submit", saveComponent);

load().catch((error) => {
  listEl.innerHTML = `<div class="empty-state">${escapeHtml(error.message)}</div>`;
});
