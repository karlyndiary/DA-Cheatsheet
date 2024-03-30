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
#### DATE 
It gives the current date in the DateTime format.
```
Syntax: DATE(<year>, <month>, <day>)
date = DATE(2013,11,18)
```
#### Datevalue 
It gives the current date in the DateTime format.
```
Syntax: DATEVALUE(date_text)
datevalue = DATEVALUE(“25 12 2002”)
```
#### DATEDIFF
Returns the number of boundaries between the time frame to compare dates with. Any of the following values may be the value of the Interval: Second, 
Minute, 
Hour, 
Day, 
Week, 
Month, 
Quarter,
Year
```
Syntax: DATEDIFF(<Date1>, <Date2>, <Interval>)
datediff = DATEDIFF(DATE (2001, 07, 01 ),DATE (2002, 12, 31 ),YEAR)
```
#### DAY
A number between 1 and 31 represents the day of the month. The date of the day you’re looking for is an argument for the DAY function. Dates can be passed to the method by inputting them in a DateTime format, using another date function, or using an expression that yields a date. Additionally, you can type a date in one of the acceptable date string formats.
```
Syntax: DAY(<date>)
day = DAY(“25-12-2002”)
```
#### Edate
A date that is the specified number of months before or after the start date is returned. To determine maturity dates or due dates that occur on the same day of the month as the date of issue, use the EDATE function.
```
Syntax: EDATE(<start_date>, <months>)
edate = EDATE(“28-11-1920”,4)
```
#### Eomonth
Returns the date of the final day of the month, before or after a specified number of months, in DateTime format. To get maturity dates or due dates that fall on the last day of the month, use the EOMONTH function.
```
Syntax: EOMONTH(<start_date>, <months>)
eomonth = EOMONTH(“28-11-1920”,3)
```
#### MONTH
Returns the month as a number from 1 to 12. 1 represents January and 12 represents December.
```
Syntax: MONTH(<datetime>)
month = MONTH(“28-11-1920”)
```
#### YEAR
Returns the year from a given date. The returned value is in the range of 1900-9999.
```
Syntax: YEAR(<date>)
year = YEAR(DATE(2022,3,12))
```
#### YearFrac
Determines the fraction of the year that the number of full days between two dates corresponds to.
```
Syntax: YEARFRAC(<start_date>, <end_date>, <basis>)
yearfrac = YEARFRAC(DATE(2022,3,12),DATE(2022,6,2),2)
```
#### NOW
Returns the current date and time of the system.
```
Syntax: NOW()
now = NOW()
```
#### Today
Gives the current date back. The TODAY function comes in handy when you want the current date to be shown on a worksheet regardless of when the workbook is opened. It can be used to compute intervals as well.
```
Syntax: TODAY()
now = NOW()
```
#### Utcnow
Gives the current date and time in UTC. The UTCNOW function’s output only varies when the formula is updated. It isn’t always being updated.
```
Syntax: UTCNOW()
utcnow = UTCNOW()
```
#### UtcToday
Gives the current date in UTC.
```
Syntax: UTCTODAY()
utctoday = UTCTODAY()
```
#### Weekday
Gives a number between 1 and 7 indicating the date’s weekday. The day defaults to being from 1 (Sunday) to 7 (Saturday).
```
Syntax: WEEKDAY(<date>, <return_type>)
weekday = WEEKDAY(DATE(2007,2,4))
```
#### Weeknum
According to the return type value, returns the week number for the specified date
```
Syntax: WEEKNUM(<date>[, <return_type>])
weeknum = WEEKNUM(DATE(2007,2,4))
```
#### UtcToday
Gives the current date in UTC.
```
Syntax: UTCTODAY()
utctoday = UTCTODAY()
```
#### QUARTER
Gives back the quarter as a number between 1 (January through March) and 4. (October – December). The output value is also blank if the input value is blank.
```
Syntax: QUARTER(<date>)
quarter = QUARTER(DATE(1990,02,14))
```

#### Calendar
```
Syntax: CALENDAR(<start_date>, <end_date>)
calendar = CALENDAR(05-01-1980,31-01-1990)
```
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

