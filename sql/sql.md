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
Create table If Not Exists Employees (employee_id int, name varchar(30), salary int);
Truncate table Employees;
insert into Employees (employee_id, name, salary) values ('2', 'Meir', '3000');
insert into Employees (employee_id, name, salary) values ('3', 'Michael', '3800');
insert into Employees (employee_id, name, salary) values ('7', 'Addilyn', '7400');
insert into Employees (employee_id, name, salary) values ('8', 'Juan', '6100');
insert into Employees (employee_id, name, salary) values ('9', 'Kannon', '7700');
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
Create table If Not Exists Salary (id int, name varchar(100), sex char(1), salary int);
Truncate table Salary;
insert into Salary (id, name, sex, salary) values ('1', 'A', 'm', '2500');
insert into Salary (id, name, sex, salary) values ('2', 'B', 'f', '1500');
insert into Salary (id, name, sex, salary) values ('3', 'C', 'm', '5500');
insert into Salary (id, name, sex, salary) values ('4', 'D', 'f', '500');
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
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');
```

Table: Person

id is the primary key column for this table.

Each row of this table contains an email. The emails will not contain uppercase letters.

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

```mysql
delete p1
from person p1
         inner join person p2
                    on p1.email = p2.email and p1.id > p2.id;
```

# 1667. Fix Names in a Table

```mysql
Create table If Not Exists Users (user_id int, name varchar(40));
Truncate table Users;
insert into Users (user_id, name) values ('1', 'aLice');
insert into Users (user_id, name) values ('2', 'bOB');
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
Create table If Not Exists Activities (sell_date date, product varchar(20));
Truncate table Activities;
insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');
```

Table Activities:

There is no primary key for this table, it may contain duplicates.

Each row of this table contains the product name and the date it was sold in a market.


Write an SQL query to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

```mysql
select sell_date,
       count(distinct product) as num_sold,
       group_concat(distinct product order by product separator ',') as products
from activities
group by sell_date
order by sell_date;
```

# 1527. Patients With a Condition

```mysql
Create table If Not Exists Patients (patient_id int, patient_name varchar(30), conditions varchar(100));
Truncate table Patients;
insert into Patients (patient_id, patient_name, conditions) values ('1', 'Daniel', 'YFEV COUGH');
insert into Patients (patient_id, patient_name, conditions) values ('2', 'Alice', '');
insert into Patients (patient_id, patient_name, conditions) values ('3', 'Bob', 'DIAB100 MYOP');
insert into Patients (patient_id, patient_name, conditions) values ('4', 'George', 'ACNE DIAB100');
insert into Patients (patient_id, patient_name, conditions) values ('5', 'Alain', 'DIAB201');
```

patient_id is the primary key for this table.

'conditions' contains 0 or more code separated by spaces.

This table contains information of the patients in the hospital.

Write an SQL query to report the patient_id, patient_name and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

```mysql
select patient_id,
       patient_name,
       conditions
from patients
where (conditions like '% DIAB1%' or conditions like 'DIAB1%');
```

