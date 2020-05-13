import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler, StandardScaler

plt.style.use('seaborn')

df = pd.read_csv(
    'processed_data.csv',
    index_col = 'Country Code'
)

# bar_plot
bar = df.plot(
    kind        = 'bar',
    secondary_y = 'Number of Bed-places',
    figsize     = (15, 10)
)

bar.set_title(
    "Europe Market for night lamp",
    fontsize = 20
)

bar.set_ylabel(
    "Individuals online (%)",
    color    = 'blue',
    fontsize = 10
)

bar.right_ax.set_ylabel(
    "Bed-places (millions)",
    color    = 'green',
    fontsize = 10
)

plt.savefig('bar_plot')

# table
original_table   = df
normalized_table = original_table.copy()

normalized_table[ : ] = MinMaxScaler().fit_transform(normalized_table[ : ]) * 100

normalized_table = normalized_table.rename(
    columns = {
        'Percentage of individuals online': '(Nor) Individuals online',
        'Number of Bed-places'            : '(Nor) Bed-places'
    }
)

merged_table = pd.merge(original_table, normalized_table, on = 'Country Code')

merged_table['(Rank) Individuals online'] = (
    merged_table['Percentage of individuals online']
    .rank(ascending = False, method = 'min')
)
merged_table['(Rank) Bed-places'] = (
    merged_table['Number of Bed-places']
    .rank(ascending = False, method = 'min')
)
merged_table['(Rank) Avg Rank'] = (
    merged_table[['(Rank) Individuals online', '(Rank) Bed-places']]
    .mean(axis = 1)
)

merged_table = merged_table.sort_values('(Rank) Avg Rank', ascending = True)

# normalized_plot
