# 1699. Number of Calls Between Two Persons

```mysql
Create table If Not Exists Calls
(
    from_id  int,
    to_id    int,
    duration int
);
Truncate table Calls;
insert into Calls (from_id, to_id, duration)
values ('1', '2', '59');
insert into Calls (from_id, to_id, duration)
values ('2', '1', '11');
insert into Calls (from_id, to_id, duration)
values ('1', '3', '20');
insert into Calls (from_id, to_id, duration)
values ('3', '4', '100');
insert into Calls (from_id, to_id, duration)
values ('3', '4', '200');
insert into Calls (from_id, to_id, duration)
values ('3', '4', '200');
insert into Calls (from_id, to_id, duration)
values ('4', '3', '499');
```

Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (
person1, person2) where person1 < person2.

Return the result table in any order.

```mysql
select least(t.from_id, t.to_id)    as person1,
       greatest(t.to_id, t.from_id) as person2,
       count(*)                     as call_count,
       sum(t.duration)              as total_duration
from calls t
group by person1,
         person2
```

# 1251. Average Selling Price

```mysql
Create table If Not Exists Prices
(
    product_id int,
    start_date date,
    end_date   date,
    price      int
);
Create table If Not Exists UnitsSold
(
    product_id    int,
    purchase_date date,
    units         int
);
Truncate table Prices;
insert into Prices (product_id, start_date, end_date, price)
values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price)
values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price)
values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price)
values ('2', '2019-02-21', '2019-03-31', '30');
Truncate table UnitsSold;
insert into UnitsSold (product_id, purchase_date, units)
values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units)
values ('1', '2019-03-01', '15');
insert into UnitsSold (product_id, purchase_date, units)
values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units)
values ('2', '2019-03-22', '30');
```

Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal
places.

Return the result table in any order.

```mysql
select p.product_id,
       round(sum(p.price * u.units) / sum(u.units), 2) as average_price
from prices p
         join unitssold u on p.product_id = u.product_id
    and u.purchase_date between p.start_date and p.end_date
group by p.product_id
```

# 1571. Warehouse Manager

```mysql
Create table If Not Exists Warehouse
(
    name       varchar(50),
    product_id int,
    units      int
);
;
Create table If Not Exists Products
(
    product_id   int,
    product_name varchar(50),
    Width        int,
    Length       int,
    Height       int
);
Truncate table Warehouse;
insert into Warehouse (name, product_id, units)
values ('LCHouse1', '1', '1');
insert into Warehouse (name, product_id, units)
values ('LCHouse1', '2', '10');
insert into Warehouse (name, product_id, units)
values ('LCHouse1', '3', '5');
insert into Warehouse (name, product_id, units)
values ('LCHouse2', '1', '2');
insert into Warehouse (name, product_id, units)
values ('LCHouse2', '2', '2');
insert into Warehouse (name, product_id, units)
values ('LCHouse3', '4', '1');
Truncate table Products;
insert into Products (product_id, product_name, Width, Length, Height)
values ('1', 'LC-TV', '5', '50', '40');
insert into Products (product_id, product_name, Width, Length, Height)
values ('2', 'LC-KeyChain', '5', '5', '5');
insert into Products (product_id, product_name, Width, Length, Height)
values ('3', 'LC-Phone', '2', '10', '10');
insert into Products (product_id, product_name, Width, Length, Height)
values ('4', 'LC-T-Shirt', '4', '10', '20');
```

Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.

```mysql
select w.name                                       as warehouse_name,
       sum(w.units * p.width * p.length * p.height) as volume
from warehouse w
         join products p
              on w.product_id = p.product_id
group by warehouse_name
```

# 1445. Apples & Oranges

```mysql
Create table If Not Exists Sales
(
    sale_date date,
    fruit     ENUM ('apples', 'oranges'),
    sold_num  int
);
Truncate table Sales;
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-01', 'apples', '10');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-01', 'oranges', '8');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-02', 'apples', '15');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-02', 'oranges', '15');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-03', 'apples', '20');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-03', 'oranges', '0');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-04', 'apples', '15');
insert into Sales (sale_date, fruit, sold_num)
values ('2020-05-04', 'oranges', '16');
```

Write an SQL query to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.

```mysql
select t.sale_date,
       sum(case when t.fruit = 'apples' then t.sold_num else -t.sold_num end) as diff
from sales t
group by t.sale_date
order by t.sale_date;
```

