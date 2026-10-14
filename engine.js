(function (root) {
  "use strict";
  var HONEST_FACTOR = 0.65; // labeled share of labeled mAh that reaches the phone
  var CABIN_WH = 100;       // labeled carry-on limit, watt-hours
  var APPROVAL_WH = 160;    // labeled airline-approval ceiling, watt-hours

  function round1(x) { return Math.round(x * 10) / 10; }

  function wattHours(mah, volts) {
    return round1(mah * volts / 1000);
  }

  function whPlan(mah, volts) {
    if (!(mah > 0) || !(volts > 0)) return { error: "the bank and the volts must be positive" };
    var wh = wattHours(mah, volts);
    var verdict;
    if (wh <= 27) verdict = "a pocket cell";
    else if (wh <= 74) verdict = "a weekend brick";
    else verdict = "a laptop lifter";
    return { wh: wh, verdict: verdict };
  }

  function chargePlan(mah, phoneMah) {
    if (!(mah > 0) || !(phoneMah > 0)) return { error: "the bank and the phone must be positive" };
    var delivered = Math.round(mah * HONEST_FACTOR);
    var charges = round1(delivered / phoneMah);
    var verdict;
    if (charges < 1) verdict = "a top-up artist";
    else if (charges <= 2) verdict = "a day extender";
    else if (charges <= 4) verdict = "a weekend away";
    else verdict = "a week off-grid";
    return { delivered: delivered, charges: charges, verdict: verdict };
  }

  function flightPlan(mah, volts) {
    if (!(mah > 0) || !(volts > 0)) return { error: "the bank and the volts must be positive" };
    var raw = mah * volts / 1000; // unrounded: the bands judge the true figure
    var wh = round1(raw);         // rounded for display only
    var verdict;
    if (raw <= CABIN_WH) verdict = "in the common cabin band";
    else if (raw <= APPROVAL_WH) verdict = "in the approval band";
    else verdict = "past the usual cabin bands";
    return { wh: wh, verdict: verdict };
  }

  function renderWh(r, mah, volts) {
    return "Your " + mah + " mAh bank at a labeled " + volts + " V holds " + r.wh
      + " Wh - " + r.verdict + ".";
  }

  function renderCharge(r, mah, phoneMah) {
    return "A " + mah + " mAh bank honestly delivers " + r.delivered + " mAh; against your "
      + phoneMah + " mAh phone that is " + r.charges + " charges - " + r.verdict + ".";
  }

  function renderFlight(r, mah, volts) {
    return "A " + mah + " mAh bank at a labeled " + volts + " V is " + r.wh + " Wh - " + r.verdict + ".";
  }

  var api = { whPlan: whPlan, chargePlan: chargePlan, flightPlan: flightPlan, renderWh: renderWh, renderCharge: renderCharge, renderFlight: renderFlight };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.BankMath = api;
})(this);
