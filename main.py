#!/usr/bin/env python3
"""Write the V1 entry text for the-plan-make-fun-will-carry-20261122-2138
to /output/entry.txt. No network access."""

import os

ENTRY_TEXT = "Day 1: open an Etsy shop selling editable funeral-program templates at $9.99. Generate 40 designs with AI art, list them ($0.20 each). Days 2-30: add 3 daily, spend $30 on Etsy Ads. Families buy same-day; 30 sales = $300, median about 20 sales = $200."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)
