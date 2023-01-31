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
Create table If Not Exists Person
(
    personId  int,
    firstName varchar(255),
    lastName  varchar(255)
);
Create table If Not Exists Address
(
    addressId int,
    personId  int,
    city      varchar(255),
    state     varchar(255)
);
Truncate table Person;
insert into Person (personId, lastName, firstName)
values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName)
values ('2', 'Alice', 'Bob');
Truncate table Address;
insert into Address (addressId, personId, city, state)
values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state)
values ('2', '3', 'Leetcode', 'California');
```

Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the
address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

```mysql
select p.firstname,
       p.lastname,
       a.city,
       a.state
from Person p
         left outer join
     Address a
     on
         p.personId = a.personId;
```

# 1581. Customer Who Visited but Did Not Make Any Transactions

```mysql
Create table If Not Exists Visits
(
    visit_id    int,
    customer_id int
);
Create table If Not Exists Transactions
(
    transaction_id int,
    visit_id       int,
    amount         int
);
Truncate table Visits;
insert into Visits (visit_id, customer_id)
values ('1', '23');
insert into Visits (visit_id, customer_id)
values ('2', '9');
insert into Visits (visit_id, customer_id)
values ('4', '30');
insert into Visits (visit_id, customer_id)
values ('5', '54');
insert into Visits (visit_id, customer_id)
values ('6', '96');
insert into Visits (visit_id, customer_id)
values ('7', '54');
insert into Visits (visit_id, customer_id)
values ('8', '54');
Truncate table Transactions;
insert into Transactions (transaction_id, visit_id, amount)
values ('2', '5', '310');
insert into Transactions (transaction_id, visit_id, amount)
values ('3', '5', '300');
insert into Transactions (transaction_id, visit_id, amount)
values ('9', '5', '200');
insert into Transactions (transaction_id, visit_id, amount)
values ('12', '1', '910');
insert into Transactions (transaction_id, visit_id, amount)
values ('13', '2', '970');
```

Write a SQL query to find the IDs of the users who visited without making any transactions and the number of times they
made these types of visits.

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
Create table If Not Exists Views
(
    article_id int,
    author_id  int,
    viewer_id  int,
    view_date  date
);
Truncate table Views;
insert into Views (article_id, author_id, viewer_id, view_date)
values ('1', '3', '5', '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('1', '3', '6', '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('2', '7', '7', '2019-08-01');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('2', '7', '6', '2019-08-02');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('4', '7', '1', '2019-07-22');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('3', '4', '4', '2019-07-21');
insert into Views (article_id, author_id, viewer_id, view_date)
values ('3', '4', '4', '2019-07-21');
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
Create table If Not Exists Weather
(
    id          int,
    recordDate  date,
    temperature int
);
Truncate table Weather;
insert into Weather (id, recordDate, temperature)
values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature)
values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature)
values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature)
values ('4', '2015-01-04', '30');
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
Create table If Not Exists SalesPerson
(
    sales_id        int,
    name            varchar(255),
    salary          int,
    commission_rate int,
    hire_date       date
);
Create table If Not Exists Company
(
    com_id int,
    name   varchar(255),
    city   varchar(255)
);
Create table If Not Exists Orders
(
    order_id   int,
    order_date date,
    com_id     int,
    sales_id   int,
    amount     int
);
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
values ('1', 'John', '100000', '6', '4/1/2006');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
values ('2', 'Amy', '12000', '5', '5/1/2010');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
values ('3', 'Mark', '65000', '12', '12/25/2008');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
values ('4', 'Pam', '25000', '25', '1/1/2005');
insert into SalesPerson (sales_id, name, salary, commission_rate, hire_date)
values ('5', 'Alex', '5000', '10', '2/3/2007');
insert into Company (com_id, name, city)
values ('1', 'RED', 'Boston');
insert into Company (com_id, name, city)
values ('2', 'ORANGE', 'New York');
insert into Company (com_id, name, city)
values ('3', 'YELLOW', 'Boston');
insert into Company (com_id, name, city)
values ('4', 'GREEN', 'Austin');
insert into Orders (order_id, order_date, com_id, sales_id, amount)
values ('1', '1/1/2014', '3', '4', '10000');
insert into Orders (order_id, order_date, com_id, sales_id, amount)
values ('2', '2/1/2014', '4', '5', '5000');
insert into Orders (order_id, order_date, com_id, sales_id, amount)
values ('3', '3/1/2014', '1', '1', '50000');
insert into Orders (order_id, order_date, com_id, sales_id, amount)
values ('4', '4/1/2014', '1', '4', '25000');
```

Table: SalesPerson

Table: Company

Table: Orders

Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with
the name "RED".

Return the result table in any order.

