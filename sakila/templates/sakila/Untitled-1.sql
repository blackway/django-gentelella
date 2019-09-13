SELECT "customer_list"."ID",
       "customer_list"."name",
       "customer_list"."address",
       "customer_list"."zip_code",
       "customer_list"."phone",
       "customer_list"."city",
       "customer_list"."country",
       "customer_list"."notes",
       "customer_list"."SID",
       ROW_NUMBER() OVER (PARTITION BY "customer_list"."SID" ORDER BY "customer_list"."ID" DESC) AS "row_number"
FROM "customer_list"
ORDER BY "row_number" ASC, "customer_list"."ID" ASC;

select t1.*
  from customer_list t1
 where 1=1
   and t1.id='604';


select * from staff;

select * from staff_list;



insert into "language-20190904-01"
select * from language;

-- auto-generated definition
create table language
(
    language_id integer  not null
        primary key autoincrement ,
    name        VARCHAR(20)  not null,
    last_update TIMESTAMP not null
);

select * from "language-20190904-01";


insert into "film_20190904-01"
select * from film;


ALTER TABLE film ADD CONSTRAINT fk_child_parent
                  FOREIGN KEY (parent_id)
                  REFERENCES parent(id);

-- auto-generated definition
create table film
(
    film_id              integer primary key autoincrement ,
    title                VARCHAR(255) not null,
    description          BLOB SUB_TYPE TEXT default NULL,
    release_year         VARCHAR(4)         default NULL,
    language_id          SMALLINT     not null
        constraint fk_film_language
            references language (language_id),
    original_language_id SMALLINT           default NULL
        constraint fk_film_language_original
            references language (language_id),
    rental_duration      SMALLINT           default 3 not null,
    rental_rate          DECIMAL(4, 2)      default 4.99 not null,
    length               SMALLINT           default NULL,
    replacement_cost     DECIMAL(5, 2)      default 19.99 not null,
    rating               VARCHAR(10)        default 'G',
    special_features     VARCHAR(100)       default NULL,
    last_update          TIMESTAMP    not null,
    constraint CHECK_special_features
        check (special_features is null or
               special_features like '%Trailers%' or
               special_features like '%Commentaries%' or
               special_features like '%Deleted Scenes%' or
               special_features like '%Behind the Scenes%'),
    constraint CHECK_special_rating
        check (rating in ('G', 'PG', 'PG-13', 'R', 'NC-17'))
);



create index idx_fk_language_id
    on film (language_id);

create index idx_fk_original_language_id
    on film (original_language_id);


select t1.*
  from "film_20190904-01" t1;





INSERT INTO "polls_question" ("question_text", "pub_date") VALUES ('test1', '2019-09-04 15:16:16');


drop table polls_choice;

-- auto-generated definition
create table polls_choice
(
    choice_id   integer      not null
        primary key autoincrement,
    choice_text varchar(200) not null,
    votes       integer      not null,
    question_id integer      not null
        references polls_question (question_id)
            deferrable initially deferred
);

create index polls_choice_question_id_c5b4b260
    on polls_choice (question_id);





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
FROM film
         INNER JOIN language ON ("film"."language_id" = "language"."language_id")
         INNER JOIN language T3 ON ("film"."original_language_id" = T3."language_id")
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
FROM film
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
FROM film
WHERE "film"."language_id" IN (1);

select count(0)
  from film t1 ;


select t1.*
  from polls_choice t1
  join polls_question t2 on t1.question_id = t2.question_id;