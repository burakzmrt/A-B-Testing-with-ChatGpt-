import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example data for Group A (Loan application on browser)
data_group_a = {
    'TransactionSuccess': np.random.choice([0, 1], size=33, p=[0.3, 0.7])
}
# Example data for Group B (Loan application in the banking mobile application)
data_group_b = {
    'TransactionSuccess': np.random.choice([0, 1], size=33, p=[0.4, 0.6])
}
# Create dataframes for Group A and Group B
df_group_a = pd.DataFrame(data_group_a)
df_group_b = pd.DataFrame(data_group_b)
# Create a column to represent groups
df_group_a['Group'] = 'Group A'
df_group_b['Group'] = 'Group B'
# Concatenate dataframes
df_concatenated = pd.concat([df_group_a, df_group_b])
# Create contingency table
contingency_table_aggregated = pd.crosstab(index=df_concatenated['TransactionSuccess'], columns=df_concatenated['Group'])
# Rename index and columns
contingency_table_aggregated.index = ['0', '1']
contingency_table_aggregated.columns.name = None
# Swap rows and columns
pivoted_df_swapped = contingency_table_aggregated.T
pivoted_df_swapped = pivoted_df_swapped.rename(columns={'0':'failure', '1': 'success'})

# Perform Chi-square test
chi2, p, _, _ = chi2_contingency(pivoted_df_swapped)
alpha=0.05
# Display the results of the chi-square test
print("\nChi-square test results:")
print(f"Chi2 value: {chi2}")
print(f"P-value: {p}")
if p < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")
