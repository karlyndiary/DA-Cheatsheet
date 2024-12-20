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
  - Change it from bar to line in the marks pane.
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

- Bubble Chart
  - Change the chart type in the marks pane to circle
  - Add sales to size
  - Add sub-category to detail, profit to colour, category to label
 
- Stacked Bubble Chart
  - Change the chart type in the marks pane to circle
  - Add sales to size
  - Add country to color
  - Add Order id to detail
 
- Map
  - Add Longitude to columns and latitude to rows
  - Add country, state to details
  - Change the chart type to map
  - Add region to color
  - Add sales to label
 
- Map with symbols
  - Add Longitude to columns and latitude to rows
  - Add country, state to details
  - Change the chart type to shape
  - Add region to color
  - Add sales to size

- No Background Map
  - Add Longitude to columns and latitude to rows
  - Add country, state to details
  - Change the chart type to Map
  - Add region to color
  - Map -> Background Layers -> Washout (%) -> 100%
 
- Night Vision Map
  - Add Longitude to columns and latitude to rows
  - Add country, state to details
  - Change the chart type to Map
  - Map -> Background Layers -> Style -> Dark
  - Add sales to size and color
  - Duplicate the longitude and change the chart type to map
  - Remove sales size and color
  - Edit Border in color -> Dual Axis

 - Histogram (1 Measure)
   - Right-click on the field -> Create -> Bins
   - Add the bins to columns and the field to rows
   - Right-click on the bins and convert it to continuous
  
- Histogram (2 Measure)
  - Create a calculated field -> ```{FIXED [Customer ID]: COUNT([Order ID])}``` -> convert it to dimension
  - Add the calculated field to columns
  - Add customer count to rows and label
 
- Calendar Chart
  - Add order date to columns and convert it to weekday [More -> Weekday]
  - Add order date to rows and convert it to weeknumber [More -> Weeknumber]
  - Add order date to filter as year and another order date filter as month -> Select one year and one month
  - Add sales to color
  - Add the order date to the label and convert it to day.

 - Waterfall Chart
   - Part to whole relationship
   - Flow Process (Typically Budgets)
   - Add sub-category to columns and profit to rows
   - Right-click on profit -> Quick Table Calculation -> Running Total
   - Change the chart type to gantt bar
   - Add profit to size and double click to edit the sum of sales on size pill and add a minus in front of it ```-sum(sales)```
   - Add profit to color and make it two step
   - Analysis -> Totals -> Show Row Grand Totals

- Pareto Chart V1
  - 80/20 Rule
  - 80% of consequences come from 20% of the causes
  - Add sub-category to columns and sales to rows
  - Sort it in descending order
  - Duplicate Sales and switch it to line chart
  - Dual Axis
  - Right-click on the 2nd sales -> Table Calculation -> Select Running Total [primary calculation] -> Add secondary calculation -> Percent of Total [secondary calculation]
  - Enable the label on the 2nd sales

- Pareto Chart V2
  - Business Question: Do 20% of the products make up 80% of the sales?
  - Add sales to rows and product name to columns and select count distinct under measures for product name
  - Add product name to detail
  - Right-click on the product name -> Table Calculation -> Select Running Total [primary calculation] -> Specific Dimensions -> Product name -> Add secondary calculation -> Percent of Total [secondary calculation] -> Specific Dimensions -> Product name
  - Repeat the above for sales as well
  - Switch the chart type to line
  - Right-click on the product name on detail -> Sort -> Field -> Sales -> Descending
  - Analytics -> Drag and drop the Reference Line on products -> 0.2 in values and constant -> ok
  - Repeat the same but this time 80% [0.8] for sales

- Butterfly Chart V1
  - Correlation
  - Compare two measures by category
  - Add sub-category to rows and count of customers and count of orders to columns
  - Add AVG(0) to columns and place it between the counts
  - Add sub-category to label to avg(0) and change the chart type to text
  - Right-click on the left count axis -> Edit axis -> Reversed
  - Add color to count of customers and count of orders
 
- Butterfly Chart V2
  - Add count of customers to columns and and sub-category to rows
  - Add count of orders to the count of customers value axis
  - Move measure names from rows to colors
  - Sort the value axis descending order
  - Over on the measure values mark pane change the count of customers to ```-COUNT([Customers.csv])```
  - Add AVG(0) to columns, switch the chart type to text and add sub-category to text
  - Dual axis and synchronize axis. Make the text white in color.

- Quadrant Chart
  - Use Case:
    - Categorize Data Points
    - Risk Management
    - Strategic Planning
  - Add discount to columns and switch the measure to average
  - Create a calculated field for profit ratio ```SUM([Profit])/SUM([Sales])```
  - Add the profit ratio to rows
  - Switch the y-axis to percentage -> Right-click on the profit ratio axis -> Format -> Under numbers -> Select Percentage -> Remove decimals
  - Repeat the same for the other axis as well
  - Add customer id to details
  - Change chart type to circle
  - Reduce the opacity to see the overlapping (70%)
  - Create two parameters -> one for discount and another for profit ratio
  - Data type: Float, Display format: percentage without decimals, Current value: 0.15 for 15%
  - Add two reference line -> Right-click on the axis -> Add reference line -> Select the parameter of the selected axis -> Label: None
  - Create a calculated field -> Quadrant color
    ```
    IF [Profit Ratio] >= [Select Profit Ratio] AND AVG([Discount]) >= [Select Discount] THEN 'Upper Right'
    ELSEIF [Profit Ratio] >= [Select Profit Ratio] AND AVG([Discount]) < [Select Discount] THEN 'Upper Left'
    ELSEIF [Profit Ratio] < [Select Profit Ratio] AND AVG([Discount]) >= [Select Discount] THEN 'Bottom Right'
    ELSE 'Bottom Left'
    END
    ```
  - Add the quadrant color to color

