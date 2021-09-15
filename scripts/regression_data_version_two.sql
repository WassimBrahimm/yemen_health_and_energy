use database demo_db;
CREATE
    OR REPLACE TABLE regression_data_version_two AS (
    WITH attacks_2015 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_2015
                 FROM conflict_facility_fact_version_2
                   WHERE year = 2015
                 GROUP BY facility_id
             ),

         attacks_2016 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_2016
                 FROM conflict_facility_fact_version_2
                   WHERE year = 2016
                 GROUP BY facility_id
             )
    SELECT fact.facility_id,
           round(attacks_2015.min_distance_2015, 3) AS min_distance_2015,
           round(attacks_2016.min_distance_2016, 3) AS min_distance_2016
    FROM "DEMO_DB"."PUBLIC"."RAW_FACILITIES" AS fact
             LEFT JOIN attacks_2015 ON
        fact.facility_id = attacks_2015.facility_id
             LEFT JOIN attacks_2016 ON
        fact.facility_id = attacks_2016.facility_id

    WHERE fact.latitude IS NOT NULL
ORDER BY facility_id DESC

);