from scipy.stats import mannwhitneyu
import numpy as np
import pandas as pd

# Generate sample data for Group A (NFC withdrawal amount) with an exponential distribution
data_group_a = {
    'WithDrawalAmount_USD': np.random.gamma(2, 70.000, 34)
}
df_group_a = pd.DataFrame(data_group_a)

# Generate sample data for Group B (Debit Card withdrawal amount) with an exponential distribution
data_group_b = {
    'WithDrawalAmount_USD': np.random.gamma(2, 50.000, 34)
}
df_group_b = pd.DataFrame(data_group_b)

# Mann-Whitney U test
u_statistic, p_value = mannwhitneyu(df_group_a['WithDrawalAmount_USD'], df_group_b['WithDrawalAmount_USD'])

# Display the results
print("Mann-Whitney U Test Results:")
print(f"U-Statistic: {u_statistic}")
print(f"P-value: {p_value}")
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the groups.")



#Monte Carlo Simulation for P value Robustness

# Assuming df_group_a and df_group_b are your DataFrames with 'WithDrawalAmount_USD' column
withdrawal_group_a = df_group_a['WithDrawalAmount_USD']
withdrawal_group_b = df_group_b['WithDrawalAmount_USD']

# Calculate the Mann-Whitney U statistic and p-value
observed_U, p_value = mannwhitneyu(withdrawal_group_a, withdrawal_group_b)

# Number of Monte Carlo simulations
num_simulations = 1000

# Combine the data
combined_data = np.concatenate([withdrawal_group_a, withdrawal_group_b])

# Initialize an array to store simulated U statistics
simulated_U = np.zeros(num_simulations)

# Perform Monte Carlo simulations
for i in range(num_simulations):
    # Shuffle the combined data
    np.random.shuffle(combined_data)
    
    # Calculate the U statistic for the shuffled data
    simulated_U[i], _ = mannwhitneyu(combined_data[:len(withdrawal_group_a)], combined_data[len(withdrawal_group_b):])

# Calculate the p-value based on the Monte Carlo simulations
monte_carlo_p_value = np.mean(simulated_U >= observed_U)

print(f"Observed U: {observed_U}, Monte Carlo p-value: {monte_carlo_p_value}")




