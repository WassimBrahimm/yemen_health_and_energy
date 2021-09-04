CREATE TABLE raw_facilities(
   Gov              VARCHAR(19) NOT NULL PRIMARY KEY
  ,District         VARCHAR(20) NOT NULL
  ,Facility_ID      INTEGER  NOT NULL
  ,Facility_Name_EN VARCHAR(55)
  ,Urban_Status     VARCHAR(4) NOT NULL
  ,North            VARCHAR(9)
  ,East             VARCHAR(9)
  ,Longitude        NUMERIC(11,8)
  ,latitude         NUMERIC(11,8)
  ,Elevation        INTEGER
  ,Facility_Type    VARCHAR(6) NOT NULL
  ,On_Grid          BOOLEAN  NOT NULL
  ,hybrid           BOOLEAN  NOT NULL
  ,elec_access      BOOLEAN  NOT NULL
  ,solar_inc        BOOLEAN  NOT NULL
  ,solar_onl        BOOLEAN  NOT NULL
  ,diesel           BOOLEAN  NOT NULL
);