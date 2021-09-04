use database demo_db;
CREATE OR REPLACE TABLE conflict_facility_fact AS (
    WITH distance_time_calcoulator AS
             (
                 select conflicts.conflict_id,
                        facilities.facility_id,
                        conflicts.event_date,
                        to_number(left(conflicts.event_date, 2))      as day,
                        SUBSTRING(conflicts.event_date, 3,
                                  length(conflicts.event_date) - 7)   as month_str,
                        CASE
                            WHEN trim(month_str) = 'December' THEN 12
                            WHEN trim(month_str) = 'November' THEN 11
                            WHEN trim(month_str) = 'October' THEN 10
                            WHEN trim(month_str) = 'September' THEN 9
                            WHEN trim(month_str) = 'August' THEN 8
                            WHEN trim(month_str) = 'July' THEN 7
                            WHEN trim(month_str) = 'June' THEN 6
                            WHEN trim(month_str) = 'May' THEN 5
                            WHEN trim(month_str) = 'April' THEN 4
                            WHEN trim(month_str) = 'March' THEN 3
                            WHEN trim(month_str) = 'February' THEN 2
                            WHEN trim(month_str) = 'January' THEN 1
                            END                                       AS month_code,

                        to_number(right(conflicts.event_date, 4))     as year,
                        to_number(HAVERSINE(conflicts.latitude, conflicts.longitude,
                                            facilities.longitude,
                                            facilities.latitude))     AS distance,
                        date(CONCAT(year, '-', month_code, '-', day)) AS conflict_date

                 FROM raw_conflicts AS conflicts
                          join raw_facilities AS facilities
                 WHERE distance IS NOT NULL
             )
    SELECT conflict_id,
           facility_id,
           conflict_date,
           distance,
           IFF(distance < 1, TRUE, FALSE)   AS distance_1_km,
           IFF(distance < 3, TRUE, FALSE)   AS distance_1_km,
           IFF(distance < 5, TRUE, FALSE)   AS distance_5_km,
           IFF(distance < 10, TRUE, FALSE)  AS distance_10_km,
    FROM distance_time_calcoulator
    );
