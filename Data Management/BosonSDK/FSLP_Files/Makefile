
# WARNINGS = -Wall
WARNINGS = 
CC = gcc
CCwin64 = tcc

CFLAGS= -I./src/inc

OBJDIR = obj

COMMON_DEPS = FSLP.h flirCRC.h flirChannels.h serialPortAdapter.h timeoutLogic.h 
COMMON_OBJBASE = flirCRC FSLP flirChannels  timeoutLogic


#update these input filenames if replaced for target hardware. 
LINUX_SERIAL = serial.c
WIN32_SERIAL = FLIR_Win32_Serial.c


#existence only dependency on the object directory
#ensures output directory exists before any of the .o files are created.
#make sure any added dependencies occur before the "|" symbol
ALLDEPS = $(patsubst %,src/inc/%,$(COMMON_DEPS)) | $(OBJDIR)

ALLOBJ32 = $(patsubst %,$(OBJDIR)/%_32.o,$(COMMON_OBJBASE))
ALLOBJ64 = $(patsubst %,$(OBJDIR)/%_64.o,$(COMMON_OBJBASE))
ALLOBJ32_LINUX = $(patsubst %,$(OBJDIR)/%_Linux32.o,$(COMMON_OBJBASE))
ALLOBJ64_LINUX = $(patsubst %,$(OBJDIR)/%_Linux64.o,$(COMMON_OBJBASE))

OSNAME := $(shell uname)
ifeq ($(OSNAME),Windows_NT)
	RM=del /S
	target = FSLP_64.dll
else ifeq ($(OSNAME),Linux)
	RM=rm -f
	target =  FSLP_64.so
else
#probably cygwin
	RM=rm -f
	target = FSLP_64.dll
endif

all:
	make $(target) 

$(OBJDIR):
	mkdir obj

obj/%_32.o: src/%.c  $(ALLDEPS)
	$(CC) $(WARNINGS) -c -o $@ $< $(CFLAGS)

obj/%_64.o: src/%.c  $(ALLDEPS)
	$(CCwin64) -v -c -o $@ $< $(CFLAGS)

obj/%_Linux32.o: src/%.c  $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m32 -c -o $@ $< $(CFLAGS)

obj/%_Linux64.o: src/%.c  $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m64 -c -o $@ $< $(CFLAGS)

obj/%_32.o: src/win32/serialPortAdapter.c  $(ALLDEPS)
	$(CC) $(WARNINGS) -c -o $@ $< $(CFLAGS)

obj/%_64.o: src/win32/serialPortAdapter.c  $(ALLDEPS)
	$(CCwin64) -v -c -o $@ $< $(CFLAGS)

obj/%_Linux32.o: src/linux/serialPortAdapter.c   $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m32 -c -o $@ $< $(CFLAGS)

obj/%_Linux64.o: src/linux/serialPortAdapter.c  $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m64 -c -o $@ $< $(CFLAGS)

obj/serialPort_32.o: src/win32/$(WIN32_SERIAL)  $(ALLDEPS)
#	$(error "Windows library still under development")
	$(CC) $(WARNINGS) -c -o $@ $< $(CFLAGS)

obj/serialPort_64.o: src/win32/$(WIN32_SERIAL)  $(ALLDEPS)
#	$(error "Windows library still under development")
	$(CCwin64) -v -c -o $@ $< $(CFLAGS)

obj/serialPort_Linux32.o: src/linux/$(LINUX_SERIAL)  $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m32 -c -o $@ $< $(CFLAGS)

# used to need this added when accidental namespace collision existed
#-Derror=weird_name_to_resolve_name_conflict_error
obj/serialPort_Linux64.o: src/linux/$(LINUX_SERIAL) $(ALLDEPS)
	$(CC) -g -fPIC $(WARNINGS) -shared -m64 -c -o $@ $< $(CFLAGS) 
	

FSLP_32.dll: $(ALLOBJ32) obj/serialPort_32.o obj/serialPortAdapter_32.o
	$(CC) $(WARNINGS) -static-libgcc -shared -o $@ $^ 

FSLP_64.dll: $(ALLOBJ64) obj/serialPort_64.o  obj/serialPortAdapter_64.o
	$(CCwin64) -v -shared -m64 -o $@ $^ 

FSLP_32.so: $(ALLOBJ32_LINUX) obj/serialPort_Linux32.o obj/serialPortAdapter_Linux32.o
	$(CC) -g -fPIC $(WARNINGS) -shared -m32 -o $@ $^ 

FSLP_64.so: $(ALLOBJ64_LINUX) obj/serialPort_Linux64.o obj/serialPortAdapter_Linux64.o
	$(CC) -g -fPIC $(WARNINGS) -shared -m64 -o $@ $^ 

.PHONY: clean
clean:
	$(RM) obj/*.o

.PHONY: clean_fslp32
clean_fslp32:
	$(RM) FSLP_32.*

.PHONY: clean_fslp64
clean_fslp64:
	$(RM) FSLP_64.*

.PHONY: clean_all
clean_all : clean clean_fslp64 clean_fslp32