# 1193. Monthly Transactions I

```mysql
Create table If Not Exists Transactions
(
    id         int,
    country    varchar(4),
    state      enum ('approved', 'declined'),
    amount     int,
    trans_date date
);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date)
values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date)
values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date)
values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date)
values ('124', 'DE', 'approved', '2000', '2019-01-07');
```

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of
approved transactions and their total amount.

Return the result table in any order.

```mysql
select date_format(date(t.trans_date), '%Y-%m')                     as month,
       t.country,
       count(*)                                                     as trans_count,
       sum(case when t.state = 'approved' then 1 else 0 end)        as approved_count,
       sum(t.amount)                                                as trans_total_amount,
       sum(case when t.state = 'approved' then t.amount else 0 end) as approved_total_amount
from transactions t
group by month,
         t.country
```

# 1633. Percentage of Users Attended a Contest

```mysql
Create table If Not Exists Users
(
    user_id   int,
    user_name varchar(20)
);
Create table If Not Exists Register
(
    contest_id int,
    user_id    int
);
Truncate table Users;
insert into Users (user_id, user_name)
values ('6', 'Alice');
insert into Users (user_id, user_name)
values ('2', 'Bob');
insert into Users (user_id, user_name)
values ('7', 'Alex');
Truncate table Register;
insert into Register (contest_id, user_id)
values ('215', '6');
insert into Register (contest_id, user_id)
values ('209', '2');
insert into Register (contest_id, user_id)
values ('208', '2');
insert into Register (contest_id, user_id)
values ('210', '6');
insert into Register (contest_id, user_id)
values ('208', '6');
insert into Register (contest_id, user_id)
values ('209', '7');
insert into Register (contest_id, user_id)
values ('209', '6');
insert into Register (contest_id, user_id)
values ('215', '7');
insert into Register (contest_id, user_id)
values ('208', '7');
insert into Register (contest_id, user_id)
values ('210', '2');
insert into Register (contest_id, user_id)
values ('207', '2');
insert into Register (contest_id, user_id)
values ('210', '7');
```

Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending
order.

```mysql
with cnt as (select count(*) as cnt
             from users t)
select r.contest_id,
       round(count(r.user_id) / c.cnt * 100, 2) as percentage
from register r
         join cnt c
group by r.contest_id
order by percentage desc,
         contest_id
```

# 1173. Immediate Food Delivery I

```mysql
Create table If Not Exists Delivery
(
    delivery_id                 int,
    customer_id                 int,
    order_date                  date,
    customer_pref_delivery_date date
);
Truncate table Delivery;
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('1', '1', '2019-08-01', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('2', '5', '2019-08-02', '2019-08-02');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('3', '1', '2019-08-11', '2019-08-11');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('4', '3', '2019-08-24', '2019-08-26');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('5', '4', '2019-08-21', '2019-08-22');
insert into Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
values ('6', '2', '2019-08-11', '2019-08-13');
```

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise,
it is called scheduled.

Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

```mysql
with all_orders_count as (select count(*) as cnt
                          from delivery t)
select round(sum(case when t.order_date = t.customer_pref_delivery_date then 1 else 0 end) / c.cnt * 100,
             2) as immediate_percentage
from delivery t
         join all_orders_count c
```

# 1211. Queries Quality and Percentage

```mysql
Create table If Not Exists Queries
(
    query_name varchar(30),
    result     varchar(50),
    position   int,
    rating     int
);
Truncate table Queries;
insert into Queries (query_name, result, position, rating)
values ('Dog', 'Golden Retriever', '1', '5');
insert into Queries (query_name, result, position, rating)
values ('Dog', 'German Shepherd', '2', '5');
insert into Queries (query_name, result, position, rating)
values ('Dog', 'Mule', '200', '1');
insert into Queries (query_name, result, position, rating)
values ('Cat', 'Shirazi', '5', '2');
insert into Queries (query_name, result, position, rating)
values ('Cat', 'Siamese', '3', '3');
insert into Queries (query_name, result, position, rating)
values ('Cat', 'Sphynx', '7', '4');
```

We define query quality as:

> The average of the ratio between query rating and its position.

We also define poor query percentage as:

> The percentage of all queries with rating less than 3.

Write an SQL query to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

