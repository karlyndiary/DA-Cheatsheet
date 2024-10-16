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
