from statsmodels.stats.power import TTestIndPower

# Set parameters
effect_size = 0.7 # moderate effect size (Cohen's d)
alpha = 0.05      # significance level
power = 0.80      # desired power
ratio = 1.0       # assumed ratio of sample sizes (1.0 for equal sample sizes)

# Create a power analysis object
power_analysis = TTestIndPower()

# Calculate the minimum required sample size
sample_size = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, ratio=ratio)

print(f"Minimum required sample size: {sample_size:.2f}")
