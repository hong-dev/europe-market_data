import pandas as pd
import plotly.graph_objs as go

from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv(
    'processed_data.csv',
    index_col = 'Country Code',
)

# bar_plot
fig = go.Figure()

fig.add_trace(go.Bar(
    x     = df.index,
    y     = df['Percentage of individuals online'],
    name  = 'Percentage of individuals online',
    yaxis = 'y',
    offsetgroup  = 1,
    marker_color = '#4C72B0'

))
fig.add_trace(go.Bar(
    x     = df.index,
    y     = df['Number of Bed-places'],
    name  = 'Number of Bed-places',
    yaxis = 'y2',
    offsetgroup = 2,
    marker_color = '#55A868'
))

fig.update_layout(
    barmode = 'group',
    title = dict(
        text      = 'Europe Market for night lamp',
        font_size = 25
    ),
    yaxis = dict(
        title     = 'Individuals online (%)',
        titlefont = dict(
            color = '#4C72B0'
        )
    ),
    yaxis2 = dict(
        title     = 'Bed-places',
        overlaying = 'y',
        side      = 'right',
        titlefont = dict(
            color = '#55A868'
        )
    )
)
fig.show()
fig.write_image('bar_plot.png', width = 1400, height = 900)

# table
original_table   = df
normalized_table = original_table.copy()

normalized_table[ : ] = MinMaxScaler().fit_transform(normalized_table[ : ]) * 100

normalized_table = normalized_table.rename(
    columns = {
        'Percentage of individuals online': '(Nor) Individuals online',
        'Number of Bed-places'            : '(Nor) Bed-places'
    }
).round(2)

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


header_values = list(merged_table.columns)
header_values.insert(0, 'Country Code')

cell_values = [merged_table[column] for column in merged_table.columns]
cell_values.insert(0, merged_table.index)

fig2 = go.Figure(
    data = [
        go.Table(
            header = dict(
                values = header_values,
                align  = 'left',
                fill_color = '#92a8cd'
            ),
            cells = dict(
                values = cell_values,
                align  = 'left',
                fill   = dict(
                    color = ['#d6dde6', '#eeeeee'])
            )
        )
    ]
)

fig2.update_layout(
    title = dict(
        text      = 'Europe Market for night lamp (sorted by Avg Rank)',
        font_size = 25,
        x         = 0.5
    )
)

fig2.show()
fig2.write_image('table.png', width = 1600, height = 1100)

# normalized_plot
fig3 = go.Figure()

fig3.add_trace(go.Bar(
    x     = merged_table.index,
    y     = merged_table['(Nor) Individuals online'],
    name  = 'Individuals online',
    marker_color = '#4C72B0'

))
fig3.add_trace(go.Bar(
    x     = merged_table.index,
    y     = merged_table['(Nor) Bed-places'],
    name  = 'Bed-places',
    marker_color = '#55A868'
))

fig3.update_layout(
    barmode = 'stack',
    title = dict(
        text      = 'Europe Market for night lamp (Normalized)',
        font_size = 25
    )
)

fig3.show()
fig3.write_image('normalized_plot.png', width = 1400, height = 900)
