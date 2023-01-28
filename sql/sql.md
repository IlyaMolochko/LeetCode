# 595. Big Countries

Table: World

name is the primary key column for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the
population, and its GDP value.

```mysql
Create table If Not Exists World
(
    name       varchar(255),
    continent  varchar(255),
    area       int,
    population int,
    gdp        int
);
Truncate table World;
insert into World (name, continent, area, population, gdp)
values ('Afghanistan', 'Asia', '652230', '25500100', '20343000000');
insert into World (name, continent, area, population, gdp)
values ('Albania', 'Europe', '28748', '2831741', '12960000000');
insert into World (name, continent, area, population, gdp)
values ('Algeria', 'Africa', '2381741', '37100000', '188681000000');
insert into World (name, continent, area, population, gdp)
values ('Andorra', 'Europe', '468', '78115', '3712000000');
insert into World (name, continent, area, population, gdp)
values ('Angola', 'Africa', '1246700', '20609294', '100990000000');
```

A country is big if:

> it has an area of at least three million (i.e., 3000000 km2), or

> it has a population of at least twenty-five million (i.e., 25000000).

Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.

```mysql
select name,
       population,
       area
from world
where area >= 3000000
   or population >= 25000000;
```

# 1757. Recyclable and Low Fat Products

```mysql
Create table If Not Exists Products
(
    product_id int,
    low_fats   ENUM ('Y', 'N'),
    recyclable ENUM ('Y','N')
);
Truncate table Products;
insert into Products (product_id, low_fats, recyclable)
values ('0', 'Y', 'N');
insert into Products (product_id, low_fats, recyclable)
values ('1', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable)
values ('2', 'N', 'Y');
insert into Products (product_id, low_fats, recyclable)
values ('3', 'Y', 'Y');
insert into Products (product_id, low_fats, recyclable)
values ('4', 'N', 'N')
```

Table: Products

product_id is the primary key for this table.

low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.

recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

```mysql
select product_id
from products
where low_fats = 'Y'
  and recyclable = 'Y';
```

# 584. Find Customer Referee

```mysql
Create table If Not Exists Customer
(
    id         int,
    name       varchar(25),
    referee_id int
);
Truncate table Customer;
insert into Customer (id, name, referee_id)
values ('1', 'Will', 'None');
insert into Customer (id, name, referee_id)
values ('2', 'Jane', 'None');
insert into Customer (id, name, referee_id)
values ('3', 'Alex', '2');
insert into Customer (id, name, referee_id)
values ('4', 'Bill', 'None');
insert into Customer (id, name, referee_id)
values ('5', 'Zack', '1');
insert into Customer (id, name, referee_id)
values ('6', 'Mark', '2');
```

Table: Customer

id is the primary key column for this table.

Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

```mysql
select t1.name
from customer t1
         left outer join
     (select id
      from customer
      where referee_id = 2) t2
     on t1.id = t2.id
where t2.id is null;
```

# 183. Customers Who Never Order

```mysql
Create table If Not Exists Customers
(
    id   int,
    name varchar(255)
);
Create table If Not Exists Orders
(
    id         int,
    customerId int
);
Truncate table Customers;
insert into Customers (id, name)
values ('1', 'Joe');
insert into Customers (id, name)
values ('2', 'Henry');
insert into Customers (id, name)
values ('3', 'Sam');
insert into Customers (id, name)
values ('4', 'Max');
Truncate table Orders;
insert into Orders (id, customerId)
values ('1', '3');
insert into Orders (id, customerId)
values ('2', '1');
```

Table: Customers

id is the primary key column for this table.

Each row of this table indicates the ID and name of a customer.

Table: Orders

id is the primary key column for this table.

customerId is a foreign key of the ID from the Customers table.

Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

Write an SQL query to report all customers who never order anything.

Return the result table in any order.

```mysql
select t1.name as Customers
from customers t1
         left outer join orders t2
                         on t1.id = t2.customerId
where t2.id is null;
```

