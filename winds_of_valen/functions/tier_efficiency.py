def tier_efficiency(v):
    """
    Convert numeric efficiency into tier:
      S, A, B, C, D

    Thresholds:
      >=50 → S
      >=25 → A
      >=15 → B
      >=10 → C
      else → D
    """

    if v >= 50: return "S"
    if v >= 25: return "A"
    if v >= 15: return "B"
    if v >= 10: return "C"
    return "D"
