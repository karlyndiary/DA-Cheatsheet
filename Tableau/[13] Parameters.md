- Parameters are variables that allow users to replace a fixed constant value
- Parameters can be used in calculations, filters, text, bins, reference lines, etc.
- Parameters are independent of the data source
- Add dynamic, flexibility and interactivity
- Enables the user to customize the view
- Reduce the number of views
- Use Case
  - Dynamic Calculations
    ```
    IF SUM([Profit]) > [Profit Parameter] THEN 'GREEN'
    ELSE 'RED'
    END
    ```
  - Dynamic Reference Lines
    - Analytics pane -> Double click on Reference Line -> choose the parameter created -> Click on value as label -> ok
  - Dynamic Filters
    - Top N Products -> Create the view -> Add the field to filter -> Top tab -> By field -> Click on the value drop-down -> Create a new parameter -> Give it a name, current value [start min value from 0], step size -> Click on ok
  - Dynamic swap between dimensions and swap between measures
    - Create the view -> Create a parameter -> Give it a name -> Select string -> Select list -> Mention the different dimensions -> Click ok
    - Show Parameter
    - Create a calculated field to make the parameter dynamic
      ```
      CASE [Choose Dimension] 
      WHEN 'Country' THEN [Country]
      WHEN 'Category' THEN [Category]
      END
      ```
      ```
      CASE [Choose Measure]
      WHEN 'Sales' THEN [Sales]
      WHEN 'Profit' THEN [Profit]
      WHEN 'Quantity' THEN [Quantity]
      END
      ```
    - Replace the fields with this calculated field
  - Dynamic Texts for Sheet Name
    - Double click on the sheet name above the chart -> Clear the name -> Click on Insert -> Click on Parameters.Choose Measure -> Type by and Click on Parameters.Choose Dimension -> Click on ok
    
    ```<Parameters.Choose Measure> by <Parameters.Choose Dimension>```
    
    ```Top <Parameters.Choose Top N Products> Products```
  - Dynamic Bins in Histogram
    - Create the view -> Click on field(bins) -> Edit Bins -> Create a new parameter -> Give it a name -> Give a current value -> Select range -> Mention min, max and step value -> Click ok
    - Show Parameter
