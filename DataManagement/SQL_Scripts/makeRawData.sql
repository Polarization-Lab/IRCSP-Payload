CREATE TABLE IRCSP.rawdata (
  id     INTEGER, 
  camera	  INTEGER,
  wavelength  FLOAT, 
  position FLOAT,
  err   INT,
  val  FLOAT,
  FOREIGN KEY(id) REFERENCES Measurements(meas_id)
);