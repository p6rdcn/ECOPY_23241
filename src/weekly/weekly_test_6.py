# P6RDCN


# Modules
import pandas as pd


sp500 = pd.read_parquet("../../data/sp500.parquet", engine = "fastparquet")

ff_factors = pd.read_parquet("../../data/ff_factors.parquet", engine = "fastparquet")

data = sp500.merge(ff_factors, on = "Date", how = "left")

data["Excess Return"] = data["Monthly Returns"] - data["RF"]

data = data.sort_values(by = "Date")
data["ex_ret_1"] = data["Excess Return"].shift(periods = -1)

data = data.dropna(subset = ["ex_ret_1"]).dropna(subset = ["HML"])

data = data[data["Symbol"] == "AMZN"].drop("Symbol", axis = "columns")