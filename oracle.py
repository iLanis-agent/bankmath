import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round0(x): return jsnum(math.floor(x + 0.5))

HONEST_FACTOR = 0.65
CABIN_WH = 100
APPROVAL_WH = 160

def watt_hours(mah, volts):
    return round1(mah * volts / 1000)

def wh_plan(mah, volts):
    if not (mah > 0) or not (volts > 0):
        return {"error": "the bank and the volts must be positive"}
    wh = watt_hours(mah, volts)
    if wh <= 27: verdict = "a pocket cell"
    elif wh <= 74: verdict = "a weekend brick"
    else: verdict = "a laptop lifter"
    return {"wh": wh, "verdict": verdict}

def charge_plan(mah, phoneMah):
    if not (mah > 0) or not (phoneMah > 0):
        return {"error": "the bank and the phone must be positive"}
    delivered = round0(mah * HONEST_FACTOR)
    charges = round1(delivered / phoneMah)
    if charges < 1: verdict = "a top-up artist"
    elif charges <= 2: verdict = "a day extender"
    elif charges <= 4: verdict = "a weekend away"
    else: verdict = "a week off-grid"
    return {"delivered": delivered, "charges": charges, "verdict": verdict}

def flight_plan(mah, volts):
    if not (mah > 0) or not (volts > 0):
        return {"error": "the bank and the volts must be positive"}
    raw = mah * volts / 1000  # unrounded: the bands judge the true figure
    wh = round1(raw)          # rounded for display only
    if raw <= CABIN_WH: verdict = "in the common cabin band"
    elif raw <= APPROVAL_WH: verdict = "in the approval band"
    else: verdict = "past the usual cabin bands"
    return {"wh": wh, "verdict": verdict}

def render_wh(r, mah, volts):
    return ("Your " + fmt(mah) + " mAh bank at a labeled " + fmt(volts) + " V holds " + fmt(r["wh"])
            + " Wh - " + r["verdict"] + ".")

def render_charge(r, mah, phoneMah):
    return ("A " + fmt(mah) + " mAh bank honestly delivers " + fmt(r["delivered"]) + " mAh; against your "
            + fmt(phoneMah) + " mAh phone that is " + fmt(r["charges"]) + " charges - " + r["verdict"] + ".")

def render_flight(r, mah, volts):
    return ("A " + fmt(mah) + " mAh bank at a labeled " + fmt(volts) + " V is " + fmt(r["wh"]) + " Wh - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[10000,3.7],[5000,3.7],[26800,3.7],[20000,3.7],[10000,3.85],[30000,3.7],[6700,3.7],[15000,3.7],[0,3.7],[10000,0]]:
    add("whPlan", wh_plan, render_wh, a)
for a in [[10000,4000],[5000,4000],[20000,4000],[26800,3000],[10000,3000],[5000,2500],[20000,5000],[10000,4500],[0,4000],[10000,0]]:
    add("chargePlan", charge_plan, render_charge, a)
for a in [[26800,3.7],[30000,3.7],[50000,3.7],[10000,3.7],[20000,3.7],[43000,3.7],[16000,3.7],[27000,3.7],[0,3.7],[26800,0],[27028,3.7],[27027,3.7],[43244,3.7],[43243,3.7]]:
    add("flightPlan", flight_plan, render_flight, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
