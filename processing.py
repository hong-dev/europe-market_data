import pandas as pd

df1 = pd.read_csv(
    'tour_cap_nat.tsv',
    sep     = '\t|,',
    engine  = 'python',
    header  = 0,
    usecols = [0, 1, 2, 3, 7],
    names   = ['accommod', 'unit', 'nace_r2', 'Country Code', 'Number of Bed-places']
)

df2 = pd.read_csv(
    'tin00083.tsv',
    sep     = '\t|,',
    engine  = 'python',
    header  = 0,
    usecols = [0, 1, 2, 3, 8],
    names   = ['indic_is', 'ind_type', 'unit', 'Country Code', 'Percentage of individuals online']
)

filtered_df1 = df1[
    (df1['accommod']  == 'BEDPL')
    & (df1['unit']    == 'NR')
    & (df1['nace_r2'] == 'I551')
]

filtered_df2 = df2[
    df2['ind_type'] == 'IND_TOTAL'
]

merged_df = pd.merge(
    filtered_df2[['Country Code', 'Percentage of individuals online']],
    filtered_df1[['Country Code', 'Number of Bed-places']],
    how = 'outer',
    on  = 'Country Code'
).set_index('Country Code').drop(['EA', 'EU27_2007', 'EU27_2020', 'EU28'])

valid_df = (
    merged_df
    .replace({'b':''}, regex = True)
    .apply(pd.to_numeric, errors = 'coerce')
    .sort_values(by = 'Percentage of individuals online', ascending = False)
)

valid_df.to_csv('processed_data.csv', index = 'Country Code')
