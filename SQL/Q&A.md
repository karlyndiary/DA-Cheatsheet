- Rolling Average
    1. Smoothing Data : Rolling averages help to reduce the impact of random fluctuations or noise in a dataset. By calculating an average over a specific window of time, 
  the resulting value provides a smoother representation of the underlying trends
    2. Trend Identification : Rolling averages help to identify trends in data over time. By smoothing out short-term fluctuations, it becomes easier to 
  discern long-term patterns and changes in the data. This is particularly useful in financial markets, where it’s often applied to stock prices or economic indicators.
    3. Seasonal Patterns : In time-series data, there might be seasonal variations that occur on a regular interval, such as daily, weekly, bi-weekly. 
  Rolling averages can help highlight these patterns by averaging data points over a period, making it easier to observe recurring trends.
    4. Identification of Anomalies : Sudden spikes or drops in data can sometimes be hard to identify in raw data due to spikes. By using the same window size, 
  you can compare the trends and variations between various entities or datasets.
  ``` ROWS BETWEEN lower_bound AND upper_bound ```
  The bounds can be any of these five options:
  - UNBOUNDED PRECEDING – All rows before the current row.
  - n PRECEDING – n rows before the current row.
  - CURRENT ROW – Just the current row.
  - n FOLLOWING – n rows after the current row.
  - UNBOUNDED FOLLOWING – All rows after the current row.

- Explain order of execution of SQL.
    - Order of execution of SQL is `From → Join → Where → Group by → Having → Select → Order by → Limit/ Offset`
    - The order of execution of an SQL query can generally be broken down into logical steps, but it's essential to understand that the SQL engine might optimize the execution order based on the query and the database's schema and indexes. However, here's the general sequence:
    1. **FROM**: The SQL engine identifies the tables involved in the query and determines how they need to be accessed. This step establishes the data sources for the query.
    2. **JOIN**: If there are joins in the query, tables are joined based on the specified conditions.
    3. **WHERE**: The WHERE clause filters the rows based on the specified conditions. Rows that don't meet the conditions are eliminated from further processing.
    4. **GROUP BY**: If there's a GROUP BY clause, rows are grouped based on the specified columns.
    5. **HAVING**: The HAVING clause filters the grouped rows based on specified conditions. It's similar to the WHERE clause but applies to grouped rows.
    6. **SELECT**: The SELECT clause determines which columns or expressions to include in the query result set.
    7. **ORDER BY**: If there's an ORDER BY clause, the result set is sorted based on the specified column(s) or expressions.
    8. **LIMIT/OFFSET**: If there's a LIMIT clause, it restricts the number of rows returned by the query. OFFSET, if used, specifies where to start returning rows from.
- What is difference between where and having?
    - Where
        - The WHERE clause filters rows based on a condition applied to individual rows before any grouping is done.
        - It is used to filter rows from the result set based on specified criteria.
        - It operates on individual rows and filters them based on conditions applied to columns.
        - It is typically used with aggregate functions when you want to filter the rows before they are grouped.
    - Having
        - The HAVING clause filters rows after they have been grouped, typically used with GROUP BY.
        - It is used to filter groups of rows that result from the GROUP BY clause based on specified criteria.
        - It operates on grouped rows rather than individual rows.
        - It is used with aggregate functions to filter the result set after it has been grouped.
- What is the use of group by?
    - GROUP BY is used in SQL to aggregate data based on one or more columns. It is typically used in conjunction with aggregate functions like COUNT, SUM, AVG, etc., to group rows that have the same values in specified columns. This allows you to perform calculations and analyze data at a higher level of granularity, such as getting totals or averages for each group, rather than for individual rows.
- Explain all types of joins in SQL?
    - SQL supports several types of joins to combine rows from two or more tables based on related columns between them:
    1. **INNER JOIN**: Returns rows that have matching values in both tables based on the join condition. If there is no match, the rows are not included in the result set.
    2. **LEFT JOIN (or LEFT OUTER JOIN)**: Returns all rows from the left table and matching rows from the right table. If there is no match, NULL values are returned for the columns from the right table.
    3. **RIGHT JOIN (or RIGHT OUTER JOIN)**: Returns all rows from the right table and matching rows from the left table. If there is no match, NULL values are returned for the columns from the left table.
    4. **FULL JOIN (or FULL OUTER JOIN)**: Returns all rows from both tables and matches rows from both tables where available. If there is no match, NULL values are returned for the columns from the table without a match.
    5. **CROSS JOIN**: Returns the Cartesian product of the two tables, i.e., all possible combinations of rows from both tables. It does not require any join condition.
