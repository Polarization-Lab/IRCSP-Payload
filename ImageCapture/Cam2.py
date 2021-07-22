# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:41:53 2020
Created on Thu Sep 10 10:38:02 2020
This defines the class Camera2
Requires Boson SDK
@author: khart
"""

from BosonSDKCopy.ClientFiles_Python import Client_API as pyClient2

class Camera2:
        def __init__(self,port) :
            self.port = port
        def make_port(self,inport):
            self.make_port = pyClient2.Initialize(manualport=inport)
        def close_port(self):
            self.close_port = pyClient2.Close(self.make_port)
        def get_serial(self):
            self.get_serial = pyClient2.bosonGetCameraSN()
            return self.get_serial
        
        def set_gain(self,state):
            self.set_gain = pyClient2.bosonSetGainMode(state)
        def set_bpr(self,state):
            self.set_bpr = pyClient2.bprSetState(state)
        def set_scnr(self,state):
            self.set_scnr = pyClient2.scnrSetEnableState(state)
        def set_tf(self,state):
            self.set_tf = pyClient2.tfSetEnableState(state)
        def set_spnr(self,state):
            self.set_spnr = pyClient2.spnrSetEnableState(state)
    
        def get_gainState(self):
            self.get_gainState = pyClient2.bosonGetGainMode()
            return self.get_gainState
        def get_bprState(self):
            self.get_bprState = pyClient2.bprGetState()
            return self.get_bprState
        def get_scnrState(self):
            self.get_scnrState = pyClient2.scnrGetEnableState()
            return self.get_scnrState
        def get_scnrMaxCorr(self):
            self.get_scnrMaxCorr = pyClient2.scnrGetMaxCorr()
            return self.get_scnrMaxCorr
        def get_tfState(self):
            self.get_tfState = pyClient2.tfGetEnableState()
            return self.get_tfState
        def get_spnrState(self):
            self.get_spnrState = pyClient2.spnrGetEnableState()
            return self.get_spnrState
    
        def take_image(self):
            self.take_image = pyClient2.captureSingleFrame()
        def get_FPATemp(self):
            self.get_FPATemp = pyClient2.bosonlookupFPATempDegCx10()
            return self.get_FPATemp
        def get_imSize(self):
            self.get_imSize = pyClient2.memGetCaptureSize()
            return self.get_imSize
        def read_pixels(self,bufferNum,offset,sizeInBytes):
            self.pixels = pyClient2.memReadCapture(bufferNum,offset,sizeInBytes)
            return self.pixels
        
        def get_syncMode(self):
            self.mode = pyClient2.bosonGetExtSyncMode()
            return self.mode
        def disable_sync(self):
            self.disable_sync = pyClient2.bosonSetExtSyncMode(pyClient2.FLR_BOSON_EXT_SYNC_MODE_E.FLR_BOSON_EXT_SYNC_DISABLE_MODE)
        def set_asSlave(self):
            self.set_asMaster = pyClient2.bosonSetExtSyncMode(pyClient2.FLR_BOSON_EXT_SYNC_MODE_E.FLR_BOSON_EXT_SYNC_SLAVE_MODE)