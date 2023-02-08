CREATE TABLE IF NOT EXISTS hh_api.clusters_employment_types 
(
    emp_id STRING,
    emp_name STRING,
    count INT64,
    insert_dt TIMESTAMP
);

CREATE TABLE IF NOT EXISTS hh_api.clusters_experience_groups 
(
    exp_id STRING,
    exp_name STRING,
    count INT64,
    insert_dt TIMESTAMP
);
