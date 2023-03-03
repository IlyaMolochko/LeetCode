# 1699. Number of Calls Between Two Persons

```mysql
Create table If Not Exists Calls (from_id int, to_id int, duration int);
Truncate table Calls;
insert into Calls (from_id, to_id, duration) values ('1', '2', '59');
insert into Calls (from_id, to_id, duration) values ('2', '1', '11');
insert into Calls (from_id, to_id, duration) values ('1', '3', '20');
insert into Calls (from_id, to_id, duration) values ('3', '4', '100');
insert into Calls (from_id, to_id, duration) values ('3', '4', '200');
insert into Calls (from_id, to_id, duration) values ('3', '4', '200');
insert into Calls (from_id, to_id, duration) values ('4', '3', '499');
```

Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

Return the result table in any order.


```mysql
select least(t.from_id, t.to_id) as person1,
       greatest(t.to_id, t.from_id) as person2,
       count(*) as call_count,
       sum(t.duration) as total_duration
from calls t
group by person1,
         person2
```

# 1251. Average Selling Price

```mysql
Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
Truncate table Prices;
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
Truncate table UnitsSold;
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');
```

Write an SQL query to find the average selling price for each product. average_price should be rounded to 2 decimal places.

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
Create table If Not Exists Warehouse (name varchar(50), product_id int, units int);
;
Create table If Not Exists Products (product_id int, product_name varchar(50), Width int,Length int,Height int);
Truncate table Warehouse;
insert into Warehouse (name, product_id, units) values ('LCHouse1', '1', '1');
insert into Warehouse (name, product_id, units) values ('LCHouse1', '2', '10');
insert into Warehouse (name, product_id, units) values ('LCHouse1', '3', '5');
insert into Warehouse (name, product_id, units) values ('LCHouse2', '1', '2');
insert into Warehouse (name, product_id, units) values ('LCHouse2', '2', '2');
insert into Warehouse (name, product_id, units) values ('LCHouse3', '4', '1');
Truncate table Products;
insert into Products (product_id, product_name, Width, Length, Height) values ('1', 'LC-TV', '5', '50', '40');
insert into Products (product_id, product_name, Width, Length, Height) values ('2', 'LC-KeyChain', '5', '5', '5');
insert into Products (product_id, product_name, Width, Length, Height) values ('3', 'LC-Phone', '2', '10', '10');
insert into Products (product_id, product_name, Width, Length, Height) values ('4', 'LC-T-Shirt', '4', '10', '20');
```

Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

Return the result table in any order.

```mysql
select w.name as warehouse_name,
       sum(w.units * p.width * p.length * p.height) as volume
from warehouse w
join products p
on w.product_id = p.product_id
group by warehouse_name
```

# 1445. Apples & Oranges

```mysql
Create table If Not Exists Sales (sale_date date, fruit ENUM('apples', 'oranges'), sold_num int);
Truncate table Sales;
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-01', 'apples', '10');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-01', 'oranges', '8');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-02', 'apples', '15');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-02', 'oranges', '15');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-03', 'apples', '20');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-03', 'oranges', '0');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-04', 'apples', '15');
insert into Sales (sale_date, fruit, sold_num) values ('2020-05-04', 'oranges', '16');
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

