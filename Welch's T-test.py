import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import pingouin as pg

data_group_a = {
    'WithDrawalAmount_USD': np.random.normal(loc=50.000, scale=10.000, size=34)
}
df_group_a = pd.DataFrame(data_group_a)

# Generate sample data for Group B (Banking card)
data_group_b = {
    'WithDrawalAmount_USD': np.random.normal(loc=45.000, scale=5.000, size=34)
}
df_group_b = pd.DataFrame(data_group_b)

# Perform Welch's t-test
t_statistic, p_value = ttest_ind(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'], equal_var=False)

# Print the results
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")

#Another Statistic Package for Welch's t-test. Each test can be used for validation.
result = pg.ttest(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'], correction=False)

# Interpret the results
alpha = 0.05  # Set your significance level
if result['p-val'][0] < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")
