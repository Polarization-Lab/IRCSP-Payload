# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:16:50 2019
@author: khart
"""
from Boson1.ClientFiles_Python import Client_API as pyClient
from Boson2.ClientFiles_Python import Client_API as pyClient2
import numpy as np
import sys
import time
from Cam1 import Camera1
from Cam2 import Camera2


def take_image(avg):
   
     
    cam1 = Camera1("COM5")
    cam2 = Camera2("COM6")

    try:
        cam1.make_port(cam1.port)
        cam2.make_port(cam2.port)
    except:
        print('Something opening camera port.')
        sys.exit(1)
    
    try:
        camSN = cam1.get_serial()
        print('Camera 1 serial number: '+str(camSN[1]))
        camSN2 = cam2.get_serial()
        print('Camera 2 serial number: '+str(camSN2[1]))
    except:
        print('Something wrong getting camera general info. Closing cam port and exiting...')
        cam1.close_port()
        cam2.close_port()
        sys.exit(2)



    """ CAMERA CONFIGURATION"""
    print('\n\n---START CAMERA CONFIGURATION---')
    
    #NUC filters
    #   Filters that are not configurable here: FFC, temperature Correction, SFFC
    gain = False
    bpr = False
    
    #Spatial and Temporal Filtering
    #   Filter that is not configurable here: SSN
    scnr = False
    tf = False
    spnr = False 
    
    #NUC Suite
    
    if gain == False:
        cam1.set_gain(pyClient.FLR_BOSON_GAINMODE_E.FLR_BOSON_LOW_GAIN)
        cam2.set_gain(pyClient2.FLR_BOSON_GAINMODE_E.FLR_BOSON_LOW_GAIN)
    else:
        cam1.set_gain(pyClient.FLR_BOSON_GAINMODE_E.FLR_BOSON_HIGH_GAIN)
        cam2.set_gain(pyClient2.FLR_BOSON_GAINMODE_E.FLR_BOSON_HIGH_GAIN)
    
    if bpr == False:
        cam1.set_bpr(pyClient.FLR_ENABLE_E.FLR_DISABLE)
        cam2.set_bpr(pyClient2.FLR_ENABLE_E.FLR_DISABLE)
    else:
        cam1.set_bpr(pyClient.FLR_ENABLE_E.FLR_ENABLE)
        cam2.set_bpr(pyClient2.FLR_ENABLE_E.FLR_ENABLE)
    
    
    try:
        gainState1 = cam1.get_gainState()
        bprState1 = cam1.get_bprState()
        
        gainState2 = cam2.get_gainState()
        bprState2 = cam2.get_bprState()
        
        
    except:
        print('Something wrong calling NUC correction states. Closing cam port and exiting...')
        cam1.close_port()
        cam2.close_port()
        sys.exit(3)
        
    
    #Spatial and temporal filtering Suite
    if scnr == False:
        cam1.set_scnr(pyClient.FLR_ENABLE_E.FLR_DISABLE)
        cam2.set_scnr(pyClient2.FLR_ENABLE_E.FLR_DISABLE)
    else:
        cam1.set_scnr(pyClient.FLR_ENABLE_E.FLR_ENABLE)
        cam2.set_scnr(pyClient2.FLR_ENABLE_E.FLR_ENABLE)
    
    if tf == False:
        cam1.set_tf(pyClient.FLR_ENABLE_E.FLR_DISABLE)
        cam2.set_tf(pyClient2.FLR_ENABLE_E.FLR_DISABLE)
    else:
        cam1.set_tf(pyClient.FLR_ENABLE_E.FLR_ENABLE)
        cam2.set_tf(pyClient2.FLR_ENABLE_E.FLR_ENABLE)
    
    if spnr == False:
        cam1.set_spnr(pyClient.FLR_ENABLE_E.FLR_DISABLE)
        cam2.set_spnr(pyClient2.FLR_ENABLE_E.FLR_DISABLE)
    else:
        cam1.set_spnr(pyClient.FLR_ENABLE_E.FLR_ENABLE)
        cam2.set_spnr(pyClient2.FLR_ENABLE_E.FLR_ENABLE)
    
    try:
        scnrState1 = cam1.get_scnrState()
        scnrMaxCorr1 = cam1.get_scnrMaxCorr()
        tfState1 = cam1.get_tfState()
        spnrState1 = cam1.get_spnrState()
        
        scnrState2 = cam2.get_scnrState()
        scnrMaxCorr2 = cam2.get_scnrMaxCorr()
        tfState2 = cam2.get_tfState()
        spnrState2 = cam2.get_spnrState()
        
    except:
        print('Something bad with calling spatial and temporal filtering states')
        cam1.close_port()
        cam2.close_port()
        sys.exit(1)



    """SET UP MASTER SLAVE"""
    
    mode1 = cam1.get_syncMode()
    mode2 = cam2.get_syncMode()
  
    cam1.set_asMaster()
    cam2.set_asSlave()
    
    
    mode1 = cam1.get_syncMode()
    mode2 = cam2.get_syncMode()
    
    """IMAGE ACQUISITION FOR CALIBRATION
        -timer functionality
        -save .tiff images
        -save .txt of raw and corrected FPA temps for each capture
    """
    
    startAll = time.perf_counter()
    loopsToRun =    avg
    secondsToWait = 10
    
    
    fpaTempCorr1 = np.zeros((loopsToRun,2))
    fpaTempCorr2 = np.zeros((loopsToRun,2))
    
    
    
    print('\n\n---START CAPTURES---\n')
    for n in range(loopsToRun):
        start = time.perf_counter()
    
   
    
        """Capture image (inferring AGC is off since gain state is fixed), dims now being read"""
        try:
            startIm = time.perf_counter()
        
            pyClient.captureSingleFrame()
            pyClient2.captureSingleFrame()
           
            print(str(startIm-start) + " seconds to execute both image commands")
            print('Cam 1: Finished Acquiring Image ' + str(n+1))
            print('Cam 2: Finished Acquiring Image ' + str(n+1))
            
        except Exception as e:
            print('Something went wrong during frame capture. Error code: {c}, Message, {m}'.format(c = type(e), m=str(e)))
            cam1.close_port()
            cam2.close_port()
            sys.exit(1)
            
            
            
        """Record FPA Temp"""
        fpaTempCorr1[n] = pyClient.bosonlookupFPATempDegCx10()
        fpaTempCorr2[n] = pyClient2.bosonlookupFPATempDegCx10()
        print('\nFPA Temp: ' + str(fpaTempCorr1[n][1]/10) + ' C,')
        print('\nFPA Temp: ' + str(fpaTempCorr2[n][1]/10) + ' C,')
        
        
        
            # get read size - output is a tuple
        try:
            #memGetSizeRet = cam1.get_imSize()
            memGetSizeRet = pyClient.memGetCaptureSize()
            
            # store capture size in bytes in new vars for later use
            capSizeinBytes = memGetSizeRet[1]
            pixRows = memGetSizeRet[2]
            pixCols = memGetSizeRet[3]
    
        except:
            print('Something went wrong during memGetCaptureSize() call. Exiting...')
            cam1.close_port()
            cam2.close_port()
            sys.exit(1)
       
        
        if n < 1:
            image1 = np.zeros((pixRows,pixCols),dtype = np.uint16,order='C')
            image2 = np.zeros((pixRows,pixCols),dtype = np.uint16,order='C')
        
        
        """Call image bytes from buffer"""
        #create np array of uint8 type
        image8b_1  = np.zeros((pixRows,2*pixCols),dtype = np.uint8,order='C')
        image8b_2  = np.zeros((pixRows,2*pixCols),dtype = np.uint8,order='C')
        image16b_1 = np.zeros((pixRows,pixCols),dtype = np.uint16,order='C')
        image16b_2 = np.zeros((pixRows,pixCols),dtype = np.uint16,order='C')
        bytesPerRead = 160
        readsPerRow = (pixCols*2)/bytesPerRead
        bufNum = 0
        
        for i in np.arange(0,pixRows,1):
                #pixRead_1 = cam1.read_pixels(bufferNum=bufNum,offset=4*i*bytesPerRead,sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead_1 = pyClient.memReadCapture(bufferNum=bufNum,offset=4*i*bytesPerRead,sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_1[i,0:bytesPerRead] = pixRead_1[1]
                
                #pixRead2_1 = cam1.read_pixels(bufferNum=bufNum,offset=((4*i+1)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead2_1 = pyClient.memReadCapture(bufferNum=bufNum,offset=((4*i+1)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_1[i,bytesPerRead:2*bytesPerRead] = pixRead2_1[1]
                
                #pixRead3_1 = cam1.read_pixels(bufferNum=bufNum,offset=((4*i+2)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead3_1 = pyClient.memReadCapture(bufferNum=bufNum,offset=((4*i+2)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_1[i,2*bytesPerRead:3*bytesPerRead] = pixRead3_1[1]
                
                #pixRead4_1 = cam1.read_pixels(bufferNum=bufNum,offset=((4*i+3)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead4_1 = pyClient.memReadCapture(bufferNum=bufNum,offset=((4*i+3)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
    
                image8b_1[i,3*bytesPerRead:4*bytesPerRead] = pixRead4_1[1]
                
        print('Finished Reading Image from Cam 1 ' + str(n+1))        
     
        
        for i in np.arange(0,pixRows,1):
                #pixRead_2 = cam2.read_pixels(bufferNum=bufNum,offset=4*i*bytesPerRead,sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead_2 = pyClient2.memReadCapture(bufferNum=bufNum,offset=4*i*bytesPerRead,sizeInBytes=bytesPerRead)  # output is a tuple
    
                image8b_2[i,0:bytesPerRead] = pixRead_2[1]
                
                #pixRead2_2 = cam2.read_pixels(bufferNum=bufNum,offset=((4*i+1)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead2_2 = pyClient2.memReadCapture(bufferNum=bufNum,offset=((4*i+1)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_2[i,bytesPerRead:2*bytesPerRead] = pixRead2_2[1]
                
                #pixRead3_2 = cam2.read_pixels(bufferNum=bufNum,offset=((4*i+2)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead3_2 = pyClient2.memReadCapture(bufferNum=bufNum,offset=((4*i+2)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_2[i,2*bytesPerRead:3*bytesPerRead] = pixRead3_2[1]
                
                #pixRead4_2 = cam2.read_pixels(bufferNum=bufNum,offset=((4*i+3)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                pixRead4_2 = pyClient2.memReadCapture(bufferNum=bufNum,offset=((4*i+3)*bytesPerRead),sizeInBytes=bytesPerRead)  # output is a tuple
                image8b_2[i,3*bytesPerRead:4*bytesPerRead] = pixRead4_2[1]
                
        print('Finished Reading Image from Cam 2 ' + str(n+1))       
        
        image16b_1 = image8b_1[:,:].view(np.uint16)    # assuming host and camera endianess match
        image16b_1 = image16b_1.view('<u2')                 # <- little endian u- unsigned 2- bytes
         
        image16b_2 = image8b_2[:,:].view(np.uint16)    # assuming host and camera endianess match
        image16b_2 = image16b_2.view('<u2')         
    
        image1 = image1 + image16b_1/avg
        image2 = image2 + image16b_2/avg
        
        
        end = time.perf_counter()
        print(str(round(end-start)) + " seconds to run one loop")
        
        if n == loopsToRun-1: #if on last loop, exit before wait time
            break;
        
        print('begin wait for ' + str(secondsToWait-round(end-start)) + ' seconds')
        time.sleep(secondsToWait-(end-start)) #wait for specified time, subtracting time for loop to run
    
    
    
    
    
    """data to return"""
    
    fpaTempCorr1 = np.mean(fpaTempCorr1[:,1]/10)
    fpaTempCorr2 = np.mean(fpaTempCorr2[:,1]/10)
               
    """REMOVE MASTER SLAVE"""
    
    cam1.disable_sync()
    cam2.disable_sync()
    
    mode1 = cam1.get_syncMode()
    mode2 = cam2.get_syncMode()
   
    cam1.close_port()
    cam2.close_port()
    
    return( fpaTempCorr1, fpaTempCorr2,image1 , image2)