- What are triggers in SQL?
    - Triggers in SQL are special types of stored procedures that are automatically executed (or fired) in response to certain events on a table, such as INSERT, UPDATE, or DELETE operations. These events can be either data manipulation events (DML) or data definition events (DDL).
        
        Triggers are defined to perform a specific action or set of actions when a triggering event occurs. They are often used for enforcing business rules, auditing changes to data, maintaining referential integrity, or automatically updating related tables.
        
        There are two main types of triggers:
        
        1. **Row-level triggers**: These triggers are fired for each row affected by the triggering event. They can access both the old (existing) and new (updated) values of the affected row.
        2. **Statement-level triggers**: These triggers are fired once for each triggering event, regardless of the number of rows affected. They cannot access individual row values and are typically used for actions that do not depend on specific row data.
        
        Triggers provide a powerful mechanism for implementing complex database logic and maintaining data integrity, but they should be used judiciously due to their potential impact on performance and complexity of the database logic.
        
- What is stored procedure in SQL
    - A stored procedure in SQL is a named collection of SQL statements and procedural logic that is stored in the database catalog. It is precompiled and saved in the database, allowing it to be executed repeatedly by invoking its name, rather than reissuing the individual SQL statements each time.
        
        Stored procedures offer several benefits:
        
        1. **Modularity**: SQL logic can be encapsulated within a stored procedure, promoting code reuse and simplifying maintenance.
        2. **Performance**: Stored procedures are precompiled and stored in a compiled format, potentially improving execution speed compared to ad-hoc SQL statements.
        3. **Security**: Permissions can be granted to execute stored procedures without granting direct access to underlying tables, enhancing security.
        4. **Ease of maintenance**: Changes to the SQL logic can be made centrally within the stored procedure, reducing the need to update multiple application code locations.
        
        Stored procedures can accept parameters, perform conditional logic, execute SQL statements, and return result sets or scalar values. They can be invoked from client applications, other stored procedures, or triggers.
        
        Overall, stored procedures are a powerful feature of SQL databases, providing a way to encapsulate and manage complex database logic within the database itself.
        
- Explain all types of window functions? (Mainly rank, row_num, dense_rank, lead & lag)
    - Window functions in SQL are used to perform calculations across a set of rows related to the current row within a specified window. Here's an explanation of the main types of window functions:
    1. **ROW_NUMBER()**: Assigns a unique sequential integer to each row within the partition of a result set. The numbering starts from 1 for the first row in each partition.
    2. **RANK()**: Assigns a unique rank to each distinct row within the partition of a result set. Rows with equal values are assigned the same rank, and the next rank is skipped. For example, if two rows tie for the first place, the next row will be assigned a rank of 3.
    3. **DENSE_RANK()**: Similar to RANK(), but does not skip ranks when there are ties. It assigns consecutive ranks to rows with equal values, ensuring that there are no gaps in the ranking sequence.
    4. **LEAD()**: Retrieves the value from a specified column in the next row within the partition of a result set. It allows you to access data from subsequent rows without using a self-join.
    5. **LAG()**: Retrieves the value from a specified column in the previous row within the partition of a result set. It allows you to access data from preceding rows without using a self-join.
    
    These window functions are typically used with the OVER() clause, which defines the window or partition over which the function operates. The window can be defined by specifying a range of rows relative to the current row or by specifying partitioning criteria to group rows into separate partitions for the calculation.
    
