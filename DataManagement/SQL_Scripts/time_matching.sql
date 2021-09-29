CREATE TABLE joint_telemetry select m.meas_id, m.time, m.cam1_temp,m.cam2_temp, t.hous_temp, t.humidity, t.pressure
from measurements m
left join telemetry t on t.time= (
  select max(t2i.time)
  from telemetry t2i
  where t2i.time <= m.time
)