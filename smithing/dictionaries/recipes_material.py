"""
recipes_material.py

Recipes for intermediate materials (bars, rods, plates).
These define the recursive crafting tree used by resolve_chain().

Each recipe entry:
    {"name": <component>, "count": <quantity>}
"""

material_breakdown_recipes: dict[str, list[dict]] = {
    "Bronze Bar": [
        {"name": "Copper Ore", "count": 1},
        {"name": "Tin Ore", "count": 1},
    ],

    "Iron Bar": [
        {"name": "Iron Ore", "count": 2},
    ],

    "Steel Bar": [
        {"name": "Iron Ore", "count": 1},
        {"name": "Coal Ore", "count": 1},
    ],

    "Mithril Bar": [
        {"name": "Mithril Ore", "count": 1},
        {"name": "Coal Ore", "count": 2},
    ],

    "Gold Bar": [
        {"name": "Gold Ore", "count": 8},
    ],

    "Silver Bar": [
        {"name": "Silver Ore", "count": 7},
    ],
    # "Ebony Bar": [{"name": "Ebony Ore", "count": 7}],

    # Rods
    "Iron Rod": [{"name": "Iron Bar", "count": 1}],
    "Steel Rod": [{"name": "Steel Bar", "count": 1}],
    "Large Steel Rod": [{"name": "Steel Rod", "count": 2}],
    "Mithril Rod": [{"name": "Mithril Bar", "count": 2}],
    "Large Mithril Rod": [{"name": "Mithril Rod", "count": 2}],
    # "Small Ebony Rod": [{"name": "Ebony Bar", "count": 2}],
    # "Ebony Rod": [{"name": "Small Ebony Rod", "count": 4}, {"name": "Ebony Bar", "count": 3}],
    # "Large Ebony Rod": [{"name": "Ebony Rod", "count": 4}, {"name": "Ebony Bar", "count": 3}],

    # Plates
    "Iron Plate": [{"name": "Iron Bar", "count": 2}],
    "Steel Plate": [{"name": "Steel Bar", "count": 2}],
    "Large Steel Plate": [{"name": "Steel Plate", "count": 2}],
    "Mithril Plate": [{"name": "Mithril Bar", "count": 4}],
    "Large Mithril Plate": [{"name": "Mithril Plate", "count": 4}],
    # "Small Ebony Plate": [{"name": "Ebony Bar", "count": 4}],
    # "Ebony Plate": [{"name": "Small Ebony Plate", "count": 4}, {"name": "Ebony Bar", "count": 3}],
    # "Large Ebony Plate": [{"name": "Ebony Plate", "count": 4}, {"name": "Ebony Bar", "count": 3}],

    # Silver
    "Silver Plate": [{"name": "Silver Bar", "count": 7}],
    "Silver Foil": [{"name": "Silver Plate", "count": 1}],

    # Gold
    "Gold Plate": [{"name": "Gold Bar", "count": 8}],
    "Golden Shield Frame": [
        {"name": "Gold Plate", "count": 5},
        {"name": "Gold Bar", "count": 3},
        {"name": "Steel Rod", "count": 2},
        {"name": "Steel Bar", "count": 2},
    ],
}
