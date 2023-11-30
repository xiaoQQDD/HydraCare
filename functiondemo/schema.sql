DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS dataset;

CREATE TABLE account (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE dataset (id integer,
gbprov text,
prov_ch text,
prov_en text,
gbcity text,
city_en text,
gbcounty text,
county_en text,
a100008_00 text,
a100008_10 text,
a100009_00 text,
a100009_10 text,
a101001_00 text,
a101001_10 text,
a101002_00 text,
a101002_10 text,
a101003_00 text,
a101003_10 text,
a101004_00 text,
a101004_10 text,
a101005_00 text,
a101005_10 text,
a101006_00 text,
a101006_10 text,
a103001_00 text,
a103001_10 text,
a104001_00 text,
a104001_10 text,
a104004_00 text,
a104004_10 text,
a104007_00 text,
a104007_10 text,
a104010_00 text,
a104010_10 text,
a105004_00 text,
a105004_10 text,
a105007_00 text,
a105007_10 text
);
