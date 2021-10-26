create
or replace table "DEMO_DB"."PUBLIC"."CLEAN_CLUSTER_FACILITY_TEST" AS
    (
        SELECT
      FACILITY_ID,
      on_grid_avl,
               IFF(URBAN = 'urban', TRUE, FALSE) AS urban,
               on_grid,
               solar_onl,
               diesel_onl,
               SOLAR_INC,
               EA,
               DIESEL_inc,
               min_distance_airborne_2015,
               min_distance_airborne_2016,
               min_distance_ground_2015,
               min_distance_ground_2016,
               CASE
                   when FACILITY_TYPE IN ('minor') THEN 1
                   when FACILITY_TYPE IN ('medium') THEN 2
                   when FACILITY_TYPE in ('major') THEN 3
                   ELSE NULL
                   END                           as FACILITY_TYPE_MODELLED
        FROM "DEMO_DB"."PUBLIC"."RAW_FACILITIES_CLUSTERING"
        WHERE latitude IS NOT NULL
          AND FACILITY_TYPE_MODELLED In (1, 2, 3)
    );