#### Mathematical Functions

#### ABS Math Function
This function returns a number’s absolute value.  Whether whole or decimal, a decimal number without its sign represents a number’s absolute value.
```
syntax: ABS(<number>) 
ABS = ABS(572369.5499999996 - 943454.36)
```
#### Ceiling Math Function
This function increases a number by rounding it up to the nearest integer or significant multiple.
```
syntax: CEILING(<number>, <significance>)
ceiling = CEILING(572369.5499999996, 0.01)
```
#### Convert Math Function
The convert function performs the transformation of a data type-specific expression.
```
syntax: CONVERT(<Expression>, <Datatype>)
convert = CONVERT(DATE(1997,12,23), INTEGER)
```
#### Currency Math Function
The currency function returns the result as a currency data type after evaluating the argument.
```
syntax: CURRENCY(<value>)
currency = CURRENCY(23.44)
```
#### Degrees Math Function
The degrees function converts a given angle from radians into degrees.
```
syntax: DEGREES (angle)
degrees = DEGREES(PI())
```
#### Divide Math Function
This function divides and provides a different result, or BLANK () when dividing by 0, as appropriate.
```
syntax: DIVIDE(<numerator>, <denominator> [, <alternate result>])
divide = DIVIDE(234,12)
```
#### Even Math Function
The number is given back and rounded to the next even integer. This function can be used to process objects that come in pairs.
```
syntax: EVEN (number)
even = EVEN(23.44)
```
#### Exp Math Function
Returns e to the power of the specified number. The natural logarithm’s base, 2.71828182845904, is equal to the constant e.
```
syntax: EXP(<number>)
exp = EXP(4)
```
#### Fact Math Function
The series 1*2*3*…*, ending in the provided number, is returned as the factorial of the supplied number.
```
syntax: FACT(<number>)
fact = FACT(5)
```
#### Floor Math Function
Brings a number down to its nearest multiple of importance by rounding it down toward zero.
```
syntax: FLOOR(<number>, <significance>)
floor = FLOOR(245.33,0.3)
```
#### GCD Math Function
This function returns the largest common divisor of two or more integers. The biggest integer that divides both numbers 1 and 2 without leaving a residual is known as the greatest common divisor.
```
syntax: GCD (number1, [number2], …)
gcd = GCD(122,4)
```
#### INT Math Function
Round and gives a number down to the nearest integer.
```
syntax: INT(<number>)
int = INT(55.44)
```
#### Iso.Ceiling Math Function
Increases a number by rounding it up to the nearest integer or significant multiple.
```
syntax: ISO.CEILING(<number> [, <significance>])
iso.ceiling = ISO.CEILING(2.999,0.2)
```
#### LCM Math Function
The least frequent multiple of integers is returned. The smallest positive integer that is a multiple of all the integer parameters (number1, number2, etc.) is known as the least common multiple. To add fractions with various denominators, use LCM.
```
syntax: LCM (number1, [number2], …)
lcm = LCM(45,56)
```
#### LN Math Function
Gives a number’s natural logarithm. Based on the value of the constant e, natural logarithms (2.71828182845904).
```
syntax: LN(<number>)
ln = LN(0.004)
```
#### LN Math Function
Gives a number’s natural logarithm. Based on the value of the constant e, natural logarithms (2.71828182845904).
```
syntax: LN(<number>)
ln = LN(0.004)
```
#### LOG Math Function
Gives a number’s logarithm to the base you specify.
```
syntax: LOG(<number>, <base>)
log = LOG(1035,3)
```
#### LOG10 Math Function
Gives the base-10 logarithm of a number.
```
syntax: LOG10(<number>)
log10 = LOG10(1035)
```
#### LN Math Function
Gives a number’s natural logarithm. Based on the value of the constant e, natural logarithms (2.71828182845904).
```
syntax: LN(<number>)
ln = LN(0.004)
```
#### MOD Math Function
Returns the leftover amount after dividing a number by a divisor. The sign of the result is always the same as the divisor.
```
syntax: MOD(<number>, <divisor>)
mod = MOD(1035,5)
```
#### MOD Math Function
Returns the leftover amount after dividing a number by a divisor. The sign of the result is always the same as the divisor.
```
syntax: MOD(<number>, <divisor>)
mod = MOD(1035,5)
```
#### MROUND Math Function
Gives you a number with the necessary multiple rounded off.
```
syntax: MROUND(<number>, <multiple>)
mround = MROUND(455.6,5)
```
#### ODD Math Function
The number is given back, rounded to the nearest odd integer.
```
syntax: ODD (number)
odd = ODD(455.6)
```
#### Pi Math Function
Gives Pi in decimal form, 3.14159265358979, with a 15-digit precision.
```
syntax: PI()
pi = PI()
```
#### Power Math Function
Returns the value of a number raised to a power of exponent.
```
syntax: POWER(<number>, <power>)
power = POWER(5,3)
```
#### Quotient Math Function
The division is done, and just the integer part of the result is returned. When you want to throw away the divisional leftover, use this function.
```
syntax: QUOTIENT(<numerator>, <denominator>)
quotient = QUOTIENT(234,3)
```
#### Radians Math Function
Converts an angle from degrees to radians.
```
syntax: RADIANS (angle)
radians = RADIANS(90)
```
#### Rand Math Function
Returns a uniformly distributed random number that is higher than or equal to 0 and less than 1. Every time the cell containing this function is recalculated, a different number is returned.
```
syntax: RAND ()
rand = RAND()
```
#### Quotient Math Function
The division is done, and just the integer part of the result is returned. When you want to throw away the divisional leftover, use this function.
```
syntax: QUOTIENT(<numerator>, <denominator>)
quotient = QUOTIENT(234,3)
```
#### RandBetween Math Function
Gives you a random number that falls between the two values you provide.
```
syntax: RANDBETWEEN(<bottom>, <top>)
randbetween = RANDBETWEEN(23,44)
```
#### Round Math Function
Rounds a value to the specified number of digits.
- The number is rounded to the specified number of decimal places if num digits are higher than zero.
- The number is rounded to the nearest integer if the num digit is 0.
- The number is rounded to the left of the decimal point if the num digits are less than 0.
```
syntax: ROUND(<number>, <num_digits>)
round = ROUND(23.44444,4)
```
#### RoundDown Math Function
Rounds a number in the direction of zero
```
syntax: ROUNDDOWN(<number>, <num_digits>)
round down = ROUNDDOWN(23.44444,1)
```
#### RoundUp Math Function
It rounds a number up, away from 0 (zero).
```
syntax: ROUNDUP(<number>, <num_digits>)
round up = ROUNDUP(23.44444,1)
```
#### Sign Math Function
Identifies a number’s sign, a calculation’s outcome, or a value in a column. If the number is positive, the function returns 1, if it is zero, it returns 0, and if it is negative, it returns -1.
```
syntax: SIGN(<number>)
sign = SIGN(23.44444)
```
#### Sqrt Math Function
Gives the square root of a number.
```
syntax: SQRT(<number>)
sqrt = SQRT(23.44444)
```
#### SqrtPi Math Function
Gives the (number times pi) square root.
```
syntax: SQRTPI (number)
sqrtpi = SQRTPI(23.44444)
```
#### Trunc Math Function
Removes the fractional or decimal portion of a number to convert it to an integer.
```
syntax: TRUNC(<number>, <num_digits>)
truncate = TRUNC(45.0000345,6)
```
#### Trigonometric Function

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
- GROUPBY: It is similar to the GROUPBY function in SQL 
- INTERSECT: This function returns the intersection of two tables without removing the duplicates.