- Box Plot
  - The Length of Box: The longer the box, the more dispersed the data The smaller, the less dispersed the data
  - Add sales to rows and sub-category to details
  - Add category to columns and change the chart type to circle
  - Add reference line -> Select box plot -> ok

- KPI
  - Analyse the performance of the business
  - Add sub-category to rows and country to column
  - Add sales to text
  - Create a KPI Color Calculated Field
    ```
    IF SUM([Sales]) >= 50000 THEN 'Green'
    ELSEIF SUM([Sales]) <= 50000 AND SUM([Sales]) >= 10000 THEN 'Orange'
    ELSE 'Red'
    END
    ```
  - Add the calculated field to color
  - Change the chart type to shape and move sales from text to detail
  - Move the KPI color from color to shape
  - Change the shapes

- KPI and Bar Chart (Bullet Chart)
  - Add sub-category to row and sales 2022 to columns.
  - Add sales 2021 to detail.
  - Right-click on the x-axis -> Add Reference Line -> value: Sales 2021, label: None, Scope: Per Cell
  - Change line color and transparency
  - Create a calculated field ->
    ```
    IF SUM([Sales 2022]) > SUM([Sales 2021]) THEN 'Green'
    ELSE 'Red'
    END
    ```
  - Add AVG(0) to columns and switch the chart type to shape
  - Add the calculated field to shape and color
  - Dual Axis and synchronize axis
  - Edit the AVG(0) to AVG(-10000) to make space for the KPI shapes and the bar chart
 
- KPI BANS
  - Change the chart type to text
  - Add sales to text
  - Add country to columns
  - Increase the number size in the text and center align it
  - Right-click on the sales under marks -> Format -> Currency (custom) -> Add currency, remove decimals and display units in K or M
  - Add Country to text -> Edit text -> Make the country text smaller than the number value and disable the header
 
- Funnel Chart
  - Progress of data through different stages
  - Add sales to rows and sub-category to color
  - Add sales to size and sort it descending order
  - Add sales and sub-category to text
  - Right-click on sales -> quick table calculation -> Percent of total
  - Add category as filter
 
- Progress Bar
  - Add sales to columns and country to rows
  - Right-click on sales -> Quick Table Calculation -> Percent of Total
  - Enable the label and add AVG(1) to columns
  - Dual axis and synchronize axis
  - Rearrange the pills in the columns and change the color of avg(1) to a lighter color
 
### How to choose the right chart?
- Change over time
  - Show trends over time
  - How does the data change evolve over time?
  - Are there any trends or patterns in data over time?
  - Line Chart
  - Sparkline Chart
  - Slope Chart
  - Bar Chart Over Time
  - Stacked Area Chart
  - Calendar Chart
  - Circle Timeline
- Magnitude
  - Show size comparisons. These can be relative absolute
  - Which categories have the highest and lowest sales
  - Show comparison of sales across different categories'
  - Bar Chart (Rows and Columns)
  - Bar Chart Side by Side
  - Stacked Bar Chart
  - Full (100%) Stacked Bar Chart
  - Lollipop Horizontal Bar Chart
  - Bubble Chart
  - Scatter Plot
- Part to whole
  - Show how a whole breaks down into its components
  - How much each category contributes to overall sales?
  - Pie Chart
  - Donut Chart
  - Full (100%) Stacked Bar Chart
  - Full (100%) Stacked Area Chart
  - Treemap
  - Waterfall Chart
- Correlation
  - Show the relationships between two or more measures
  - Is there a correlation between two measures?
  - How strongly related are the two variables?
  - Custom Scatter Plot
  - Quadrant Chart
  - Dual Line Chart
  - Bar & Line Chart (2)
  - Butterfly Chart V2
  - Histogram (2 Measures)
- Ranking
  - Show an item's position in an ordered list (Relative Ranking)
  - Show top 10 customers by sales
  - Show the lowest 10 products by sales
  - Bar Chart (Rows and Columns)
  - Lollipop Horizontal Chart
  - Rounded Bar Chart
  - Slope Chart
  - Funnel Chart
  - Bump Chart
  - Butterfly Chart V2
- Distribution
  - Show values in a dataset and how often they occur
  - What is the distribution of customers' ages?
  - What are the busiest times in our workday?
  - Histogram (2 Measures)
  - Box Plot
  - Dot Plot
  - Custom Scatter Plot
  - Quadrant Chart
  - Barcode Chart
  - Barbell Chart
- Spatial
  - Use when geospatial patterns in your data are more important than anything else
  - Which city/state has the highest sales?
  - Map
  - No Background Map
  - Map with symbols
  - Night Vision Map
- Flow
  - Visualize the movement or flow of data over time
  - How do things move from one point to another?
  - Waterfall Chart
