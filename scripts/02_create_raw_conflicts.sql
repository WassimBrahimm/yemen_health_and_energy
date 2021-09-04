USE DATABASE DEMO_DB;
CREATE OR REPLACE TABLE raw_conflicts(
   conflict_id    VARCHAR(8) NOT NULL PRIMARY KEY
  ,event_date     VARCHAR(15) NOT NULL
  ,year           INTEGER  NOT NULL
  ,time_precision INTEGER  NOT NULL
  ,event_type     VARCHAR(50) NOT NULL
  ,sub_event_type VARCHAR(100) NOT NULL
  ,actor1         VARCHAR(100) NOT NULL
  ,assoc_actor_1  VARCHAR(300)
  ,inter1         INTEGER  NOT NULL
  ,actor2         VARCHAR(100)
  ,assoc_actor_2  VARCHAR(300)
  ,inter2         INTEGER  NOT NULL
  ,interaction    INTEGER  NOT NULL
  ,region         VARCHAR(20) NOT NULL
  ,country        VARCHAR(10) NOT NULL
  ,admin1         VARCHAR(30) NOT NULL
  ,admin2         VARCHAR(50) NOT NULL
  ,admin3         VARCHAR(50)
  ,location       VARCHAR(70) NOT NULL
  ,latitude       NUMERIC(7,4) NOT NULL
  ,longitude      NUMERIC(7,4) NOT NULL
  ,geo_precision  INTEGER  NOT NULL
  ,source         VARCHAR(200) NOT NULL
  ,source_scale   VARCHAR(50) NOT NULL
  ,notes          VARCHAR(2000) NOT NULL
  ,fatalities     INTEGER  NOT NULL
  ,timestamp      INTEGER  NOT NULL
  ,iso3           VARCHAR(5) NOT NULL
);