use database demo_db;
CREATE
    OR REPLACE TABLE regression_data_version_one AS (
    WITH airborne_2015 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_airborne_2015
                 FROM conflict_facility_fact
                 WHERE conflict_type = 'airborne'
                   AND year = 2015
                 GROUP BY facility_id
             ),

         airborne_2016 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_airborne_2016
                 FROM conflict_facility_fact
                 WHERE conflict_type = 'airborne'
                   AND year = 2016
                 GROUP BY facility_id
             ),
         ground_2015 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_ground_2015
                 FROM conflict_facility_fact
                 WHERE conflict_type = 'ground'
                   AND year = 2015
                 GROUP BY facility_id
             ),

         ground_2016 AS
             (
                 SELECT facility_id,
                        MIN(distance) AS min_distance_ground_2016
                 FROM conflict_facility_fact
                 WHERE conflict_type = 'ground'
                   AND year = 2016
                 GROUP BY facility_id
             )
    SELECT fact.facility_id,
           airborne_2015.min_distance_airborne_2015,
           airborne_2016.min_distance_airborne_2016,
           ground_2015.min_distance_ground_2015,
           ground_2016.min_distance_ground_2016
    FROM "DEMO_DB"."PUBLIC"."RAW_FACILITIES" AS fact
             LEFT JOIN airborne_2015 ON
        fact.facility_id = airborne_2015.facility_id
             LEFT JOIN airborne_2016 ON
        fact.facility_id = airborne_2016.facility_id
             LEFT JOIN ground_2015 ON
        fact.facility_id = ground_2015.facility_id
             LEFT JOIN ground_2016 ON
        fact.facility_id = ground_2016.facility_id
    WHERE fact.latitude IS NOT NULL
ORDER BY facility_id DESC
);
