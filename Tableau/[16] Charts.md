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
- Multiple Small Line Chart: Add country to the column. Add category and sales to the row. Add the order date to the column and convert it to month. Add country to colour. Over on the Label mark pane -> switch from ALL to Line end for the values. Disable the Label start of line.
- Highlighted Line Chart (1): Create a line chart as usual. Add a field to colour. Right-click on the pill -> Show highlight -> Select an option from the drop-down to highlight and dim the rest of the lines.
- Highlighted Line Chart (2): Create a line chart as usual. Add a field to detail. Create a Parameter with the field values. Create a calculated field with ```[Country] = [Select Country]```. Add the calculated field to the colour. Change the colour of false to grey. Add the calculated field to size. Right-click on the legend and edit size -> Click on reverse.


- Bump Chart
  - To show the rank
  - Add the Order date and convert it to quarter.
  - Add sales.
  - Add country to color.
  - Right-click on sales -> Quick table calculation -> Rank
  - Right-click on sales -> Edit table calculation -> Specific Dimension -> Select field
  - Reverse the rank axes -> Right-click on the axes -> Edit axes -> Reversed
  - Duplicate the sales on the same row.
  - On the 2nd chart -> Switch the shape to circle. -> Increase the size
  - Right-click on the 2nd sales pill and select dual axes. -> Synchronize axes


- Sparkline
  - Add the Order date and convert it to quarter.
  - Add sales.
  - Add country to the row.
  - Add sales to label -> Min/Max -> Select quarter in the field
  - Resize the chart.
 

- Barbell Chart
  - Perfect for categories
  - Show the range between two values
  - To compare years. Longer the line means larger the difference in sales between the two years.
  - Add sub-category to row.
  - Create two calculated fields -> ```IF YEAR([Order Date]) = 2021 THEN [Sales] ELSE NULL END```, ```IF YEAR([Order Date]) = 2022 THEN [Sales] ELSE NULL END```
  - Add the 2021 calculated field to columns. Change the shape to a circle.
  - Add the 2022 calculated field to the x-axis.
  - Duplicate measure values on the columns
  - Change the shape from a circle to line
  - Move the measure names to path.
  - Right-click on the duplicated measure values on the column and select dual axis.
  - Switch the order of measure values on the columns to put the line behind the circles. 


- Rounded Bar Chart
  - Add sales to columns and sub-category to row
  - Add AVG(0) to columns
  - Add the AVG(0) to the x-axis of sales to generate measure values and names.
  - Change it from bar to line.
  - Move measure names from rows to path
  - Increase the line size.
  - Add measure values to color


 - Slope Chart
   - To show how rank changes over time
   - Add order date to column and sales to rows.
   - Filter to show the last two years.
   - Add country to detail
   - Add country to label and select line ends.
   - Duplicate the sales on the rows.
   - Change the shape to circle.
   - Right-click on the 2nd sales -> Dual axis
   - Synchronize axis


- Bar and Line Chart (1)
  - Add sales to row and order date to columns and switch to month
  - Switch it to a bar chart
  - Analytics -> Average Line


- Bar and Line Chart (2)
  - Correlation
  - Compare two measures
  - Add order date to columns and switch to month. Add order count to row
  - Add count of customers to row
  - Switch to circle line in color marks.
  - Dual axis
 

- Bullet Chart
  - Compare Two measures
    - Current year vs Previous year
    - Actual vs Target
  - Add sub-category to row and sales 2022 to columns.
  - Add sales 2021 to detail.
  - Right-click on the x-axis -> Add Reference Line -> value: Sales 2021, label: None, Scope: Per Cell
  - Change line color and transparency
   

- Horizontal Lollipop Chart
  - Use Case
    - Ranking and highlighting important information in circle
  - Add sub-category to rows and sales to columns.
  - Reduce the line size. [Make sure its changed to bar]
  - Duplicates sales on columns and change the shape to circle and increase the size
  - Dual axis and synchronize axis

- Area Chart
  - To analysis change over time
  - Add order date to columns and switch to month. Add sales to row.
  - Change the chart to area

- Lined Area Chart
  - Add order date to columns and switch to month. Add sales to row.
  - Change the chart to area
  - Duplicate sales in the row and change the chart type to line.
  - Dual Axis and synchronize axis
 
- Stacked Area Chart
  - Add order date to columns and switch to month. Add sales to row.
  - Change the chart to area
  - Add Category field to colour
 
- Full (100%) Stacked Area Chart
  - Add order date to columns and switch to month. Add sales to row.
  - Change the chart to area
  - Add Category field to colour
  - Right-click on sales -> Quick Table Calculation -> Percent of Total
  - Right-click on sales -> Edit Table Calculation -> Specific Dimensions -> Category field
 
- Small Multiple Area Chart
  - Add country and order date to columns and switch to month. 
  - Add category and sales to row.
  - Add category to colour
 
- Scatter Plot
  - To find outliers
  - Correlation
  - Add sales to columns and profit to rows
  - Add customer id to detail
 
- Custom Scatter Plot
  - To find outliers
  - Correlation
  - Add sales to columns and profit to rows
  - Add customer id to detail
  - Add count of orders to size
  - Add country to color, add a border to the circles and turn down the opacity.
 
- Dot Plot
  - Distribution of data across categories
  - Add sales to columns
  - Add order date to rows and switch it to months discrete
  - Add order id to details
  - Add category to colour

- Circle Timeline
  - Analyse trends over time
  - Correlation between two measures
  - Add sub-category to row
  - Add order date to columns and switch it to quarter continues
  - Add sales to size
  - Add profit to colour
 
- Pie Chart
  - Add sales to angle and country to colour

- Donut Chart
  - Add sales to angle and country to colour
  - Add AVG(0) to columns and duplicate it -> Dual Axis and synchronize axis
  - On the 2nd AVG(0) in the marks pane, change the chart type to a circle, reduce the size and change the colour to white.
  - On the 2nd AVG(0) -> add sales to label -> Edit the text
 
- Treemap
  - Part to whole relationship
  - Plot Hierarchical Data
  - Change the chart type to square
  - Add sales to size
  - Add category to color
  - Expand the category to the lowest level

- Heatmap
  - Correlation between two categories
  - Add country to columns and sub-category to rows
  - Add sales to label and color
  - Change the chart type in the marks pane to square
