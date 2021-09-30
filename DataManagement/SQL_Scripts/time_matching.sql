create TABLE IRCSP.Measurements
select m.meas_id, m.time, m.cam1_temp,m.cam2_temp, t.hous_temp, t.humidity, t.pressure
from IRCSP.cameraLog m
left join IRCSP.log t on t.time= (
  select max(t2i.time)
  from IRCSP.log t2i
  where t2i.time <= m.time
)