CREATE TABLE date_ (
	d_datekey          INTEGER,
	d_date             TEXT ENCODING DICT(32),
	d_dayofweek        TEXT ENCODING DICT(8),
	d_month            TEXT ENCODING DICT(8),
	d_year             SMALLINT,
	d_yearmonthnum     INTEGER,
	d_yearmonth        TEXT ENCODING DICT(16),
	d_daynuminweek     SMALLINT,
	d_daynuminmonth    SMALLINT,
	d_daynuminyear     SMALLINT,
	d_monthnuminyear   SMALLINT,
	d_weeknuminyear    SMALLINT,
	d_sellingseason    TEXT ENCODING DICT(8),
	d_lastdayinweekfl  SMALLINT,
	d_lastdayinmonthfl SMALLINT,
	d_holidayfl        SMALLINT,
	d_weekdayfl        SMALLINT
);

CREATE TABLE supplier (
	s_suppkey INTEGER,
	s_name    TEXT ENCODING DICT(32),
	s_address TEXT ENCODING DICT(32),
	s_city    TEXT ENCODING DICT(16),
	s_nation  TEXT ENCODING DICT(8),
	s_region  TEXT ENCODING DICT(8),
	s_phone   TEXT ENCODING DICT(32)
);

CREATE TABLE customer (
	c_custkey    INTEGER,
	c_name       TEXT ENCODING DICT(32),
	c_address    TEXT ENCODING DICT(32),
	c_city       TEXT ENCODING DICT(16),
	c_nation     TEXT ENCODING DICT(8),
	c_region     TEXT ENCODING DICT(8),
	c_phone      TEXT ENCODING DICT(32),
	c_mktsegment TEXT ENCODING DICT(8)
);

CREATE TABLE part (
	p_partkey   INTEGER,
	p_name      TEXT ENCODING DICT(32),
	p_mfgr      TEXT ENCODING DICT(8),
	p_category  TEXT ENCODING DICT(8),
	p_brand1    TEXT ENCODING DICT(16),
	p_color     TEXT ENCODING DICT(8),
	p_type      TEXT ENCODING DICT(8),
	p_size      TEXT ENCODING DICT(8),
	p_container TEXT ENCODING DICT(8)
);

CREATE TABLE lineorder (
	lo_orderkey      INTEGER,
	lo_linenumber    INTEGER,
	lo_custkey       INTEGER,
	lo_partkey       INTEGER,
	lo_suppkey       INTEGER,
	lo_orderdate     INTEGER,
	lo_orderpriority TEXT ENCODING DICT(8),
	lo_shippriority  TEXT ENCODING DICT(8),
	lo_quantity      INTEGER,
	lo_extendedprice INTEGER,
	lo_ordtotalprice INTEGER,
	lo_discount      INTEGER,
	lo_revenue       INTEGER,
	lo_supplycost    INTEGER,
	lo_tax           INTEGER,
	lo_commitdate    INTEGER,
	lo_shipmode      TEXT ENCODING DICT(8)
);