```mysql
select t.query_name,
       round(sum(t.rating / t.position) / count(*), 2)                          as quality,
       round(sum(case when t.rating < 3 then 1 else 0 end) / count(*) * 100, 2) as poor_query_percentage
from queries t
group by t.query_name;
```

# 1607. Sellers With No Sales

```mysql
Create table If Not Exists Customer
(
    customer_id   int,
    customer_name varchar(20)
);
Create table If Not Exists Orders
(
    order_id    int,
    sale_date   date,
    order_cost  int,
    customer_id int,
    seller_id   int
);
;
Create table If Not Exists Seller
(
    seller_id   int,
    seller_name varchar(20)
);
;
Truncate table Customer;
insert into Customer (customer_id, customer_name)
values ('101', 'Alice');
insert into Customer (customer_id, customer_name)
values ('102', 'Bob');
insert into Customer (customer_id, customer_name)
values ('103', 'Charlie');
Truncate table Orders;
insert into Orders (order_id, sale_date, order_cost, customer_id, seller_id)
values ('1', '2020-03-01', '1500', '101', '1');
insert into Orders (order_id, sale_date, order_cost, customer_id, seller_id)
values ('2', '2020-05-25', '2400', '102', '2');
insert into Orders (order_id, sale_date, order_cost, customer_id, seller_id)
values ('3', '2019-05-25', '800', '101', '3');
insert into Orders (order_id, sale_date, order_cost, customer_id, seller_id)
values ('4', '2020-09-13', '1000', '103', '2');
insert into Orders (order_id, sale_date, order_cost, customer_id, seller_id)
values ('5', '2019-02-11', '700', '101', '2');
Truncate table Seller;
insert into Seller (seller_id, seller_name)
values ('1', 'Daniel');
insert into Seller (seller_id, seller_name)
values ('2', 'Elizabeth');
insert into Seller (seller_id, seller_name)
values ('3', 'Frank');
```

Write an SQL query to report the names of all sellers who did not make any sales in 2020.

Return the result table ordered by seller_name in ascending order.

```mysql
select t.seller_name
from seller t
where t.seller_id not in
      (select t.seller_id
       from orders t
       where t.sale_date between '2020-01-01' and '2020-12-31')
order by t.seller_name;
```

# 619. Biggest Single Number

```mysql
Create table If Not Exists MyNumbers
(
    num int
);
Truncate table MyNumbers;
insert into MyNumbers (num)
values ('8');
insert into MyNumbers (num)
values ('8');
insert into MyNumbers (num)
values ('3');
insert into MyNumbers (num)
values ('3');
insert into MyNumbers (num)
values ('1');
insert into MyNumbers (num)
values ('4');
insert into MyNumbers (num)
values ('5');
insert into MyNumbers (num)
values ('6');
```

A single number is a number that appeared only once in the MyNumbers table.

Write an SQL query to report the largest single number. If there is no single number, report null.

```mysql
select max(t.num) as num
from (select t.num
      from mynumbers t
      group by t.num
      having count(t.num) = 1) t
```

# 1112. Highest Grade For Each Student

```mysql
Create table If Not Exists Enrollments
(
    student_id int,
    course_id  int,
    grade      int
);
Truncate table Enrollments;
insert into Enrollments (student_id, course_id, grade)
values ('2', '2', '95');
insert into Enrollments (student_id, course_id, grade)
values ('2', '3', '95');
insert into Enrollments (student_id, course_id, grade)
values ('1', '1', '90');
insert into Enrollments (student_id, course_id, grade)
values ('1', '2', '99');
insert into Enrollments (student_id, course_id, grade)
values ('3', '1', '80');
insert into Enrollments (student_id, course_id, grade)
values ('3', '2', '75');
insert into Enrollments (student_id, course_id, grade)
values ('3', '3', '82');
```

Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should
find the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

```mysql
with max_grade as (select t.student_id,
                          max(t.grade) as grade
                   from enrollments t
                   group by t.student_id)
select t.student_id,
       min(t.course_id) as course_id,
       t.grade
from enrollments t
         join max_grade g
              on t.student_id = g.student_id and t.grade = g.grade
group by t.student_id,
         t.grade
order by t.student_id
```

# 1398. Customers Who Bought Products A and B but Not C

