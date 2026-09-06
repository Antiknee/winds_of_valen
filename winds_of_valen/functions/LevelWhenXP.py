"""
level_when_xp.py

Utility function for determining the player's smithing level
based on cumulative XP.

The function returns the highest level whose XP threshold
is less than or equal to the provided XP value.
"""

from winds_of_valen.global_dicts.skill_exp_table import skill_exp_table


def LevelWhenXP(xp: int) -> int:
    """
    Determine the highest smithing level whose XP threshold is <= xp.

    Parameters
    ----------
    xp : int
        The cumulative XP value.

    Returns
    -------
    int
        The corresponding smithing level.
    """
    for lvl in sorted(skill_exp_table.keys(), reverse=True):
        if xp >= skill_exp_table[lvl]:
            return lvl
    return 1

