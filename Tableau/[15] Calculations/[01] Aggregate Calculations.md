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

- Aggregate Calculations:
  - Aggregation will happen in the visualization view, sum[Revenue]

- LOD Expressions
  - Control LOD = {Fixed category: sum[Revenue]}
  - Category A has 3 products of revenue, 40, 60, and 20 -> since its a fixed category -> it will sum these up -> 120

- Table Calculations
  - 
