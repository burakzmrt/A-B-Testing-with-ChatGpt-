import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
#Set a random seed for reproducibility
np.random.seed(42)

#Generate fictive data for Group A (clicks and impressions)
group_a_clicks = np.random.choice([0, 1], size=33, p=[0.4, 0.6])
# Random clicks between 10 and 50
group_a_impressions = np.random.choice([0, 1], size=33, p=[0.1, 0.9])
# Random impressions between 100 and 500
# Create a dataframe for Group A
data_group_a = {
    'Clicks': group_a_clicks,
    'Impressions': group_a_impressions
}

df_group_a = pd.DataFrame(data_group_a)



#Generate fictive data for Group B (clicks and impressions)
group_b_clicks = np.random.choice([0, 1], size=33, p=[0.6, 0.4])  # Random clicks between 15 and 55
group_b_impressions = np.random.choice([0, 1], size=33, p=[0.1, 0.9])# Random impressions between 120 and 550

# Create a dataframe for Group A
data_group_b = {
    'Clicks': group_b_clicks,
    'Impressions': group_b_impressions
}

df_group_b = pd.DataFrame(data_group_b)

click_a = df_group_a["Clicks"].sum()
impression_a = df_group_a["Impressions"].sum()
print(click_a/impression_a)

click_b = df_group_b["Clicks"].sum()
impression_b = df_group_b["Impressions"].sum()
print(click_b/impression_b)

nclicks = np.array([click_a,click_b])
nad_views = np.array([impression_a,impression_b])

z_statistic, p_value=proportions_ztest(count=nclicks,nobs=nad_views) 

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference.")
