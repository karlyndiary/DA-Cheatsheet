## Table of Contents

- [Introduction](#introduction)
- [Dax Functions](#dax-functions)
    - [Date and Time Functions](#date-and-time-functions)
    - [Logical Functions](#logical-functions)
    - [Mathematical and Trigonometric Functions](#mathematical-and-trigonometric-functions)
    - [Statistical Functions](#statistical-functions)
    - [Text Functions](#text-functions)
    - [Table Manipulation Functions](#table-manipulation-functions)
    - [Filter Index](#filter-index)
    - [DAX COUPDAY Financial Function](#dax-coupday-financial-function)
- [DAX Window Function](#dax-window-function)
## Introduction

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

#### sin(θ) Trigonometric Function
Returns the sine of the specified angle.
sine of 45° in radians.
```
syntax: SIN(number)
sin = SIN(RADIANS(45))
```
#### cos(θ) Trigonometric Function
The Power BI DAX COS function returns the cosine value of the angle.
cosine of 60° in radians.
```
syntax: COS(number)
COS = COS(RADIANS(60))
```
#### sinh(θ) Trigonometric Function
Returns a number’s hyperbolic sine.
Hyperbolic sine of 13 in radians.
```
syntax: SINH(number)
sinh = SINH(13)
```
#### cosh(θ) Trigonometric Function
Returns the hyperbolic cosine of any real number equal to or greater than 1.
The hyperbolic cosine of 12 in radians.
```
syntax: COSH(number)
cosh = COSH(12)
```
#### tan(θ) Trigonometric Function
Returns the angle’s tangent.
tangent of -3 in radians.
```
syntax: TAN(number)
tan = TAN(-3)
```
#### tanh(θ) Trigonometric Function
The hyperbolic tangent of a number is returned by it.
The hyperbolic tangent of 23 in radians.
```
syntax: TANH(number)
tanh = TANH(23)
```
#### cot(θ) Trigonometric Function
The function returns the cotangent of a real angle with a radian value.
The cotangent of 25 in radians.
```
syntax: COT(number)
cot = COT(25)
```
#### coth(θ) Trigonometric Function
The hyperbolic cotangent of a hyperbolic angle whose absolute value must be greater than 1, is returned by the function.
The hyperbolic cotangent of 37 in radians.
```
syntax: COTH(number)
coth = COTH(37)
```
#### asin(θ) Trigonometric Function
A number’s arcsine, or inverse sine, is returned by the ASIN() function. The angle whose sine is number is called the arcsine. The returned angle is between -pi/2 and pi/2 in radians. The number in radian must be from -1 to 1.
Inverse sine of 0.8 in radians.
```
syntax: ASIN(number)
asin = ASIN(0.8)
```
#### asinh(θ) Trigonometric Function
The function ASINH(number) returns the real number’s inverse hyperbolic sine. As ASINH(SINH(number)) equals number, the value whose hyperbolic sine is number is called the inverse hyperbolic sine.
inverse hyperbolic sine of 55 in radians.
```
syntax: ASINH(number)
asinh = ASINH(55)
```
#### acos(θ) Trigonometric Function
The function ACOS() returns the real number’s arccosine, or inverse cosine. The angle whose cosine is a number is called an arccosine. The returning angle is specified from 0 to pi in radians. The number in radian must be from -1 to 1.
arccosine of -0.5 in radians.
```
syntax: ACOS(number)
acos = ACOS(-0.5)
```
#### acosh(θ) Trigonometric Function
Returns a real number’s inverse hyperbolic cosine. It must be greater than or equal to one. ACOSH(COSH(number)) corresponds to a  number because the inverse hyperbolic cosine is the value whose hyperbolic cosine is a number.
inverse hyperbolic of 60 cosine in radians.
```
syntax: ACOSH(number)
acosh = ACOSH(60)
```
#### atan(θ) Trigonometric Function
Provides a number’s arctangent, or inverse tangent. The angle whose tangent is a number is an arctangent. The returned angle is between -π/2 and π/2 in radians.
inverse tangent of 48 in radians.
```
syntax: ATAN(number)
atan = ATAN(48)
```
#### atanh(θ) Trigonometric Function
The function ATANH() returns a number’s inverse hyperbolic tangent. The number must be ranged from -1 to 1. (excluding -1 and 1). In other words, ATANH(TANH(number)) equals number. The inverse hyperbolic tangent is the value whose hyperbolic tangent is a number.
inverse hyperbolic tangent of 0.7 in radians.
```
syntax: ATNH(number)
atanh = ATANH(0.7)
```
#### acot(θ) Trigonometric Function
The function ACOT() returns the arccotangent or inverse cotangent, or principal value, of an integer.
The inverse cotangent of 60 in radians.of
```
syntax: ACOT(number)
acot = ACOT(60)
```
#### acoth(θ) Trigonometric Function
ACOTH() returns a number of inverse hyperbolic cotangents.
The inverses hyperbolic cotangent of 33 in radians.
```
syntax: COTH(number)
acoth = ACOTH(33)
```

### Statistical Functions

- COMBIN: It is used to calculate the number of combinations for a given number without repetition.
- COMBINA: It gives the number of combinations for a given value with repetition.
- GEOMEAN: Returns the geometric mean of column values.
- MEDIAN: Returns the median value in a column 
- PERMUT: This function gives the number of permutations for given values 
- STDEV.P: It is used to calculate the standard deviation of the complete population.
- STDEV.S: It is used to calculate the standard deviation of the sample population.

### Text Functions

#### BLANK ()
Returns a blank.
```
Blank = If(Employee[Number of Days] = 0, BLANK (), Employee[Salary]/Employee[Number of Days])
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
Find = FIND("hi", "Abhinav")
```

#### FORMAT ()
Converts a value to text according to the specified format.
```
Format = FORMAT(Employee[DOJ],"MM-DD-YYYY")
```

### Table Manipulation Functions

- CROSSJOIN: Returns the cartesian product of two tables that contains rows from both tables.
- DISTINCT table: This function returns a table with unique values. Rows with duplicate values are eliminated from the table.
- GROUPBY: It is similar to the GROUPBY function in SQL 
- INTERSECT: This function returns the intersection of two tables without removing the duplicates.

### Filter Index 

- DAX Filter Index retrieves a row from a table based on a specified position.
- Position parameter is 1-based, meaning the first row is at position 1, second row at position 2, and so forth.
- Negative positions indicate counting from the end, -1 being the last row, -2 being the second last, and so on.
- If the specified position is outside the bounds or zero, or if it's BLANK(), an empty table is returned.
- The relation parameter specifies the table from which the output is retrieved. If omitted, it needs to be derived from orderBy and partitionBy parameters.
- The orderBy parameter specifies the order of rows within each split. If omitted, it defaults to all columns in the relation that aren't already specified in partitionBy.
- The blanks parameter determines how empty values are handled during sorting, with the default option being KEEP where blank values are sorted before numerical or date values and before all strings.
- The partitionBy parameter defines how the relationship is partitioned. If omitted, the entire relation is treated as a single partition.

```
Syntax: INDEX(<position>[, <relation>][, <orderBy>][, <blanks>][, <partitionBy>])
Table = INDEX(1,ALL(DimDate[EnglishMonthName]))
Table 2 = INDEX(1, DISTINCT(DimDate), ORDERBY(DimDate[DateKey], ASC), DEFAULT, PARTITIONBY(DimDate[EnglishMonthName]))
```

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

## DAX COUPDAY Financial Function

#### COUPDAYBS
ACOTH() returns a number of inverse hyperbolic cotangents.
The inverses hyperbolic cotangent of 33 in radians.
```
syntax: COTH(number)
acoth = ACOTH(33)
```
#### COUPDAYS
ACOTH() returns a number of inverse hyperbolic cotangents.
The inverses hyperbolic cotangent of 33 in radians.
```
syntax: COTH(number)
acoth = ACOTH(33)
```
#### COUPDAYSNC
ACOTH() returns a number of inverse hyperbolic cotangents.
The inverses hyperbolic cotangent of 33 in radians.
```
syntax: COTH(number)
acoth = ACOTH(33)
```


