# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:38:02 2020
This defines the class Camera1
Requires Boson SDK
@author: khart
"""
from BosonSDK.ClientFiles_Python import Client_API as pyClient

class Camera1:
        def __init__(self,port) :
            self.port = port
        def make_port(self,inport):
            self.make_port = pyClient.Initialize(manualport=inport)
        def close_port(self):
            self.close_port = pyClient.Close(self.make_port)
        def get_serial(self):
            self.get_serial = pyClient.bosonGetCameraSN()
            return self.get_serial
        
        def set_gain(self,state):
            self.set_gain = pyClient.bosonSetGainMode(state)
        def set_bpr(self,state):
            self.set_bpr = pyClient.bprSetState(state)
        def set_scnr(self,state):
            self.set_scnr = pyClient.scnrSetEnableState(state)
        def set_tf(self,state):
            self.set_tf = pyClient.tfSetEnableState(state)
        def set_spnr(self,state):
            self.set_spnr = pyClient.spnrSetEnableState(state)
    
        def get_gainState(self):
            self.get_gainState = pyClient.bosonGetGainMode()
            return self.get_gainState
        def get_bprState(self):
            self.get_bprState = pyClient.bprGetState()
            return self.get_bprState
        def get_scnrState(self):
            self.get_scnrState = pyClient.scnrGetEnableState()
            return self.get_scnrState
        def get_scnrMaxCorr(self):
            self.get_scnrMaxCorr = pyClient.scnrGetMaxCorr()
            return self.get_scnrMaxCorr
        def get_tfState(self):
            self.get_tfState = pyClient.tfGetEnableState()
            return self.get_tfState
        def get_spnrState(self):
            self.get_spnrState = pyClient.spnrGetEnableState()
            return self.get_spnrState
    
        def take_image(self):
            self.take_image = pyClient.captureSingleFrame()
        def get_FPATemp(self):
            self.get_FPATemp = pyClient.bosonlookupFPATempDegCx10()
            return self.get_FPATemp
        def get_imSize(self):
            self.get_imSize = pyClient.memGetCaptureSize()
            return self.get_imSize
        def read_pixels(self,bufferNum,offset,sizeInBytes):
            self.pixels = pyClient.memReadCapture(bufferNum,offset,sizeInBytes)
            return self.pixels
        
        def get_syncMode(self):
            self.mode = pyClient.bosonGetExtSyncMode()
            return self.mode
        def disable_sync(self):
            self.disable_sync = pyClient.bosonSetExtSyncMode(pyClient.FLR_BOSON_EXT_SYNC_MODE_E.FLR_BOSON_EXT_SYNC_DISABLE_MODE)
        def set_asMaster(self):
            self.set_asMaster = pyClient.bosonSetExtSyncMode(pyClient.FLR_BOSON_EXT_SYNC_MODE_E.FLR_BOSON_EXT_SYNC_MASTER_MODE)
        