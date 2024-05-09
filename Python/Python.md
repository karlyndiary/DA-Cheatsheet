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
### Pivot Table
A pivot table is a data summarization tool commonly used in data processing programs like pandas. It aggregates a table of data by one or more keys, arranging the data in a rectangle with some of the group keys along the rows and the other group keys along the columns. Pivot tables in pandas are especially useful for quickly summarizing large datasets and for performing complex grouping operations.

The DataFrame you want to use.
- The index or keys to group by along the rows.
- The columns or keys to group by along the columns.
- The values on which to perform the aggregation.
- The aggfunc, which defines the aggregation function to be applied (e.g., sum, mean, count, etc.).

A pivot table takes a DataFrame as input and performs the following operations:

- Grouping: It groups the data based on one or more columns, known as the “index” or “row” values.
- Aggregating: It applies an aggregation function to calculate summary statistics on a specific column or set of columns.
      The aggregation function can be sum, mean, count, min, max, etc.
- Reshaping: It reshapes the data by creating a new table with the grouped values as rows and columns.

```
import numpy as np

# Example sales data
data = {
    'Region': ['North', 'South', 'South', 'East', 'North', 'West', 'West', 'South'],
    'Category': ['Fruit', 'Vegetables', 'Fruit', 'Dairy', 'Fruit', 'Dairy', 'Vegetables', 'Fruit'],
    'Sales': [100, 150, 200, 200, 300, 250, 400, 300]
}

df_sales = pd.DataFrame(data)

# Pivot table to find average sales by region and category
pivot_sales = pd.pivot_table(df_sales, values='Sales', index='Category', columns='Region', aggfunc=np.mean)

print(pivot_sales)
```

Result:
| Category   | East | North | South | West |
|------------|------|-------|-------|------|
| Dairy      | 200  | NaN   | NaN   | 250  |
| Fruit      | NaN  | 200   | 250   | NaN  |
| Vegetables | NaN  | NaN   | 150   | 400  |

### Explain assign()

The assign() method in Pandas is used to add new columns to a DataFrame or to modify existing ones, all while returning a new DataFrame and leaving the original unaltered. This method is especially useful when you want to perform data transformations cleanly and functionally without affecting the underlying data structure.

- Non destructive and flexible

```
import pandas as pd

# Sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [23, 35, 45, 12]
}

df = pd.DataFrame(data)

# Using assign() to add new columns
new_df = df.assign(
    age_group=lambda x: pd.cut(x['age'], bins=[0, 18, 30, 40, 50, 100],
                    labels=['Child', 'Young Adult', 'Adult', 'Middle Aged', 'Senior']),
    decade=lambda x: (x['age'] // 10) * 10
)

print(new_df)
```
| name    | age | age_group   | decade |
|---------|-----|-------------|--------|
| Alice   | 23  | Young Adult | 20     |
| Bob     | 35  | Adult       | 30     |
| Charlie | 45  | Middle Aged | 40     |
| David   | 12  | Child       | 10     |

Bins: The purpose of using bins in this context is to convert a continuous numerical variable (age) into categorical data, which can make analysis and visualization easier.
- 0 to 18: This interval includes ages from 0 up to but not including 18. The label for this bin is "Child."
- 18 to 30: This interval includes ages from 18 up to but not including 30. The label for this bin is "Young Adult." and so on.

