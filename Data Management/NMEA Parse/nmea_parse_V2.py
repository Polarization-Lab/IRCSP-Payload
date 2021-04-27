'''
Program: nmea_parse.py
Author: Eduardo D Contreras
Date: 01/30/2021
Class: ENGR498 - Design of Payload for near-space deployment of IR Optics
Project Sponsors: Kira Hart & Meredith Kupinski

Mentor: Catherine Merrill

Team Members: Nayleth Ramirez, Jeremy Parkinson, Jaclyn John, Thor Niel, Wassim Khawam

Description: The program is designed to automate the appending of GPS NMEA data into
approximately 2,160 HDF5 files that will be created and stored during the flight mission.

The program when executed searches for all HDF5 file types in the current working directory,
opens a HDF5 file, retrieves the in-flight file creation timestamp stored in the HDF5 file,
opens the GPS NMEA Data text file created in-flight, parses only the ($GPGGA & $GPRMC) message
types/lines in the text file, retrieves a timestamp from the ($GPGGA & $GPRMC) message types/lines,
compares both timestamps with each other and only writes the GPS NMEA Data to the HDF5 file for
the timestamps that are exact matches with each other.

'''

import os, datetime
import h5py


def os_timestamp(filename):
    """os_timestamp(): Function currently reads the filename and retrieves the Operating
                System timestamp attribute from the HDF5 file and returns it to be used
                in parse_nmea function. Designed to be a helper function for main.

    Parameters:
                filename - the filename of the HDF5 file.


    Returns: Operating System timestamp. String literal. ex. Hours & Minutes (18:21)
    """

    with h5py.File(filename, "a") as h5:
        return h5.attrs["OS_time"]


def increment_time(os_time):
    """increment_time(): Function will increment the OS_time by one minute. Function designed
                as a helper function for error handling purposes.

    Parameters:
                filename - the filename of the HDF5 file.


    Returns: Operating System timestamp. String literal. ex. Hours & Minutes (18:21)
    """

    os_time_obj = datetime.datetime.strptime(os_time, "%H:%M") + datetime.timedelta(minutes=1)
    return os_time_obj.strftime("%H:%M")