- What is difference between Delete and Truncate?
    - Both DELETE and TRUNCATE are SQL commands used to remove data from a table, but they differ in their functionality and behavior:
    1. **DELETE**:
        - DELETE is a DML (Data Manipulation Language) command.
        - It removes one or more rows from a table based on a condition specified in the WHERE clause.
        - DELETE operation can be rolled back using the ROLLBACK command if it is executed within a transaction.
        - It fires any associated triggers on the table for each row deleted.
        - DELETE can be selective, allowing you to specify which rows to remove based on criteria.
    2. **TRUNCATE**:
        - TRUNCATE is a DDL (Data Definition Language) command.
        - It removes all rows from a table, effectively resetting the table to its original state.
        - TRUNCATE operation cannot be rolled back using the ROLLBACK command because it is not logged in the transaction log.
        - It resets any identity columns or auto-increment sequences on the table to their initial values.
        - TRUNCATE is faster and requires fewer system resources compared to DELETE, especially for large tables.
        - TRUNCATE cannot be used with a WHERE clause; it removes all rows from the table unconditionally.
    
    In summary, DELETE is used to selectively remove rows from a table based on specific criteria, while TRUNCATE is used to remove all rows from a table without any conditions and is faster but less flexible than DELETE.
    
- What is difference between DML, DDL and DCL?
    - DML, DDL, and DCL are three categories of SQL commands with distinct purposes:
    1. **DML (Data Manipulation Language)**:
        - DML commands are used to manipulate data stored in the database.
        - Examples of DML commands include SELECT, INSERT, UPDATE, and DELETE.
        - These commands affect the data within tables, allowing users to retrieve, add, modify, or remove data.
    2. **DDL (Data Definition Language)**:
        - DDL commands are used to define, modify, or remove the structure of database objects.
        - Examples of DDL commands include CREATE, ALTER, DROP, TRUNCATE, and RENAME.
        - These commands are used to create and modify tables, indexes, views, constraints, and other database objects.
    3. **DCL (Data Control Language)**:
        - DCL commands are used to control access to data within the database.
        - Examples of DCL commands include GRANT and REVOKE.
        - These commands are used to grant or revoke permissions and privileges on database objects to users or roles.
    
    In summary:
    
    - DML commands are for manipulating data within tables.
    - DDL commands are for defining or modifying the structure of database objects.
    - DCL commands are for controlling access to data by granting or revoking permissions and privileges.
- What are aggregate function and when do we use them? explain with few example.
- Aggregate functions in SQL are functions that perform a calculation on a set of values and return a single value as a result. These functions operate on multiple rows of data and typically group the rows into a single value based on the specified criteria.
    
    Aggregate functions are commonly used with the GROUP BY clause to perform calculations on groups of rows rather than individual rows. They are often used in conjunction with SELECT statements to generate summary information from a dataset.
    
    Here are a few examples of aggregate functions and when they are used:
    
    1. **COUNT()**: Counts the number of rows in a result set or the number of non-null values in a specific column.
        ```sql
        SELECT COUNT(*) AS total_rows FROM table_name;
        SELECT COUNT(column_name) AS non_null_values FROM table_name;
        ```
    2. **SUM()**: Calculates the sum of values in a column.
        ```sql
        SELECT SUM(sales_amount) AS total_sales FROM sales_table;
        ```
    3. **AVG()**: Calculates the average of values in a column.
        ```sql
        SELECT AVG(salary) AS average_salary FROM employees;
        ```
    4. **MIN()**: Returns the minimum value in a column.
        ```sql
        SELECT MIN(age) AS youngest_age FROM students;
        ```
    5. **MAX()**: Returns the maximum value in a column.
        ```sql
        SELECT MAX(price) AS highest_price FROM products;
        ```
          Aggregate functions are used whenever you need to perform calculations on groups of rows, such as finding totals, averages, or extremes (minimum/maximum values), and when generating summary statistics from a dataset. They are essential tools for data analysis and reporting in SQL.
    
