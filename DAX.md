- DAX stands for Data Analysis Expression.
- DAX queries return results as a table within the tool.
- DAX queries are commonly utilized to create and test the performance of formulas in Power BI Desktop.
- These queries are often employed to generate derived data columns or tables.
- DAX queries impact the data within Power BI Desktop but do not affect the data in Power Query Editor.
- DAX may also contain nested functions.
- DAX enables us to perform very complex calculations on the data.

Remove Unwanted Columns
```
Home/Queries/Transform data -> Home/Manage Columns/Remove Columns
```
Remove Blank Rows
```
Home/Queries/Transform data -> Home/Manage Columns/Remove Rows/Remove Blank Rows
```
Adding Calculated Column
```
Table tools/New column
Cost = Superstore[Sales] - Superstore[Profit]
```
DAX Syntax
```
A = B(C[D])EF
Variable = Dax Function(Table Name[Columns]) Mathematical operators
```
- A represents the variable that will store the result of the DAX expression.
- B represents the inbuilt DAX function which will be discussed later in this article.
- C represents the Table name on whose data we need to perform the calculation.
- D represents the columns of the table whose data ks is to be operated upon.
- E and F are optional parameters and represent mathematical operators and values respectively.

## Dax Functions  
### Date and Time Functions 
- DATE: It gives the current date in the DateTime format.
- DATEDIFF: This function is used to get the difference in the number of days between two dates.
- DAY: Returns the day of a month as a number from 1 to 31.
- MONTH: Returns the month as a number from 1 to 12. 1 represents January and 12 represents December.
- YEAR: Returns the year from a given date. The returned value is in the range of 1900-9999.
- NOW: Returns the current date and time of the system.
- QUARTER: Returns the quarter number of a year from a given date.


### Information Functions

- ISBLANK: Returns the value as True and False depending upon if the value is blank or not.
- ISEMPTY: Returns True if a table is empty and False if the table contains data.
- ISEVEN: Returns True if a number is even else False.
- ISODD: Returns True if a number is Odd, else False.
- ISLOGICAL: Returns True if a value is boolean, else False.
- ISTEXT: Returns True if the value is text, else False
- USERNAME: Returns the domain name and username from the login credentials used to log in to the system.

#### Contains
Functions returns true or false depending on whether the values for all of the referred columns exist or are contained in those columns. If the values for all the referred columns are not contained, the function returns false.
```
Syntax: CONTAINS(<table>, <column value> <value>[<column value>, <value>]…)
ContainsMeasure = CONTAINS('Example Data_Inf_Func', 'Example Data_Inf_Func'[Ontime Delivery], "Yes", 'Example Data_Inf_Func'[Products Returned], "yes")
```
#### ContainsString
Depending on whether one string contains another, this function returns true or false. 
```
Syntax: CONTAINSSTRING(<within text>, <find text>)
Contains String Measure = CONTAINSSTRING(SELECTEDVALUE('Example Data_Inf_Func'[Furniture]),"Sofas")
```
#### ContainsStringExact
Whether one string contains another is indicated by a return value of TRUE or FALSE
```
Syntax: CONTAINSSTRINGEXACT(<within_text>, <find_text>)
ContainsStringExtract = CONTAINSSTRINGEXACT(SELECTEDVALUE('Example Data_Inf_Func'[Furniture]),"Sofas")
```
#### IsBlank
If the value is blank, this function returns true;    
```
Syntax: ISBLANK(<Value>)
Is_blank = ISBLANK(Sheet1[name])
```
#### IsNumber
This function determines whether a value is a number before returning either true or false.                   
```
Syntax:  ISNUMBER(<value>)
Is_number = ISNUMBER(Sheet1[id])
```

### Logical Functions

#### IF
Checks whether the expression supplied to it evaluates to True or False and then executes the statements depending upon the result.
```
Syntax: IF(<logical_test>, <value_if_true>[, <value_if_false>])
Sales Status = IF(Data_Logical_Func[Net Sales]>500,"High", "Low")
```
#### AND
Return True if both the expressions supplied evaluate to True.
```
Syntax: AND(<logical1>,<logical2>)
Canada Sales = IF(AND(Data_Logical_Func[Country]="Canada", Data_Logical_Func[Net Sales]>500), "Valid", "Invalid")
```
#### COALESCE
Identifies the first expression that is not BLANK and returns it. BLANK is returned if all expressions evaluate to NULL.
```
Syntax: COALESCE(<expression>, <expression>[, <expression>]…)
CoalDemo = COALESCE(Data_Logical_Func[Country Code], BLANK(), BLANK(), "Default", BLANK())
```
#### IFERROR
Returns the value of the expression itself unless the expression returns an error, in which case it returns a specified value.
```
Syntax: IFERROR(value, value_if_error)
ErrorDemo = IFERROR(Data_Logical_Func[Net Sales],0)
```
#### NOT
This function converts either FALSE or TRUE values into the other.
```
Syntax: NOT(<logical>)
CanadaNotDemo = IF(NOT(Data_Logical_Func[Country]="Canada"), "Valid","Invalid")
```
#### OR
Returns true if any one of the expressions supplied to it evaluates to True.
```
Syntax: OR(<logical1>,<logical2>)
CanadaSales = IF(OR(Data_Logical_Func[Country]="Canada", Data_Logical_Func[Net Sales]>500),"Valid","Invalid")
```
#### SWITCH
Returns one of several potential result expressions after comparing an expression to a list of values.
```
Syntax: SWITCH(<expression>, <value>, <result>[, <value>, <result>]…[, <else>])
Country Code = SWITCH(Data_Logical_Func[Country], "Canada", "CA", "Germany", "GE", "France", "FR")
```

