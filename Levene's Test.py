#Levene's Test for checking homogeneity of group variances
from scipy.stats import levene


statistic, p_value = levene(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Levene's Test for Equality of Variances:")
print(f"Test Statistic: {statistic}")
print(f"P-value: {p_value}")
alpha= 0.05
if p_value < alpha:
    print("Reject the null hypothesis. Unequal variances are provided.")
else:
    print("Fail to reject the null hypothesis. Homogenous variances are provided  .")