- Which is faster between CTE and Subquery?
    - The speed difference between Common Table Expressions (CTEs) and subqueries can vary depending on the specific query, database engine, indexing, and other factors. However, in many cases, there isn't a significant performance difference between them, as modern SQL database engines are optimized to handle both efficiently.
        
        That said, there are some considerations to keep in mind:
        
        1. **Readability and Maintainability**: CTEs often provide better readability and maintainability, especially for complex queries with multiple levels of nesting. They allow you to break down the query into smaller, more manageable parts.
        2. **Query Optimization**: Some database engines might optimize CTEs and subqueries differently. For example, a well-written subquery might be optimized to use an index more efficiently, resulting in better performance.
        3. **Materialization**: CTEs are often materialized, meaning they are computed and stored temporarily in memory or disk before being used in the main query. Depending on the size of the dataset and the complexity of the query, materialization can impact performance. Subqueries may or may not be materialized, depending on the database engine's optimization strategy.
        
        In general, it's recommended to use whichever construct makes your query more readable and maintainable, as the performance difference between CTEs and subqueries is often negligible. However, if you encounter performance issues with a particular query, you can try experimenting with both CTEs and subqueries to see if one performs better than the other in your specific scenario. Additionally, profiling tools provided by the database engine can help identify performance bottlenecks and optimize queries accordingly.
        
- What are constraints and types of Constraints?
    - Constraints in SQL are rules that enforce data integrity and ensure that data stored in a database follows predefined criteria or conditions. Constraints are applied to columns or tables and help maintain the accuracy, consistency, and reliability of the data.
    - **Primary Key Constraint**:
        - Ensures each row in a table is uniquely identifiable.
        - Primary key columns cannot contain duplicate or NULL values.
    - **Foreign Key Constraint**:
        - Establishes a relationship between two tables.
        - Foreign key columns in a child table reference the primary key columns of a parent table, enforcing referential integrity.
    - **Unique Constraint**:
        - Ensures that values in a column or combination of columns are unique across the table.
        - Similar to a primary key constraint but allows NULL values.
    - **Check Constraint**:
        - Specifies a condition that must be satisfied for each row in a table.
        - Check constraints ensure data inserted or updated in a table meets specific criteria.
    - **Not Null Constraint**:
        - Ensures that a column does not contain NULL values.
        - Specifies that a column must have a value for every row in a table.
- Types of Keys?
    - In a relational database, keys are used to uniquely identify rows within a table and establish relationships between tables. Here are the main types of keys:
    1. **Primary Key**:
        - A primary key is a column or a set of columns that uniquely identifies each row in a table.
        - It must contain unique values and cannot contain NULL values.
        - Each table can have only one primary key.
        - Example: EmployeeID in an Employees table.
    2. **Foreign Key**:
        - A foreign key is a column or a set of columns in a table that establishes a link between data in two tables.
        - It refers to the primary key of another table and enforces referential integrity.
        - It can contain duplicate values and NULL values unless explicitly constrained.
        - Example: DepartmentID in an Employees table referencing the DepartmentID primary key in a Departments table.
    3. **Unique Key**:
        - A unique key is a column or a set of columns that ensures each value in the column(s) is unique across the table.
        - Unlike a primary key, a unique key can contain NULL values, but if a column is defined as unique, only one NULL value is allowed.
        - Each table can have multiple unique keys.
        - Example: EmailAddress in a Users table.
    4. **Composite Key**:
        - A composite key is a combination of two or more columns that uniquely identifies each row in a table.
        - It is used when no single column can uniquely identify rows.
        - Example: (DepartmentID, ProjectID) in a Projects table.
    5. **Candidate Key**:
        - A candidate key is a column or a set of columns that can uniquely identify each row in a table.
        - It may or may not be chosen as the primary key.
        - Example: Both EmployeeID and SocialSecurityNumber could potentially serve as candidate keys in an Employees table.