#### Distinct()
It is a Table Manipulation function that returns a table or manipulates existing tables. Measures are used in some of the most common data analyses.
```
Syntax: DISTINCT (<column name>)
Distinct = DISTINCT(Data_Logical_Func[Country])
```

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
DAX COUPDAYBS reveals how many days there are between the start of a coupon period and its settlement date.
```
syntax: COUPDAYBS(<settlement>, <maturity>, <frequency>[, <basis>])
COUPDAYBS = EVALUATEANDLOG(COUPDAYBS(DATE(2011, 1, 25),DATE(2011, 11, 15), 2, 1))
```
- settlement: The settlement date for the security. The day after the issuance date - when the security is traded to the buyer is known as the settlement date for securities.
- maturity: The maturity date of the security. The security’s expiration date is known as the maturity date.
- frequency: The quantity of annual coupon payments. The frequency for annual payments is 1, for semi-annual payments is 2, and for quarterly payments is 4.
- basis: The kind of day count foundation to employ (optional). Basis is taken to be 0 if it is omitted. Below this table is a list of the acceptable values.

| Basis | Day Count Basis      |
|-------|----------------------|
| 0     | US (NASD) 30/360     |
| 1     | Actual/actual        |
| 2     | Actual/360           |
| 3     | Actual/365           |
| 4     | European 30/360      |

