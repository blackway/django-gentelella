select t1.customer_id
      ,max(t1.first_name) as first_name
      ,max(t1.last_name) as last_name
      ,round(sum(t2.amount), 2) as amount
 from customer t1
 join payment t2
   on t1.customer_id = t2.customer_id
group by t1.customer_id
;

select count(0)
  from (
        select t1.customer_id
              ,max(t1.first_name) as first_name
              ,max(t1.last_name) as last_name
              ,round(sum(t2.amount), 2) as amount
         from customer t1
         join payment t2
           on t1.customer_id = t2.customer_id
        group by t1.customer_id
           )
;