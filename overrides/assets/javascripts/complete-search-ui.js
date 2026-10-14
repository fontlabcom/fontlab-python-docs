// this_file: overrides/assets/javascripts/complete-search-ui.js
// Extend the stock config and report transport failure beside its unchanged results.
(() => {
  const script = document.currentScript;
  const element = document.getElementById("__config");
  const config = JSON.parse(element.textContent);
  const name = `complete-search-${crypto.randomUUID()}`;
  const worker = new URL(script.dataset.worker, location.href);
  worker.searchParams.set("channel", name);
  config.search = worker.href;
  element.textContent = JSON.stringify(config);
  const channel = new BroadcastChannel(name);
  const output = document.querySelector(".md-search__output");
  if (!output) return;
  const panel = document.createElement("div");
  panel.className = "md-search-result__meta";
  panel.dataset.completeSearchStatus = "";
  panel.setAttribute("role", "status");
  panel.setAttribute("aria-live", "polite");
  const label = document.createElement("span");
  const retry = document.createElement("button");
  retry.type = "button";
  retry.textContent = "Retry search";
  retry.setAttribute("aria-label", "Retry unavailable documentation search");
  retry.style.cssText = "margin-inline-start:1em;text-decoration:underline;cursor:pointer";
  let connected = false;
  retry.onclick = () => {
    retry.disabled = true; label.textContent = "Retrying search…";
    if (connected) channel.postMessage({type:"retry"});
    else location.reload();
  };
  panel.append(label, retry);
  panel.hidden = true;
  output.prepend(panel);
  const update = data => {
    if (data.state === "metrics") return;
    panel.hidden = data.state !== "error";
    retry.disabled = false;
    if (data.state === "error") label.textContent = "Documentation search is unavailable. ";
    const meta = output.querySelector(".md-search-result > .md-search-result__meta");
    const list = output.querySelector(".md-search-result__list");
    if (meta) meta.hidden = data.state === "error";
    if (list) list.hidden = data.state === "error";
    output.dataset.completeSearchState = data.state;
  };
  const deadline = setTimeout(() => update({state:"error"}), 30000);
  channel.onmessage = ({data}) => {
    connected = true;
    if (data.state === "ready" || data.state === "error") clearTimeout(deadline);
    update(data);
  };
  addEventListener("pagehide", () => { clearTimeout(deadline); channel.close(); }, {once:true});
})();
