Select email from Person group by email having count(email) > 1;

select email from
(
select email, count(email) as num from person group by email
) as statistic
where num > 1
;
