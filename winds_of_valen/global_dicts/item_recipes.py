
# item_recipes: dict[str, list[dict]]
"""
Crafting recipes for final items (weapons, armor, etc.).

Each recipe entry:
    {"name": <component>, "count": <quantity>}

Example from source:
    "Bronze Sword": [{"name": "Bronze Bar", "count": 6}]
    "Iron Platelegs": [{"name": "Iron Plate", "count": 4}, ...]
"""

item_recipes = {
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

    # "Mining Gloves": [
    #     {"name": "Steel Plate", "count": 2},
    #     {"name": "Steel Bar", "count": 2},
    #     {"name": "Rough Leather", "count": 2}
    # ],

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

    # "Ore Crate": [
    #     {"name": "Large Mithril Plate", "count": 6},
    #     {"name": "Gold Bar", "count": 12},
    #     {"name": "Steel Bar", "count": 4}
    # ],

    # "Volcanic Ring": [
    #     {"name": "Charred Ring Piece 1", "count": 1},
    #     {"name": "Charred Ring Piece 2", "count": 1},
    #     {"name": "Charred Ring Piece 3", "count": 1},
    #     {"name": "Gold Bar", "count": 1}
    # ],

    # "Volcanic Ward": [
    #     {"name": "Volcanic Core", "count": 1},
    #     {"name": "Golden Shield Frame", "count": 1},
    #     {"name": "Gold Bar", "count": 2}
    # ],

    # "DuskKnight Boots": [
    #     {"name": "Exquisite Silk Boot Line", "count": 1},
    #     {"name": "DuskKnight Boot Left Sabaton", "count": 1},
    #     {"name": "DuskKnight Boot Right Sabaton", "count": 1},
    #     {"name": "DuskKnight Boot Greave", "count": 2},
    #     {"name": "Ebony Bar", "count": 2},
    #     {"name": "Dusk Knight Schematics", "count": 1}
    # ],

    # "DuskKnight Platelegs": [
    #     {"name": "Exquisite Silk Pant Line", "count": 1},
    #     {"name": "DuskKnight Leg Cuisses", "count": 1},
    #     {"name": "DuskKnight Leg Tuille", "count": 1},
    #     {"name": "DuskKnight Leg Tasset", "count": 2},
    #     {"name": "DuskKnight Leg Poleyn", "count": 1},
    #     {"name": "Dusk Knight Schematics", "count": 1}
    # ],

    # "DuskKnight Platebody": [
    #     {"name": "Exquisite Silk Vest Line", "count": 1},
    #     {"name": "DuskKnight Body Breastplate", "count": 1},
    #     {"name": "DuskKnight Body Pauldron", "count": 2},
    #     {"name": "DuskKnight Body Rerebrace", "count": 1},
    #     {"name": "DuskKnight Body Couter", "count": 2},
    #     {"name": "DuskKnight Body Vambrace", "count": 2},
    #     {"name": "Dusk Knight Schematics", "count": 1}
    # ],

    # "DuskKnight Helmet": [
    #     {"name": "DuskKnight Helmet Face Plate", "count": 1},
    #     {"name": "DuskKnight Helmet Head Plate", "count": 1},
    #     {"name": "DuskKnight Helmet Spike", "count": 1},
    #     {"name": "Ebony Bar", "count": 1},
    #     {"name": "Dusk Knight Schematics", "count": 1}
    # ]
}
