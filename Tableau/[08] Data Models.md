- 3 Types of Data Model
  - Conceptual Data Model:
    - High-level representation of the data model without going into details on how the data model is implemented.
  - Logical Data Model:
    - Go into detail on how the data is structured and organized.
    - We define each attribute of each entity and it includes constraints as well as more.
    - This data model is used by database designers and developers as a blueprint for implementation
  - Physical Data Model
    - This represents the actual representation of the data model.
    - It includes all technical details about how to store the data, like the data types of the attributes, the primary and foreign keys, indexes, and so on.
    - This data model is used by developers to create and manage the databases. 

- Analytical Data Models
  - For analytics, data warehousing and business intelligence, we need special data models that are optimized for queries and reporting. It should be flexible and easy to understand.
  - Two Data Models
    - Star Schema
      - The fact table in the middle is surrounded by dim tables
      - Simple and easy
      - Used when the dataset is small or medium
    - Snowflake Schema
      - The fact table in the middle is surrounded by dim tables, the dimensions here are broken down into subdimensions.
      - More Complex
      - Large Dataset

| Fact Table                         | Dimension Table                      |
|-------------------------------------|--------------------------------------|
| Stores **measurable metrics**       | Stores **descriptive attributes**    |
| Contains **foreign keys** to dimensions | Contains the **primary keys**      |
| Represents **business events/transactions** | Represents **business entities** |
| Rows are **numerous and large**     | Rows are **fewer and smaller**       |
| Contains **quantitative data** (e.g., revenue) | Contains **qualitative data** (e.g., customer name) |

- How to combine and connect the table?
  - Relationship
  - Joins
  - Union
  - Data Blending

- Visualization
  - Visualizations can be built using the tables from the logical layer.
  - Additional data sources, along with the tables in the logical layer, can be combined using data blending (if they come from different sources).
- Data Source
  - Logical Layer: The top-level abstraction that hides the details of the physical layer. It’s beneficial when there are multiple tables in the physical layer. In this layer, tables are combined using relationships rather than traditional joins, enabling better flexibility and performance.
  - Physical Layer: This is where the actual physical tables reside. These tables can be combined using joins or unions, depending on the data integration needs.

  - All tables that are dragged and dropped onto the data source are in the logical layer.
  - Logical layer - relationships
  - Double-click on one of the tables in the logical layer to enter the physical layer.
  - In the physical layer, joins and unions.

### Joins
- Table A and Table B -> Table A is the left table and Table B is the right table
- For joins, we need a key field available in both tables, and we need to decide on the type of join.
  - Inner Join: Returns only the common rows that exist in both tables (i.e., where the join condition is satisfied in both the left and right tables).
  - Left Join (or Left Outer Join): Returns all rows from the left table, and the matching rows from the right table. If there is no match, NULLs are returned for columns from the right table.
  - Right Join (or Right Outer Join): Returns all rows from the right table, and the matching rows from the left table. If there is no match, NULLs are returned for columns from the left table.
  - Full Join (or Full Outer Join): Returns all rows from both the left and right tables. If there’s no match, NULLs are returned for the non-matching side.
- For joins, drag and drop the second table in the physical layer on the white space
  
### Union
- A Union combines two or more tables by appending the rows of the right table beneath the left table, effectively stacking them vertically.
- No key is required for a Union; it simply concatenates the tables based on the order of the rows.
- The column names and data types must match for the Union to be successful. If the column names differ, Tableau will still create the Union, but the mismatched columns will be filled with NULLs.
- Same structure
- For union, drag and drop the second table right below the first table to create a union. Two grey lines would appear, indicating the union was a success.
- A new column would be created to tell us that each row belongs to which of the two tables we just merged.
- New Union -> Wildcard [Automatic] -> Example: Orders* [* indicated nothing or anything after Orders]

### Relationship
- Relationship stays in the logical layer.
- After placing the first table in the white space, drag and drop the second table as well. It automatically forms a connection between the two tables.
- Need to set up 3 things at the relationship level
  - Key  
  - Performance Options: Cardinality and Integrity
    - Cardinality
      - Many to Many - Full scan[results are good, too long to compute] [Default if not sure]
      - Many to One - Correct relationship and results are good.
      - One to Many - Results are not correct, unnecessary scans.
      - One-to-One - Results are not correct, no unnecessary scans.
 - Integrity:
   
| Left Table           | Right Table          | Join Types      |
  |----------------------|----------------------|-----------------|
  | Some Record Match    | Some Record Match    | Inner Join, Left Join, Right Join, Full Join      |
  | All Record Match     | Some Record Match    | Inner Join, Right Join       |
  | Some Record Match    | All Record Match     | Inner Join, Left Join      |
  | All Record Match     | All Record Match     | Inner Join       |
   
- Data Profiling: The process of examining and investigating the data to understand the contents of the table.

### Data Blending
- It takes place at the visualization layer, not in the logical layer.
- Data source imported into Tableau is the primary data source and the secondary data source is external.
- Only Left Join by default.
- Steps:
  - Import primary data source as usual. Click on the database icon next to the primary data source name -> click on New Data Source
- Data Blending works by sheet by sheet only. So each worksheet, you can make a new decision[eg: Can switch between which table is the primary or the secondary table]
- Primary table -> Denoted in Blue
- Secondary table -> Denoted in Orange
- Broken Link chain -> Primary key not activated. To activate it, click on it, and to deactivate it, again click on it.

### Difference between Joins and Unions
- Join combines Fields
- Union combines Rows

### Difference between Joins and Data Blending
- Joins: First combine then aggregate
- Data Blending: First aggregate then combine
  - * means multiple values
  ![2024-10-17 - 11_13_19 - Course_ Tableau Ultimate Course A-Z_ From Zero to Hero (2024) _ Udemy](https://github.com/user-attachments/assets/56e519b4-cf7f-437f-9754-ad7401ba0779)

### Difference between Joins and Relationship
- Joins
- Relationship
