select * from auth_group
select * from auth_group_permissions
select * from auth_permission
select * from auth_user
select * from auth_user_groups
select * from auth_user_user_permissions
select * from django_admin_log
select * from django_content_type
select * from django_migrations
select * from django_session
select * from store_category
select * from store_customer
select * from store_order where customer_id = 1 order by date_delivery DESC
select * from store_products


update store_order set status = 0 where id = 1

select O.id , C.first_name , C.last_name , O.quantity , P.name , O.price , O.address , O.phone , O.date, O.status
from store_order O , store_customer C , store_products P
where O.customer_id = C.id
and O.product_id = P.id
and O.status = 0


select O.id , C.first_name , C.last_name , O.quantity , P.name , O.price , O.address , O.date_delivery, O.status
from store_order O , store_customer C , store_products P
where O.customer_id = C.id
and O.product_id = P.id
group by first_name , date_delivery


select PRINTF("$%.2f", sum(quantity * price))  as Total , date_delivery , C.first_name , C.last_name , date_order
from store_order O , store_customer C
where status = 3
and O.customer_id = C.id
group by date_delivery , O.customer_id
order by date_delivery DESC


select * , substr(address,1,50)
from store_order
where id = 57

select address
from store_order
where id = 57