```mysql
with orders_with_red as (select o.sales_id
                         from orders o
                                  inner join company c
                                             on o.com_id = c.com_id
                         where c.name = 'RED')
select s.name
from SalesPerson s
         left join
     orders_with_red o
     on s.sales_id = o.sales_id
where o.sales_id is null;
```

# User Activity for the Past 30 Days I

```mysql
Create table If Not Exists Activity
(
    user_id       int,
    session_id    int,
    activity_date date,
    activity_type ENUM ('open_session', 'end_session', 'scroll_down', 'send_message')
);
Truncate table Activity;
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'scroll_down');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-20', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-21', 'send_message');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-21', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'send_message');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'end_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('4', '3', '2019-06-25', 'open_session');
insert into Activity (user_id, session_id, activity_date, activity_type)
values ('4', '3', '2019-06-25', 'end_session');
```

Table: Activity

```mysql
select t.activity_date           as day,
       count(distinct t.user_id) as active_users
from activity t
where datediff('2019-07-27', t.activity_date) >= 0
  and datediff('2019-07-27', t.activity_date) < 30
group by t.activity_date;
```

# 1693. Daily Leads and Partners

```mysql
Create table If Not Exists DailySales
(
    date_id    date,
    make_name  varchar(20),
    lead_id    int,
    partner_id int
);
Truncate table DailySales;
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'toyota', '0', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'toyota', '1', '0');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'toyota', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-7', 'toyota', '0', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-7', 'toyota', '0', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'honda', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-8', 'honda', '2', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-7', 'honda', '0', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-7', 'honda', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id)
values ('2020-12-7', 'honda', '2', '1');
```

Table: DailySales

```mysql
select t.date_id,
       t.make_name,
       count(distinct t.lead_id)    as unique_leads,
       count(distinct t.partner_id) as unique_partners
from DailySales t
group by t.date_id,
         t.make_name;
```

# 1729. Find Followers Count

```mysql
Create table If Not Exists Followers
(
    user_id     int,
    follower_id int
);
Truncate table Followers;
insert into Followers (user_id, follower_id)
values ('0', '1');
insert into Followers (user_id, follower_id)
values ('1', '0');
insert into Followers (user_id, follower_id)
values ('2', '0');
insert into Followers (user_id, follower_id)
values ('2', '1');
```

Table: Followers

```mysql
select t.user_id,
       count(t.user_id) as followers_count
from followers t
group by t.user_id
order by t.user_id;
```

# 586. Customer Placing the Largest Number of Orders

```mysql
Create table If Not Exists orders
(
    order_number    int,
    customer_number int
);
Truncate table orders;
insert into orders (order_number, customer_number)
values ('1', '1');
insert into orders (order_number, customer_number)
values ('2', '2');
insert into orders (order_number, customer_number)
values ('3', '3');
insert into orders (order_number, customer_number)
values ('4', '3');
```

Table: Orders

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

```mysql
select t.customer_number
from orders t
group by t.customer_number
order by count(*) desc
limit 1;
```

# 511. Game Play Analysis I

```mysql
Create table If Not Exists Activity
(
    player_id    int,
    device_id    int,
    event_date   date,
    games_played int
);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played)
values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '4', '2018-07-03', '5');
```

Table: Activity

Write an SQL query to report the first login date for each player.

Return the result table in any order.

```mysql
select t.player_id,
       min(t.event_date) as first_login
from activity t
group by t.player_id;
```

# 1890. The Latest Login in 2020

```mysql
Create table If Not Exists Logins
(
    user_id    int,
    time_stamp datetime
);
Truncate table Logins;
insert into Logins (user_id, time_stamp)
values ('6', '2020-06-30 15:06:07');
insert into Logins (user_id, time_stamp)
values ('6', '2021-04-21 14:06:06');
insert into Logins (user_id, time_stamp)
values ('6', '2019-03-07 00:18:15');
insert into Logins (user_id, time_stamp)
values ('8', '2020-02-01 05:10:53');
insert into Logins (user_id, time_stamp)
values ('8', '2020-12-30 00:46:50');
insert into Logins (user_id, time_stamp)
values ('2', '2020-01-16 02:49:50');
insert into Logins (user_id, time_stamp)
values ('2', '2019-08-25 07:59:08');
insert into Logins (user_id, time_stamp)
values ('14', '2019-07-14 09:00:00');
insert into Logins (user_id, time_stamp)
values ('14', '2021-01-06 11:59:59');
```

Table: Logins

Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login
in 2020.

Return the result table in any order.

```mysql
select t.user_id,
       max(t.time_stamp) as last_stamp
from logins t
where year(t.time_stamp) = 2020
group by user_id; 
```

# 1741. Find Total Time Spent by Each Employee

