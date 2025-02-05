import matplotlib.pyplot as plt
import pandas as pd

# Sample Data (replace with your actual data)
data = {
    'Date': ['07/2019', '07/2019', '11/2019', '11/2019'],
    'Source': ['Searches', 'Direct', 'Searches', 'Direct'],
    'Visitors': [40, 70, 90, 80]
}
df = pd.DataFrame(data)

# Pivot the data for plotting
df_pivot = df.pivot(index='Date', columns='Source', values='Visitors')

# Plotting
ax = df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Visitors by Web Traffic Sources')
plt.xlabel('Date')
plt.ylabel('Visitors (in Thousands)')
plt.xticks(rotation=0)  # Keep x-axis labels horizontal
plt.legend(title='Traffic Source')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add a subtle grid

# Show Plot
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()

