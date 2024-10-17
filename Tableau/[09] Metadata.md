After loading the data to the data source, tableau will now start analysing the content of the data to make assumptions about the datatype and roles.
- Data Types [Operation Calculation]
  - Basic Types
    - Whole Numbers
    - Decimal Numbers
    - String [Text]
    - Date
        ![image](https://github.com/user-attachments/assets/0fd76827-7d70-4a2b-9d10-b49440444be3)
    - Date & Time
        ![image](https://github.com/user-attachments/assets/f2b505f5-ab55-4cf1-b583-bf93d0f2e5cf)
      - The date format can be changed using the predefined format or custom formats.
      - Changing the date format in the marks pane under Text option -> This applies only to the current worksheet.
      - Changing the date format in the Data pane -> drop-down -> Default Properties -> Date format -> Predefined or custom. This applies to all the worksheets.
    - Boolean [True or False]
  - Roles
    - Geographic Roles: City, Country, Pin Code
    - Image Roles:
      - png, jpeg, jpg
      - URL should begin with http or https
      - Image file must be > 128kb
      - Max no of images in each field will be 500
  - Advanced Data Types
    - Groups
    - Cluster Groups
    - Bins
    - Sets
- Role I
  - Dimension: Level of Detail 
  - Measure: Aggregation
- Role II
  - Discrete [Separate Values]
  - Continuous [Connected Values]

- The primary key should be of the same data type. [Tableau would indicate if the datatypes don't match]
- You can change the data type on the data source page or the worksheet page.
