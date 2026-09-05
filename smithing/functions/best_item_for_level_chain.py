from smithing.dictionaries.level_req import level_req

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
