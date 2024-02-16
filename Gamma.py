import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility (optional)
np.random.seed(42)

# Generate sample data for Group A (NFC withdrawal amount) with an exponential distribution
data_group_a = {
    'WithDrawalAmount_USD': np.random.gamma(2, 65.000, 34)
}
df_group_a = pd.DataFrame(data_group_a)

# Generate sample data for Group A (NFC withdrawal amount) with an exponential distribution
data_group_b = {
    'WithDrawalAmount_USD': np.random.gamma(2, 50.000, 34)
}
df_group_b = pd.DataFrame(data_group_b)


# Plot histograms for visual inspection
plt.hist(withdrawal_group_a, bins=15, alpha=0.5, label='Group A', color='blue')
plt.hist(withdrawal_group_b, bins=15, alpha=0.5, label='Group B', color='orange')
plt.title('Gamma Distribution for A/B Testing')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frequency')
plt.legend()
plt.show()




