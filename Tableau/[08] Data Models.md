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
- Data Source
  - Logical Layer: Top-level layer that hides all the details in the physical layer. This is good when we have a ton of tables in the physical layer. Here the two physical tables can now be merged using a relationship.
  - Physical Layer: A few physical tables and we can combine them using joins or unions
  
