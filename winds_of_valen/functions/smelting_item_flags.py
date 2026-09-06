"""
smelting_item_flags.py

Utility for determining whether an item is a smeltable item.
"""

from winds_of_valen.global_dicts.global_data import global_data
material_breakdown_recipes = global_data["material_breakdown_recipes"]
from winds_of_valen.global_dicts.global_data import global_data
item_recipes = global_data["item_recipes"]


def is_smelting_item(name: str) -> bool:
    return name in material_breakdown_recipes or name in item_recipes

