# P6RDCN


# Modules
from pathlib import Path
import random
import pandas as pd
import src.utils.distributions as distributions
import src.weekly.weekly_test_2 as weekly

file_to_load = Path.cwd().parent.joinpath('data').joinpath('chipotle.tsv')


# 1. Task
food = pd.read_csv(file_to_load, sep='\t')


# 2. Task
def change_price_to_float(input_df):
    input_df["item_price"] = pd.to_numeric(input_df["item_price"].str.replace("$", ""), errors = "coerce")
    return input_df


# 3. Task
def number_of_observations(input_df):
    new_df = input_df.copy()
    return len(new_df)


# 4. Task
def items_and_prices(input_df):
    new_df = input_df.copy()
    return new_df[["item_name", "item_price"]]


# 5. Task
def sorted_by_price(input_df):
    new_df = items_and_prices(input_df)
    return new_df.sort_values("item_price", ascending = False)


# 6. Task
def avg_price(input_df):
    new_df = input_df.copy()
    return new_df["item_price"].mean()


# 7. Task
def unique_items_over_ten_dollars(input_df):
    new_df = input_df.copy()
    return pd.DataFrame(new_df[new_df["item_price"] > 10])


# 8. Task
def items_starting_with_s(input_df):
    new_df = input_df.copy()
    return new_df[new_df["item_name"].str.startswith("S")]["item_name"].drop_duplicates()


# 9. Task
def first_three_columns(input_df):
    new_df = input_df.copy()
    return new_df.iloc[:, 0:3]


# 10. Task
def every_column_except_last_two(input_df):
    new_df = input_df.copy()
    return new_df.iloc[:, 0:len(new_df.columns)-2]


# 11. Task
def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    new_df = input_df.copy()
    return new_df[new_df[column_to_filter].isin(rows_to_keep)].loc[:, columns_to_keep]


# 12. Task
def generate_quartile(input_df):
    def quartile(i):
        if i >= 30:
            return 'premium'
        elif i >= 20:
            return 'high-cost'
        elif i >= 10:
            return 'medium-cost'
        else:
            return 'low-cost'

    input_df["Quartile"] = input_df["item_price"].apply(quartile)
    return input_df


# 13. Task
def average_price_in_quartiles(input_df):
    new_df = input_df.copy()
    return new_df.groupby("Quartile")["item_price"].mean()


# 14. Task
def minmaxmean_price_in_quartile(input_df):
    new_df = input_df.copy()
    return new_df.groupby("Quartile")["item_price"].agg(['min', 'max', 'mean'])


# 15. Task
def gen_uniform_mean_trajectories(distribution = (distributions.UniformDistribution(random, 0, 1)), number_of_trajectories = 2, length_of_trajectory = 100):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list


# 16. Task
def gen_logistic_mean_trajectories(distribution = (distributions.LogisticDistribution(random, 1, 3.3)), number_of_trajectories = 2, length_of_trajectory = 100):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list


# 17. Task
def gen_laplace_mean_trajectories(distribution = (weekly.LaplaceDistribution(random, 1, 3.3)), number_of_trajectories = 2, length_of_trajectory = 100):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list


# 18. Task
def gen_cauchy_mean_trajectories(distribution = (distributions.CauchyDistribution(random, 2, 4)), number_of_trajectories = 2, length_of_trajectory = 100):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list


# 19. Task
def gen_chi2_mean_trajectories(distribution = (distributions.ChiSquaredDistribution(random, 3)), number_of_trajectories = 2, length_of_trajectory = 100):
    new_list = []
    random.seed(42)

    def cumavg_list(input_list):
        return [sum(input_list[0:x + 1]) / len(input_list[0:x + 1]) for x in range(len(input_list))]

    for i in range(number_of_trajectories):
        new_list.append(cumavg_list([distribution.gen_rand() for _ in range(length_of_trajectory)]))

    return new_list