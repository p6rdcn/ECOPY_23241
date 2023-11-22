# P6RDCN


# Modules
import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
from scipy.optimize import minimize


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


class LinearRegressionNP:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

        self.n = self.right_hand_side.shape[0]
        self.X = np.concatenate((np.ones((self.n, 1)), self.right_hand_side), axis=1)
        self.k = self.X.shape[1]
        self.dof = self.n - self.k

        self.residuals = None
        self.variance = None
        self.SE = None
        self.betas = None

    def fit(self):
        self.betas = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.left_hand_side

    def get_params(self):
        return pd.Series(self.betas, name = "Beta coefficients")

    def get_pvalues(self):
        self.residuals = self.left_hand_side - self.X @ self.betas
        self.variance = self.residuals.T @ self.residuals / self.dof
        self.SE = np.sqrt(np.diag(self.variance * np.linalg.inv(self.X.T @ self.X)))
        t_values = self.betas / self.SE
        p_values = 2 * (1 - stats.t.cdf(abs(t_values), self.dof))
        return pd.Series(p_values, name = "P-values for the corresponding coefficients")

    def get_wald_test_result(self, constraints):
        R = np.asmatrix(constraints)
        m = R.shape[0]
        RBr = R @ self.betas
        RXTXRT = R @ np.linalg.inv(self.X.T @ self.X) @ R.T
        wald_value = RBr @ np.linalg.inv(RXTXRT) @ RBr.T / m / self.variance
        p_value = 1 - stats.f.cdf(wald_value.item(), m, self.dof)
        return f"Wald: {wald_value.item():.3f}, p-value: {p_value:.3f}"

    def get_model_goodness_values(self):
        y_mean = self.left_hand_side.mean()
        y_centered = self.left_hand_side - y_mean
        crs = 1 - self.residuals.T @ self.residuals / (y_centered.T @ y_centered)
        ars = 1 - (1 - crs) * (self.n - 1) / self.dof
        return f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"


class LinearRegressionGLS:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

        self.n = self.right_hand_side.shape[0]
        self.X = np.concatenate((np.ones((self.n, 1)), self.right_hand_side), axis = 1)
        self.k = self.X.shape[1]
        self.dof = self.n - self.k

        self.gls_betas = None
        self.v_inv = None
        # self.gls_X = None
        # self.gls_y = None
        self.gls_residuals = None
        self.gls_variance = None
        self.gls_SE = None

    def fit(self):
        ols_betas = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.left_hand_side
        ols_resid = self.left_hand_side - self.X @ ols_betas
        y = np.log(ols_resid ** 2)
        log_betas = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ y
        predictions = np.sqrt(np.exp(self.X @ log_betas))
        self.v_inv = np.diag(1.0 / predictions)
        self.gls_betas = np.linalg.inv(self.X.T @ self.v_inv @ self.X) @ self.X.T @ self.v_inv @ self.left_hand_side
        # c = np.linalg.cholesky(self.v_inv)
        # self.gls_X = c @ self.X
        # self.gls_y = c @ self.left_hand_side

    def get_params(self):
        return pd.Series(self.gls_betas, name = "Beta coefficients")

    def get_pvalues(self):
        self.gls_residuals = self.left_hand_side - self.X @ self.gls_betas
        self.gls_variance = self.gls_residuals.T @ self.gls_residuals / self.dof
        self.gls_SE = np.sqrt(np.diag(self.gls_variance * np.linalg.inv(self.X.T @ self.v_inv @ self.X)))
        t_values = self.gls_betas / self.gls_SE
        p_values = 2 * (1 - stats.t.cdf(abs(t_values), self.dof))
        return pd.Series(p_values, name = "P-values for the corresponding coefficients")

    def get_wald_test_result(self, constraints):
        R = np.asmatrix(constraints)
        m = R.shape[0]
        RBr = R @ self.gls_betas
        RXTXRT = R @ np.linalg.inv(self.X.T @ self.v_inv @ self.X) @ R.T
        wald_value = RBr @ np.linalg.inv(RXTXRT) @ RBr.T / m / self.gls_variance
        p_value = 1 - stats.f.cdf(wald_value.item(), m, self.dof)
        return f"Wald: {wald_value.item():.3f}, p-value: {p_value:.3f}"

    def get_model_goodness_values(self):
        SST = self.left_hand_side.T @ self.v_inv @ self.left_hand_side
        SSR = self.left_hand_side.T @ self.v_inv @ self.X @ np.linalg.inv(
            self.X.T @ self.v_inv @ self.X) @ self.X.T @ self.v_inv @ self.left_hand_side
        crs = 1 - SSR / SST
        ars = 1 - (1 - crs) * (self.n - 1) / self.dof
        return f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"


class LinearRegressionML:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

        self.n = self.right_hand_side.shape[0]
        self.X = np.concatenate((np.ones((self.n, 1)), self.right_hand_side), axis=1)
        self.k = self.X.shape[1]
        self.dof = self.n - self.k

        self.betas = None
        self.residuals = None
        self.variance = None
        self.SE = None

    def fit(self):
        def negative_log_likelihood(params, X, y):
            initial_intercept, initial_slope1, initial_slope2, initial_slope3, initial_sigma = params
            betas = [initial_intercept, initial_slope1, initial_slope2, initial_slope3]
            y_pred = X @ betas
            return -1 * np.sum(stats.norm.logpdf(y, y_pred, initial_sigma))

        initial_params = [0.1, 0.1, 0.1, 0.1, 0.1]
        result = minimize(fun=negative_log_likelihood, x0=initial_params, args=(self.X, self.left_hand_side),
                          method="L-BFGS-B")
        self.betas = result.x[:4]
        self.variance = result.x[-1] ** 2 * self.n / self.dof

    def get_params(self):
        return pd.Series(self.betas, name="Beta coefficients")

    def get_pvalues(self):
        self.residuals = self.left_hand_side - self.X @ self.betas
        #self.variance = self.residuals.T @ self.residuals / self.dof
        self.SE = np.sqrt(np.diag(self.variance * np.linalg.inv(self.X.T @ self.X)))
        t_values = self.betas / self.SE
        p_values = 2 * (1 - stats.t.cdf(abs(t_values), self.dof))
        return pd.Series(p_values, name="P-values for the corresponding coefficients")

    def get_model_goodness_values(self):
        y_mean = self.left_hand_side.mean()
        y_centered = self.left_hand_side - y_mean
        crs = 1 - self.residuals.T @ self.residuals / (y_centered.T @ y_centered)
        ars = 1 - (1 - crs) * (self.n - 1) / self.dof
        return f"Centered R-squared: {crs:.3f}, Adjusted R-squared: {ars:.3f}"