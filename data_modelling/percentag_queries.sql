SELECT
CLUSTER,
AVG(MIN_DISTANCE_AIRBORNE_2015 + MIN_DISTANCE_AIRBORNE_2016)AS avg_dist_air,
AVG(MIN_DISTANCE_GROUND_2015 + MIN_DISTANCE_GROUND_2016)AS avg_dist_ground

FROM "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
GROUP BY CLUSTER
ORDER BY CLUSTER;
---- facilities

select CLUSTER,
FACILITY_TYPE_MODELLED,
  CASE
                   when FACILITY_TYPE_MODELLED IN (1) THEN 'minor'
                   when FACILITY_TYPE_MODELLED IN (2) THEN 'medium'
                   when FACILITY_TYPE_MODELLED in (3) THEN 'major'
                   ELSE NULL
                   END    AS facility_type,
count(FACILITY_TYPE_MODELLED) * 100.0 / sum(count(FACILITY_TYPE_MODELLED)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER=7
group by CLUSTER,FACILITY_TYPE_MODELLED
order by CLUSTER,FACILITY_TYPE_MODELLED
------ urban
select CLUSTER,
urban,
count(urban) * 100.0 / sum(count(urban)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER=7
group by CLUSTER,urban
order by CLUSTER,urban
------ on_grid
select CLUSTER,
on_grid,
count(on_grid) * 100.0 / sum(count(on_grid)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER=7
group by CLUSTER,on_grid
order by CLUSTER,on_grid
---- min max for distances.f
SELECT
MIN (MIN_DISTANCE_AIRBORNE_2015),
MAX  (MIN_DISTANCE_AIRBORNE_2015),
MIN (MIN_DISTANCE_ground_2015),
MAX  (MIN_DISTANCE_ground_2016)

FROM "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where cluster=1
------ Solar_onl
select CLUSTER,
Solar_onl,
count(Solar_onl) * 100.0 / sum(count(Solar_onl)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER in (7)

group by CLUSTER,Solar_onl
order by CLUSTER
-------- Solar_inc
select CLUSTER,
Solar_inc,
count(Solar_inc) * 100.0 / sum(count(Solar_inc)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER in (7)

group by CLUSTER,Solar_inc
order by CLUSTER

-------- Diesel_onl
select CLUSTER,
Diesel_onl,
count(Diesel_onl) * 100.0 / sum(count(Solar_inc)) over()
from "DEMO_DB"."PUBLIC"."CLUSTERED_FACILITIES"
where CLUSTER in (7)

group by CLUSTER,Diesel_onl
order by CLUSTER