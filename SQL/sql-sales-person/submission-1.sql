-- Write your query below
select name from sales_person
where sales_person.sales_id not in
(select sales_id from orders where com_id=(select com_id from company where company.name='CRIMSON'))