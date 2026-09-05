"""
mining_exp.py

Mining XP awarded per raw material gathered.
Used by resolve(), resolve_chain(), and resolve_time().
"""

mining_exp: dict[str, int] = {
    "Copper Ore": 15,
    "Tin Ore": 15,
    "Iron Ore": 30,
    "Coal Ore": 80,
    "Mithril Ore": 150,
    "Silver Ore": 300,
    "Gold Ore": 350,
    # "Ebony Ore": 550,
}
