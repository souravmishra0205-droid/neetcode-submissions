-- Write your query below
select name from sales_person
where not exists
(select 1 from orders 
join company
on company.com_id = orders.com_id
where orders.sales_id = sales_person.sales_id and company.name = 'CRIMSON'
)