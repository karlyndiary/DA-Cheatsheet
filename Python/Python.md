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



- Chaining comparison: if 4 < mark <=6: print("pass")
- List comprehension(used to list all the columns that start with a particular word) for loop can be used. 
    - loan_columns = [] 
    - for col in credit.columns:
    - if 'loan' in col:
    - loan_columns.append(col)
    - or loan_columns = [col for col in credit.columns if 'loan' in col]
    - loan_columns -> This returns the list of columns that contains the word 'loan' in it.
-  Pandas Profiling:
-  Highlighting tables: Apply colours to a data frame
    - def highlight_min_max(data_frame, min_color, max_color) : 
    - numeric_cols = data_frame.select_dtypes ( [np. number]).columns
    - #This first line creates a styler object
    - final data = data_frame.style.highlight_max (color=max_color, subset=numeric_cols)
    - #On this second line, no need to use ".style"
    - final data final data.highlight_min(color = min_color, subset=numeric_cols) 
    - return final data
    - #Function to apply ORANGE to min and GREEN to max
    - highlight_min_max (my_data, min_color='orange', max_color="green")
- Type hinting:
