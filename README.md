# printer-toner-reorder-planner

Plan toner reorders from level and daily page use: days until empty from the cartridge yield, REORDER when under 14 days left — soonest empty first, so no printer runs dry mid-week.

## How to run

```sh
python3 main.py printers.csv
```

## Example output

```
HP-OfficeJet: REORDER (10% toner, 50 pages/day, 4.0 days left)
Canon-LBP: OK (80% toner, 50 pages/day, 32.0 days left)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
