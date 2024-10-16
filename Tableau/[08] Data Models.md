- 3 Types of Data Model
  - Conceptual Data Model:
    - High-level representation of the data model without going into details on how the data model is implemented.
  - Logical Data Model:
    - Go into detail on how the data is structured and organized.
    - We define each attributes of each entity and it includes constraints as well and more.
    - This data model is used by database designers and developers as a blueprint for implementation
  - Physical Data Model
    - This represents the actual representation of the data model.
    - It includes all technical details about how to store the data, like the data types of the attributes, the primary and foreign keys, indexes, and so on.
    - This data model is used by developers to create and manage the databases. 

- Analytical Data Models
  - For analytics, data warehousing and business intelligence, we need special data models that are optimized for queries and reporting. It should be flexiable and easy to understand.
  - Two Data Models
    - Star Schema
      - The fact table in the middle surrounded by dim tables
    - Snowflake Schema
      The fact table in the middle is surrounded by dim tables, the dimensions here are broken down into subdimensions.
