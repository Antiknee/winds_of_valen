"""
exp_table.py

Smithing XP awarded for crafting each item.
This dictionary is used by resolve(), resolve_chain(), and leveling functions.
"""

exp_table: dict[str, int] = {
    "Bronze Bar": 15,
    "Bronze Helmet": 60,
    "Bronze Platebody": 60,
    "Bronze Platelegs": 120,
    "Bronze Sword": 90,

    "Iron Bar": 30,
    "Iron Rod": 10,
    "Iron Plate": 30,
    "Iron Helmet": 120,
    "Iron Platebody": 300,
    "Iron Platelegs": 240,
    "Iron Sword": 180,

    "Steel Bar": 55,
    "Steel Rod": 30,
    "Large Steel Rod": 40,
    "Steel Plate": 60,
    "Large Steel Plate": 70,
    "Steel Helmet": 220,
    "Steel Platebody": 550,
    "Steel Platelegs": 440,
    "Steel Sword": 330,

    "Mithril Bar": 155,
    "Mithril Rod": 250,
    "Large Mithril Rod": 275,
    "Mithril Plate": 500,
    "Large Mithril Plate": 550,
    "Mithril Helmet": 620,
    "Mithril Platebody": 1550,
    "Mithril Platelegs": 1240,
    "Mithril Sword": 930,

    "Silver Bar": 675,
    "Silver Plate": 400,
    "Silver Foil": 400,

    "Gold Bar": 800,
    "Gold Plate": 400,
    "Golden Shield Frame": 1000,

    # Future content
    # "Ebony Bar": 1800,
    # "Small Ebony Rod": 3000,
    # "Ebony Rod": 3250,
    # "Large Ebony Rod": 3500,
    # "Small Ebony Plate": 6000,
    # "Ebony Plate": 6500,
    # "Large Ebony Plate": 7000,
    # ...
}
