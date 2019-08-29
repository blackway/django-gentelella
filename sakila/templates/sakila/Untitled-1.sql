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

INSERT INTO "customer" ("customer_id", "store_id", "first_name", "last_name", "email", "address_id", "active",
                        "create_date", "last_update")
                        SELECT 601, 1, '1', '2', '3', 601, '', '2019-08-28 16:47:59.753593', '2019-08-28 16:47:59.753593';


select t1.customer_id
      ,t1.first_name
      ,t1.last_name
      ,t1.email
      ,t1.active
      ,t1.last_update
      ,t2.address
      ,t3.city
      ,t4.country
  from customer t1
  join address t2
    on t1.address_id = t2.address_id
   and t1.customer_id=599
  join city t3 on t2.city_id = t3.city_id
  join country t4 on t3.country_id = t4.country_id
  ;

-- select_related Customer.objects.filter(pk=599).select_related()
SELECT "customer"."customer_id",
       "customer"."store_id",
       "customer"."first_name",
       "customer"."last_name",
       "customer"."email",
       "customer"."address_id",
       "customer"."active",
       "customer"."create_date",
       "customer"."last_update",
       COUNT("payment"."payment_id")  AS "payment_count",
       ROUND(SUM("payment"."amount")) AS "total_amount",
       "store"."store_id",
       "store"."manager_staff_id",
       "store"."address_id",
       "store"."last_update",
       "country"."country_id",
       "country"."country",
       "country"."last_update",
       "address"."address_id",
       "address"."address",
       "address"."address2",
       "address"."district",
       "address"."city_id",
       "address"."postal_code",
       "address"."phone",
       "address"."last_update",
       "city"."city_id",
       "city"."city",
       "city"."country_id",
       "city"."last_update",
       T7."country_id",
       T7."country",
       T7."last_update"
FROM "customer"
         LEFT OUTER JOIN "payment" ON ("customer"."customer_id" = "payment"."customer_id")
         INNER JOIN "store" ON ("customer"."store_id" = "store"."store_id")
         INNER JOIN "country" ON ("store"."address_id" = "country"."country_id")
         INNER JOIN "address" ON ("customer"."address_id" = "address"."address_id")
         INNER JOIN "city" ON ("address"."city_id" = "city"."city_id")
         INNER JOIN "country" T7 ON ("city"."country_id" = T7."country_id")
WHERE "customer"."customer_id" = 599
GROUP BY "customer"."customer_id", "customer"."store_id", "customer"."first_name", "customer"."last_name",
         "customer"."email", "customer"."address_id", "customer"."active", "customer"."create_date",
         "customer"."last_update", "store"."store_id", "store"."manager_staff_id", "store"."address_id",
         "store"."last_update", "country"."country_id", "country"."country", "country"."last_update",
         "address"."address_id", "address"."address", "address"."address2", "address"."district", "address"."city_id",
         "address"."postal_code", "address"."phone", "address"."last_update", "city"."city_id", "city"."city",
         "city"."country_id", "city"."last_update", T7."country_id", T7."country", T7."last_update"
LIMIT 21;

-- prefetch_related Customer.objects.filter(pk=599).prefetch_related()
SELECT "customer"."create_date",
       "customer"."last_update",
       "customer"."customer_id",
       "customer"."store_id",
       "customer"."first_name",
       "customer"."last_name",
       "customer"."email",
       "customer"."address_id",
       "customer"."active",
       COUNT("payment"."payment_id")  AS "payment_count",
       ROUND(SUM("payment"."amount")) AS "total_amount"
FROM "customer"
         LEFT OUTER JOIN "payment" ON ("customer"."customer_id" = "payment"."customer_id")
WHERE "customer"."customer_id" = 599
GROUP BY "customer"."create_date", "customer"."last_update", "customer"."customer_id", "customer"."store_id",
         "customer"."first_name", "customer"."last_name", "customer"."email", "customer"."address_id",
         "customer"."active"
LIMIT 21;


-- Film.objects.select_related()
SELECT "film"."last_update",
       "film"."film_id",
       "film"."title",
       "film"."description",
       "film"."release_year",
       "film"."language_id",
       "film"."original_language_id",
       "film"."rental_duration",
       "film"."rental_rate",
       "film"."length",
       "film"."replacement_cost",
       "film"."rating",
       "film"."special_features",
       "language"."last_update",
       "language"."language_id",
       "language"."name",
       T3."last_update",
       T3."language_id",
       T3."name"
FROM "film"
         INNER JOIN "language" ON ("film"."language_id" = "language"."language_id")
         INNER JOIN "language" T3 ON ("film"."original_language_id" = T3."language_id")
LIMIT 21;


select t1.*
  from film t1
  join language t2 on t1.language_id = t2.language_id
  left join language t3 on t1.original_language_id = t3.language_id
--   join language t3 on t1.original_language_id = t3.language_id
;


-- Film.objects.prefetch_related()
SELECT "film"."last_update",
       "film"."film_id",
       "film"."title",
       "film"."description",
       "film"."release_year",
       "film"."language_id",
       "film"."original_language_id",
       "film"."rental_duration",
       "film"."rental_rate",
       "film"."length",
       "film"."replacement_cost",
       "film"."rating",
       "film"."special_features"
FROM "film"
LIMIT 21;

select t1.*
  from language t1
;

select t1.*
  from film t1
 where 1=1
   and t1.language_id <> 1
;


-- query = Language.objects.prefetch_related('film_set').get(id=1)
SELECT "film"."last_update",
       "film"."film_id",
       "film"."title",
       "film"."description",
       "film"."release_year",
       "film"."language_id",
       "film"."original_language_id",
       "film"."rental_duration",
       "film"."rental_rate",
       "film"."length",
       "film"."replacement_cost",
       "film"."rating",
       "film"."special_features"
FROM "film"
WHERE "film"."language_id" IN (1);

select count(0)
  from film t1 ;