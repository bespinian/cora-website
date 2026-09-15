/* The Google Ads tag (AW-18327942303). This file is the configuration and the
   conversion snippet Google hands out with the conversion action, kept out of
   the markup like the rest of the site's JavaScript. It also fetches gtag.js
   itself - see below - so the pages carry one script tag rather than two.

   The tag sits on every page, not only the nine that carry a form, because an
   ad click lands wherever the ad points and the click id has to be recorded
   there for the conversion to be attributed to it later.

   gtag_report_conversion is Google's own helper, meant to be wired to a link
   that navigates away - it fires the event, then follows `url` once the tag has
   reported. The lead form never navigates: contact-form.js calls this with no
   argument the moment Formspree accepts a submission, so the callback simply
   does nothing and the event is all that is left. */
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());
gtag("config", "AW-18327942303");

/* Google's own snippet puts an async <script> for gtag.js in the head. That
   costs a third-party handshake and ~120 KB on a host that only speaks
   HTTP/1.1, all of it landing while the hero image - the LCP element on every
   page - is still coming down; the preload scanner finds such a tag wherever in
   the document it sits, so moving it down the markup would not have helped.
   Fetching it on `load` instead puts it strictly after the paint it was
   delaying. Nothing is lost: the calls above queue on dataLayer and gtag.js
   replays the whole queue when it arrives, and a conversion cannot be reported
   before a visitor has had time to submit the form anyway. */
window.addEventListener("load", function () {
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=AW-18327942303";
  document.head.appendChild(s);
});

function gtag_report_conversion(url) {
  var callback = function () {
    if (typeof url != "undefined") {
      window.location = url;
    }
  };
  gtag("event", "conversion", {
    send_to: "AW-18327942303/snIDCLO10vYcEJ_puKNE",
    event_callback: callback,
  });
  return false;
}
