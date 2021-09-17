create or replace table clean_cluster_facility AS
    (
        SELECT
--            facility_id,
Electy_Access,
--            Electy_Source,
on_grid_avl,
IFF(URBAN = 'urban', TRUE, FALSE) AS urban,
on_grid,
--            on_grid_eff_supp,-- ???
ea,
solar_inc,
solar_onl,
diesel_inc,
diesel_onl,
hybrid,
min_distance_airborne_2015,
min_distance_airborne_2016,
min_distance_ground_2015,
min_distance_ground_2016,
CASE
      when FACILITY_TYPE='' THEN 1
      when FACILITY_TYPE='medium' THEN 2
      when FACILITY_TYPE='' THEN 3
      ELSE NULL
      END as FACILITY_TYPE
        FROM raw_facilities_clustering
        WHERE latitude IS NOT NULL
      AND FACILITY_TYPE IS NOT NULL
    );
