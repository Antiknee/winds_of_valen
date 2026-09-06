"""
best_item_for_level_chain.py

Select the best item for a level based on chain efficiency only.
"""

from winds_of_valen.global_dicts.global_data import global_data
level_req = global_data["level_req"]


def best_item_for_level_chain(level: int, df_smelting):
    allowed = []

    for _, row in df_smelting.iterrows():
        item = row["item"]
        req = level_req.get(item, 999)
        if level >= req:
            allowed.append(row)

    if not allowed:
        return None

    return max(allowed, key=lambda r: r["chain_efficiency"])