# 1873. Calculate Special Bonus

```mysql
Create table If Not Exists Employees
(
    employee_id int,
    name        varchar(30),
    salary      int
);
Truncate table Employees;
insert into Employees (employee_id, name, salary)
values ('2', 'Meir', '3000');
insert into Employees (employee_id, name, salary)
values ('3', 'Michael', '3800');
insert into Employees (employee_id, name, salary)
values ('7', 'Addilyn', '7400');
insert into Employees (employee_id, name, salary)
values ('8', 'Juan', '6100');
insert into Employees (employee_id, name, salary)
values ('9', 'Kannon', '7700');
```

Table: Employees

employee_id is the primary key for this table.

Each row of this table indicates the employee ID, employee name, and salary.

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID
of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee
is 0 otherwise.

Return the result table ordered by employee_id.

```mysql
select employee_id,
       (case
            when employee_id % 2 = 1 and name not like 'M%'
                then salary
            else 0
           end) as bonus
from employees
order by employee_id;
```

# 627. Swap Salary

```mysql
Create table If Not Exists Salary
(
    id     int,
    name   varchar(100),
    sex    char(1),
    salary int
);
Truncate table Salary;
insert into Salary (id, name, sex, salary)
values ('1', 'A', 'm', '2500');
insert into Salary (id, name, sex, salary)
values ('2', 'B', 'f', '1500');
insert into Salary (id, name, sex, salary)
values ('3', 'C', 'm', '5500');
insert into Salary (id, name, sex, salary)
values ('4', 'D', 'f', '500');
```

Table: Salary

id is the primary key for this table.

The sex column is ENUM value of type ('m', 'f').

The table contains information about an employee.

Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single
update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

```mysql
update salary
set sex =
        case
            when sex = 'm' then 'f'
            else 'm'
            end;
```

# 196. Delete Duplicate Emails

```mysql
Create table If Not Exists Person
(
    Id    int,
    Email varchar(255)
);
Truncate table Person;
insert into Person (id, email)
values ('1', 'john@example.com');
insert into Person (id, email)
values ('2', 'bob@example.com');
insert into Person (id, email)
values ('3', 'john@example.com');
```

Table: Person

id is the primary key column for this table.

Each row of this table contains an email. The emails will not contain uppercase letters.

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you
are supposed to write a DELETE statement and not a SELECT one.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of
code and then show the Person table. The final order of the Person table does not matter.

```mysql
delete p1
from person p1
         inner join person p2
                    on p1.email = p2.email and p1.id > p2.id;
```

# 1667. Fix Names in a Table

```mysql
Create table If Not Exists Users
(
    user_id int,
    name    varchar(40)
);
Truncate table Users;
insert into Users (user_id, name)
values ('1', 'aLice');
insert into Users (user_id, name)
values ('2', 'bOB');
```

user_id is the primary key for this table.

This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

```mysql
select user_id,
       concat(upper(substring(name, 1, 1)), lower(substring(name, 2))) as name
from users
order by user_id;
```

# 1484. Group Sold Products By The Date

```mysql
Create table If Not Exists Activities
(
    sell_date date,
    product   varchar(20)
);
Truncate table Activities;
insert into Activities (sell_date, product)
values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product)
values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product)
values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product)
values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product)
values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product)
values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product)
values ('2020-05-30', 'T-Shirt');
```

Table Activities:

There is no primary key for this table, it may contain duplicates.

Each row of this table contains the product name and the date it was sold in a market.

Write an SQL query to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

```mysql
select sell_date,
       count(distinct product)                                       as num_sold,
       group_concat(distinct product order by product separator ',') as products
from activities
group by sell_date
order by sell_date;
```

# 1527. Patients With a Condition