### Mathematical and Trigonometric Functions

- SIN: It gives the sine of the value supplied to it.
- COS: It returns the cosine of a given value.
- TAN: It returns the tangent of a given value.
- COSEC: It gives the cosecant of a value 
- SEC: It returns the secant of a value.
- COT: It returns the cotangent of a value 
- ROUND: It takes 2 arguments. First is the number to be rounded off and second is the number of digits to which the number should be rounded off.

### Statistical Functions

- COMBIN: It is used to calculate the number of combinations for a given number without repetition.
- COMBINA: It gives the number of combinations for a given value with repetition.
- GEOMEAN: Returns the geometric mean of column values.
- MEDIAN: Returns the median value in a column 
- PERMUT: This function gives the number of permutations for given values 
- STDEV.P: It is used to calculate the standard deviation of the complete population.
- STDEV.S: It is used to calculate the standard deviation of the sample population.

### Text Functions

- CONCATENATE: This function is used to join two strings or words.
- EXACT: It compares two strings and returns True if they are exactly the same.
- LEN: It is used to find the length of the string.
- LOWER: Converts a string to lowercase.
- UPPER: Converts a string to upper case.
- TRIM: This function removes all the whitespaces from the beginning and starting of a given string.

#### BLANK ()
Returns a blank.
```

```

#### LEN ()
Returns the number of characters in a text string.
```
Length = LEN(Employee[EmpName])
```

#### CONCATENATE ()
Joins two text strings into one text string.
```
NameID = CONCATENATE(Employee[EmpID], Employee[EmpName])
```

#### CONCATENATEX ()
Concatenates the result of an expression evaluated for each row in a table.
```
CityWiseEmp = CONCATENATEX(Employee, Employee[EmpName], ",") 
```

#### LEFT ()
Returns the specified number of characters from the left side of a given text string.
```
Left = LEFT(Employee[EmpName])
Left2 = Left(Employee[EmpName], 2)
```

#### RIGHT ()
Returns the specified number of characters from the right side of a given text string.
```
Right = RIGHT(Employee[EmpName])
Right3 = RIGHT(Employee[EmpName], 3)
```

#### MID ()
Returns a string of characters from the middle of a  text string. 
```
Mid2 = MID(Employee[EmpName], 3, 2)
```

#### UPPER ()
Converts a text string to all uppercase letters.
```
Upper = UPPER(Employee[EmpName])
```

#### LOWER ()
Converts a text string to all lowercase letters.
```
Lower = LOWER(Employee[EmpName])
```

#### TRIM ()
Removes all spaces from text.
```
Trim = TRIM(Employee[EmpName])
```

#### SUBSTITUTE ()
Replace existing text with new text in a text string.
```
Substitute = SUBSTITUTE(Employee[EmpName],"Abhinav","Adam") 
```

#### REPLACE ()
Replaces a part of a text string.
```
Replace = REPLACE(Employee[Salary], 2,3,999) 
Replaces the characters from 2nd character to 3 characters. 
From 1200 to 1999
```

#### EXACT ()
Compares two text strings and returns TRUE if they are exactly the same, otherwise returns FALSE.
```
Exact = EXACT("Abhinav", "Adam")
```

#### FIND ()
Returns the starting position of one text string within another text string.
```

```

#### FORMAT ()
Converts a value to text according to the specified format.
```

```

### Table Manipulation Functions

- CROSSJOIN: Returns the cartesian product of two tables that contains rows from both tables.
- DISTINCT table: This function returns a table with unique values. Rows with duplicate values are eliminated from the table.
- GROUPBY: It is similar to the GROUPBY function in SQL 
- INTERSECT: This function returns the intersection of two tables without removing the duplicates.

## DAX Window Function
The WINDOW function in DAX facilitates computations like Moving Averages or Running Sums, offering flexibility with absolute or relative positioning for extracting result slices based on ranges.

Filter Window
```
WINDOW ( from[, from_type], to[, to_type][, <relation>][, <orderBy>][, <blanks>][, <partitionBy>] )
```
- from: Defines the starting point of the window.
Can be relative (REL) or absolute (ABS).
    - REL: Rows to go back or forward from the current row.
    - ABS: Position from the beginning or end of the partition.
- to: Indicates the end of the window, similar to 'from'.
- from_type: Specifies the behavior of 'from' (REL or ABS).
- to_type: Defines the behavior of 'to', similar to 'from_type'.
- relation: Optional table expression for retrieving output.
If used, all columns in orderBy and partitionBy must originate from this table.
- orderBy: Optional clause for specifying sorting within each partition.
- blanks: Specifies how to handle blank data when sorting (e.g., KEEP).
- partitionBy: Optional clause defining partitioning columns for the relationship.
