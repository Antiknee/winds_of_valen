# winds_of_valen/global_dicts/global_data.py
"""
global_data.py

Single canonical dictionary for smithing data (EXCLUDES skill XP table and mining_exp).
Contains only the dictionaries you requested.
"""

from typing import Dict

global_data: Dict[str, dict] = {}

# craft_time
global_data["craft_time"] = {
    "Bronze Bar": 3,
    "Iron Bar": 4,
    "Steel Bar": 6,
    "Mithril Bar": 8,
    "Gold Bar": 20,
    "Silver Bar": 10,
    "Iron Plate": 4,
    "Iron Rod": 15,
    "Steel Plate": 5,
    "Steel Rod": 3,
    "Large Steel Plate": 5,
    "Large Steel Rod": 3,
    "Mithril Plate": 22,
    "Mithril Rod": 13,
    "Large Mithril Plate": 22,
    "Large Mithril Rod": 13,
    "Silver Plate": 15,
    "Silver Foil": 15,
    "Gold Plate": 15,
    "Golden Shield Frame": 60,
    "Bronze Sword": 10,
    "Bronze Platelegs": 16,
    "Bronze Platebody": 18,
    "Bronze Helmet": 6,
    "Iron Sword": 8.5,
    "Iron Platelegs": 12,
    "Iron Platebody": 14,
    "Iron Helmet": 5,
    "Steel Sword": 16,
    "Steel Platelegs": 18,
    "Steel Platebody": 20,
    "Steel Helmet": 10,
    "Mithril Sword": 35,
    "Mithril Platelegs": 75,
    "Mithril Platebody": 85,
    "Mithril Helmet": 45,
}

# material_breakdown_recipes (intermediates)
global_data["material_breakdown_recipes"] = {
    "Bronze Bar":[{"name":"Copper Ore","count":1},{"name":"Tin Ore","count":1}],
    "Iron Bar":[{"name":"Iron Ore","count":2}],
    "Steel Bar":[{"name":"Iron Ore","count":1},{"name":"Coal Ore","count":1}],
    "Mithril Bar":[{"name":"Mithril Ore","count":1},{"name":"Coal Ore","count":2}],
    "Gold Bar":[{"name":"Gold Ore","count":8}],
    "Silver Bar":[{"name":"Silver Ore","count":7}],
    "Iron Rod":[{"name":"Iron Bar","count":1}],
    "Steel Rod":[{"name":"Steel Bar","count":1}],
    "Large Steel Rod":[{"name":"Steel Rod","count":2}],
    "Mithril Rod":[{"name":"Mithril Bar","count":2}],
    "Large Mithril Rod":[{"name":"Mithril Rod","count":2}],
    "Iron Plate":[{"name":"Iron Bar","count":2}],
    "Steel Plate":[{"name":"Steel Bar","count":2}],
    "Large Steel Plate":[{"name":"Steel Plate","count":2}],
    "Mithril Plate":[{"name":"Mithril Bar","count":4}],
    "Large Mithril Plate":[{"name":"Mithril Plate","count":4}],
    "Silver Plate":[{"name":"Silver Bar","count":7}],
    "Silver Foil":[{"name":"Silver Plate","count":1}],
    "Gold Plate":[{"name":"Gold Bar","count":8}],
    "Golden Shield Frame":[
        {"name":"Gold Plate","count":5},
        {"name":"Gold Bar","count":3},
        {"name":"Steel Rod","count":2},
        {"name":"Steel Bar","count":2}
    ],
}

