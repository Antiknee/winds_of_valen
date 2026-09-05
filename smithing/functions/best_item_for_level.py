"""
best_item_for_level.py

Determine the best item to craft at a given level
based on cycle or chain efficiency.

Returns the DataFrame row of the best item.
"""

from smithing.dictionaries.level_req import level_req
from smithing.app import df_smelting


def best_item_for_level(level: int):
    allowed = []

    for _, row in df_smelting.iterrows():
        item = row["item"]
        req = level_req.get(item, 999)
        if level >= req:
            allowed.append(row)

    if not allowed:
        return None

    def score(row):
        return max(row["cycle_efficiency"], row["chain_efficiency"])

    return max(allowed, key=score)
