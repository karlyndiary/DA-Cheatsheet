1. Write down the query to print the first letter of the store in Upper Case and all other letter in Lower Case.
```
SELECT CONCAT(UPPER(SUBSTRING(customer_name, 1, 1)), LOWER(SUBSTRING(customer_name, 2, LENGTH(customer_name)))) as stores
FROM atliq.customers
```
+---------------------------+
|       stores              |
+---------------------------+
|       Surge stores        |
+---------------------------+
|       Surface stores      |
+---------------------------+
|       Premium stores      |
+---------------------------+
|       Nomad stores        |
+---------------------------+
|       Info stores         |
+---------------------------+

2. Write down the query to display all employee name in one cell seprated by ',' ex:-"Vikas, nikita, Ashish, Nikhil , Danish"
```
select concat(group_concat(customer_name separator ', ')) as emp
from atliq.customers
```
Surge Stores, Nomad Stores, Excel Stores, Surface Stores, Premium Stores, Electricalsara Stores, Info Stores, Acclaimed Stores, Electricalsquipo Stores, Atlas Stores, Flawless Stores, Integration Stores, Unity Stores, Forward Stores, Electricalsbea Store...

