CREATE OR REPLACE TABLE facilities(
   Facility_ID      INTEGER  NOT NULL PRIMARY KEY
  ,Gov_Code         INTEGER  NOT NULL
  ,Gouvernorat      VARCHAR(50) NOT NULL
  ,District         VARCHAR(50) NOT NULL
  ,Facility_Name_EN VARCHAR(55)
  ,Urban_Status     INTEGER
  ,Longitude        NUMERIC(11,8)
  ,latitude         NUMERIC(11,8)
  ,Facility_Type    VARCHAR(2) NOT NULL
  ,Owenership       INTEGER
  ,Finance_Source   INTEGER
  ,Partner_Support  INTEGER
  ,temp_permenant   INTEGER
  ,Planned_Grid     INTEGER
  ,Off_Grid         INTEGER
  ,Electy_Access    Boolean
  ,Electy_Source    VARCHAR(3) NOT NULL
  ,Conflict_2016    VARCHAR(30)
  ,Conflict_2015    VARCHAR(30)
  ,on_grid_avl      Boolean
);