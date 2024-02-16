import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a random seed for reproducibility
np.random.seed(42)

# Generate sample data for Group A (NFC card withdrawal amount)
data_group_a = {
    'WithDrawalAmount_USD': np.random.normal(loc=60.000, scale=10.000, size=34)
}
df_group_a = pd.DataFrame(data_group_a)

# Generate sample data for Group B (Banking card)
data_group_b = {
    'WithDrawalAmount_USD': np.random.normal(loc=100.000, scale=10.000, size=34)
}
df_group_b = pd.DataFrame(data_group_b)



# Two-sample t-test
from scipy.stats import ttest_ind

t_statistic, p_value = ttest_ind(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Two-Sample T-Test Results:")
print(f"T-Statistic: {t_statistic}")
print(f"P-value:"'{:.20f}'.format(p_value))

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")
