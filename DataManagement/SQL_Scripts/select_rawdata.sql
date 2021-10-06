SELECT id , position, val
FROM IRCSP.rawdata 
WHERE wavelength = 8 AND camera = 1 AND 110 <= position AND position <= 125;