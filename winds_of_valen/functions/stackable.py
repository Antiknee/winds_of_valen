"""
stackable.py

Indicates whether an item stacks in inventory.

Rules:
- Raw items never stack.
- Bars, plates, rods (intermediate materials) never stack.
- Final craftable items never stack.
- Special items (Essence, Schematics) may stack.
"""

from winds_of_valen.global_dicts.global_data import global_data
raw_items = global_data["raw_items"]
from winds_of_valen.global_dicts.global_data import global_data
material_breakdown_recipes = global_data["material_breakdown_recipes"]
from winds_of_valen.global_dicts.global_data import global_data
item_recipes = global_data["item_recipes"]


# Base stackability definitions
stackable: dict[str, bool] = {
    "Essence": True,
    "Dusk Knight Schematics": True,

    "Exquisite Silk Boot Line": False,
    "Exquisite Silk Pant Line": False,
    "Exquisite Silk Vest Line": False,

    "Elven Cloth Pant Line": False,
    "Elven Cloth Vest Line": False,

    "Thick Leather Pant Line": False,
    "Thick Leather Vest Line": False,

    "Rough Leather": False,
    "Rough Cloth": False,

    "Charred Ring Piece 1": False,
    "Charred Ring Piece 2": False,
    "Charred Ring Piece 3": False,

    "Volcanic Core": False,
}


# Raw items never stack
for r in raw_items:
    stackable[r] = False

# Intermediate materials (bars, plates, rods) never stack
for m in material_breakdown_recipes:
    stackable[m] = False

# Final craftable items never stack
for item in item_recipes:
    stackable[item] = False


def is_stackable(name: str) -> bool:
    """
    Returns whether an item is stackable in inventory.

    Any missing item defaults to False.
    """
    return stackable.get(name, False)

