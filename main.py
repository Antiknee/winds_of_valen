"""
main.py

Launcher for Winds of Valen smithing engine.
Runs the top-level app workflow and prints summaries.
"""

from smithing.app import df_smelting, df_planA1


def main():
    print("\n=== Winds of Valen Smithing Engine ===\n")

    print("Top 10 smelting efficiencies:\n")
    print(df_smelting.head(10))

    print("\n=== Leveling Plan A1 (Global Aggregation) ===\n")
    print(df_planA1)

    print("\nDone.\n")


if __name__ == "__main__":
    main()
