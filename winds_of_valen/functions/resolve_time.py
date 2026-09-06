"""
resolve_time.py

Compute total crafting time for an item including all recursive
subcomponents.

Uses:
- craft_time
- full_recipes

Returns:
    total seconds (float)
"""

from winds_of_valen.global_dicts.global_data import global_data
craft_time = global_data["craft_time"]
from winds_of_valen.global_dicts.global_data import global_data
full_recipes = global_data["full_recipes"]


def resolve_time(item: str, qty: int = 1) -> float:
    """
    Compute total crafting time for an item including all recursive
    subcomponents.

    Parameters
    ----------
    item : str
        Item name to resolve.
    qty : int
        Quantity of the item.

    Returns
    -------
    float
        Total crafting time in seconds.
    """

    total = 0

    # time for the item itself
    total += craft_time.get(item, 0) * qty

    # time for all sub‑components
    for ing in full_recipes.get(item, []):
        total += resolve_time(ing["name"], ing["count"] * qty)

    return total

