import pandas as pd
import matplotlib.pyplot as plt

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


# normalized_plot