#### COUPDAYS
DAX COUPDAYS gives the total number of days that make up the coupon term, including the settlement date.
```
syntax: COUPDAYS(<settlement>, <maturity>, <frequency>[, <basis>])
Coupdays = EVALUATEANDLOG({COUPDAYS(DATE(2011,1,25),DATE(2011,12,15),2,1)})
```
- settlement: The settlement date for the security. The day after the issuance date when the security is traded to the buyer is known as the settlement date for securities.
- maturity: The maturity date of the security. The security’s expiration date is known as the maturity date.
- frequency: The quantity of annual coupon payments. The frequency for annual payments is 1, for semi-annual payments is 2, and for quarterly payments is 4.
- basis: The kind of day count foundation to employ (optional). Basis is taken to be 0 if it is omitted. Below this table is a list of the acceptable values.

| Basis           | Day Count Basis      |
|-----------------|----------------------|
| 0 or omitted    | US (NASD) 30/360     |
| 1               | Actual/actual        |
| 2               | Actual/360           |
| 3               | Actual/365           |
| 4               | European 30/360      |

#### COUPDAYSNC
The number of days between the settlement date and the following coupon date is returned.
```
Syntax: COUPDAYSNC(<settlement>, <maturity>, <frequency>[, <basis>])
Coupdaysnc = EVALUATEANDLOG({COUPDAYSNC(DATE(2011, 1, 25), DATE(2011, 11, 15), 2, 1)})
```
- settlement: The settlement date for the security. The day after the issuance date when the security is traded to the buyer is known as the settlement date for securities.
- maturity: The maturity date of the security. The security’s expiration date is known as the maturity date.
- frequency: The quantity of annual coupon payments. The frequency for annual payments is 1, for semi-annual payments is 2, and for quarterly payments is 4.
- basis: The kind of day count foundation to employ (optional). Basis is taken to be 0 if it is omitted. Below this table is a list of the acceptable values.

| Basis           | Day Count Basis      |
|-----------------|----------------------|
| 0 or omitted    | US (NASD) 30/360     |
| 1               | Actual/actual        |
| 2               | Actual/360           |
| 3               | Actual/365           |
| 4               | European 30/360      |

## DAX Depreciation Functions

#### AMORDEGRC
The function calculates depreciation for each accounting period, similar to AMORLINC, but with a depreciation coefficient applied based on the asset's lifespan.
```
Syntax: AMORDEGRC(<cost>, <date_purchased>, <first_period>, <salvage>, <period>, <rate>[, <basis>])
Amordegrc = EVALUATEANDLOG(AMORDEGRC(2400, DATE(2008,8,19),DATE(2008,12,31), 300, 1, 0.15, 1)) 
```
- Cost: The initial cost of the asset.
- Purchase date: The date when the asset was acquired.
- Date of the first period: The date when the first period starts.
- Salvage: The value at the end of the depreciation (sometimes called the "residual value").
- Period: The period of depreciation.
- Rate: The rate of depreciation.
- Basis: The type of day count basis to use.

