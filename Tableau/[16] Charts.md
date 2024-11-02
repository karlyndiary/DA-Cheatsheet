https://public.tableau.com/app/profile/karen.judelyn.fernandes/viz/Charts_17305223908710/DualAxes?publish=yes
- Individual Axes:
  - Multiple measures on the single axes.
  - Customize Charts individually.
  - Unlimited No of Measures
- Single Axes:
  - Create a view with one measure and one dimension
  - Drag the second measure onto the value axes until you see a double green bar, then drop it there.
  - Can't Customize Charts individually except for colors
- Dual Axes:
  - Create a view with two or more measures and one dimension
  - Right-click on the second measure and select dual-axis
  - Right-click on the value axes and select the synchronize axis
  - Customize Charts individually.
  - 2nd Method: Create the view as usual
    - Drag the 2nd measure on the view to the right end of the view till you see the green bar, when you do, drop the measure right there
    - Don't synchronize the axis

### Bar Chart
- Bar Chart: Use a bar chart with a high cardinality dimension
- Column Chart: Use a column chart with a low cardinality dimension
- Side by side Bar Chart: Add country and order date to the column. Add sales to row. Filter the order date to display just the last two years.
- Over-Time Bar Chart: Add the order date to the column and drill down to the quarter. Add the sales row. 
- Stacked Bar Chart: Add order data to the column and convert it to the month. Add the order date to the filter, and select the last year. Add sales to row. Add category to colour.
  - Analyse change over time
  - 1 to whole relationship
- 100% Stacked Bar Chart: Same as a stacked bar chart. Head over to sales in the rows -> Right-click -> Quick Table Calculation -> Percent of Total -> Right-click -> Edit Table Calculation -> Specific Dimension -> Remove the dimension that is not related to the bar chart in terms of making it a stacked bar chart.
- Multiple Small Bar Chart: Add country to the column. Add category and sales to the row. Add the order date to the column and convert it to month. Add country to colour.
- Bar in Bar Chart: Add sales and quantity to columns and make it dual axes. Add sub-category to rows. Head to the quantity marks pane and make the size of the bar chart smaller.
- Barcode Chart: Add sales to the columns and sub-category to the rows. Bring in a high-cardinality dimension like product name to details.

### Line Chart
- Line Chart: Add sales to row and order date to column. Convert the order date to month.
- Customized Line Chart: Add sales, discount, profit, unit price and count of orders to row. Add the order date to the column and convert the order date to month.
- Multiple Line Chart: Add the order date to the column and convert the order date to quarter month. Add sales to rows. Add category to colour.
- Dual Line Chart: Add the order date to the column and convert the order date to quarter month. Add sales and profit to the row and make it dual axes. change the colours.
- Cumulative Line Chart: Add the order date to the column and convert the order date to month. Add sales to the row. Right-click on sales -> Quick Table Calculation -> Running Total. Add category to colour. Over on the Label mark pane -> switch from ALL to Line end for the values. Disable Label start of line.
- 
