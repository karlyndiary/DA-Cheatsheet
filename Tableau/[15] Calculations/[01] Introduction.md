- Four ways to create a calculated field
  - In the Data Pane -> Right-click on the field -> Calculated Field
  - Date Pane -> Drop-down near search -> Calculated Field
  - Analysis Tab
  - Right-click on the field -> Calculated Field

- The calculated field created under the analysis tab is global
- Calculated field - locally - double click on the field in the view -> Upper([First Name])
- Comment line -> //

- Colors
  - Logical Expression and Operators:  Black
  - Parameter:  Purple
  - Functions:  Blue
  - Dimensions and measures: Orange
  - Comments: Grey

- Nested Calculations
  - The result of one calculation used as an input in another calculation

- Row Level Calculations:
  - Processes rows individually
  - Doesn't aggregate data
  - Stores data in the data source
  - Example: Price * Quantity = Revenue
  - Number Functions: Abs, Floor
  - String Functions: Trim, Split
  - Date Functions: Datename, Dateadd
  - Null Functions: zn, isnull
  - Logical Functions: if-else, case when

- Aggregate Calculations:
  - Aggregation will happen in the visualization view, sum[Revenue]
  - Max, Min, Avg, Count, Count Distinct, Sum, Attribute

- Level of Details Expressions
  - LOD Expressions will happen in the visualization view
  - Control LOD = {Fixed category: sum[Revenue]}
  - Category A has 3 products of revenue, 40, 60, and 20 -> since it's a fixed category -> it will sum these up -> 120
  - Fixed, Include, Exclude

- Table Calculations
  - Table Calculations will happen in the visualization view
  - Example: Rank(sum(revenue))
  - Returns rank to each row
  - Data will not be stored in the data source
  - Running, Window, Rank, First, Last, Index, Lookup
  - The values calculated depend on the view

- Order of computation
  - Row Level Calculation
  - Aggregate Calculations
  - Table Calculations

- How do you choose the right calculations?
  - Do you have to aggregate data -> No -> Row Level Calculation
  - Do you have to aggregate data -> Yes -> Is all the required data already on the viz? -> Yes -> Table Calculation
  - Do you have to aggregate data -> Yes -> Is all the required data already on the viz? -> No -> Does the LOD in the viz match the question -> Yes -> Aggregate Calculation else LOD Calculation
