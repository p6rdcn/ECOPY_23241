# P6RDCN


# Modules
import pandas as pd
import statsmodels.api as sm


class LinearRegressionSM:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.model = None

    def fit(self):
        X = sm.add_constant(self.right_hand_side)
        model = sm.OLS(self.left_hand_side, X).fit()
        self.model = model

    def get_params(self):
        coefficients = self.model.params
        return pd.Series(coefficients, name = "Beta coefficients")

    def get_pvalues(self):
        p_vals = self.model.pvalues
        return pd.Series(p_vals, name = "P-values for the corresponding coefficients")

    def get_wald_test_result(self, constraints):
        wald_test = self.model.wald_test(constraints, scalar = True)
        f_value = wald_test.statistic
        p_value = wald_test.pvalue
        return f"F-value: {f_value:.3}, p-value: {p_value:.3}"

    def get_model_goodness_values(self):
        ars = self.model.rsquared_adj
        ak = self.model.aic
        by = self.model.bic
        return f"Adjusted R-squared: {ars:.3f}, Akaike IC: {ak:.2e}, Bayes IC: {by:.2e}"