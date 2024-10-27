### Number Functions

- Ceiling: Rounds up the number. Ceiling(1.8) => 2
  - Ceiling([Sales])
- Floor: Rounds down the number. Floor(1.8) => 1
  - Floor([Sales])
- Round: Round the number to its nearest integer. Round(1.8) => 2
  - Round([Sales]), Round([Sales], 2)

### String Function

- Change Case
  - Upper: Uppercase. Upper(Name) => LOLA. Good for Codes
  - Lower: Lowercase. Lower(Name) => lola. Good for long sentences.

- Remove Spaces
  - LTrim: Removes leading spaces. LTrim( Product) => Product
  - RTrim: Removes trailing spaces. RTrim(Product ) => Product
  - Trim: Removes leading and trailing spaces. Trim( Product ) => Product

- Extract
  - Left: Left(Canon-456-cer5, 5) => Canon
  - Right: Right(Canon-456-cer5, 4) => cer5
  - Mid: Mid(Canon-456-cer5, start, length) => Mid(Canon-456-cer5, 7, 3) => 456

- Search for patterns
  - Startwith: It checks if the string begins with a specific substring
    - Returns True or False.
    - Startwith(string, substring)
    - startwith(Canon-456-cer5, "Canon") => True
    - startwith(Canon-456-cer5, "non") => False
  - Endwith: Returns True or False.
    - Endwith(string, substring)
    - endwith(Canon-456-cer5, "cer5") => True
    - endwith(Canon-456-cer5, "cer") => False
  - Contains: Returns True or False.
    - Contains(string, substring)
    - Contains(Canon-456-cer5, "-") => returns True
    - Contains(Canon-456-cer5, "54") => returns False
  - Find: Returns the first position.
    - Find(Canon-456-cer5, "-") => returns 6
  - Findnth: Returns the nth position.
    - Findnth(string, substring, occurrence) 
    - Findnth(Canon-456-cer5, "-", 7) => returns 10
- Combine and split
  - Concat: [First Name] + " " + [Last Name]
  - Split: split(string, delimiter, token number). The token number is the part of the section in the string.
    - 3 Methods
      - Calculated Field: SPLIT([Customer Email], "_", 1)
      - Automatic Split: Right-click on the field -> Transform -> Split
      - Customized Split: Right-click on the field -> Transform -> Custom Split

- Replace
  - Replace(string, substring, replacement)
  - If no substring is found, it returns null

### Date Functions

- Extract Datepart
  - Datepart: Global change -> Calculated field. Local change -> Format
    - Datepart(date_part, date) => Returns a number
    - DATEPART("year", [Order Date])
    - DATEPART("month", [Order Date])
  - Datename: Datename(date_part, date) => Returns a string
    - DATENAME("month", [Order Date])
    - LEFT(DATENAME("month",[Order Date]), 3) => Returns the month name with just 3 letters
  - Datetrunc: Datetrunc(date_part, date) => Returns a date and time
    - DATETRUNC("month", [Order Date])
    - Right-click -> Change datatype to date to get rid of time.
  - Day: Day([Order Date]=> Returns a number
  - Month: Month([Order Date]) => Returns a number
  - Quarter: QUARTER([Order Date]) => Returns a number
  - Year: Year([Order Date]) => Returns a number
- Add Subtract
  - DateAdd: Dateadd(date_part, interval, date) => Returns a date
    - DATEADD("year", 1, [Order Date]) => Increments a year
  - Datediff: Subtracts two dates.
    - DateDiff(Date_part, start_data, end_date) => Returns a number
    - DATEDIFF("day", [Order Date], [Shipping Date])
- Current Date & Time: Returns current date and time
  - Today: today()
  - Now: now()

- Null Functions
  - The main purpose of null functions is to handle missing values
  - Calculation Accuracy
  - Data Quality and completeness
  - ZN: Replaces nulls with 0.
    - ZN([Sales])
  - IFNULL: Replaces null with a specific value.
    - IFNULL([Sales], 0)
    - IFNULL([Country], "N/A")
  - ISNULL: Replaces null with.
    - Returns true if the value is null else false
    - ISNULL([Country])

- Logical Functions
  - Conditional Operations
    - If:
      - If [Sales] > 1000 THEN 'High' END [Else it will return null]
    - Else:
      - If [Sales] > 1000 THEN 'High' Else 'Low' END
    - ElseIf:
      - If [Sales] > 1000 THEN 'High' ElseIf [Sales] > 500 THEN 'Medium' Else 'Low' END
      - KPI Colors
      - IF SUM([Sales]) > 200000 THEN 'green'
        ELSEIF SUM([Sales]) > 100000 THEN 'orange'
        ELSEIF SUM([Sales]) <= 100000 THEN 'red'
        END
    - IIF:
      - IIF([Sales] > 1000, 'High', 'Low')
    - Case When:
      - Case [Country] When "Germany" Then "DE" When "Franee" Then "FR" When "United States" Then "US" ELSE "Other" END
      - Accepts only string values
  - Logical Operators: Returns True or False. Used to combine multiple conditions
    - AND:
      - Both the values should be true
      - If [Sales] > 1000 AND [Country] = 'Germany' Then 'High' END
    - OR:
      - One of the values should be true
      - If [Sales] > 1000 OR [Country] = 'Germany' Then 'High' END
    - NOT:
      - It returns a reverse value. If it's true then it returns false.
      - IF NOT [Country] = 'Germany' THEN [Sales] END
