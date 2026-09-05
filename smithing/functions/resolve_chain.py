"""
resolve_chain.py

Fully resolve an item into:
- all recursive materials (raw + intermediates)
- total recursive smithing XP
- total mining XP
- total recursive time
"""

from smithing.dictionaries.full_recipes import full_recipes
from smithing.dictionaries.exp_table import exp_table
from smithing.dictionaries.mining_exp import mining_exp
from smithing.dictionaries.raw_items import raw_items
from smithing.functions.resolve_time import resolve_time


def resolve_chain(item: str, qty: int = 1) -> dict:
    materials = {}
    recursive_smithing_exp = 0
    raw_mining_exp = 0

    def expand(name: str, count: int):
        nonlocal recursive_smithing_exp, raw_mining_exp

        if name in exp_table:
            recursive_smithing_exp += exp_table[name] * count

        if name in mining_exp:
            raw_mining_exp += mining_exp[name] * count
            materials[name] = materials.get(name, 0) + count
            return

        for ing in full_recipes.get(name, []):
            expand(ing["name"], ing["count"] * count)

        materials[name] = materials.get(name, 0) + count

    expand(item, qty)

    if item in materials:
        del materials[item]

    total_time = resolve_time(item, qty)

    return {
        "materials": materials,
        "total_smithing_exp": recursive_smithing_exp,
        "raw_mining_exp": raw_mining_exp,
        "total_time": total_time,
    }
