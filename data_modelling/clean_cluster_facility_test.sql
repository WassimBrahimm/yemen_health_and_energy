create or replace table clean_cluster_facility_test AS
    (
        SELECT on_grid_avl,
               IFF(URBAN = 'urban', TRUE, FALSE) AS urban,
               on_grid,
               solar_onl,
               diesel_onl,
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
        FROM raw_facilities_clustering
        WHERE latitude IS NOT NULL
          AND FACILITY_TYPE_MODELLED In (1, 2, 3)
    );