```mysql
Create table If Not Exists Employees
(
    emp_id    int,
    event_day date,
    in_time   int,
    out_time  int
);
Truncate table Employees;
insert into Employees (emp_id, event_day, in_time, out_time)
values ('1', '2020-11-28', '4', '32');
insert into Employees (emp_id, event_day, in_time, out_time)
values ('1', '2020-11-28', '55', '200');
insert into Employees (emp_id, event_day, in_time, out_time)
values ('1', '2020-12-3', '1', '42');
insert into Employees (emp_id, event_day, in_time, out_time)
values ('2', '2020-11-28', '3', '33');
insert into Employees (emp_id, event_day, in_time, out_time)
values ('2', '2020-12-9', '47', '74');
```

Table: Employees

Write an SQL query to calculate the total time in minutes spent by each employee on each day at the office. Note that
within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is
out_time - in_time.

Return the result table in any order.

```mysql
select t.event_day                 as day,
       t.emp_id,
       sum(t.out_time - t.in_time) as total_time
from employees t
group by t.emp_id,
         t.event_day;
```

# 1393. Capital Gain/Loss

```mysql
Create Table If Not Exists Stocks (stock_name varchar(15), operation ENUM('Sell', 'Buy'), operation_day int, price int);
Truncate table Stocks;
insert into Stocks (stock_name, operation, operation_day, price) values ('Leetcode', 'Buy', '1', '1000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '2', '10');
insert into Stocks (stock_name, operation, operation_day, price) values ('Leetcode', 'Sell', '5', '9000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Handbags', 'Buy', '17', '30000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '3', '1010');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '4', '1000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '5', '500');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Buy', '6', '1000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Handbags', 'Sell', '29', '7000');
insert into Stocks (stock_name, operation, operation_day, price) values ('Corona Masks', 'Sell', '10', '10000');
```

Write an SQL query to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

```mysql
select t.stock_name,
       sum(case when t.operation = 'Buy' then -t.price else t.price end) as capital_gain_loss
from stocks t
group by t.stock_name;
```

# 1407. Top Travellers

```mysql
Create Table If Not Exists Users (id int, name varchar(30));
Create Table If Not Exists Rides (id int, user_id int, distance int);
Truncate table Users;
insert into Users (id, name) values ('1', 'Alice');
insert into Users (id, name) values ('2', 'Bob');
insert into Users (id, name) values ('3', 'Alex');
insert into Users (id, name) values ('4', 'Donald');
insert into Users (id, name) values ('7', 'Lee');
insert into Users (id, name) values ('13', 'Jonathan');
insert into Users (id, name) values ('19', 'Elvis');
Truncate table Rides;
insert into Rides (id, user_id, distance) values ('1', '1', '120');
insert into Rides (id, user_id, distance) values ('2', '2', '317');
insert into Rides (id, user_id, distance) values ('3', '3', '222');
insert into Rides (id, user_id, distance) values ('4', '7', '100');
insert into Rides (id, user_id, distance) values ('5', '13', '312');
insert into Rides (id, user_id, distance) values ('6', '19', '50');
insert into Rides (id, user_id, distance) values ('7', '7', '120');
insert into Rides (id, user_id, distance) values ('8', '19', '400');
insert into Rides (id, user_id, distance) values ('9', '7', '230');
```

Table: Users

Table: Rides

Write an SQL query to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.


```mysql
select u.name,
       sum(case when r.distance is null then 0 else r.distance end) as travelled_distance
from users u
left outer join rides r
on u.id = r.user_id
group by r.user_id,
         u.name
order by travelled_distance desc,
         u.name;
```


# 1158. Market Analysis I

```mysql
Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10));
Create table If Not Exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int);
Create table If Not Exists Items (item_id int, item_brand varchar(10));
Truncate table Users;
insert into Users (user_id, join_date, favorite_brand) values ('1', '2018-01-01', 'Lenovo');
insert into Users (user_id, join_date, favorite_brand) values ('2', '2018-02-09', 'Samsung');
insert into Users (user_id, join_date, favorite_brand) values ('3', '2018-01-19', 'LG');
insert into Users (user_id, join_date, favorite_brand) values ('4', '2018-05-21', 'HP');
Truncate table Orders;
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2018-08-02', '2', '1', '3');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2018-08-04', '1', '4', '2');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2018-08-04', '1', '3', '4');
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4');
Truncate table Items;
insert into Items (item_id, item_brand) values ('1', 'Samsung');
insert into Items (item_id, item_brand) values ('2', 'Lenovo');
insert into Items (item_id, item_brand) values ('3', 'LG');
insert into Items (item_id, item_brand) values ('4', 'HP');
```

Table: Users

Table: Orders

Table: Items

Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.


```mysql
select t.user_id       as buyer_id,
       t.join_date,
       count(order_id) as orders_in_2019
from users t
         left outer join orders o
                         on t.user_id = o.buyer_id
                             and year(o.order_date) = 2019
group by t.user_id, t.join_date;
```

