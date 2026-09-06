"""
best_item_for_level.py

Determine the best item to craft at a given level based on
cycle or chain efficiency.

Returns the DataFrame row of the best item.
"""

from winds_of_valen.global_dicts.global_data import global_data
level_req = global_data["level_req"]
from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe

# Build the smelting dataframe once at import time
df, df_smelting = build_smelting_dataframe()


def best_item_for_level(level: int):
    """
    Determine the best item to craft at a given level
    based on cycle or chain efficiency.

    Parameters
    ----------
    level : int
        The player's smithing level.

    Returns
    -------
    pandas.Series or None
        The DataFrame row of the best item, or None if no items are allowed.
    """

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