```mysql
Create table If Not Exists Patients
(
    patient_id   int,
    patient_name varchar(30),
    conditions   varchar(100)
);
Truncate table Patients;
insert into Patients (patient_id, patient_name, conditions)
values ('1', 'Daniel', 'YFEV COUGH');
insert into Patients (patient_id, patient_name, conditions)
values ('2', 'Alice', '');
insert into Patients (patient_id, patient_name, conditions)
values ('3', 'Bob', 'DIAB100 MYOP');
insert into Patients (patient_id, patient_name, conditions)
values ('4', 'George', 'ACNE DIAB100');
insert into Patients (patient_id, patient_name, conditions)
values ('5', 'Alain', 'DIAB201');
```

patient_id is the primary key for this table.

'conditions' contains 0 or more code separated by spaces.

This table contains information of the patients in the hospital.

Write an SQL query to report the patient_id, patient_name and conditions of the patients who have Type I Diabetes. Type
I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

```mysql
select patient_id,
       patient_name,
       conditions
from patients
where (conditions like '% DIAB1%' or conditions like 'DIAB1%');
```

# 1965. Employees With Missing Information

```mysql
Create table If Not Exists Employees
(
    employee_id int,
    name        varchar(30)
);
Create table If Not Exists Salaries
(
    employee_id int,
    salary      int
);
Truncate table Employees;
insert into Employees (employee_id, name)
values ('2', 'Crew');
insert into Employees (employee_id, name)
values ('4', 'Haven');
insert into Employees (employee_id, name)
values ('5', 'Kristian');
Truncate table Salaries;
insert into Salaries (employee_id, salary)
values ('5', '76071');
insert into Salaries (employee_id, salary)
values ('1', '22517');
insert into Salaries (employee_id, salary)
values ('4', '63539');
```

Table: Employees

employee_id is the primary key for this table.

Each row of this table indicates the name of the employee whose ID is employee_id.

Table: Salaries

employee_id is the primary key for this table.

Each row of this table indicates the salary of the employee whose ID is employee_id.

Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is
missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.

```mysql
select e.employee_id
from employees e
         left outer join salaries s
                         on e.employee_id = s.employee_id
where s.salary is null
union
select s.employee_id
from employees e
         right outer join salaries s
                          on e.employee_id = s.employee_id
where e.name is null
order by employee_id;
```

# 1795. Rearrange Products Table

```mysql
Create table If Not Exists Products
(
    product_id int,
    store1     int,
    store2     int,
    store3     int
);
Truncate table Products;
insert into Products (product_id, store1, store2, store3)
values ('0', '95', '100', '105');
insert into Products (product_id, store1, store2, store3)
values ('1', '70', 'None', '80');
```

Table: Products

product_id is the primary key for this table.

Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.

If the product is not available in a store, the price will be null in that store's column.

Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). If a product is not
available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

```mysql
select product_id, 'store1' as store, store1 as price
from products
where store1 is not null
union
select product_id, 'store2' as store, store2 as price
from products
where store2 is not null
union
select product_id, 'store3' as store, store3 as price
from products
where store3 is not null;
```

# 608. Tree Node

```mysql
Create table If Not Exists Tree
(
    id   int,
    p_id int
);
Truncate table Tree;
insert into Tree (id, p_id)
values ('1', 'None');
insert into Tree (id, p_id)
values ('2', '1');
insert into Tree (id, p_id)
values ('3', '1');
insert into Tree (id, p_id)
values ('4', '2');
insert into Tree (id, p_id)
values ('5', '2');
```

Table: Tree

id is the primary key column for this table.

Each row of this table contains information about the id of a node and the id of its parent node in a tree.

The given structure is always a valid tree.

Each node in the tree can be one of three types:

"Leaf": if the node is a leaf node.

"Root": if the node is the root of the tree.

"Inner": If the node is neither a leaf node nor a root node.

Write an SQL query to report the type of each node in the tree.

Return the result table in any order.

```mysql
select t.id,
       if(t.p_id is null,
          'Root', if(t.id in (select t.p_id from tree t), 'Inner', 'Leaf')) as type
from tree t;
```

# 176. Second Highest Salary

