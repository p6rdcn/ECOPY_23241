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
        coefficients_df = pd.DataFrame({"Beta coefficients": coefficients})
        return coefficients_df.squeeze()

    def get_pvalues(self):
        p_vals = self.model.pvalues
        p_vals_df = pd.DataFrame({"P-values for the corresponding coefficients": p_vals})
        return p_vals_df.squeeze()

    def get_wald_test_result(self, restriction_matrix):
        test = self.model.wald_test(restriction_matrix)
        fvalue = self.model.fvalue
        pvalue = self.model.f_pvalue
        return f"F-value: {fvalue:.2f}, p-value: {pvalue:.3f}"

    def get_model_goodness_values(self):
        ars = self.model.rsquared_adj
        ak = self.model.aic
        by = self.model.bic
        return f"Adjusted R-squared: {ars:.3f}, Akaike IC: {ak:.2e}, Bayes IC: {by:.2e}"