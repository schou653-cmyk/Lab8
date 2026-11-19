import pandas as pd


def task1_load_explore():

    df = pd.read_csv("labor.csv")
    print(df.head())
    print(df.columns)
    print(df.shape)
    print(df.dtypes)

    wage_series = df["wage-increase-first-year"]
    print(wage_series)

    return df

# TASK 1 WRITTEN QUESTIONS

'''
1. There are 57 rows and 17 columns
2. Uses object and float64 data types
3. Missing values are represented as NaN meaning 'Not a Number'
4. A series is 1-dimensional while a dataframe is 2-dimentional

'''


def task2_access_data(df):

    wage_series = df['wage-increase-first-year']
    print(wage_series.iloc[0])
    print(wage_series.loc[0])
    print(df.iloc[0:5])
    wage_columns = df[['wage-increase-first-year', 'wage-increase-second-year']]
    print(wage_columns)
    print(df.loc[0, 'wage-increase-second-year'])
    print(df.loc[0:3, ['wage-increase-first-year', 'wage-increase-second-year']])
    print(df.iloc[0:4, 2:4])

    return

# TASK 2 WRITTEN QUESTIONS
'''

1. .loc[] selects data using row and columns labels
    while .iloc[] uses integer positions
2. You can select multiple rows and columns with either .loc[] or .iloc[]
    the only difference is once uses labels while the other user relies on positioning
3. Selecting one column returns a Series which is 1-dimensional while multiple columns returns a dataframe
    which is 2-dimensional

'''

def task3_filter_data(df):

    good_outcomes = df[df["class"] == 'good']
    print(good_outcomes)
    bad_outcomes = df[df["class"] == 'bad']
    print(bad_outcomes)
    dispute1 = df[df['wage-increase-first-year'] > 2.5]
    print(dispute1)
    dispute2 = df[df['statutory-holidays'] > 10]
    print(dispute2)
    dispute3 = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    print(dispute3)
    print(dispute3.shape[0])
    average_first_year  = df['wage-increase-first-year'].mean()
    print(average_first_year)
    max_first_year = df['wage-increase-first-year'].max()
    print(max_first_year)

    return


# TASK 3 WRITTEN QUESTIONS

'''

1. There are 37 good outcomes and 20 bad outcomes
2. 28 disputes satisfy both conditions in dispute 3
3.  Average first year wage increase is 3.80%

'''



    


