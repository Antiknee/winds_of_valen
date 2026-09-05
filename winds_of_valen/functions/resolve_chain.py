"""
resolve_chain.py

Fully resolve an item into:
- all recursive materials (raw + intermediates)
- total recursive smithing XP
- total mining XP
- total recursive time
"""

from winds_of_valen.global_dicts.full_recipes import full_recipes
from winds_of_valen.global_dicts.exp_table import exp_table
from winds_of_valen.global_dicts.mining_exp import mining_exp
from winds_of_valen.global_dicts.raw_items import raw_items

from winds_of_valen.functions.resolve_time import resolve_time


def resolve_chain(item: str, qty: int = 1) -> dict:
    materials = {}
    recursive_smithing_exp = 0
    raw_mining_exp = 0

    def expand(name: str, count: int, is_final: bool = False):
        nonlocal recursive_smithing_exp, raw_mining_exp

        # smithing XP for ANY craftable item
        if name in exp_table:
            recursive_smithing_exp += exp_table[name] * count

        # mining XP for raw materials
        if name in mining_exp:
            raw_mining_exp += mining_exp[name] * count
            materials[name] = materials.get(name, 0) + count
            return

        # recurse into recipe
        for ing in full_recipes.get(name, []):
            expand(ing["name"], ing["count"] * count)

        # count the crafted node itself
        materials[name] = materials.get(name, 0) + count

    expand(item, qty, is_final=True)

    # remove final crafted item
    materials.pop(item, None)

    total_time = resolve_time(item, qty)

    return {
        "materials": materials,
        "total_smithing_exp": recursive_smithing_exp,
        "raw_mining_exp": raw_mining_exp,
        "total_time": total_time,
    }
