
CREATE TABLE IRCSP.log (
  meas_id INT PRIMARY KEY,
  hous_temp FLOAT NOT NULL,
  cam1_temp FLOAT NOT NULL,
  cam2_temp FLOAT NOT NULL,
  pressure FLOAT NOT NULL,
  altitude FLOAT ,
  epoch_time FLOAT NOT NULL,
  time DATETIME,
  humidity FLOAT NOT NULL,
  accceleration FLOAT NOT NULL
  );