| Basis | Date system                    |
|-------|--------------------------------|
| 0     | 360 days (NASD method)         |
| 1     | Actual                         |
| 3     | 365 days in a year             |
| 4     | 360 days in a year (European method) |

#### AMORLINC
This function provides the depreciation amount for each accounting period. It uses a depreciation coefficient based on the asset's lifespan, unlike AMORLINC.
```
Syntax: AMORLINC(<cost>, <date_purchased>, <first_period>, <salvage>, <period>, <rate>[, <basis>])
Amorlinc = EVALUATEANDLOG(AMORLINC(2400, DATE(2008,8,9),DATE(2008,12,31),300,1,0.15,1))
```
#### DB
Gives back an asset’s depreciation over a given period using the fixed-declining balanced approach.	
```
Syntax: DB(<cost>, <salvage>, <life>, <period>[, <month>])
DB = EVALUATEANDLOG(DB(1000000,0,6,1,2))
```
- Cost: The asset’s initial price.
- Salvage: The final value after depreciation (sometimes called the salvage value of the asset). This number may be zero.
- Life: The length of time that an asset is depreciated (sometimes called the useful life of the asset).
- Period: The time frame that you want to use to determine depreciation. The same un- its must be used for a period and life. between 1 and life, please (inclusive).
- Month: The total number of months in the first year, if applicable. A month is taken to be 12 if it is absent.

#### DDB
This function calculates the asset's depreciation using the fixed-declining balance method for the given time period.
```
Syntax: DDB(<cost>, <salvage>, <life>, <period>[, <factor>])
DBB = EVALUATEANDLOG(DDB(1000000, 0, 6, 1, 2))
```
#### SLN
Provides a one-time asset’s straight-line depreciation.	
```
Syntax: SLN(<cost>, <salvage>, <life>)
SLN = EVALUATEANDLOG(SLN(30000,7500,10))
```
- Cost- The asset’s initial price.
- Salvage- The final value after depreciation (sometimes called the salvage value of the asset). This number may be zero.
- Life- The length of time that an asset is depreciated (sometimes called the useful life of the asset).

#### SYD
Returns the asset’s annualized depreciation over a given time period.	
```
Syntax: SYD(<cost>, <salvage>, <life>, <per>)
SYD = EVALUATEANDLOG(SYD(30000.00, 7500.00, 10, 1))
```

