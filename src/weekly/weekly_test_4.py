# P6RDCN


# Modules
import pandas as pd
import matplotlib.pyplot as plt
import random


# 1. task
euro12 = pd.read_csv("..\\data\\Euro_2012_stats_TEAM.csv")


# 2. task
def number_of_participants(input_df):
    new_df = input_df.copy()
    return len(new_df)


# 3. task
def goals(input_df):
    new_df = input_df.copy()
    return new_df[["Team", "Goals"]]


# 4. task
def sorted_by_goal(input_df):
    new_df = input_df.copy()
    return goals(new_df).sort_values("Goals", ascending = False)


# 5. task
def avg_goal(input_df):
    new_df = input_df.copy()
    return new_df["Goals"].mean()


# 6. task
def countries_over_five(input_df):
    new_df = input_df.copy()
    return new_df[new_df["Goals"] >= 6]["Team"]


# 7. task
def countries_starting_with_g(input_df):
    new_df = input_df.copy()
    return new_df[new_df["Team"].str.startswith("G")]["Team"]


# 8. task
def first_seven_columns(input_df):
    new_df = input_df.copy()
    return new_df.iloc[:, 0:7]


# 9. task
def every_column_except_last_three(input_df):
    new_df = input_df.copy()
    return new_df.iloc[:, 0:len(new_df.columns) - 3]


# 10. task
def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    new_df = input_df.copy()
    return new_df[new_df[column_to_filter].isin(rows_to_keep)].loc[:, columns_to_keep]


# 11. task
def generate_quartile(input_df):
    new_df = input_df.copy()

    def quartile(i):
        if i >= 6:
            return 1
        elif i >= 5:
            return 2
        elif i >= 3:
            return 3
        else:
            return 4

    new_df["Quartile"] = new_df["Goals"].apply(quartile)
    return new_df


# 12. task
def average_yellow_in_quartiles(input_df):
    new_df = input_df.copy()
    q1 = new_df["Passes"].quantile(0.25)
    q2 = new_df["Passes"].quantile(0.5)
    q3 = new_df["Passes"].quantile(0.75)

    def quartile(i):
        if i >= q3:
            return 1
        elif i >= q2:
            return 2
        elif i >= q1:
            return 3
        else:
            return 4

    new_df["Passes_quart"] = new_df["Passes"].apply(quartile)
    return new_df.groupby("Passes_quart")["Passes"].mean().reset_index()


# 13. task
def minmax_block_in_quartile(input_df):
    new_df = input_df.copy()
    q1 = new_df["Blocks"].quantile(0.25)
    q2 = new_df["Blocks"].quantile(0.5)
    q3 = new_df["Blocks"].quantile(0.75)

    def quartile(i):
        if i >= q3:
            return 1
        elif i >= q2:
            return 2
        elif i >= q1:
            return 3
        else:
            return 4

    new_df["Blocks_quart"] = new_df["Blocks"].apply(quartile)
    return new_df.groupby("Blocks_quart")["Blocks"].agg(['min', 'max']).reset_index()


# 14. task
def scatter_goals_shots(input_df):
    fig, ax = plt.subplots()
    ax.scatter(input_df["Goals"], input_df["Shots on target"])
    ax.set_xlabel("Goals")
    ax.set_ylabel("Shots on target")
    ax.set_title("Goals and Shot on target")
    return plt.show()


# 15. task
def scatter_goals_shots_by_quartile(input_df):
    new_df = generate_quartile(input_df)
    fig, ax = plt.subplots()
    scatter = ax.scatter(new_df["Goals"], new_df["Shots on target"], c = new_df["Quartile"], label = new_df["Quartile"])
    ax.set_xlabel("Goals")
    ax.set_ylabel("Shots on target")
    ax.set_title("Goals and Shot on target")
    ax.legend(*scatter.legend_elements(), title = "Quartiles")
    return plt.show()


# 16. task
def gen_pareto_mean_trajectories(pareto_distribution, number_of_trajectories, length_of_trajectory):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([pareto_distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list