```mysql
select (select distinct salary
        from employee
        order by salary desc
        limit 1 offset 1) as SecondHighestSalary
;
```

# 175. Combine Two Tables

```mysql
Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255));
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255));
Truncate table Person;
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');
Truncate table Address;
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');
```

Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

```mysql
select 
        p.firstname,
        p.lastname,
        a.city,
        a.state
from 
        Person p
left outer join 
        Address a
on 
    p.personId = a.personId;
```

# 1581. Customer Who Visited but Did Not Make Any Transactions

```mysql
Create table If Not Exists Visits(visit_id int, customer_id int);
Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int);
Truncate table Visits;
insert into Visits (visit_id, customer_id) values ('1', '23');
insert into Visits (visit_id, customer_id) values ('2', '9');
insert into Visits (visit_id, customer_id) values ('4', '30');
insert into Visits (visit_id, customer_id) values ('5', '54');
insert into Visits (visit_id, customer_id) values ('6', '96');
insert into Visits (visit_id, customer_id) values ('7', '54');
insert into Visits (visit_id, customer_id) values ('8', '54');
Truncate table Transactions;
insert into Transactions (transaction_id, visit_id, amount) values ('2', '5', '310');
insert into Transactions (transaction_id, visit_id, amount) values ('3', '5', '300');
insert into Transactions (transaction_id, visit_id, amount) values ('9', '5', '200');
insert into Transactions (transaction_id, visit_id, amount) values ('12', '1', '910');
insert into Transactions (transaction_id, visit_id, amount) values ('13', '2', '970');
```

Write a SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

```mysql
select v.customer_id,
       count(v.customer_id) as count_no_trans
from visits v
left outer join transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by v.customer_id;
```

# 1148. Article Views I

```mysql
Create table If Not Exists Views (article_id int, author_id int, viewer_id int, view_date date);
Truncate table Views;
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '5', '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '6', '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '7', '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '6', '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date) values ('4', '7', '1', '2019-07-22');
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21');
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21');
```

Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

```mysql
select distinct(author_id) as id
from views
where author_id = viewer_id
order by id;
```

# 197. Rising Temperature

```mysql
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');
```

Table: Weather

Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

```mysql
select t1.id as Id
from weather t1
         inner join weather t2
                    on datediff(t1.recordDate, t2.recordDate) = 1
                        and t1.temperature > t2.temperature;
```

# 

```mysql
Create table If Not Exists SalesPerson (sales_id int, name varchar(255), salary int, commission_rate int, hire_date date);
Create table If Not Exists Company (com_id int, name varchar(255), city varchar(255));
Create table If Not Exists Orders (order_id int, order_date date, com_id int, sales_id int, amount int);
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('1', 'John', '100000', '6', '4/1/2006');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('2', 'Amy', '12000', '5', '5/1/2010');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('3', 'Mark', '65000', '12', '12/25/2008');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('4', 'Pam', '25000', '25', '1/1/2005');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date) values ('5', 'Alex', '5000', '10', '2/3/2007');
insert into Company (com_id, name, city) values ('1', 'RED', 'Boston');
insert into Company (com_id, name, city) values ('2', 'ORANGE', 'New York');
insert into Company (com_id, name, city) values ('3', 'YELLOW', 'Boston');
insert into Company (com_id, name, city) values ('4', 'GREEN', 'Austin');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('1', '1/1/2014', '3', '4', '10000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('2', '2/1/2014', '4', '5', '5000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('3', '3/1/2014', '1', '1', '50000');
insert into Orders (order_id, order_date, com_id, sales_id, amount) values ('4', '4/1/2014', '1', '4', '25000');
```

Table: SalesPerson

Table: Company

Table: Orders

Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

```mysql
with orders_with_red as (
    select o.sales_id
    from orders o
    inner join company c
    on o.com_id = c.com_id
    where c.name = 'RED'
)
select s.name
from SalesPerson s
left join 
orders_with_red o
on s.sales_id = o.sales_id
where o.sales_id is null;
```

