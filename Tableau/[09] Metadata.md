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
    - Dimensions contain qualitative or categorial values
    - Example: Product Name, Product Category, Location
    - Use of Dimensions: Categorize, Filtering, Level of Details
  - Measure: Aggregation
    - Contains Quantitative and numerical values
    - Example: Sales, Profit, Quantity
    - Measures can be aggregated
  - All fields that can be aggregated are a measure otherwise it's a dimension.
  - OLAP: Online Analytical Processing
    - The core concept is the multidimensional OLAP online analytical processing. So the concept says if you want to answer the business questions or do data analysis, first, we have to build the data model that has the shape of a cube with multidimensions.
    - First we have the dimensions of the cube and the second informations we have those cells. Those cells can store informations like data numbers and we call it measures. So each cube has two informations the dimensions and the cells the measures.
    - Example: We have the cube of sales and it has three dimensions. The first dimension is the locations. And inside the locations we have three members USA, France and Germany. Those three values are the member of the dimension location. And we have another dimension called time. And it has three members in the dimension January, February and March. And the third dimension we have the categories. And now inside the sales of the cube we have the measure sales. So now our cube is ready with the dimensions and measure.
    - For example find the total sales in USA. So what can happen? We can select the dimension location and filter the dimension to have only the member USA. This operation in the cube we call it slicing the cube. And then we're going to aggregate the measure and we will get the total sales of 120. And if we have cube, we can do multiple operations like slicing, dicing, roll up, drill down and pivot.
|                          | **Dimensions**                   | **Measures**                        |
|--------------------------|-----------------------------------|-------------------------------------|
| **Definition**            | Descriptive Values                | Quantitative Values                 |
| **Example**               | Category, Country, ID             | Sales, Profit, Quantity             |
| **Aggregation**           | Can Not be aggregated             | Aggregable [SUM, AVG, MIN, MAX]     |
| **Data Types**            | [String, Date, Boolean, Number]   | [Number]                            |
| **Role of Analysis**      | Filtering, Grouping, Organizing Data | Calculations & Numerical Analysis   |
| **Granularity**           | LOD: Level of Details             | Determine Quantity being Measured   |

- Role II+
  - Discrete [Separate Values] [Blue]
  - Continuous [Connected Values] [Green]

- The primary key should be of the same data type. [Tableau would indicate if the datatypes don't match]
- You can change the data type on the data source page or the worksheet page.
