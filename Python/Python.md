## Pandas
Returns the first n rows of the DataFrame.
```
df.head(n)
```
Returns the last n rows of the DataFrame.
```
df.tail(n)
```
Provides a concise summary of the DataFrame including column data types and non-null values.
```
df.info()
```
Generates descriptive statistics summarizing the central tendency, dispersion, and shape of the dataset's distribution.
```
df.describe()
```
Returns a tuple representing the dimensionality of the DataFrame (rows, columns).
```
df.shape
```
Returns the column labels of the DataFrame.
```
df.columns
```
Returns the index labels of the DataFrame.
```
df.index
```
Returns the data types of each column in the DataFrame.
```
df.dtypes
```
Returns a DataFrame of the same shape as the original with True/False values indicating the presence of missing values (NaN).
```
df.isnull()
```
Returns a DataFrame with missing values removed.
```
df.dropna()
```
Returns a copy of the DataFrame with missing values filled or imputed with the specified value.
```
df.fillna(value)
```
Groups the DataFrame using a mapper or by a Series of columns and returns a groupby object for further operations.
```
df.groupby(n)
```
Merges DataFrame objects by performing a database-style join operation based on columns or indexes.
```
df.merge(n)
```
Creates a spreadsheet-style pivot table as a DataFrame.
```
df.pivot_table()
```
Applies a function along an axis of the DataFrame.
```
df.apply()
```
Sorts the DataFrame by specified column(s).
```
df.sort_values()
```
Returns unique values in a DataFrame column.
```
df.unique()
```
Returns the number of unique values in a DataFrame column.
```
df.nunique()
```
Returns a Series containing counts of unique values in a DataFrame column.
```
df.value_counts()
```
Retrieve rows and columns from a DataFrame by label(s) or boolean array.
```
df.loc[]
```
Retrieve rows and columns from a DataFrame by integer position(s).
```
df.iloc[]
```
Generate a new DataFrame with specified columns removed.
```
df.drop()
```
Modify the names of one or more axes of the DataFrame.
```
df.rename()
```
Convert a pandas object to a specified data type.
```
df.astype()
```
Calculate pairwise correlations of columns, excluding NA/null values.
```
df.corr()
```
Compute pairwise correlations between rows or columns of two DataFrame objects.
```
df.corrwidth()
```
Eliminate duplicate rows from the DataFrame.
```
df.drop_duplicates()
```
Identify missing values (NaN in numeric arrays, None/NaN in object arrays).
```
df.isna()
```
Recognize non-missing values (no NA values).
```
df.notna()
```
Transform a DataFrame from wide format to long format, possibly retaining identifier variables.
```
df.melt()
```
Apply vectorized string functions to Series and Index objects.
```
df.str()
```
Populate NA/NaN values using the specified method.
```
df.fillna()
```
Discard missing values.
```
df.dropna()
```
Determine whether elements in DataFrame are present in specified values.
```
df.isin()
```
Retrieve the first n rows ordered by columns in descending order.
```
df.nlargest()
```
Fetch the first n rows ordered by columns in ascending order.
```
df.nsmallest()
```
Obtain a random sample of items from an axis of the object.
```
df.sample()
```
Simplify frequency conversion and resampling of time series data.
```
df.resample()
```

### Difference between count() and value_counts()
- count() counts all non-null entries in a DataFrame or Series.
- value_counts() returns the count for each unique category in a categorical column (Series), showing how many times each unique value appears.

### Difference between mean() and transform('mean')
- By using transform('mean'), the calculation is performed element-wise, meaning that each row in the original DataFrame receives the corresponding average salary for its department, preserving the shape and alignment of the DataFrame. This ensures that each employee's average salary is correctly assigned based on their department.
- The mean() function calculates the average salary for each department, resulting in a Series where the index corresponds to the department and the values are the average salaries.

### Datetime
- .dt.year: Extracts the year component.
- .dt.month: Extracts the month component.
- .dt.day: Extracts the day of the month.
- .dt.hour: Extracts the hour component.
- .dt.minute: Extracts the minute component.
- .dt.second: Extracts the second component.
- .dt.weekday: Returns the day of the week as an integer (Monday=0, Sunday=6).
- .dt.dayofweek: Same as .dt.weekday.
- .dt.dayofyear: Returns the day of the year.
- .dt.date: Extracts the date part from a datetime (ignores time component).
- .dt.time: Extracts the time part from a datetime (ignores date component).

### Difference between unique() and drop_duplicates()
- unique():
    - Specific to pandas Series.
    - It extracts and returns an array of all unique values from the Series.
    - Analyze the distinct values from a column. 
- drop_duplicates():
    - Used on both Series and DataFrames.
    - It removes duplicate rows based on all columns or a subset of specified columns.
    - Retains the original data structure 
```
import pandas as pd

# Creating a DataFrame
data = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4, 4],
    'Value': ['A', 'B', 'B', 'C', 'D', 'D', 'E']
})

# Using .unique() on a Series
unique_ids = data['ID'].unique()
print("Unique IDs:", unique_ids)
# Output: Unique IDs: [1 2 3 4]

# Using .drop_duplicates() on the whole DataFrame
unique_rows = data.drop_duplicates()
print("Unique rows based on all columns:\n", unique_rows)
# Output:
#    ID Value
# 0   1     A
# 1   2     B
# 3   3     C
# 4   4     D
# 6   4     E

# Using .drop_duplicates() specifying a column
unique_ids_df = data[['ID']].drop_duplicates()
print("Unique IDs as DataFrame:\n", unique_ids_df)
# Output:
#    ID
# 0  1
# 1  2
# 3  3
# 4  4
```