def parse_nmea(filename, os_time, gps_data):
    """parse_nmea(): Function currently searches for message lines containing $GPRMC & $GPGGA
                in the text file, appends them into a list and extracts a timestamp to create a
                Dictionary key with the message line data as the value pair. The function compares
                the HDF5 timestamp with the Dictionary keys, if match is found, it will write message
                line data found in the matching Dictionary value to the currently open HDF5 file.
                The function will increment the timestamp until a timestamp match exist with the
                Dictionary keys.

    Parameters:
                filename - HDF5 File created during flight.
                os_time - file creation timestamp stored in HDF5 file during flight.
                gps_data - GPS NMEA message data from text file.


    Returns: None. Appends NMEA Messages to Existing - HDF5 File in current working directory.
    """
    #Time/Speed Test - Start
    start = datetime.datetime.now()

    #Lists to Store GPS Message Types From Text File
    GPRMC_list = []
    GPGGA_list = []
    GPRMC_result = []
    GPGGA_result = []

    #Read the Message Lines in Text File.
    lines = gps_data.readlines()

    #Find Message Lines That Startwith $GPRMC & $GPGGA, Append to Lists
    for message in lines:
        if message.startswith("$GPRMC"):
            GPRMC_list.append(message)

        if message.startswith("$GPGGA"):
            GPGGA_list.append(message)

    #Split the Messages in GPRMC list to create time variable
    gprmc_dict = {}
    for gprmc_lines in GPRMC_list:
        gprmc_split = gprmc_lines.split(",")
        gprmc_time = gprmc_split[1][0:2] + ':' + gprmc_split[1][2:4]
        #Set GPS Time as Key in dictionary with message as the pair value.
        gprmc_dict[gprmc_time] = gprmc_lines

    #Match key value pairs in GPRMC GPS NMEA Dictionary
    if os_time not in gprmc_dict.keys():
        new_time1 = increment_time(os_time)
        while new_time1 not in gprmc_dict.keys():
            new_time1 = increment_time(new_time1)
        else:
            GPRMC_result.append(gprmc_dict[new_time1])
    else:
        GPRMC_result.append(gprmc_dict[os_time])


    #Split the Messages in GPGGA list to create time variable
    gpgga_dict = {}
    for gpgga_lines in GPGGA_list:
        gpgga_split = gpgga_lines.split(",")
        gpgga_time = gpgga_split[1][0:2] + ':' + gpgga_split[1][2:4]
        # Set GPS Time as Key in dictionary with message as the pair value.
        gpgga_dict[gpgga_time] = gpgga_lines

    #Match key value pairs in GPGGA GPS NMEA Dictionary
    if os_time not in gpgga_dict.keys():
        new_time2 = increment_time(os_time)
        while new_time2 not in gpgga_dict.keys():
            new_time2 = increment_time(new_time2)
        else:
            GPGGA_result.append(gpgga_dict[new_time2])
    else:
        GPGGA_result.append(gpgga_dict[os_time])



    #Split Message to Extract Data Values & Create Variables
    for gprmc_data in GPRMC_result:
        gprmc_split = gprmc_data.split(",")

    #Create Variables for GPS $GPRMC Data Values
    #nmea_type2 = gprmc_split[0]
    gprmc_timestamp = gprmc_split[1][0:2] + ':' + gprmc_split[1][2:4]
    gprmc_latitude = gprmc_split[3] + ", " + gprmc_split[4] #Latittude Direction in N/S
    gprmc_longitude = gprmc_split[5] + ", " + gprmc_split[6] #Longitute Direction in E/W
    gprmc_speed = gprmc_split[7] # Speed in Knots
    gprmc_date = gprmc_split[9][2:4] + '/' + gprmc_split[9][0:2] + '/' + gprmc_split[9][4:6]



    #Split Message to Extract Data Values & Create Variables
    for gpgga_data in GPGGA_result:
        gpgga_split = gpgga_data.split(",")


    #Create Variables for GPS $GPGGA Data Values
    gpgga_timestamp = gpgga_split[1][0:2] + ':' + gpgga_split[1][2:4]
    gpgga_latitude = gpgga_split[2] + ", " + gpgga_split[3] # Latittude Direction in N/S
    gpgga_longitude = gpgga_split[4] + ", " + gpgga_split[5]  # Longitute Direction in E/W
    gpgga_altitude = gpgga_split[9]  # Altitude Above Sea-Level in Meters



    #Append NMEA Messages to Existing - HDF5 File
    with h5py.File(filename, "a") as h5: # Open as Read-Write ("a" - creates file if doesn't exist)
        h5["$GPGGA/Time"] = gpgga_timestamp
        h5["$GPGGA/Latitude"] = gpgga_latitude
        h5["$GPGGA/Longitude"] = gpgga_longitude
        h5["$GPGGA/Sea_Level"] = gpgga_altitude


        h5["$GPRMC/Date"] = gprmc_date
        h5["$GPRMC/Time"] = gprmc_timestamp
        h5["$GPRMC/Latitude"] = gprmc_latitude
        h5["$GPRMC/Longitude"] = gprmc_longitude
        h5["$GPRMC/Speed"] = gprmc_speed










    #Time/Speed Test - Finish
    finish = datetime.datetime.now()
    print(filename, "Data Appending Completed:", finish - start)


#==========================================================
def main():
    '''
    Main function currently executes a print statement which shows files in the current working directory.
    Utilized for cross-reference to ensure both Python program & GPS NMEA text file exist in same directory.
    Opens up text file and executes parse_nmea function.
    '''

    #Check Current Working Directory (cwd)
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print()
    print("Directory Path %r: \n" % (cwd))
    print("List of File Names: %s \n" % (files))

    #Set to works on .hdf5 file type extension.
    for filename in files:
        #Modify the endswith portion with another file type extension, if necessary.
        if filename.endswith(".hdf5"):
            os_time = os_timestamp(filename)
            #Provide ACTUAL file name of text file below which contains GPS NMEA data.
            with open('GPS_Test_DATA.txt', "r") as gps_data:
                parse_nmea(filename, os_time, gps_data)



if __name__ == '__main__':
    main()


