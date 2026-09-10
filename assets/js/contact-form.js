/* The #contact form posts to Formspree over fetch, so submitting never leaves
   the page. The handler is delegated off the document, and every message it
   prints comes from the data-cf-* attributes on the form itself - so one file
   serves all nine pages that carry a form, in all three languages. */
(function () {
  var SEL = "form[data-contact-form]";

  function say(form, key, ok) {
    var el = form.querySelector("[data-cf-status]");
    if (!el) return;
    el.textContent = form.getAttribute("data-cf-" + key) || "";
    /* the colour comes from the stylesheet, so it follows the colour scheme */
    el.className = "form-status is-shown " + (ok ? "is-ok" : "is-error");
  }

  document.addEventListener("submit", function (ev) {
    var form = ev.target;
    if (!form || typeof form.matches !== "function" || !form.matches(SEL))
      return;
    ev.preventDefault();

    /* "at least one of these" is the one rule the browser cannot check itself */
    var group = form.querySelector("[data-cf-interest]");
    if (group && !group.querySelector("input:checked")) {
      say(form, "need-interest", false);
      var first = group.querySelector("input");
      if (first) first.focus();
      return;
    }

    var btn = form.querySelector("button[type=submit]");
    if (btn) btn.disabled = true;
    say(form, "sending", true);

    fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    })
      .then(function (res) {
        if (!res.ok) throw new Error("formspree: " + res.status);
        var fields = form.querySelector("[data-cf-fields]");
        if (fields) fields.style.display = "none";
        say(form, "sent", true);
        form.reset();
      })
      .catch(function () {
        if (btn) btn.disabled = false;
        say(form, "error", false);
      });
  });
})();