### copy()
The .copy() method in pandas is used to create a deep copy of a DataFrame. This means that it creates a completely independent copy of the DataFrame, including the data and the indices. Any changes made to the copy will not affect the original DataFrame, and vice versa.
```
# Make a copy of the DataFrame
df_copy = df.copy()
```
### notna()
The notna() method in pandas is used to detect existing (non-missing) values in a DataFrame or Series. It is useful for identifying where data is not null (i.e., it's not NaN, None, or NaT depending on the data type). This method returns a boolean mask of the same shape as the original data, with True for entries that are not null and False for entries that are null.
```
# Use notna() to check non-null values across the DataFrame
non_nulls_df = df.notna()
print(non_nulls_df)
```

### as_index = False
The as_index=False parameter in the groupby() method of a pandas DataFrame controls how the resulting aggregation is displayed. Specifically, when using groupby(), pandas will by default set the keys used for grouping as the index of the new DataFrame generated by an aggregation operation. 
```
# Grouping by 'voter' without as_index=False
grouped_with_index = df.groupby('voter').mean()
print("Grouped with Index:")
print(grouped_with_index)

# Grouping by 'voter' with as_index=False
grouped_without_index = df.groupby('voter', as_index=False).mean()
print("\nGrouped without Index:")
print(grouped_without_index)
```
Grouped with Index
| voter | score |
|-------|-------|
| Alice |  8.67 |
| Bob   |  7.83 |

Grouped without Index
| index | voter | score |
|-------|-------|-------|
| 0     | Alice |  8.67 |
| 1     | Bob   |  7.83 |

### Differences between Lists and Tuples
| Feature          | Lists                              | Tuples                            |
|------------------|------------------------------------|-----------------------------------|
| Enclosure        | Square brackets `[]`               | Parentheses `()`                  |
| Mutability       | Mutable (can be modified)          | Immutable (cannot be modified)    |
| Operations       | More functionalities (insert, pop, sort) | Fewer functionalities            |
| Size & Performance | Require more memory, generally slower | Require less memory, generally faster |

### Explain loc and iloc
| Feature          | `iloc`                                                              | `loc`                                                                      |
|------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Description**  | Integer location based indexing                                     | Label-based location indexing                                              |
| **Indexing Type**| Integer indexes (position-based)                                    | Labels (name or key-based)                                                 |
| **Use Cases**    | When you know the exact position of the data in the DataFrame.      | When your DataFrame has meaningful row/column labels.                      |
| **Input Type**   | Integers or arrays of integers.                                     | Labels, slices of labels, or boolean arrays.                               |
| **Flexibility**  | Select data by position, not sensitive to row/column names.         | Works with label names, can slice using labels, supports boolean selection.|
| **Error Handling**| Throws error if indices are out of bounds.                         | Throws error if labels are not found in the DataFrame's index.             |
| **Example**      | `df.iloc[0, 1]` retrieves the element at first row, second column. | `df.loc['2024-01-01']` retrieves data for the row with index label '2024-01-01'. |
| **Index Adjustment for N-th Item** | Using `iloc[N-1]` retrieves the N-th item, adjusting for zero-based indexing. Example: `iloc[2]` for the 3rd item. | Using `loc` with exact labels, no adjustment needed for indexing. Example: `loc['item_label']`. |
| **Application in Pandas** | `iloc[N-1]` retrieves the N-th item from a one-dimensional Series. `iloc[:, N-1]` retrieves the N-th column in a DataFrame. | Direct access using row or column labels. Can utilize boolean arrays for more complex selections. |

### Difference between Series and Dataframe
| Feature           | Series                                                       | DataFrame                                                      |
|-------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| **Type**          | 1-dimensional labeled array                                  | 2-dimensional labeled data structure                           |
| **Dimensions**    | Single dimension                                             | Two dimensions (rows and columns)                              |
| **Data Storage**  | Capable of storing data of any type (integer, string, etc.)  | Can store multiple columns of different data types             |
| **Indexing**      | Has a single axis index                                      | Has both row index and column labels                           |
| **Construction**  | Can be created from a list, dictionary, or scalar value      | Can be created from a dictionary of Series, lists, arrays, etc.|
| **Use Case**      | Useful for operations involving a single column or row       | Suitable for more complex data manipulations with multiple columns and rows |
| **Flexibility**   | Less flexible for complex operations involving multiple columns | More flexible for complex operations and transformations involving multiple columns |
| **Functionality** | Limited to 1-dimensional operations and manipulations        | Supports extensive functionalities including merging, reshaping, pivoting, and more |
| **Visualization** | Basic plotting capabilities (line, bar, etc.)                | More robust plotting capabilities and easier integration with plotting libraries like Matplotlib and Seaborn |

### Explain Upsampling and Downsampling
Upsampling and downsampling are techniques used to adjust the time frequency of data in time series analysis. Here are examples to clarify each process:

### 1. Upsampling

**Upsampling** refers to increasing the frequency of the data samples. This is typically done when you have lower frequency data (such as monthly data) and you want to convert it into a higher frequency (such as daily data). This often introduces missing values, which may need to be filled.

**Example**:

Suppose you have a time series of monthly sales data and you want to convert it into daily data.

```python
import pandas as pd

# Create monthly data
data = {'Sales': [200, 240, 310]}
index = pd.date_range('2024-01-01', periods=3, freq='M')
df = pd.DataFrame(data, index=index)

print("Monthly Data:")
print(df)

# Upsample to daily data
daily_data = df.resample('D').ffill()  # Forward fill to handle missing values

print("\nDaily Data:")
print(daily_data.head(10))  # Show the first 10 days
```

In this example, we upsample from monthly to daily frequency using forward fill to replace NaN values with the last observed value.

### 2. Downsampling

**Downsampling** refers to decreasing the frequency of the data samples. This is common when you have high frequency data (such as daily data) and you want to summarize it into lower frequency (such as monthly or quarterly data).

**Example**:

Suppose you have daily sales data and you want to aggregate it into monthly totals.

```python
import pandas as pd

# Create daily data
index = pd.date_range('2024-01-01', periods=90, freq='D')
data = {'Sales': range(1, 91)}
df = pd.DataFrame(data, index=index)

print("Daily Data:")
print(df.head())

# Downsample to monthly data, summing up the daily sales
monthly_data = df.resample('M').sum()

print("\nMonthly Data:")
print(monthly_data)
```

In this example, daily sales data is aggregated into monthly totals using the `sum()` function after resampling to monthly frequency.
Some of the most commonly used aggregation functions include:

- Sum: Aggregates by summing the values within each resampled period. Commonly used for totaling sales, counts, or any other quantitative data over time.
- Mean: Calculates the average of values within each period. Useful for finding the typical value when data points are dense and continuous over time.
- Max: Determines the maximum value within each period. Useful in scenarios where you need to know the peak or maximum observed value, such as temperature readings.
- Min: Finds the minimum value within each period. Like max, it is useful for data such as temperature, pricing, or other measurements where the extremes are important.
- Count: Counts the number of non-null data points within each period. This is particularly useful for attendance records, log entries, or any scenario where the volume of activity is relevant.
- Median: Computes the statistical median (the middle value) of the values in each period. This can be more robust than the mean in the presence of outliers.
- Std: Computes the standard deviation of the values, which indicates how much the values are spread out over each period.
- Var: Calculates the variance of the data points, providing a measure of the spread of the data relative to the mean.

Here are all the frequencies that can be used with the resample() function in Python:
- B: - business day
- C: - custom business day
- D: - calendar day
- W: - weekly
- M: - monthly
- SM: - semi-monthly
- BM: - business month
- CBM: - custom business month
- MS: - month start
- BMS: - business month start
- Q: - quarter
- BQ: - business quarter
- QS: - quarter start
- BQS: - business quarter start
- A: - year
- BA: - business year
- AS: - year start
- BAS: - business year start
- H: - hour
- T: - minute
- S: - second
- L: - millisecond
- U: - microsecond
- N: - nanosecond