```mysql
Create table If Not Exists Customers
(
    customer_id   int,
    customer_name varchar(30)
);
Create table If Not Exists Orders
(
    order_id     int,
    customer_id  int,
    product_name varchar(30)
);
Truncate table Customers;
insert into Customers (customer_id, customer_name)
values ('1', 'Daniel');
insert into Customers (customer_id, customer_name)
values ('2', 'Diana');
insert into Customers (customer_id, customer_name)
values ('3', 'Elizabeth');
insert into Customers (customer_id, customer_name)
values ('4', 'Jhon');
Truncate table Orders;
insert into Orders (order_id, customer_id, product_name)
values ('10', '1', 'A');
insert into Orders (order_id, customer_id, product_name)
values ('20', '1', 'B');
insert into Orders (order_id, customer_id, product_name)
values ('30', '1', 'D');
insert into Orders (order_id, customer_id, product_name)
values ('40', '1', 'C');
insert into Orders (order_id, customer_id, product_name)
values ('50', '2', 'A');
insert into Orders (order_id, customer_id, product_name)
values ('60', '3', 'A');
insert into Orders (order_id, customer_id, product_name)
values ('70', '3', 'B');
insert into Orders (order_id, customer_id, product_name)
values ('80', '3', 'D');
insert into Orders (order_id, customer_id, product_name)
values ('90', '4', 'C');
```

Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy
the product "C" since we want to recommend them to purchase this product.

Return the result table ordered by customer_id.

```mysql
select t.customer_id,
       t.customer_name
from customers t
         join orders o
              on t.customer_id = o.customer_id
group by t.customer_id,
         t.customer_name
having sum(case when o.product_name = 'A' then 1 else 0 end) > 0
   and sum(case when o.product_name = 'B' then 1 else 0 end) > 0
   and sum(case when o.product_name = 'C' then 1 else 0 end) = 0
order by t.customer_id
```

# 1440. Evaluate Boolean Expression

```mysql
Create Table If Not Exists Variables (name varchar(3), value int);
Create Table If Not Exists Expressions (left_operand varchar(3), operator ENUM('>', '<', '='), right_operand varchar(3));
Truncate table Variables;
insert into Variables (name, value) values ('x', '66');
insert into Variables (name, value) values ('y', '77');
Truncate table Expressions;
insert into Expressions (left_operand, operator, right_operand) values ('x', '>', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('x', '<', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('y', '>', 'x');
insert into Expressions (left_operand, operator, right_operand) values ('y', '<', 'x');
insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'x');
```

Write an SQL query to evaluate the boolean expressions in Expressions table.

Return the result table in any order.

```mysql
select t.left_operand,
       t.operator,
       t.right_operand,
       (case
            when t.operator = '=' and lft.value = rht.value then 'true'
            when t.operator = '>=' and lft.value >= rht.value then 'true'
            when t.operator = '<=' and lft.value <= rht.value then 'true'
            when t.operator = '>' and lft.value > rht.value then 'true'
            when t.operator = '<' and lft.value < rht.value then 'true'
            else 'false' end) as value
from expressions t
         join variables lft
              on t.left_operand = lft.name
         join variables rht
              on t.right_operand = rht.name;
```

# 1264. Page Recommendations

```mysql
Create table If Not Exists Friendship (user1_id int, user2_id int);
Create table If Not Exists Likes (user_id int, page_id int);
Truncate table Friendship;
insert into Friendship (user1_id, user2_id) values ('1', '2');
insert into Friendship (user1_id, user2_id) values ('1', '3');
insert into Friendship (user1_id, user2_id) values ('1', '4');
insert into Friendship (user1_id, user2_id) values ('2', '3');
insert into Friendship (user1_id, user2_id) values ('2', '4');
insert into Friendship (user1_id, user2_id) values ('2', '5');
insert into Friendship (user1_id, user2_id) values ('6', '1');
Truncate table Likes;
insert into Likes (user_id, page_id) values ('1', '88');
insert into Likes (user_id, page_id) values ('2', '23');
insert into Likes (user_id, page_id) values ('3', '24');
insert into Likes (user_id, page_id) values ('4', '56');
insert into Likes (user_id, page_id) values ('5', '11');
insert into Likes (user_id, page_id) values ('6', '33');
insert into Likes (user_id, page_id) values ('2', '77');
insert into Likes (user_id, page_id) values ('3', '77');
insert into Likes (user_id, page_id) values ('6', '88');
```

Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.

Return result table in any order without duplicates.

