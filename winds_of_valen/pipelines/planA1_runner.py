"""
planA1_runner.py

Runs Option A1 end‑to‑end and produces df_planA1.
"""

import pandas as pd

from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe
from winds_of_valen.functions.leveling_plan_A1 import leveling_plan_A1
from winds_of_valen.functions.aggregate_plan_global import aggregate_plan_global


df, df_smelting = build_smelting_dataframe()

planA1_raw = leveling_plan_A1(1, 60, df_smelting)
planA1 = aggregate_plan_global(planA1_raw)

df_planA1 = pd.DataFrame(planA1)
