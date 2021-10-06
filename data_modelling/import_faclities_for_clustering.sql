-- create raw_facilities_clustering
use database demo_db;
CREATE OR REPLACE TABLE raw_facilities_clustering(
   Key_Code                   VARCHAR(30) NOT NULL PRIMARY KEY
  ,Key                        INTEGER  NOT NULL
  ,Gov_Code                   INTEGER  NOT NULL
  ,Gov                        VARCHAR(50) NOT NULL
  ,Dis_Code                   INTEGER  NOT NULL
  ,District                   VARCHAR(50) NOT NULL
  ,facility_id                INTEGER  NOT NULL
  ,Facility_Name_EN           VARCHAR(100)
  ,North                      VARCHAR(9)
  ,East                       VARCHAR(9)
  ,Longitude                  VARCHAR(17)
  ,latitude                   VARCHAR(17)
  ,Elevation                  INTEGER
  ,Facility_Type              VARCHAR(6) NOT NULL
  ,Owenership                 INTEGER
  ,Finance_Source             INTEGER
  ,Partner_Support            INTEGER
  ,TempPermnt                 INTEGER
  ,T                          boolean
  ,Planned_Grid               INTEGER
  ,OffGrid                    INTEGER
  ,Electy_Access              boolean  NOT NULL
  ,Electy_Source              VARCHAR(3) NOT NULL
  ,Conflict_2016              boolean  NOT NULL
  ,Past_Conflict15            boolean  NOT NULL
  ,No_Conflict                boolean
  ,on_grid_avl                boolean  NOT NULL
  ,min_distance_airborne_2015 NUMERIC(13,10)
  ,min_distance_airborne_2016 NUMERIC(13,10)
  ,min_distance_ground_2015   NUMERIC(13,10)
  ,min_distance_ground_2016   NUMERIC(12,9)
  ,min_distance_2015          NUMERIC(13,10)
  ,min_distance_2016          NUMERIC(13,10)
  ,min_distance_sama_2015     NUMERIC(13,10)
  ,min_distance_sama_2016     NUMERIC(12,9)
  ,min_distance_ar_2015       NUMERIC(12,9)
  ,min_distance_ar_2016       NUMERIC(12,9)
  ,min_distance_naot_2015     NUMERIC(12,9)
  ,min_distance_naot_2016     NUMERIC(12,9)
  ,min_distance_grt_2015      NUMERIC(12,9)
  ,min_distance_grt_2016      NUMERIC(12,9)
  ,min_distance_air_2015      NUMERIC(13,10)
  ,min_distance_air_2016      NUMERIC(13,10)
  ,urban                      VARCHAR(5)
  ,on_grid                    boolean  NOT NULL
  ,on_grid_eff_supp           boolean  NOT NULL
  ,ea                         boolean  NOT NULL
  ,solar_inc                  boolean  NOT NULL
  ,solar_onl                  boolean  NOT NULL
  ,diesel_inc                 boolean  NOT NULL
  ,diesel_onl                 boolean  NOT NULL
  ,hybrid                     boolean  NOT NULL
  ,factype                    VARCHAR(20)
);
-- create file format
ALTER FILE FORMAT "DEMO_DB"."PUBLIC".load_csv SET COMPRESSION = 'NONE' FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n'
SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '\042' TRIM_SPACE = TRUE ERROR_ON_COLUMN_COUNT_MISMATCH =
TRUE ESCAPE = 'NONE' ESCAPE_UNENCLOSED_FIELD = '\134' DATE_FORMAT = 'AUTO' TIMESTAMP_FORMAT = 'AUTO' NULL_IF = ('');