```mysql
with friends as (select t.user2_id as friend_id
                 from friendship t
                 where t.user1_id = 1
                 union
                 select t.user1_id as friend_id
                 from friendship t
                 where t.user2_id = 1),
     user1_likes as (select t.page_id
                     from likes t
                     where t.user_id = 1),
     others_likes as (select t.user_id,
                             t.page_id
                      from likes t
                      where t.user_id <> 1)
select distinct t.page_id as recommended_page
from others_likes t
         join friends f
              on t.user_id = f.friend_id
where t.page_id not in (select *
                        from user1_likes t)
```

# 570. Managers with at Least 5 Direct Reports

```mysql
Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
Truncate table Employee;
insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', 'None');
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
```

Write an SQL query to report the managers with at least five direct reports.

Return the result table in any order.

```mysql
select t.name
from employee t
where t.id in (select e.managerId
               from employee e
               group by e.managerId
               having count(e.managerId) >= 5)
```

# 1303. Find the Team Size

```mysql
Create table If Not Exists Employee (employee_id int, team_id int);
Truncate table Employee;
insert into Employee (employee_id, team_id) values ('1', '8');
insert into Employee (employee_id, team_id) values ('2', '8');
insert into Employee (employee_id, team_id) values ('3', '8');
insert into Employee (employee_id, team_id) values ('4', '7');
insert into Employee (employee_id, team_id) values ('5', '9');
insert into Employee (employee_id, team_id) values ('6', '9');
```

Write an SQL query to find the team size of each of the employees.

Return result table in any order.

```mysql
select t.employee_id,
       e.team_size
from employee t
         join
     (select t.team_id,
             count(t.team_id) as team_size
      from employee t
      group by t.team_id) e
     on t.team_id = e.team_id
```

# 1280. Students and Examinations

```mysql
Create table If Not Exists Students (student_id int, student_name varchar(20));
Create table If Not Exists Subjects (subject_name varchar(20));
Create table If Not Exists Examinations (student_id int, subject_name varchar(20));
Truncate table Students;
insert into Students (student_id, student_name) values ('1', 'Alice');
insert into Students (student_id, student_name) values ('2', 'Bob');
insert into Students (student_id, student_name) values ('13', 'John');
insert into Students (student_id, student_name) values ('6', 'Alex');
Truncate table Subjects;
insert into Subjects (subject_name) values ('Math');
insert into Subjects (subject_name) values ('Physics');
insert into Subjects (subject_name) values ('Programming');
Truncate table Examinations;
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Programming');
insert into Examinations (student_id, subject_name) values ('2', 'Programming');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Programming');
insert into Examinations (student_id, subject_name) values ('13', 'Physics');
insert into Examinations (student_id, subject_name) values ('2', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
```

Write an SQL query to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

```mysql
select
    s.student_id,
    s.student_name,
    t.subject_name,
    count(e.subject_name) as attended_exams
from students s
join subjects t
left join examinations e
on s.student_id = e.student_id
and t.subject_name = e.subject_name
group by s.student_id, 
         t.subject_name
order by s.student_id,
         t.subject_name;
```

# 184. Department Highest Salary

```mysql
Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');
```

Write an SQL query to find employees who have the highest salary in each of the departments.

Return the result table in any order.

```mysql
with max_salary as (select max(t.salary) as salary,
                           t.departmentid
                    from employee t
                    group by departmentid)
select d.name as department,
       e.name as employee,
       e.salary
from employee e
         join max_salary t
              on e.departmentid = t.departmentid
                  and e.salary = t.salary
         join department d
              on d.id = e.departmentid;
```

# 580. Count Student Number in Departments

```mysql
Create table If Not Exists Student (student_id int,student_name varchar(45), gender varchar(6), dept_id int);
Create table If Not Exists Department (dept_id int, dept_name varchar(255));
Truncate table Student;
insert into Student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2');
Truncate table Department;
insert into Department (dept_id, dept_name) values ('1', 'Engineering');
insert into Department (dept_id, dept_name) values ('2', 'Science');
insert into Department (dept_id, dept_name) values ('3', 'Law');
```

Write an SQL query to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

```mysql
select d.dept_name,
       count(s.student_id) as student_number
from department d
         left join student s
                   on d.dept_id = s.dept_id
group by d.dept_name
order by student_number desc,
         d.dept_name;
```
