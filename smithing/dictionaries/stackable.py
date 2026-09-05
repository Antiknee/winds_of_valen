"""
stackable.py

Indicates whether an item stacks in inventory.

Rules:
- Raw items never stack.
- Bars, plates, rods (intermediate materials) never stack.
- Final craftable items never stack.
- Special items (Essence, Schematics) may stack.

Also provides:
    is_stackable(name: str) -> bool
"""

from smithing.dictionaries.raw_items import raw_items
from smithing.dictionaries.recipes_material import material_breakdown_recipes
from smithing.dictionaries.recipes_item import item_recipes

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

    Stackability is defined in the `stackable` dictionary.
    Any missing item defaults to False.
    """
    return stackable.get(name, False)
