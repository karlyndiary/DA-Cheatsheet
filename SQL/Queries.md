1. Write down the query to print the first letter of the store in Upper Case and all other letter in Lower Case.
```
SELECT CONCAT(UPPER(SUBSTRING(customer_name, 1, 1)), LOWER(SUBSTRING(customer_name, 2, LENGTH(customer_name)))) as stores
FROM atliq.customers
```
+---------------------------+
|       Store Name          |
+---------------------------+
|       Surge stores        |
+---------------------------+
|       Surface stores      |
+---------------------------+
|       Premium stores      |
+---------------------------+
|       Nomad stores        |
+---------------------------+

2. Write down the query to display all employee name in one cell seprated by ',' ex:-"Vikas, nikita, Ashish, Nikhil , Danish"
```
select concat(group_concat(customer_name separator ', ')) as customer_names
from atliq.customers
```
customer_names
-------------------------------
Surge Stores, Nomad Stores, Excel Stores, Surface Stores, Premium Stores, Electricalsara Stores, Info Stores, Acclaimed Stores, Electricalsquipo Stores, Atlas Stores, 
Flawless Stores, Integration Stores, Unity Stores, Forward Stores, Electricalsbea Store...

3. Write down the query to retrieve the customer_name and the respective customer_name values, where multiple customers of the same type are listed in the same cell separated by commas.
```
SELECT customer_name,  GROUP_CONCAT(customer_name SEPARATOR ', ') AS customer_name
FROM atliq.customers
GROUP BY customer_type;
```

4. You have a table(FuelDetail) with ID, Fuel, And Date columns.
--Fuel column is contain fuel quantity at a particular time when car start traveling. So we need to find out
that when the driver fill Petrol in his/her car.
--By FuelDetail Table image on the top of this post, you can understand the query.
--Car start driving at 10 Am on 25th April with petrol(10 liter)
--at 11 AM Petrol was 9 liters
--at 12 AM petrol was 8 liters
--at 2 PM (14) petrol was 12 liters...
--This means that he/she fill the petrol at 25th April 2014 at 2PM
--Next time he fill petrol at 7PM 25th April 2014
--and Next time he fill petrol at 11PM 25th April 2014
```
SELECT c1.fuel AS `Fuel quantity Now`, c1.`Date`, c.fuel AS `Fuel quantity Before`, c.`Date`
FROM FuelDetail c
JOIN FuelDetail c1 ON c1.`Date` = (
    SELECT MIN(`Date`) 
    FROM FuelDetail 
    WHERE `Date` > c.`Date`
)
WHERE c1.fuel > c.fuel;
```

5. Suppose that you have table Employee with a column EName which contain
Records Employee name(EName) as A,B,A,A,B,D,C,M,A, Write a query which will
change/Swap the EName A to B and B to A.
```
UPDATE Employee
set EName = (CASE
WHEN EName='A' THEN 'B'
WHEN EName='B' THEN 'A'
ELSE EName
END)
```

6. Write a query to create a clone of existing table.
```
CREATE TABLE customer_data2.cust_address SELECT * FROM customer_data2.customer_address WHERE 1=0; -> clones only the structure
CREATE TABLE customer_data2.cust_add SELECT * FROM customer_data2.customer_address -> clones the structure and data
```

7. Write a query to calculate number of A in string 'VIKASAAA'?
```
SELECT LENGTH('VIKASAAA') - LENGTH(REPLACE('VIKASAAA', 'A', ''))
```
