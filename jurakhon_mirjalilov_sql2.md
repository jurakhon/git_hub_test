
-- ### Task 1 - CREATE
-- Create tables: Employees, Departments, Locations, Jobs. 
--  - Employees: id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commision_pct, department_id.
--  - Departments: id, department_name, manager_name, location_id.
--  - Locations: id, city, region, street_address.
--  - Jobs: id, title, is_active.

--  Realationships:
--  - one to one: Departments with Locations
--  - one to many: Departments with Employees
--  - one to many: Jobs with Employees
create table Employees(
	id serial primary key,
	first_name varchar(100),
	last_name varchar(100),
	phone_number varchar(20),
	hire_date date,
	salary numeric,
	commission_pct numeric,
	department_id int references Departments(id),
	job_id int references Jobs(id)
)

create table Departments(
	id serial primary key,
	department_name varchar(250),
	manager_name varchar(150),
	location_id int references Locations(id)
)

create table Locations(
	id serial primary key,
	city varchar(100),
	region varchar(100),
	street_address varchar(250)
)

create table Jobs(
	id serial primary key,
	title varchar(150),
	is_active boolean default False
)

drop table jobs
drop table employees
drop table departments
drop table locations

-- ### Task 2 - INSERT
--  - INSEERT 5 JOBS - backend, frontend, fullstack, designer, manager.
insert into jobs(title, is_active) values
('backend', True),
('frontend', True),
('fullstack', True),
('designer', True),
('manager', True)
--  - INSERT 3 DEPARTMENTS - management, accountant, development
insert into departments(department_name, manager_name) values
('management', 'alijon kurbonov'),
('accountant', 'muhammad boronov'),
('development', 'sunnatullo ibragimov')
--  - INSERT 5 LOCATION - any location
insert into locations(city, region, street_address) values
('dushanbe', 'sino', 'bobojon gafurov st n5'),
('khujand', 'rudaki', 'khujand st n33'),
('bokhtar', 'region5', 'somoni st n76'),
('kulob', 'sino', 'ahmad donish st n7'),
('dushanbe', 'sino2', 'gissarskaya st n15')
--  - INSERT 10 EMPLOYEES:
--     - 3 employees must be managers of each department
--     - 5 employees must be developers 
--     - 2 employees must be accountants
insert into Employees(first_name, last_name, phone_number, hire_date, salary, commission_pct, department_id) values
('abdullo', 'kurbonov','+992919112243', '2023-06-19', 1200, 10, 1),
('najmiddin', 'vohidov','+992919112883', '2020-06-19', 1700, 10, 1),
('sunnat', 'jalilov','+992919112113', '2019-06-19', 1800, 10, 1),
('alijon', 'jumaev','+992919112243', '2018-06-19', 3000, 10, 3),
('kurbon', 'nuriddinov','+992919112224', '2015-04-13', 2000, 10, 3),
('kamoliddin', 'valiev','+992919114433', '2023-06-10', 4000, 10, 3),
('umedjon', 'alizoda','+992919113433', '2021-08-22', 3700, 10, 3),
('bedil', 'tojiev','+992919112233', '2021-02-19', 1900, 10, 3),
('vohidjon', 'murodov','+9929194312233', '2024-02-19', 1600, 10, 2),
('murodjon', 'sayfiddinov','+992879112233', '2022-06-19', 1500, 10, 2)


-- ### Task 3 ALTER
--     a) Add a column to store employee birthdate (Добавьте столбец для хранения даты рождения сотрудника)
alter table employees
add birthdate date

--     b) Change the data type of phone_number in employees to allow more characters (Измените тип данных phone_number в employees, чтобы разрешить больше символов)
alter table Employees
alter column phone_number type varchar(50)

--     c) Rename the commission_pct column to commission_percentage in employees(Переименуйте столбец commission_pct в commission_percentage в employees)
alter table Employees
rename column commission_pct to commission_percentage
--     d) Add a unique constraint on the email column in employees if it wasn't defined before (Добавьте уникальное ограничение для столбца email в employees, если оно не было определено ранее)
alter table Employees
add unique (phone_number) -- syntax hamin. dar tablitsa email pur nakardiyam, baroi hamin phone_num kati kor kardam.
--     e) Modify the is_active column in the jobs table to default to TRUE (Измените столбец is_active в таблице jobs, чтобы значение по умолчанию было TRUE)
alter table jobs
alter table is_active
set default TRUE

-- ### Task 4 SELECT
--     a) Filter all departments located in 'New York' (Отфильтровать все отделы, расположенные в «Нью-Йорке»)
select * from locations where city = 'dushanbe'
--     b) Filter all employees hired after January 1, 2022 (Отфильтровать всех сотрудников, нанятых после 1 января 2022 г.)
select * from employees where hire_date > '2022-01-01'
--     c) Filter employees whose email ends with '@example.com' (Отфильтровать сотрудников, чей адрес электронной почты заканчивается на «@example.com»)
select * from employees where email like '%example.com'
--     d) Filter jobs where the title contains the word 'Manager' (Отфильтровать вакансии, в названии которых содержится слово «Менеджер»)
select * from jobs where title like '%manager%'
--     e) Filter employees who do not belong to the departments with ids 2 and 4 (Отфильтровать сотрудников, которые не относятся к отделам с идентификаторами 2 и 4)
select * from employees where department_id not = 2 or department_id not = 4
select * from employees
where department_id not in (2, 4)
--     f) Filter employees with a salary between 4000 and 8000 (Отфильтровать сотрудников с зарплатой от 4000 до 8000)
select * from employees where salary between 4000 and 8000



-- ### Task 5 JOIN
--     a) Retrieve all employees along with their department names (Получить всех сотрудников вместе с названиями их отделов)
select e.*, d.department_name
from Employees e
join Departments d on e.department_id = d.id
--     b) Retrieve all employees, their department names, and the location city (Получить всех сотрудников, названия их отделов и город расположения)
select e.*, d.department_name, l.city
from Employees e
join Departments d on e.department_id = d.id
join Locations l on d.location_id = l.id
--     d) Retrieve all departments and their managers' names (include departments without managers) (Получить все отделы и имена их менеджеров (включая отделы без менеджеров))
--     e) Retrieve all employees and their departments, including employees without departments and departments without employees (Получить всех сотрудников и их отделы, включая сотрудников без отделов и отделы без сотрудников)
select e.*, d.department_name
from Employees e
full join Departments d on e.department_id = d.id

--     f) Retrieve employees who work in the 'Sales' department along with their job titles (Получить сотрудников, которые работают в отделе «Продажи», вместе с их должностями)
--     g) Retrieve the number of employees in each department (Получить количество сотрудников в каждом отделе)
select d.department_name, count(e.id) as employee_count
from Departments d
left join Employees e ON d.id = e.department_id
groub by d.department_name
--     h) Retrieve employees whose salary is higher than the average salary of their department (Получить сотрудников, чья зарплата выше средней зарплаты их отдела)
