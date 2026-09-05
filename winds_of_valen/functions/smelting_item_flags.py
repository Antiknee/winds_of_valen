"""
smelting_item_flags.py

Utility for determining whether an item is a smeltable item.
"""

from winds_of_valen.global_dicts.material_breakdown_recipes import material_breakdown_recipes
from winds_of_valen.global_dicts.item_recipes import item_recipes


def is_smelting_item(name: str) -> bool:
    return name in material_breakdown_recipes or name in item_recipes
