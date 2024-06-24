- Write a SQL query to find the second highest salary from the table emp. (Column name – id, salary)
    ```
    select max(salary) from emp where salary < (select max(salary) from emp)
    ```
- Write a SQL query to find the numbers which consecutively occurs 3 times. (Column name – id, numbers)
   ```
    
    ```
- Write a SQL query to find the days when temperature was higher than its previous dates. (Column name – Days, Temp)
    ```
    
    ```
- Write a SQL query to delete Duplicate rows in a table.
    ```
    WITH CTE AS (
        SELECT 
            product_id,
            product_name,
            price,
            ROW_NUMBER() OVER (PARTITION BY product_name, price ORDER BY product_id) AS row_num
        FROM 
            products
    )
    DELETE FROM CTE
    WHERE row_num > 1;
    ```
- Write a SQL query for cumulative sum of salary of each employee from Jan to July. (Column name – Emp_id, Month, Salary).
    ```
    select emp_id, month, salary, 
    	sum(salary) over (partition by emp_id order by month) as cummulative_sum
    from emp 
    where month between 'jan' and 'july'
    ```
- Write a SQL query to display year on year growth for each product. (Column name – transaction_id, Product_id, transaction_date, spend). Output will have year, product_id & yoy_growth.
    ```
        
    ```
- Write a SQL query to find rolling average of posts on daily bais for each user_id.(Column_name – user_id, date, post_count). Round up the average upto two decimal places.
    ```
        
    ```
- Write a SQL query to get emp id and department for each department who recently joined the organization and still in working. (column -emp id, first name, last name, date of join, date of exit , department.)
   ```
        
   ```
- How many rows will come in outputs of Left, Right, Inner and outer join from two tables having duplicate rows.
    For Example:-
    Left table A-
    Column
    1
    1
    1
    2
    2
    3
    4
    5
    Right table B-
    Column
    1
    1
    2
    2
    2
    3
    3
    3
    4
    ```
    
    ```
- Write a query to get mean, median and mode for earning? (Column – Emp_id, salary)
    ```
        
    ```
- Given: Table X: Columns: ids with values 1, 1, 1, 1. Table Y: Columns: ids with values 1, 1, 1, 1, 1, 1, 1, 1. Task: Determine the count of rows in the output of the following queries:
    
    Select * From X join Y on X.ids != Y.ids
    
    Select * From X left join Y on X.ids != Y.ids
    
    Select * From X right join Y on X.ids != Y.ids
    
    Select * From X full outer join Y on X.ids != Y.ids