- Different types of Operators ?
    - In SQL, operators are used to perform operations on data, compare values, and manipulate data. Here are the main types of operators:
    1. **Arithmetic Operators**:
        - Used to perform arithmetic operations such as addition, subtraction, multiplication, division, and modulus.
        - Examples: + (addition), - (subtraction), * (multiplication), / (division), % (modulus).
    2. **Comparison Operators**:
        - Used to compare values and return a Boolean result (true or false).
        - Examples: = (equal to), != or <> (not equal to), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to).
    3. **Logical Operators**:
        - Used to combine multiple conditions and evaluate them as a single Boolean expression.
        - Examples: AND (logical AND), OR (logical OR), NOT (logical NOT).
    4. **Concatenation Operator**:
        - Used to concatenate strings or concatenate strings with non-string values.
        - In some databases, the concatenation operator is represented by the || symbol.
        - Example: || (concatenation operator).
    5. **Bitwise Operators**:
        - Used to perform bitwise operations on binary values.
        - Examples: & (bitwise AND), | (bitwise OR), ^ (bitwise XOR), ~ (bitwise NOT), << (left shift), >> (right shift).
    6. **Assignment Operator**:
        - Used to assign a value to a variable or column.
        - Example: = (assignment operator).
    7. **NULL Comparison Operators**:
        - Used to compare values with NULL.
        - Examples: IS NULL (checks if a value is NULL), IS NOT NULL (checks if a value is not NULL).
- Difference between Group By and Where?
- What is difference between varchar and nvarchar?
    - VARCHAR [Variable-length Character Data] is suitable for storing character data that only includes characters from a single-byte character set, such as English, Spanish, or French.
    - NVARCHAR [National Variable-length Character Data] is suitable for storing character data that may include characters from different languages and require support for multilingual text, such as Chinese, Japanese, Arabic, or any other language that uses Unicode characters.
- Similar for char and nchar?
- What is an index? Explain its different types.
  
- Differentiate between UNION and UNION ALL.
- What are the various types of relationships in SQL?
    
    
    | One-to-One (1:1) Relationship | One-to-Many Relationship | Many-to-Many Relationship |
    | --- | --- | --- |
    | Each record in the first table (parent table) is related to exactly one record in the second table (child table), and vice versa | Each record in the parent table can be related to one or more records in the child table, but each record in the child table is related to only one record in the parent table. | Each record in the first table can be related to one or more records in the second table, and vice versa. |
    | Example: Employee and Employee_Details tables, where each employee has exactly one set of details. | Example: Department and Employee tables, where each department can have multiple employees, but each employee belongs to only one department. | Example: Student and Course tables, where each student can enroll in multiple courses, and each course can have multiple students.|
- Difference between Primary Key and Secondary Key?
- Find the second highest salary of an employee?
    
    ```
    select max(salary) from emp
    where salary < (select max(salary) from emp)
    ```
    
- Write retention query in SQL?
    - Retention Rate = (No of customers at the end of the month - No of new customers) * 100 / No of customers at the start of the month
    ```
    SELECT 
        ((end_customers - new_customers) / start_customers) * 100 AS retention_rate
    FROM 
        (
            SELECT 
                COUNT(CASE WHEN join_date <= 'start_date' THEN customer_id END) AS start_customers,
                COUNT(CASE WHEN join_date <= 'end_date' THEN customer_id END) AS end_customers
            FROM 
                customers_table
        ) AS customer_counts,
        (
            SELECT 
                COUNT(CASE WHEN join_date BETWEEN 'start_date' AND 'end_date' THEN customer_id END) AS new_customers
            FROM 
                customers_table
        ) AS new_customers_count;
    ```
    
- Write year-on-year growth in SQL?
- Write a query for cummulative sum in SQL?
    - 5,3,8,2,7 ⇒ 5 + 3 + 8 + 2 + 7 ⇒ 25
    
    ```
    select date, amount, sum(amount) over(order by date) as cummulative_sum
    from sales
    ```
- Difference between Function and Store procedure ?
- What are Views? Do we use variable in views? What are the limitations of views?
    - A view in SQL is a virtual table that does not store data itself. Instead, it executes the SQL query used to define it every time it is accessed, presenting the result set of that query as a table. This allows users to simplify complex queries, encapsulate business logic, and present data in a specific format without duplicating storage.
  ```
  create view order_summary   --> Creating the view
  as
  select o.ord_id, o.date, p.prod_name,
      c.cust_name - (p.priceo.quantity) ((p.price o.quantity) disc_percent : : float/100) as cost
  from tb_customer_data c
  join tb_order_details o
  on o.cust_id=c.cust_id
  join tb_product_info p
  on p.prod_id = o.prod_id;

  select from order_summary;  --> Calling the view
  ```