## DAX Aggregate & Counting Functions
These functions calculate a (scalar) value such as the count for all rows in a column or table as defined by the expression. Measures are used in some of the most common data analyses.
#### Average
This function computes the average of the values contained in the provided column as input.
```
Syntax: AVERAGE(<column>)
average = AVERAGE('SLS Order Detials_Master'[Image])
```
#### AverageA
Gives the average (arithmetic mean) of the values in a column. The AVERAGEA function averages the values in a column and also manages non-numeric data types in accordance with the following guidelines:
- Values that are TRUE, count as 1.
- Empty text (“”) counts as 0 (zero). Non-numeric text values have a count of 0 (zero).
- FALSE values are counted as 0 values (zero).
```
Syntax: AVERAGEA(<column>)
averagea = AVERAGEA('SLS Order Detials_Master'[Unit Price (INR/Unit)])
```
#### AverageX
Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.
```
Syntax: AVERAGEX(<table>,<expression>)
averagex = AVERAGEX('SLS Order Detials_Master',
                    'SLS Order Detials_Master'[Unit Price (INR/Unit)]+
                    'SLS Order Detials_Master'[Tax amount (INR)])
```
#### COUNT
This function only accepts a column as an argument. The following types of values are counted in rows using the COUNT function:
- Numbers
- Dates
- Strings
```
Syntax: COUNT(<column>)
Count = COUNT(Data_Logical_Func[Country])
```
#### COUNTA
Determines how many rows in the chosen column have non-blank values. The function returns a blank if it cannot locate any rows to count.
```
Syntax: COUNTA(<column>)
CountA = COUNTA(Data_Logical_Func[Country])
```
#### CountX
It evaluates an expression over a table and counts the number of rows that contain a number or an expression that evaluates to a number. It can be used to calculate the counts of rows based on certain expressions within FILTER. 
```
Syntax: COUNTX(<table, expression>) 
Syntax: COUNTX(FILTER(<table, expression>, [column of which counts needs to be returned]))
CountX = COUNTX(FILTER(Data_Logical_Func, Data_Logical_Func[Qty Sold]>=350), Data_Logical_Func[Product])
```
#### COUNTAX
It counts non-blank results when evaluating the result of an expression over a table. When determining the outcome of an expression over a table, the COUNTAX function counts results that are not blank.
```
Syntax: COUNTAX(<table, expression>)
CountAX = COUNTAX(Data_Logical_Func, Data_Logical_Func[Net Sales])
```
#### DistinctCount
It determines how many unique values there are in a column. This function only accepts a column as an argument.
```
Syntax: DISTINCTCOUNT(<table>)
DistinctCount = DISTINCTCOUNT(Data_Logical_Func[Country])
```
#### DistinctCountNoBlank
Counts the number of distinct values in a column.
```
Syntax: DISTICTCOUNTNOBLANK(<column>)
distinct count no blank = DISTINCTCOUNTNOBLANK('SLS Order Detials_Master'[Product Name] )
```
#### CountBlank
It analyzes the outcome of an expression across a table and counts outcomes that are not blank. A column is the only argument this function accepts. Columns can include any kind of data, but only blank cells are counted. Due to the fact that zero is a valid numeric value and not a blank cell, cells with the value zero (0) are not counted.
```
Syntax: COUNTBLANK(<column>)
CountBlank = COUNTBLANK(Data_Logical_Func[Country Code])
```
#### CountRows
It determines how many rows there are in the supplied table or a table that has been defined using an expression.
```
Syntax: COUNTROWS([<table>])
CountRows = COUNTROWS(Data_Logical_Func)
```
#### Max
Returns the largest numeric value in a column, or between two scalar expressions.
```
Syntax: MAX(<column>)
max = MAX('SLS Order Detials_Master'[Unit Price (INR/Unit)])
```
#### MaxA
Returns the largest value in a column.
```
Syntax: MAXA(<column>)
maxa = MAXA('SLS Order Detials_Master'[Total amount (INR)])
```
#### Maxx 
Evaluates an expression for each row of a table and return the largest numeric value.
```
Syntax: MAXX(<table, expression>)
maxx = MAXX('SLS Order Detials_Master', 
                    'SLS Order Detials_Master'[Image] +
                    'SLS Order Detials_Master'[Unit Price (INR/Unit)])
```
#### Min
Returns the smallest numeric value in a column, or between two scalar expressions.
```
Syntax: MIN(<column>)
min = MIN('SLS Order Detials_Master'[Unit Price (INR/Unit)])
```
#### MinA
Returns the smallest value in a column, including any logical values and numbers represented as text.
```
Syntax: MINA(<column>)
mina = MINA('SLS Order Detials_Master'[Tax amount (INR)])
```
#### MinX
Returns the smallest numeric value that results from evaluating an expression for each row of a table.
```
Syntax: MINX(<table, expression>)
minx = MINX('SLS Order Detials_Master', 
                'SLS Order Detials_Master'[Image] +
                'SLS Order Detials_Master'[Unit Price (INR/Unit)])
```
#### Product
Returns the product of the numbers in a column.
```
Syntax: PRODUCT(<column>)
product = PRODUCT(Sheet1[Unit Price (INR/Unit)])
```
#### ProductX
Returns the product of an expression evaluated for each row in a table.
```
Syntax: PRODUCTX(<table, expression>)
productx = PRODUCTX(Sheet1,Sheet1[Image]+Sheet1[Unit Price (INR/Unit)])
```
#### Sum
Adds all the numbers in a column.
```
Syntax: SUM(<column>)
sum = SUM(Sheet1[Unit Price (INR/Unit)])
```
#### SumX
Returns the sum of an expression evaluated for each row in a table.
```
Syntax: SUMX(<table, expression>)
sumx = SUMX(Sheet1,Sheet1[Image]+Sheet1[Unit Price (INR/Unit)])
```
