https://public.tableau.com/app/profile/karen.judelyn.fernandes/viz/LODExpression_17297449978720/Comparativesalesanalysisbycategory

- How it works?
  - Aggregate the rows at the dimension level used in the calculation
  - Level of Details is the LOD Expression
  - The calculations are performed on the data within the data source
  - Results will be calculated on the FLY
- Syntax: {Fixed | Include | Exclude List of Dimensions : Aggregation}
- Static
  - Fixed
    - {Fixed [Category] : SUM([Sales])}
    - {Fixed [Category], [Product Name]: SUM([Sales])}
    - It works similarly to group by and aggregate in SQL. Groups by category and returns the sum of sales.
    - The values calculated here won't change even with the change in filters
    - Two Types of LOD:
      - One mentioned in the view is LOD (VIZ)
      - One mentioned in the calculated field is LOD (Expression)
    - Use Case:
      - Customer Order Frequency: Show the description of customers by number of orders.
      - Suppose you are using [Country] and [Category] dimensions in the view and then used the following LOD Calculation:
      FIXED [Category] : SUM([Sales])}
      What is the level of details that tableau will use to aggregate the sales?
      Answer: Category
- Dynamic
  - Include
    - The INCLUDE Level of Detail (LOD) expression in Tableau calculates an aggregation by including additional dimensions, regardless of whether they are present in the current view or visualization.
    - The "include" function includes the specified dimension in the calculation, making it dependent on the dimensions present in the view.
    - {Include [Category] : SUM([Sales])}
    - Suppose you are using [Country] and [Category] dimensions in the view and then used the following LOD Calculation:
      INCLUDE [Category] : SUM([Sales])}
      What is the level of details that tableau will use to aggregate the sales?
      Answer: Both Category and Country
      
   - Exclude
    - The "exclude" function in LOD expressions is used to remove specific dimensions from the calculation based on the dimensions in the view, making it dynamic and dependent on the view.
    - Calculate the aggregation, excluding the dimension.
    - {Exclude [Category] : SUM([Sales])}
    - Suppose you are using [Country] and [Category] dimensions in the view and then used the following LOD Calculation:
      EXCLUDE [Category] : SUM([Sales])}
      What is the level of details that tableau will use to aggregate the sales?
      Answer: Country
