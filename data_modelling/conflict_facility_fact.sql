use database demo_db;
CREATE OR REPLACE TABLE conflict_facility_fact_v3 AS (
    WITH distance_time_calcoulator AS
             (
                 select conflicts.conflict_id,
                        facilities.facility_id,
                        conflicts.event_date,
                        to_number(left(conflicts.event_date, 2))         as day,
                        SUBSTRING(conflicts.event_date, 4,
                                  3)                                     as month_str,
                        CASE
                            WHEN trim(month_str) = 'Dec' THEN 12
                            WHEN trim(month_str) = 'Nov' THEN 11
                            WHEN trim(month_str) = 'Oct' THEN 10
                            WHEN trim(month_str) = 'Sep' THEN 9
                            WHEN trim(month_str) = 'Aug' THEN 8
                            WHEN trim(month_str) = 'July' THEN 7
                            WHEN trim(month_str) = 'Jun' THEN 6
                            WHEN trim(month_str) = 'May' THEN 5
                            WHEN trim(month_str) = 'Apr' THEN 4
                            WHEN trim(month_str) = 'Mar' THEN 3
                            WHEN trim(month_str) = 'Feb' THEN 2
                            WHEN trim(month_str) = 'Jan' THEN 1
                            END                                          AS month_code,

                        to_number(right(conflicts.event_date, 2)) + 2000 as year,
                        HAVERSINE(conflicts.latitude,
                                  conflicts.longitude,
                                  facilities.longitude,
                                  facilities.latitude)                   AS distance,
                        date(CONCAT(year, '-', month_code, '-', day))    AS conflict_date,
                        CASE
                            WHEN
                                SUB_EVENT_TYPE = 'Shelling/artillery/missile attack'
                                THEN 'sama'
                            WHEN
                                SUB_EVENT_TYPE = 'Armed clash'
                                THEN 'ar'
                            WHEN
                                SUB_EVENT_TYPE = 'Government regains territory'
                                THEN 'grt'
                            WHEN
                                SUB_EVENT_TYPE = 'Non-state actor overtakes territory'
                                THEN 'naot'
                            WHEN
                                SUB_EVENT_TYPE = 'Air/drone strike'
                                THEN 'air'
                            END                                          AS conflict_type

                 FROM raw_conflicts AS conflicts
                          join raw_facilities AS facilities
                 WHERE distance IS NOT NULL
             )
    SELECT conflict_id,
           facility_id,
           conflict_date,
           year,
           distance,
           conflict_type,
           IFF(distance < 1, TRUE, FALSE)  AS distance_1_km,
           IFF(distance < 3, TRUE, FALSE)  AS distance_3_km,
           IFF(distance < 5, TRUE, FALSE)  AS distance_5_km,
           IFF(distance < 10, TRUE, FALSE) AS distance_10_km
    FROM distance_time_calcoulator
    WHERE conflict_type IS not null
)