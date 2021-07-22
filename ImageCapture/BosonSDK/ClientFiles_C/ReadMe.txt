do_build.bat is an extremely simple makefile replacement.
You will need to copy the appropriate DLL and .def file from ../Emulator_Files into this directory to build the example correctly.
Line 11 of Example.c will need to be updated to match whatever serial port number your OS assigns the boson.
See http://www.teuniz.net/RS-232/ for more details on how the serial ports are enumerated.