# item_recipes (final items)
global_data["item_recipes"] = {
    "Bronze Sword": [{"name": "Bronze Bar", "count": 6}],
    "Bronze Platelegs": [{"name": "Bronze Bar", "count": 8}, {"name": "Rough Leather", "count": 2}],
    "Bronze Platebody": [{"name": "Bronze Bar", "count": 10}, {"name": "Rough Leather", "count": 3}],
    "Bronze Helmet": [{"name": "Bronze Bar", "count": 4}],
    "Iron Sword": [{"name": "Iron Rod", "count": 4}, {"name": "Iron Bar", "count": 2}],
    "Iron Platelegs": [{"name": "Iron Plate", "count": 4}, {"name": "Rough Cloth", "count": 3}],
    "Iron Platebody": [{"name": "Iron Plate", "count": 5}, {"name": "Rough Cloth", "count": 4}],
    "Iron Helmet": [{"name": "Iron Plate", "count": 2}],
    "Steel Sword": [{"name": "Large Steel Rod", "count": 6}, {"name": "Steel Rod", "count": 4}],
    "Steel Platelegs": [{"name": "Large Steel Plate", "count": 3}, {"name": "Steel Plate", "count": 2}, {"name": "Thick Leather Pant Line", "count": 1}],
    "Steel Platebody": [{"name": "Large Steel Plate", "count": 4}, {"name": "Steel Plate", "count": 3}, {"name": "Thick Leather Vest Line", "count": 1}],
    "Steel Helmet": [{"name": "Large Steel Plate", "count": 2}, {"name": "Steel Rod", "count": 2}],
    "Mithril Sword": [{"name": "Large Mithril Rod", "count": 2}, {"name": "Mithril Rod", "count": 8}, {"name": "Mithril Bar", "count": 3}, {"name": "Essence", "count": 1000}],
    "Mithril Platelegs": [{"name": "Large Mithril Plate", "count": 3}, {"name": "Mithril Plate", "count": 4}, {"name": "Mithril Bar", "count": 3}, {"name": "Elven Cloth Pant Line", "count": 1}],
    "Mithril Platebody": [{"name": "Large Mithril Plate", "count": 4}, {"name": "Mithril Plate", "count": 4}, {"name": "Mithril Bar", "count": 5}, {"name": "Elven Cloth Vest Line", "count": 1}],
    "Mithril Helmet": [{"name": "Large Mithril Plate", "count": 2}, {"name": "Mithril Rod", "count": 4}, {"name": "Mithril Bar", "count": 1}],
}

# full_recipes = merge of material_breakdown_recipes + item_recipes
full = {}
full.update(global_data["material_breakdown_recipes"])
full.update(global_data["item_recipes"])
global_data["full_recipes"] = full

# level_req
global_data["level_req"] = {
    "Bronze Bar": 1, "Iron Bar": 10, "Steel Bar": 20, "Mithril Bar": 30,
    "Gold Bar": 40, "Silver Bar": 40, "Bronze Sword": 2, "Bronze Platelegs": 4,
    "Bronze Platebody": 6, "Bronze Helmet": 8, "Iron Sword": 12, "Iron Platelegs": 14,
    "Iron Platebody": 16, "Iron Helmet": 18, "Steel Sword": 22, "Steel Platelegs": 24,
    "Steel Platebody": 26, "Steel Helmet": 28, "Mithril Sword": 32, "Mithril Platelegs": 34,
    "Mithril Platebody": 36, "Mithril Helmet": 38, "Iron Plate": 10, "Iron Rod": 11,
    "Steel Plate": 20, "Steel Rod": 21, "Large Steel Plate": 21, "Large Steel Rod": 23,
    "Mithril Plate": 30, "Mithril Rod": 31, "Large Mithril Plate": 31, "Large Mithril Rod": 33,
    "Silver Plate": 40, "Silver Foil": 45, "Gold Plate": 40, "Golden Shield Frame": 50
}

# stackable
stackable = {
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
global_data["stackable"] = stackable

# raw_items with flag 1/0
global_data["raw_items"] = {
    "Copper Ore": 1, "Tin Ore": 1, "Iron Ore": 1, "Coal Ore": 1,
    "Mithril Ore": 1, "Silver Ore": 1, "Gold Ore": 1
}
