"""
recipes_item.py

Crafting recipes for final items (weapons, armor, etc.).

Each recipe entry:
    {"name": <component>, "count": <quantity>}

These recipes are combined with material_breakdown_recipes
to form full_recipes in full_recipes.py.
"""

item_recipes: dict[str, list[dict]] = {
    "Bronze Sword": [
        {"name": "Bronze Bar", "count": 6}
    ],
    "Bronze Platelegs": [
        {"name": "Bronze Bar", "count": 8},
        {"name": "Rough Leather", "count": 2}
    ],
    "Bronze Platebody": [
        {"name": "Bronze Bar", "count": 10},
        {"name": "Rough Leather", "count": 3}
    ],
    "Bronze Helmet": [
        {"name": "Bronze Bar", "count": 4}
    ],

    "Iron Sword": [
        {"name": "Iron Rod", "count": 4},
        {"name": "Iron Bar", "count": 2}
    ],
    "Iron Platelegs": [
        {"name": "Iron Plate", "count": 4},
        {"name": "Rough Cloth", "count": 3}
    ],
    "Iron Platebody": [
        {"name": "Iron Plate", "count": 5},
        {"name": "Rough Cloth", "count": 4}
    ],
    "Iron Helmet": [
        {"name": "Iron Plate", "count": 2}
    ],

    "Steel Sword": [
        {"name": "Large Steel Rod", "count": 6},
        {"name": "Steel Rod", "count": 4}
    ],
    "Steel Platelegs": [
        {"name": "Large Steel Plate", "count": 3},
        {"name": "Steel Plate", "count": 2},
        {"name": "Thick Leather Pant Line", "count": 1}
    ],
    "Steel Platebody": [
        {"name": "Large Steel Plate", "count": 4},
        {"name": "Steel Plate", "count": 3},
        {"name": "Thick Leather Vest Line", "count": 1}
    ],
    "Steel Helmet": [
        {"name": "Large Steel Plate", "count": 2},
        {"name": "Steel Rod", "count": 2}
    ],

    "Mithril Sword": [
        {"name": "Large Mithril Rod", "count": 2},
        {"name": "Mithril Rod", "count": 8},
        {"name": "Mithril Bar", "count": 3},
        {"name": "Essence", "count": 1000}
    ],
    "Mithril Platelegs": [
        {"name": "Large Mithril Plate", "count": 3},
        {"name": "Mithril Plate", "count": 4},
        {"name": "Mithril Bar", "count": 3},
        {"name": "Elven Cloth Pant Line", "count": 1}
    ],
    "Mithril Platebody": [
        {"name": "Large Mithril Plate", "count": 4},
        {"name": "Mithril Plate", "count": 4},
        {"name": "Mithril Bar", "count": 5},
        {"name": "Elven Cloth Vest Line", "count": 1}
    ],
    "Mithril Helmet": [
        {"name": "Large Mithril Plate", "count": 2},
        {"name": "Mithril Rod", "count": 4},
        {"name": "Mithril Bar", "count": 1}
    ],
}
