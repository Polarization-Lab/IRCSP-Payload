#  /////////////////////////////////////////////////////
#  // DO NOT EDIT.  This is a machine generated file. //
#  /////////////////////////////////////////////////////


from .Client_Dispatcher import *
from .Serializer_Struct import *
from .Serializer_BuiltIn import *
from .EnumTypes import *

__commandCount = 0
def fixSpecialBytes(seqnum):
	seqbytes = bytearray([0x00,0x00,0x00,0x00])
	UINT_32ToByte(seqnum,seqbytes,0)
	seqbytes = seqbytes.replace(b'\x8E',b'\x8F')
	seqbytes = seqbytes.replace(b'\x9E',b'\x9F')
	seqbytes = seqbytes.replace(b'\xAE',b'\xAF')
	newseqnum = byteToUINT_32(seqbytes,0)
	#if newseqnum != seqnum:
		#print("seqfix: 0x{:08X} -> 0x{:08X}".format(seqnum,newseqnum))
	return newseqnum

# Begin Module: gao
def CLIENT_pkg_gao_SetGainState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetGainState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetFfcState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetFfcState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetTempCorrectionState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetTempCorrectionState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetIConstL(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetIConstL():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetIConstM(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetIConstM():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetAveragerState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetAveragerState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetNumFFCFrames(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetNumFFCFrames():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_GetAveragerThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_GetRnsState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000012, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetTestRampState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000013, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetTestRampState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetSffcState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000017, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetSffcState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000018, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_SetRpmState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000019, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetRpmState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000001A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

def CLIENT_pkg_gao_GetRpmThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0000001C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read threshold from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	threshold = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of threshold handling
	
	return returnCode, threshold
	
#End of Module: gao

def CLIENT_pkg_gao_SetFfcZeroMeanState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000025, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: gao

def CLIENT_pkg_gao_GetFfcZeroMeanState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00000026, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: gao

# Begin Module: lagrange
# Begin Module: roic
def CLIENT_pkg_roic_GetFPATemp():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_GetFrameCount():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_GetActiveNormalizationTarget():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_SetFPARampState(state):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write state to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(state.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: roic

def CLIENT_pkg_roic_GetFPARampState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020015, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read state from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	state = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of state handling
	
	return returnCode, state
	
#End of Module: roic

def CLIENT_pkg_roic_GetSensorADC1():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020019, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_GetSensorADC2():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0002001A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_SetFPATempOffset(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0002001B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: roic

def CLIENT_pkg_roic_GetFPATempOffset():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0002001C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_SetFPATempMode(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0002001D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: roic

def CLIENT_pkg_roic_GetFPATempMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0002001E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ROIC_TEMP_MODE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

def CLIENT_pkg_roic_GetFPATempTable():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 64
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020020, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read table from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	table = byteToFLR_ROIC_FPATEMP_TABLE_T(receiveData,inPtr)
	inPtr+=64
	# end of table handling
	
	return returnCode, table
	
#End of Module: roic

def CLIENT_pkg_roic_SetFPATempValue(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020022, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: roic

def CLIENT_pkg_roic_GetFPATempValue():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00020023, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: roic

# Begin Module: bpr
def CLIENT_pkg_bpr_SetState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00030002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: bpr

def CLIENT_pkg_bpr_GetState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00030001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: bpr

# Begin Module: telemetry
def CLIENT_pkg_telemetry_SetState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: telemetry

def CLIENT_pkg_telemetry_GetState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: telemetry

def CLIENT_pkg_telemetry_SetLocation(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: telemetry

def CLIENT_pkg_telemetry_GetLocation():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_TELEMETRY_LOC_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: telemetry

def CLIENT_pkg_telemetry_SetPacking(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: telemetry

def CLIENT_pkg_telemetry_GetPacking():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00040006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_TELEMETRY_PACKING_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: telemetry

# Begin Module: boson
def CLIENT_pkg_boson_GetCameraSN():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_GetCameraPN():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 20
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLR_BOSON_PARTNUMBER_T(receiveData,inPtr)
	inPtr+=20
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_GetSensorSN():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_RunFFC():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_SetFFCTempThreshold(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetFFCTempThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_SetFFCFrameThreshold(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetFFCFrameThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_GetFFCInProgress():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_Reboot():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_SetFFCMode(ffcMode):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ffcMode to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(ffcMode.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050012, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetFFCMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050013, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read ffcMode from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	ffcMode = FLR_BOSON_FFCMODE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of ffcMode handling
	
	return returnCode, ffcMode
	
#End of Module: boson

def CLIENT_pkg_boson_SetGainMode(gainMode):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write gainMode to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(gainMode.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetGainMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050015, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read gainMode from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	gainMode = FLR_BOSON_GAINMODE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of gainMode handling
	
	return returnCode, gainMode
	
#End of Module: boson

def CLIENT_pkg_boson_WriteDynamicHeaderToFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050018, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_ReadDynamicHeaderFromFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050019, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_RestoreFactoryDefaultsFromFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005001B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_RestoreFactoryBadPixelsFromFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050020, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_WriteBadPixelsToFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050021, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetSoftwareRev():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050022, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None, None
	
	inPtr = 0 #simple array index
	
	# read major from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	major = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of major handling
	
	# read minor from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	minor = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of minor handling
	
	# read patch from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	patch = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of patch handling
	
	return returnCode, major, minor, patch
	
#End of Module: boson

def CLIENT_pkg_boson_SetBadPixelLocation(row, col):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write row to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(row,sendData,outPtr)
	outPtr += 4
	
	# write col to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(col,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005002D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_lookupFPATempDegCx10():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050030, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_lookupFPATempDegKx10():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050031, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_WriteLensNvFfcToFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050033, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_WriteLensGainToFlash():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050035, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_SetLensNumber(lensNumber):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write lensNumber to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(lensNumber,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050038, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetLensNumber():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050039, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read lensNumber from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	lensNumber = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of lensNumber handling
	
	return returnCode, lensNumber
	
#End of Module: boson

def CLIENT_pkg_boson_SetTableNumber(tableNumber):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write tableNumber to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(tableNumber,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005003A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetTableNumber():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005003B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read tableNumber from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	tableNumber = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of tableNumber handling
	
	return returnCode, tableNumber
	
#End of Module: boson

def CLIENT_pkg_boson_GetSensorPN():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 32
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005003F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read sensorPN from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	sensorPN = byteToFLR_BOSON_SENSOR_PARTNUMBER_T(receiveData,inPtr)
	inPtr+=32
	# end of sensorPN handling
	
	return returnCode, sensorPN
	
#End of Module: boson

def CLIENT_pkg_boson_SetGainSwitchParams(parm_struct):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 16
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write parm_struct to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_BOSON_GAIN_SWITCH_PARAMS_TToByte(parm_struct,sendData,outPtr)
	outPtr += 16
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050040, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetGainSwitchParams():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 16
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050041, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read parm_struct from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	parm_struct = byteToFLR_BOSON_GAIN_SWITCH_PARAMS_T(receiveData,inPtr)
	inPtr+=16
	# end of parm_struct handling
	
	return returnCode, parm_struct
	
#End of Module: boson

def CLIENT_pkg_boson_GetSwitchToHighGainFlag():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050042, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read switchToHighGainFlag from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	switchToHighGainFlag = byteToUCHAR(receiveData,inPtr)
	inPtr+=1
	# end of switchToHighGainFlag handling
	
	return returnCode, switchToHighGainFlag
	
#End of Module: boson

def CLIENT_pkg_boson_GetSwitchToLowGainFlag():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050043, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read switchToLowGainFlag from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	switchToLowGainFlag = byteToUCHAR(receiveData,inPtr)
	inPtr+=1
	# end of switchToLowGainFlag handling
	
	return returnCode, switchToLowGainFlag
	
#End of Module: boson

def CLIENT_pkg_boson_GetCLowToHighPercent():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050044, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read cLowToHighPercent from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	cLowToHighPercent = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of cLowToHighPercent handling
	
	return returnCode, cLowToHighPercent
	
#End of Module: boson

def CLIENT_pkg_boson_GetMaxNUCTables():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050045, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read maxNUCTables from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	maxNUCTables = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of maxNUCTables handling
	
	return returnCode, maxNUCTables
	
#End of Module: boson

def CLIENT_pkg_boson_GetMaxLensTables():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050046, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read maxLensTables from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	maxLensTables = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of maxLensTables handling
	
	return returnCode, maxLensTables
	
#End of Module: boson

def CLIENT_pkg_boson_GetFfcWaitCloseFrames():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005004E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: boson

def CLIENT_pkg_boson_SetFfcWaitCloseFrames(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005004F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_CheckForTableSwitch():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050050, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetDesiredTableNumber():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050052, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read desiredTableNumber from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	desiredTableNumber = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of desiredTableNumber handling
	
	return returnCode, desiredTableNumber
	
#End of Module: boson

def CLIENT_pkg_boson_GetFfcStatus():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050054, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read ffcStatus from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	ffcStatus = FLR_BOSON_FFCSTATUS_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of ffcStatus handling
	
	return returnCode, ffcStatus
	
#End of Module: boson

def CLIENT_pkg_boson_GetFfcDesired():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050055, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read ffcDesired from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	ffcDesired = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of ffcDesired handling
	
	return returnCode, ffcDesired
	
#End of Module: boson

def CLIENT_pkg_boson_GetSwRevInHeader():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050056, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None, None
	
	inPtr = 0 #simple array index
	
	# read major from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	major = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of major handling
	
	# read minor from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	minor = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of minor handling
	
	# read patch from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	patch = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of patch handling
	
	return returnCode, major, minor, patch
	
#End of Module: boson

def CLIENT_pkg_boson_GetLastFFCFrameCount():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005005D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read frameCount from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	frameCount = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of frameCount handling
	
	return returnCode, frameCount
	
#End of Module: boson

def CLIENT_pkg_boson_GetLastFFCTempDegKx10():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005005E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read temp from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	temp = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of temp handling
	
	return returnCode, temp
	
#End of Module: boson

def CLIENT_pkg_boson_GetTableSwitchDesired():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005005F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read tableSwitchDesired from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	tableSwitchDesired = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of tableSwitchDesired handling
	
	return returnCode, tableSwitchDesired
	
#End of Module: boson

def CLIENT_pkg_boson_GetOverTempThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050061, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read temperatureInC from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	temperatureInC = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of temperatureInC handling
	
	return returnCode, temperatureInC
	
#End of Module: boson

def CLIENT_pkg_boson_GetLowPowerMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050062, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read lowPowerMode from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	lowPowerMode = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of lowPowerMode handling
	
	return returnCode, lowPowerMode
	
#End of Module: boson

def CLIENT_pkg_boson_GetOverTempEventOccurred():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050063, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read overTempEventOccurred from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	overTempEventOccurred = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of overTempEventOccurred handling
	
	return returnCode, overTempEventOccurred
	
#End of Module: boson

def CLIENT_pkg_boson_SetPermitThermalShutdownOverride(permitThermalShutdownOverride):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write permitThermalShutdownOverride to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(permitThermalShutdownOverride.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050064, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetPermitThermalShutdownOverride():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050065, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read permitThermalShutdownOverride from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	permitThermalShutdownOverride = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of permitThermalShutdownOverride handling
	
	return returnCode, permitThermalShutdownOverride
	
#End of Module: boson

def CLIENT_pkg_boson_GetMyriadTemp():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050068, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read myriadTemp from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	myriadTemp = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of myriadTemp handling
	
	return returnCode, myriadTemp
	
#End of Module: boson

def CLIENT_pkg_boson_GetNvFFCNucTableNumberLens0():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005006D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read nvFFCNucTableNumberLens0 from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	nvFFCNucTableNumberLens0 = byteToINT_32(receiveData,inPtr)
	inPtr+=4
	# end of nvFFCNucTableNumberLens0 handling
	
	return returnCode, nvFFCNucTableNumberLens0
	
#End of Module: boson

def CLIENT_pkg_boson_GetNvFFCNucTableNumberLens1():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005006F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read nvFFCNucTableNumberLens1 from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	nvFFCNucTableNumberLens1 = byteToINT_32(receiveData,inPtr)
	inPtr+=4
	# end of nvFFCNucTableNumberLens1 handling
	
	return returnCode, nvFFCNucTableNumberLens1
	
#End of Module: boson

def CLIENT_pkg_boson_GetNvFFCFPATempDegKx10Lens0():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050071, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read nvFFCFPATempDegKx10Lens0 from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	nvFFCFPATempDegKx10Lens0 = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of nvFFCFPATempDegKx10Lens0 handling
	
	return returnCode, nvFFCFPATempDegKx10Lens0
	
#End of Module: boson

def CLIENT_pkg_boson_GetNvFFCFPATempDegKx10Lens1():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050073, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read nvFFCFPATempDegKx10Lens1 from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	nvFFCFPATempDegKx10Lens1 = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of nvFFCFPATempDegKx10Lens1 handling
	
	return returnCode, nvFFCFPATempDegKx10Lens1
	
#End of Module: boson

def CLIENT_pkg_boson_SetFFCWarnTimeInSecx10(ffcWarnTime):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ffcWarnTime to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(ffcWarnTime,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050074, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetFFCWarnTimeInSecx10():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050075, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read ffcWarnTime from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	ffcWarnTime = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of ffcWarnTime handling
	
	return returnCode, ffcWarnTime
	
#End of Module: boson

def CLIENT_pkg_boson_GetOverTempEventCounter():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050076, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read overTempEventCounter from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	overTempEventCounter = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of overTempEventCounter handling
	
	return returnCode, overTempEventCounter
	
#End of Module: boson

def CLIENT_pkg_boson_SetOverTempTimerInSec(overTempTimerInSec):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write overTempTimerInSec to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(overTempTimerInSec,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050077, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetOverTempTimerInSec():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050078, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read overTempTimerInSec from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	overTempTimerInSec = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of overTempTimerInSec handling
	
	return returnCode, overTempTimerInSec
	
#End of Module: boson

def CLIENT_pkg_boson_UnloadCurrentLensCorrections():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050079, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_SetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write timeForQuickFFCsInSecs to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(timeForQuickFFCsInSecs,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005007A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetTimeForQuickFFCsInSecs():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005007B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read timeForQuickFFCsInSecs from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	timeForQuickFFCsInSecs = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of timeForQuickFFCsInSecs handling
	
	return returnCode, timeForQuickFFCsInSecs
	
#End of Module: boson

def CLIENT_pkg_boson_ReloadCurrentLensCorrections():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005007C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetBootTimestamps():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 16
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0005007F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None, None, None
	
	inPtr = 0 #simple array index
	
	# read FirstLight from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None, None
	FirstLight = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of FirstLight handling
	
	# read StartInit from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None, None
	StartInit = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of StartInit handling
	
	# read BosonExecDone from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None, None
	BosonExecDone = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of BosonExecDone handling
	
	# read Timestamp4 from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None, None
	Timestamp4 = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of Timestamp4 handling
	
	return returnCode, FirstLight, StartInit, BosonExecDone, Timestamp4
	
#End of Module: boson

def CLIENT_pkg_boson_SetExtSyncMode(mode):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write mode to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(mode.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050098, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: boson

def CLIENT_pkg_boson_GetExtSyncMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00050099, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read mode from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	mode = FLR_BOSON_EXT_SYNC_MODE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of mode handling
	
	return returnCode, mode
	
#End of Module: boson

# Begin Module: dvo
def CLIENT_pkg_dvo_SetAnalogVideoState(analogVideoState):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write analogVideoState to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(analogVideoState.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetAnalogVideoState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read analogVideoState from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	analogVideoState = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of analogVideoState handling
	
	return returnCode, analogVideoState
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetOutputFormat(format):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write format to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(format.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetOutputFormat():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read format from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	format = FLR_DVO_OUTPUT_FORMAT_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of format handling
	
	return returnCode, format
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetOutputYCbCrSettings(settings):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 12
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write settings to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_DVO_YCBCR_SETTINGS_TToByte(settings,sendData,outPtr)
	outPtr += 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetOutputYCbCrSettings():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read settings from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	settings = byteToFLR_DVO_YCBCR_SETTINGS_T(receiveData,inPtr)
	inPtr+=12
	# end of settings handling
	
	return returnCode, settings
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetOutputRGBSettings(settings):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write settings to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_DVO_RGB_SETTINGS_TToByte(settings,sendData,outPtr)
	outPtr += 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetOutputRGBSettings():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read settings from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	settings = byteToFLR_DVO_RGB_SETTINGS_T(receiveData,inPtr)
	inPtr+=8
	# end of settings handling
	
	return returnCode, settings
	
#End of Module: dvo

def CLIENT_pkg_dvo_ApplyCustomSettings():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetDisplayMode(displayMode):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write displayMode to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(displayMode.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetDisplayMode():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read displayMode from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	displayMode = FLR_DVO_DISPLAY_MODE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of displayMode handling
	
	return returnCode, displayMode
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetType(tap):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write tap to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(tap.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0006000F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetType():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read tap from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	tap = FLR_DVO_TYPE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of tap handling
	
	return returnCode, tap
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetVideoStandard(videoStandard):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write videoStandard to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(videoStandard.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060011, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetVideoStandard():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060012, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read videoStandard from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	videoStandard = FLR_DVO_VIDEO_STANDARD_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of videoStandard handling
	
	return returnCode, videoStandard
	
#End of Module: dvo

def CLIENT_pkg_dvo_SetCheckVideoDacPresent(checkVideoDacPresent):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write checkVideoDacPresent to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(checkVideoDacPresent.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060013, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dvo

def CLIENT_pkg_dvo_GetCheckVideoDacPresent():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00060014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read checkVideoDacPresent from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	checkVideoDacPresent = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of checkVideoDacPresent handling
	
	return returnCode, checkVideoDacPresent
	
#End of Module: dvo

# Begin Module: capture
def CLIENT_pkg_capture_SingleFrame():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00070001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: capture

def CLIENT_pkg_capture_Frames(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 10
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_CAPTURE_SETTINGS_TToByte(data,sendData,outPtr)
	outPtr += 10
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00070002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: capture

def CLIENT_pkg_capture_SingleFrameWithSrc(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00070003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: capture

def CLIENT_pkg_capture_SingleFrameToFile():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00070004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: capture

# Begin Module: scnr
def CLIENT_pkg_scnr_SetEnableState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetEnableState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetThColSum(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetThColSum():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetThPixel(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetThPixel():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetMaxCorr(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetMaxCorr():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetThPixelApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetMaxCorrApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetThColSumSafe(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetThColSumSafe():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetThPixelSafe(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetThPixelSafe():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0008000F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

def CLIENT_pkg_scnr_SetMaxCorrSafe(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scnr

def CLIENT_pkg_scnr_GetMaxCorrSafe():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00080011, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: scnr

# Begin Module: agc
def CLIENT_pkg_agc_SetPercentPerBin(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetPercentPerBin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetLinearPercent(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetLinearPercent():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetOutlierCut(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetOutlierCut():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_GetDrOut():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetMaxGain(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetMaxGain():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_Setdf(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_Getdf():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetGamma(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetGamma():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_GetFirstBin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_GetLastBin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090012, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetDetailHeadroom(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090013, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetDetailHeadroom():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_Setd2br(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090015, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_Getd2br():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090016, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetSigmaR(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090017, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetSigmaR():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090018, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetUseEntropy(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009001E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetUseEntropy():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0009001F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetROI(roi):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write roi to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_ROI_TToByte(roi,sendData,outPtr)
	outPtr += 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090020, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090021, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read roi from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	roi = byteToFLR_ROI_T(receiveData,inPtr)
	inPtr+=8
	# end of roi handling
	
	return returnCode, roi
	
#End of Module: agc

def CLIENT_pkg_agc_GetMaxGainApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090025, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_GetSigmaRApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090026, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_SetOutlierCutBalance(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090027, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: agc

def CLIENT_pkg_agc_GetOutlierCutBalance():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090028, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: agc

def CLIENT_pkg_agc_GetOutlierCutApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00090029, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None
	
	inPtr = 0 #simple array index
	
	# read percentHigh from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	percentHigh = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of percentHigh handling
	
	# read percentLow from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	percentLow = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of percentLow handling
	
	return returnCode, percentHigh, percentLow
	
#End of Module: agc

# Begin Module: tf
def CLIENT_pkg_tf_SetEnableState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: tf

def CLIENT_pkg_tf_GetEnableState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_SetDelta_nf(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: tf

def CLIENT_pkg_tf_GetDelta_nf():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_SetTHDeltaMotion(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(data,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: tf

def CLIENT_pkg_tf_GetTHDeltaMotion():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_SetWLut(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 32
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_TF_WLUT_TToByte(data,sendData,outPtr)
	outPtr += 32
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: tf

def CLIENT_pkg_tf_GetWLut():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 32
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLR_TF_WLUT_T(receiveData,inPtr)
	inPtr+=32
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_GetMotionCount():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_SetMotionThreshold(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: tf

def CLIENT_pkg_tf_GetMotionThreshold():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A000F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_GetDelta_nfApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0016, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

def CLIENT_pkg_tf_GetTHDeltaMotionApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000A0017, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of data handling
	
	return returnCode, data
	
#End of Module: tf

# Begin Module: mem
def CLIENT_pkg_mem_ReadCapture(bufferNum, offset, sizeInBytes):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 7
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 256
	
	# write bufferNum to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UCHARToByte(bufferNum,sendData,outPtr)
	outPtr += 1
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write sizeInBytes to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_16ToByte(sizeInBytes,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUCHARArray(receiveData,inPtr,sizeInBytes)
	inPtr+=sizeInBytes
	# end of data handling
	
	return returnCode, data
	
#End of Module: mem

def CLIENT_pkg_mem_GetCaptureSize():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None, None
	
	inPtr = 0 #simple array index
	
	# read bytes from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	bytes = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of bytes handling
	
	# read rows from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	rows = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of rows handling
	
	# read columns from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	columns = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of columns handling
	
	return returnCode, bytes, rows, columns
	
#End of Module: mem

def CLIENT_pkg_mem_WriteFlash(location, index, offset, sizeInBytes, data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = sizeInBytes + 11
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write location to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(location.value,sendData,outPtr)
	outPtr += 4
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write sizeInBytes to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_16ToByte(sizeInBytes,sendData,outPtr)
	outPtr += 2
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(data,sizeInBytes,sendData,outPtr)
	outPtr += sizeInBytes
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: mem

def CLIENT_pkg_mem_ReadFlash(location, index, offset, sizeInBytes):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 11
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 256
	
	# write location to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	INT_32ToByte(location.value,sendData,outPtr)
	outPtr += 4
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write sizeInBytes to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_16ToByte(sizeInBytes,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUCHARArray(receiveData,inPtr,sizeInBytes)
	inPtr+=sizeInBytes
	# end of data handling
	
	return returnCode, data
	
#End of Module: mem

def CLIENT_pkg_mem_GetFlashSize(location):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write location to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, bytes
	INT_32ToByte(location.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read bytes from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	bytes = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of bytes handling
	
	return returnCode, bytes
	
#End of Module: mem

def CLIENT_pkg_mem_EraseFlash(location, index):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 5
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write location to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(location.value,sendData,outPtr)
	outPtr += 4
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: mem

def CLIENT_pkg_mem_EraseFlashPartial(location, index, offset, length):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 13
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write location to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(location.value,sendData,outPtr)
	outPtr += 4
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write length to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(length,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF0009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: mem

def CLIENT_pkg_mem_ReadCurrentGain(offset, sizeInBytes):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 6
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 256
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write sizeInBytes to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UINT_16ToByte(sizeInBytes,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUCHARArray(receiveData,inPtr,sizeInBytes)
	inPtr+=sizeInBytes
	# end of data handling
	
	return returnCode, data
	
#End of Module: mem

def CLIENT_pkg_mem_GetGainSize():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xFFFF000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None, None
	
	inPtr = 0 #simple array index
	
	# read bytes from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	bytes = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of bytes handling
	
	# read rows from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	rows = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of rows handling
	
	# read columns from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None, None
	columns = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of columns handling
	
	return returnCode, bytes, rows, columns
	
#End of Module: mem

# Begin Module: colorLut
def CLIENT_pkg_colorLut_SetControl(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000B0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: colorLut

def CLIENT_pkg_colorLut_GetControl():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000B0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: colorLut

def CLIENT_pkg_colorLut_SetId(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000B0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: colorLut

def CLIENT_pkg_colorLut_GetId():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000B0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_COLORLUT_ID_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: colorLut

# Begin Module: spnr
def CLIENT_pkg_spnr_SetEnableState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetEnableState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_SPNR_STATE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetFrameDelay(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetFrameDelay():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetSFApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0015, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read sf from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	sf = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of sf handling
	
	return returnCode, sf
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetPSDKernel(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 256
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_SPNR_PSD_KERNEL_TToByte(data,sendData,outPtr)
	outPtr += 256
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetPSDKernel():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 256
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLR_SPNR_PSD_KERNEL_T(receiveData,inPtr)
	inPtr+=256
	# end of data handling
	
	return returnCode, data
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetSFMin(sfmin):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write sfmin to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(sfmin,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetSFMin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read sfmin from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	sfmin = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of sfmin handling
	
	return returnCode, sfmin
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetSFMax(sfmax):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write sfmax to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(sfmax,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetSFMax():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C001F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read sfmax from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	sfmax = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of sfmax handling
	
	return returnCode, sfmax
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetDFMin(dfmin):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write dfmin to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(dfmin,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0020, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetDFMin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0021, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read dfmin from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	dfmin = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of dfmin handling
	
	return returnCode, dfmin
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetDFMax(dfmax):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write dfmax to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(dfmax,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0022, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetDFMax():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0023, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read dfmax from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	dfmax = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of dfmax handling
	
	return returnCode, dfmax
	
#End of Module: spnr

def CLIENT_pkg_spnr_SetNormTarget(normTarget):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write normTarget to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(normTarget,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0024, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetNormTarget():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0025, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read normTarget from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	normTarget = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of normTarget handling
	
	return returnCode, normTarget
	
#End of Module: spnr

def CLIENT_pkg_spnr_GetNormTargetApplied():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000C0026, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read normTargetApplied from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	normTargetApplied = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of normTargetApplied handling
	
	return returnCode, normTargetApplied
	
#End of Module: spnr

# Begin Module: scaler
def CLIENT_pkg_scaler_GetMaxZoom():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000D0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read zoom from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	zoom = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of zoom handling
	
	return returnCode, zoom
	
#End of Module: scaler

def CLIENT_pkg_scaler_SetZoom(zoomParams):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 12
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write zoomParams to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_SCALER_ZOOM_PARAMS_TToByte(zoomParams,sendData,outPtr)
	outPtr += 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000D0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scaler

def CLIENT_pkg_scaler_GetZoom():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 12
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000D0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read zoomParams from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	zoomParams = byteToFLR_SCALER_ZOOM_PARAMS_T(receiveData,inPtr)
	inPtr+=12
	# end of zoomParams handling
	
	return returnCode, zoomParams
	
#End of Module: scaler

def CLIENT_pkg_scaler_SetFractionalZoom(zoomNumerator, zoomDenominator, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 32
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write zoomNumerator to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomNumerator,sendData,outPtr)
	outPtr += 4
	
	# write zoomDenominator to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomDenominator,sendData,outPtr)
	outPtr += 4
	
	# write zoomXCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomXCenter,sendData,outPtr)
	outPtr += 4
	
	# write zoomYCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomYCenter,sendData,outPtr)
	outPtr += 4
	
	# write inChangeEnable to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(inChangeEnable.value,sendData,outPtr)
	outPtr += 4
	
	# write zoomOutXCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomOutXCenter,sendData,outPtr)
	outPtr += 4
	
	# write zoomOutYCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomOutYCenter,sendData,outPtr)
	outPtr += 4
	
	# write outChangeEnable to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(outChangeEnable.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000D0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scaler

def CLIENT_pkg_scaler_SetIndexZoom(zoomIndex, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 28
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write zoomIndex to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomIndex,sendData,outPtr)
	outPtr += 4
	
	# write zoomXCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomXCenter,sendData,outPtr)
	outPtr += 4
	
	# write zoomYCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomYCenter,sendData,outPtr)
	outPtr += 4
	
	# write inChangeEnable to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(inChangeEnable.value,sendData,outPtr)
	outPtr += 4
	
	# write zoomOutXCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomOutXCenter,sendData,outPtr)
	outPtr += 4
	
	# write zoomOutYCenter to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(zoomOutYCenter,sendData,outPtr)
	outPtr += 4
	
	# write outChangeEnable to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(outChangeEnable.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000D0008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: scaler

# Begin Module: sysctrl
def CLIENT_pkg_sysctrl_SetFreezeState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000E0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sysctrl

def CLIENT_pkg_sysctrl_GetFreezeState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000E0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sysctrl

def CLIENT_pkg_sysctrl_GetCameraFrameRate():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x000E0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read frameRate from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	frameRate = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of frameRate handling
	
	return returnCode, frameRate
	
#End of Module: sysctrl

# Begin Module: testRamp
def CLIENT_pkg_testRamp_SetType(index, data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 5
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_GetType(index):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_TESTRAMP_TYPE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_SetSettings(index, data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 7
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_TESTRAMP_SETTINGS_TToByte(data,sendData,outPtr)
	outPtr += 6
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_GetSettings(index):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 6
	
	# write index to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, data
	UCHARToByte(index,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLR_TESTRAMP_SETTINGS_T(receiveData,inPtr)
	inPtr+=6
	# end of data handling
	
	return returnCode, data
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_SetMotionState(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(data.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_GetMotionState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_SetIndex(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(data,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_GetIndex():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUCHAR(receiveData,inPtr)
	inPtr+=1
	# end of data handling
	
	return returnCode, data
	
#End of Module: testRamp

def CLIENT_pkg_testRamp_GetMaxIndex():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00100008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUCHAR(receiveData,inPtr)
	inPtr+=1
	# end of data handling
	
	return returnCode, data
	
#End of Module: testRamp

# Begin Module: symbology
def CLIENT_pkg_symbology_SetEnable(draw_symbols):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write draw_symbols to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(draw_symbols.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateBitmap(ID, pos_X, pos_Y, width, height):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 9
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_SendData(ID, size, text):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 131
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write size to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(size,sendData,outPtr)
	outPtr += 2
	
	# write text to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(text,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateArc(ID, pos_X, pos_Y, width, height, start_angle, end_angle, color):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 21
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	# write start_angle to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(start_angle,sendData,outPtr)
	outPtr += 4
	
	# write end_angle to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(end_angle,sendData,outPtr)
	outPtr += 4
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateText(ID, pos_X, pos_Y, width, height, font, size, alignment, color, text):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 146
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	# write font to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	CHARToByte(font,sendData,outPtr)
	outPtr += 1
	
	# write size to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(size,sendData,outPtr)
	outPtr += 2
	
	# write alignment to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(alignment.value,sendData,outPtr)
	outPtr += 2
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	# write text to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(text,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_MoveSprite(ID, pos_X, pos_Y):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 5
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_AddToGroup(ID, group_ID):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write group_ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(group_ID,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_RemoveFromGroup(ID, group_ID):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write group_ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(group_ID,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_UpdateAndShow(ID, visible):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write visible to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(visible,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_UpdateAndShowGroup(group_ID, visible):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write group_ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(group_ID,sendData,outPtr)
	outPtr += 1
	
	# write visible to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(visible,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_Delete(ID):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_DeleteGroup(group_ID):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write group_ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(group_ID,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateFilledRectangle(ID, pos_X, pos_Y, width, height, color):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 13
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014000E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateOutlinedRectangle(ID, pos_X, pos_Y, width, height, color):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 13
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140010, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateBitmapFromPng(ID, pos_X, pos_Y, size):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 7
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write size to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(size,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140012, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateCompressedBitmap(ID, pos_X, pos_Y, width, height):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 9
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140014, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateBitmapFromPngFile(ID, pos_X, pos_Y, path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 133
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140016, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_ResetWritePosition(ID):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 1
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140018, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_MoveByOffset(ID, off_X, off_Y):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 5
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write off_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(off_X,sendData,outPtr)
	outPtr += 2
	
	# write off_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(off_Y,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140019, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_MoveGroupByOffset(ID, off_X, off_Y):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 5
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write off_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(off_X,sendData,outPtr)
	outPtr += 2
	
	# write off_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(off_Y,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateFilledEllipse(ID, pos_X, pos_Y, width, height, color):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 13
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write width to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(width,sendData,outPtr)
	outPtr += 2
	
	# write height to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(height,sendData,outPtr)
	outPtr += 2
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_CreateLine(ID, pos_X, pos_Y, pos_X2, pos_Y2, color):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 13
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	# write pos_X2 to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X2,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y2 to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y2,sendData,outPtr)
	outPtr += 2
	
	# write color to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(color,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_SetZorder(ID, zorder):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write zorder to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(zorder,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_SaveConfiguration():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001E, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_ReloadConfiguration():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0014001F, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_GetEnable():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140020, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read draw_symbols from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	draw_symbols = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of draw_symbols handling
	
	return returnCode, draw_symbols
	
#End of Module: symbology

def CLIENT_pkg_symbology_SetClonesNumber(ID, numberOfClones):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 2
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write numberOfClones to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(numberOfClones,sendData,outPtr)
	outPtr += 1
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140021, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_MoveCloneByOffset(ID, cloneID, pos_X, pos_Y):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 6
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write cloneID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(cloneID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140022, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

def CLIENT_pkg_symbology_MoveCloneSprite(ID, cloneID, pos_X, pos_Y):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 6
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write ID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(ID,sendData,outPtr)
	outPtr += 1
	
	# write cloneID to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(cloneID,sendData,outPtr)
	outPtr += 1
	
	# write pos_X to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_X,sendData,outPtr)
	outPtr += 2
	
	# write pos_Y to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_16ToByte(pos_Y,sendData,outPtr)
	outPtr += 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00140023, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: symbology

# Begin Module: fileOps
def CLIENT_pkg_fileOps_Dir():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read dirent from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	dirent = byteToUCHARArray(receiveData,inPtr,128)
	inPtr+=128
	# end of dirent handling
	
	return returnCode, dirent
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Cd(path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 128
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 128
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, pwd
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read pwd from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	pwd = byteToUCHARArray(receiveData,inPtr,128)
	inPtr+=128
	# end of pwd handling
	
	return returnCode, pwd
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Md(path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 128
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Fopen(path, mode):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 256
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, id
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	# write mode to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, id
	UCHARArrayToByte(mode,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read id from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	id = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of id handling
	
	return returnCode, id
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Fclose(id):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Fread(id, length):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 132
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, buf, ret
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	# write length to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, buf, ret
	UINT_32ToByte(length,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None
	
	inPtr = 0 #simple array index
	
	# read buf from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	buf = byteToUCHARArray(receiveData,inPtr,128)
	inPtr+=128
	# end of buf handling
	
	# read ret from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	ret = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of ret handling
	
	return returnCode, buf, ret
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Fwrite(id, length, buf):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 136
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, ret
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	# write length to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, ret
	UINT_32ToByte(length,sendData,outPtr)
	outPtr += 4
	
	# write buf to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, ret
	UCHARArrayToByte(buf,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read ret from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	ret = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of ret handling
	
	return returnCode, ret
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Ftell(id):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, offset
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read offset from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	offset = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of offset handling
	
	return returnCode, offset
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Fseek(id, offset, origin):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 12
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	# write offset to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(offset,sendData,outPtr)
	outPtr += 4
	
	# write origin to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(origin,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Ftruncate(id, length):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(id,sendData,outPtr)
	outPtr += 4
	
	# write length to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(length,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00160009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Rmdir(path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 128
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0016000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Rm(path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 128
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0016000B, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_Rename(oldpath, newpath):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 256
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write oldpath to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(oldpath,128,sendData,outPtr)
	outPtr += 128
	
	# write newpath to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARArrayToByte(newpath,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0016000C, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: fileOps

def CLIENT_pkg_fileOps_GetFileSize(path):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 128
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write path to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, fileLength
	UCHARArrayToByte(path,128,sendData,outPtr)
	outPtr += 128
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x0016000D, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read fileLength from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	fileLength = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of fileLength handling
	
	return returnCode, fileLength
	
#End of Module: fileOps

# Begin Module: jffs2
def CLIENT_pkg_jffs2_Mount():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00170001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: jffs2

def CLIENT_pkg_jffs2_Unmount():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00170002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: jffs2

def CLIENT_pkg_jffs2_GetState():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x00170007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read state from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	state = FLR_JFFS2_STATE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of state handling
	
	return returnCode, state
	
#End of Module: jffs2

# Begin Module: splashScreen
def CLIENT_pkg_splashScreen_SetDuration(screen_num, periodMs):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	# write periodMs to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(periodMs,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: splashScreen

def CLIENT_pkg_splashScreen_SetDataType(screen_num, filetype):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	# write filetype to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(filetype.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: splashScreen

def CLIENT_pkg_splashScreen_SetBackground(screen_num, backgroundColor):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	# write backgroundColor to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(backgroundColor,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: splashScreen

def CLIENT_pkg_splashScreen_GetDuration(screen_num):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, periodMs
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read periodMs from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	periodMs = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of periodMs handling
	
	return returnCode, periodMs
	
#End of Module: splashScreen

def CLIENT_pkg_splashScreen_GetDataType(screen_num):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, filetype
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read filetype from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	filetype = FLR_SPLASHSCREEN_FILETYPE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of filetype handling
	
	return returnCode, filetype
	
#End of Module: splashScreen

def CLIENT_pkg_splashScreen_GetBackground(screen_num):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write screen_num to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, backgroundColor
	UINT_32ToByte(screen_num,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001A0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read backgroundColor from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	backgroundColor = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of backgroundColor handling
	
	return returnCode, backgroundColor
	
#End of Module: splashScreen

# Begin Module: systemSymbols
def CLIENT_pkg_systemSymbols_GetID(symbol):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 5
	
	# write symbol to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, id, id_type
	INT_32ToByte(symbol.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001B0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None, None
	
	inPtr = 0 #simple array index
	
	# read id from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	id = byteToUCHAR(receiveData,inPtr)
	inPtr+=1
	# end of id handling
	
	# read id_type from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None, None
	id_type = FLR_SYSTEMSYMBOLS_ID_TYPE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of id_type handling
	
	return returnCode, id, id_type
	
#End of Module: systemSymbols

def CLIENT_pkg_systemSymbols_SetID(symbol, id, id_type):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 9
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write symbol to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(symbol.value,sendData,outPtr)
	outPtr += 4
	
	# write id to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UCHARToByte(id,sendData,outPtr)
	outPtr += 1
	
	# write id_type to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(id_type.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001B0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: systemSymbols

def CLIENT_pkg_systemSymbols_GetEnable(symbol):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	# write symbol to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, enabled
	INT_32ToByte(symbol.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001B0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read enabled from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	enabled = FLR_ENABLE_E(byteToINT_32(receiveData,inPtr))
	inPtr+=4
	# end of enabled handling
	
	return returnCode, enabled
	
#End of Module: systemSymbols

def CLIENT_pkg_systemSymbols_SetEnable(symbol, enabled):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write symbol to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(symbol.value,sendData,outPtr)
	outPtr += 4
	
	# write enabled to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	INT_32ToByte(enabled.value,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001B0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: systemSymbols

# Begin Module: sffc
def CLIENT_pkg_sffc_GetScaleFactor():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_GetDeltaTempLinearCoeff():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_SetDeltaTempLinearCoeff(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sffc

def CLIENT_pkg_sffc_GetDeltaTempOffsetCoeff():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_SetDeltaTempOffsetCoeff(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sffc

def CLIENT_pkg_sffc_GetFpaTempLinearCoeff():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_SetFpaTempLinearCoeff(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sffc

def CLIENT_pkg_sffc_GetFpaTempOffsetCoeff():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToFLOAT(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_SetFpaTempOffsetCoeff(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLOATToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sffc

def CLIENT_pkg_sffc_GetDeltaTempTimeLimitInSecs():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C0009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read data from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	data = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of data handling
	
	return returnCode, data
	
#End of Module: sffc

def CLIENT_pkg_sffc_SetDeltaTempTimeLimitInSecs(data):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 4
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write data to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	UINT_32ToByte(data,sendData,outPtr)
	outPtr += 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001C000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: sffc

# Begin Module: imageStats
def CLIENT_pkg_imageStats_GetTotalHistPixelsInROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0000, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read totalPixelsInROI from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	totalPixelsInROI = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of totalPixelsInROI handling
	
	return returnCode, totalPixelsInROI
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetPopBelowLowToHighThresh():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0001, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read popBelowLowToHighThresh from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	popBelowLowToHighThresh = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of popBelowLowToHighThresh handling
	
	return returnCode, popBelowLowToHighThresh
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetPopAboveHighToLowThresh():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 4
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0002, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read popAboveHighToLowThresh from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	popAboveHighToLowThresh = byteToUINT_32(receiveData,inPtr)
	inPtr+=4
	# end of popAboveHighToLowThresh handling
	
	return returnCode, popAboveHighToLowThresh
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_SetROI(roi):
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 8
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	# write roi to sendData buffer
	if(outPtr >= sendBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW
	FLR_ROI_TToByte(roi,sendData,outPtr)
	outPtr += 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0003, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 8
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0004, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read roi from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	roi = byteToFLR_ROI_T(receiveData,inPtr)
	inPtr+=8
	# end of roi handling
	
	return returnCode, roi
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetFirstBin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0005, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read firstBin from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	firstBin = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of firstBin handling
	
	return returnCode, firstBin
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetLastBin():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0006, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read lastBin from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	lastBin = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of lastBin handling
	
	return returnCode, lastBin
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetMean():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0007, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read mean from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	mean = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of mean handling
	
	return returnCode, mean
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetFirstBinInROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0008, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read firstBinInROI from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	firstBinInROI = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of firstBinInROI handling
	
	return returnCode, firstBinInROI
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetLastBinInROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D0009, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read lastBinInROI from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	lastBinInROI = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of lastBinInROI handling
	
	return returnCode, lastBinInROI
	
#End of Module: imageStats

def CLIENT_pkg_imageStats_GetMeanInROI():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 2
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0x001D000A, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode, None
	
	inPtr = 0 #simple array index
	
	# read meanInROI from receiveData buffer
	if(inPtr >= expectedReceiveBytes):
		return FLR_RESULT.R_API_PKG_BUFFER_OVERFLOW, None
	meanInROI = byteToUINT_16(receiveData,inPtr)
	inPtr+=2
	# end of meanInROI handling
	
	return returnCode, meanInROI
	
#End of Module: imageStats

# Begin Module: dummy
def CLIENT_pkg_dummy_BadCommand():
	global __commandCount
	# Create bytearray object for inputs
	sendBytes = 0
	sendData = bytearray(sendBytes)
	outPtr = 0 #simple array index in python
	expectedReceiveBytes = 0
	
	returnCode, receiveData = CLIENT_dispatch(__commandCount, 0xDEADBEEF, sendData, sendBytes, expectedReceiveBytes)
	__commandCount = fixSpecialBytes(__commandCount+1)
	
	# Check for any errorcode
	if(returnCode.value):
		return returnCode
	
	inPtr = 0 #simple array index
	
	return returnCode
	
#End of Module: dummy

