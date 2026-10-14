# Bank math

The label names the watt-hours, the watt-hours name the charges, and the flight names the limit.

A power bank is sold by its milliamp-hours, counted at the cell's own voltage. Bank math turns that number into the three answers that matter: the watt-hours the label should have led with, the honest charges your phone actually gets after conversion losses, and the verdict on whether the bank clears the carry-on line.

## The three tools

- **Watt-hour plan** - bank capacity (mAh) and labeled cell voltage (default 3.7 V) become watt-hours: `round1(mAh * V / 1000)`, banded as a pocket cell, a weekend brick, or a laptop lifter.
- **Charge plan** - bank capacity against phone battery size, after a labeled 65% honest delivery factor, becomes the charges you actually get: `round1(mAh * 0.65 / phone)`, banded from a top-up artist to a week off-grid.
- **Flight plan** - the watt-hours against a labeled 100 Wh common cabin band (airline-approval band up to 160 Wh) become the band the bank falls in: the common cabin band, the approval band, or past the usual cabin bands. Bands are judged on the unrounded figure; only the display rounds.

## Honesty notes

Illustrative planning arithmetic only. Every rate is a labeled default you can change by reading your own label or measuring your own bank, and the flight bands name capacity, not permission to fly. Where your device prints a watt-hour rating, use that number instead of any estimate. A real bank ages and sags in the cold. Airline rules live with the airline: many carriers also limit how many power banks you may carry and do not allow recharging one onboard, so check your carrier's current rules before the flight, and never pack a lithium bank in checked luggage.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
