# material_breakdown_recipes: dict[str, list[dict]]
"""
Recipes for intermediate materials (bars, rods, plates).

These define the recursive crafting tree.

Example:
    "Bronze Bar": [{"name": "Copper Ore", "count": 1},
                   {"name": "Tin Ore", "count": 1}]
"""

material_breakdown_recipes = {
    "Bronze Bar":[{"name":"Copper Ore","count":1},{"name":"Tin Ore","count":1}],
    "Iron Bar":[{"name":"Iron Ore","count":2}],
    "Steel Bar":[{"name":"Iron Ore","count":1},{"name":"Coal Ore","count":1}],
    "Mithril Bar":[{"name":"Mithril Ore","count":1},{"name":"Coal Ore","count":2}],
    "Gold Bar":[{"name":"Gold Ore","count":8}],
    "Silver Bar":[{"name":"Silver Ore","count":7}],
    # "Ebony Bar":[{"name":"Ebony Ore","count":7}],

    "Iron Rod":[{"name":"Iron Bar","count":1}],
    "Steel Rod":[{"name":"Steel Bar","count":1}],
    "Large Steel Rod":[{"name":"Steel Rod","count":2}],
    "Mithril Rod":[{"name":"Mithril Bar","count":2}],
    "Large Mithril Rod":[{"name":"Mithril Rod","count":2}],
    # "Small Ebony Rod":[{"name":"Ebony Bar","count":2}],
    # "Ebony Rod":[{"name":"Small Ebony Rod","count":4},{"name":"Ebony Bar","count":3}],
    # "Large Ebony Rod":[{"name":"Ebony Rod","count":4},{"name":"Ebony Bar","count":3}],

    "Iron Plate":[{"name":"Iron Bar","count":2}],
    "Steel Plate":[{"name":"Steel Bar","count":2}],
    "Large Steel Plate":[{"name":"Steel Plate","count":2}],
    "Mithril Plate":[{"name":"Mithril Bar","count":4}],
    "Large Mithril Plate":[{"name":"Mithril Plate","count":4}],
    # "Small Ebony Plate":[{"name":"Ebony Bar","count":4}],
    # "Ebony Plate":[{"name":"Small Ebony Plate","count":4},{"name":"Ebony Bar","count":3}],
    # "Large Ebony Plate":[{"name":"Ebony Plate","count":4},{"name":"Ebony Bar","count":3}],

    "Silver Plate":[{"name":"Silver Bar","count":7}],
    "Silver Foil":[{"name":"Silver Plate","count":1}],

    "Gold Plate":[{"name":"Gold Bar","count":8}],
    "Golden Shield Frame":[
        {"name":"Gold Plate","count":5},
        {"name":"Gold Bar","count":3},
        {"name":"Steel Rod","count":2},
        {"name":"Steel Bar","count":2}]
    # ],

    # "DuskKnight Boot Left Sabaton":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Boot Right Sabaton":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Leg Tuille":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":1}
    # ],
    # "DuskKnight Leg Poleyn":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":1}
    # ],
    # "DuskKnight Body Pauldron":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":1}
    # ],
    # "DuskKnight Body Couter":[
    #     {"name":"Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":1}
    # ],
    # "DuskKnight Body Rerebrace":[
    #     {"name":"Ebony Plate","count":2},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Body Vambrace":[
    #     {"name":"Ebony Plate","count":2},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Leg Tasset":[
    #     {"name":"Ebony Plate","count":3},
    #     {"name":"Silver Foil","count":3}
    # ],
    # "DuskKnight Boot Greave":[
    #     {"name":"Large Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Leg Cuisses":[
    #     {"name":"Large Ebony Plate","count":2},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Helmet Face Plate":[
    #     {"name":"Large Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Helmet Head Plate":[
    #     {"name":"Large Ebony Plate","count":1},
    #     {"name":"Silver Foil","count":2}
    # ],
    # "DuskKnight Helmet Spike":[
    #     {"name":"Large Ebony Rod","count":1},
    #     {"name":"Silver Foil","count":1}
    # ],
    # "DuskKnight Body Breastplate":[
    #     {"name":"Large Ebony Plate","count":4},
    #     {"name":"Silver Foil","count":8}
    # ]
}


