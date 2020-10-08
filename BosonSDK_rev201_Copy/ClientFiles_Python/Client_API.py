#  /////////////////////////////////////////////////////
#  // DO NOT EDIT.  This is a machine generated file. //
#  /////////////////////////////////////////////////////

from .Client_Packager import *
from .EnumTypes import *
from .ReturnCodes import FLR_RESULT,SendToCameraList


from .EmulatorFiles.UART_HalfDuplex import UART

def Initialize(manualini=None,manualport=None,manualbaud=None,uselegacy=False):
	uart = UART(useLegacy=uselegacy) #Open the UART dll
	if manualini:
		uart.OpenPort(ini_name=manualini,manual_port=manualport,manual_baud=manualbaud)
	else:
		uart.OpenPort(manual_port=manualport,manual_baud=manualbaud)
	SendToCameraList.insert(0,uart.SendToCamera)
	SendToCameraList.insert(1,uart.SendFrame)
	SendToCameraList.insert(2,uart.ReadFrame)
	return uart

def Close(uart):
	uart.ClosePort()
	uart.close()

MaxMemoryChunk = 256

def gaoSetGainState(data):
	'''Usage: returnCode = SetGainState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetGainState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetGainState()


def gaoGetGainState():
	'''Usage: returnCode, data = GetGainState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetGainState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetGainState()


def gaoSetFfcState(data):
	'''Usage: returnCode = SetFfcState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetFfcState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFfcState()


def gaoGetFfcState():
	'''Usage: returnCode, data = GetFfcState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetFfcState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFfcState()


def gaoSetTempCorrectionState(data):
	'''Usage: returnCode = SetTempCorrectionState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetTempCorrectionState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetTempCorrectionState()


def gaoGetTempCorrectionState():
	'''Usage: returnCode, data = GetTempCorrectionState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetTempCorrectionState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetTempCorrectionState()


def gaoSetIConstL(data):
	'''Usage: returnCode = SetIConstL(data)
		Input_01 data <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetIConstL(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetIConstL()


def gaoGetIConstL():
	'''Usage: returnCode, data = GetIConstL()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<INT_16>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetIConstL()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetIConstL()


def gaoSetIConstM(data):
	'''Usage: returnCode = SetIConstM(data)
		Input_01 data <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetIConstM(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetIConstM()


def gaoGetIConstM():
	'''Usage: returnCode, data = GetIConstM()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<INT_16>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetIConstM()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetIConstM()


def gaoSetAveragerState(data):
	'''Usage: returnCode = SetAveragerState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetAveragerState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetAveragerState()


def gaoGetAveragerState():
	'''Usage: returnCode, data = GetAveragerState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetAveragerState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetAveragerState()


def gaoSetNumFFCFrames(data):
	'''Usage: returnCode = SetNumFFCFrames(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetNumFFCFrames(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetNumFFCFrames()


def gaoGetNumFFCFrames():
	'''Usage: returnCode, data = GetNumFFCFrames()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetNumFFCFrames()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetNumFFCFrames()


def gaoGetAveragerThreshold():
	'''Usage: returnCode, data = GetAveragerThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetAveragerThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetAveragerThreshold()


def gaoGetRnsState():
	'''Usage: returnCode, data = GetRnsState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetRnsState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetRnsState()


def gaoSetTestRampState(data):
	'''Usage: returnCode = SetTestRampState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetTestRampState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetTestRampState()


def gaoGetTestRampState():
	'''Usage: returnCode, data = GetTestRampState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetTestRampState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetTestRampState()


def gaoSetSffcState(data):
	'''Usage: returnCode = SetSffcState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetSffcState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetSffcState()


def gaoGetSffcState():
	'''Usage: returnCode, data = GetSffcState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetSffcState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSffcState()


def gaoSetRpmState(data):
	'''Usage: returnCode = SetRpmState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetRpmState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetRpmState()


def gaoGetRpmState():
	'''Usage: returnCode, data = GetRpmState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetRpmState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetRpmState()


def gaoGetRpmThreshold():
	'''Usage: returnCode, threshold = GetRpmThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 threshold <class 'int'> <<UINT_16>>
	'''
	returnCode, threshold = CLIENT_pkg_gao_GetRpmThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, threshold)
# End of GetRpmThreshold()


def gaoSetFfcZeroMeanState(data):
	'''Usage: returnCode = SetFfcZeroMeanState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_gao_SetFfcZeroMeanState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFfcZeroMeanState()


def gaoGetFfcZeroMeanState():
	'''Usage: returnCode, data = GetFfcZeroMeanState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_gao_GetFfcZeroMeanState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFfcZeroMeanState()


def roicGetFPATemp():
	'''Usage: returnCode, data = GetFPATemp()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetFPATemp()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFPATemp()


def roicGetFrameCount():
	'''Usage: returnCode, data = GetFrameCount()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetFrameCount()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFrameCount()


def roicGetActiveNormalizationTarget():
	'''Usage: returnCode, data = GetActiveNormalizationTarget()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetActiveNormalizationTarget()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetActiveNormalizationTarget()


def roicSetFPARampState(state):
	'''Usage: returnCode = SetFPARampState(state)
		Input_01 state FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_roic_SetFPARampState(state)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFPARampState()


def roicGetFPARampState():
	'''Usage: returnCode, state = GetFPARampState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 state FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, state = CLIENT_pkg_roic_GetFPARampState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, state)
# End of GetFPARampState()


def roicGetSensorADC1():
	'''Usage: returnCode, data = GetSensorADC1()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetSensorADC1()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSensorADC1()


def roicGetSensorADC2():
	'''Usage: returnCode, data = GetSensorADC2()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetSensorADC2()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSensorADC2()


def roicSetFPATempOffset(data):
	'''Usage: returnCode = SetFPATempOffset(data)
		Input_01 data <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_roic_SetFPATempOffset(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFPATempOffset()


def roicGetFPATempOffset():
	'''Usage: returnCode, data = GetFPATempOffset()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<INT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetFPATempOffset()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFPATempOffset()


def roicSetFPATempMode(data):
	'''Usage: returnCode = SetFPATempMode(data)
		Input_01 data FLR_ROIC_TEMP_MODE_E <<FLR_ROIC_TEMP_MODE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_roic_SetFPATempMode(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFPATempMode()


def roicGetFPATempMode():
	'''Usage: returnCode, data = GetFPATempMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ROIC_TEMP_MODE_E <<FLR_ROIC_TEMP_MODE_E>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetFPATempMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFPATempMode()


def roicGetFPATempTable():
	'''Usage: returnCode, table = GetFPATempTable()
		Output_00 returnCode <FLR_RESULT>
		Output_01 table FLR_ROIC_FPATEMP_TABLE_T <<FLR_ROIC_FPATEMP_TABLE_T>>
	'''
	returnCode, table = CLIENT_pkg_roic_GetFPATempTable()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, table)
# End of GetFPATempTable()


def roicSetFPATempValue(data):
	'''Usage: returnCode = SetFPATempValue(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_roic_SetFPATempValue(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFPATempValue()


def roicGetFPATempValue():
	'''Usage: returnCode, data = GetFPATempValue()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_roic_GetFPATempValue()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFPATempValue()


def bprSetState(data):
	'''Usage: returnCode = SetState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_bpr_SetState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetState()


def bprGetState():
	'''Usage: returnCode, data = GetState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_bpr_GetState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetState()


def telemetrySetState(data):
	'''Usage: returnCode = SetState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_telemetry_SetState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetState()


def telemetryGetState():
	'''Usage: returnCode, data = GetState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_telemetry_GetState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetState()


def telemetrySetLocation(data):
	'''Usage: returnCode = SetLocation(data)
		Input_01 data FLR_TELEMETRY_LOC_E <<FLR_TELEMETRY_LOC_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_telemetry_SetLocation(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetLocation()


def telemetryGetLocation():
	'''Usage: returnCode, data = GetLocation()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_TELEMETRY_LOC_E <<FLR_TELEMETRY_LOC_E>>
	'''
	returnCode, data = CLIENT_pkg_telemetry_GetLocation()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetLocation()


def telemetrySetPacking(data):
	'''Usage: returnCode = SetPacking(data)
		Input_01 data FLR_TELEMETRY_PACKING_E <<FLR_TELEMETRY_PACKING_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_telemetry_SetPacking(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetPacking()


def telemetryGetPacking():
	'''Usage: returnCode, data = GetPacking()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_TELEMETRY_PACKING_E <<FLR_TELEMETRY_PACKING_E>>
	'''
	returnCode, data = CLIENT_pkg_telemetry_GetPacking()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetPacking()


def bosonGetCameraSN():
	'''Usage: returnCode, data = GetCameraSN()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetCameraSN()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetCameraSN()


def bosonGetCameraPN():
	'''Usage: returnCode, data = GetCameraPN()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_BOSON_PARTNUMBER_T <<FLR_BOSON_PARTNUMBER_T>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetCameraPN()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetCameraPN()


def bosonGetSensorSN():
	'''Usage: returnCode, data = GetSensorSN()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetSensorSN()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSensorSN()


def bosonRunFFC():
	'''Usage: returnCode = RunFFC()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_RunFFC()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of RunFFC()


def bosonSetFFCTempThreshold(data):
	'''Usage: returnCode = SetFFCTempThreshold(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetFFCTempThreshold(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFFCTempThreshold()


def bosonGetFFCTempThreshold():
	'''Usage: returnCode, data = GetFFCTempThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetFFCTempThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFFCTempThreshold()


def bosonSetFFCFrameThreshold(data):
	'''Usage: returnCode = SetFFCFrameThreshold(data)
		Input_01 data <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetFFCFrameThreshold(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFFCFrameThreshold()


def bosonGetFFCFrameThreshold():
	'''Usage: returnCode, data = GetFFCFrameThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetFFCFrameThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFFCFrameThreshold()


def bosonGetFFCInProgress():
	'''Usage: returnCode, data = GetFFCInProgress()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<INT_16>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetFFCInProgress()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFFCInProgress()


def bosonReboot():
	'''Usage: returnCode = Reboot()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_Reboot()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Reboot()


def bosonSetFFCMode(ffcMode):
	'''Usage: returnCode = SetFFCMode(ffcMode)
		Input_01 ffcMode FLR_BOSON_FFCMODE_E <<FLR_BOSON_FFCMODE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetFFCMode(ffcMode)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFFCMode()


def bosonGetFFCMode():
	'''Usage: returnCode, ffcMode = GetFFCMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 ffcMode FLR_BOSON_FFCMODE_E <<FLR_BOSON_FFCMODE_E>>
	'''
	returnCode, ffcMode = CLIENT_pkg_boson_GetFFCMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, ffcMode)
# End of GetFFCMode()


def bosonSetGainMode(gainMode):
	'''Usage: returnCode = SetGainMode(gainMode)
		Input_01 gainMode FLR_BOSON_GAINMODE_E <<FLR_BOSON_GAINMODE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetGainMode(gainMode)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetGainMode()


def bosonGetGainMode():
	'''Usage: returnCode, gainMode = GetGainMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 gainMode FLR_BOSON_GAINMODE_E <<FLR_BOSON_GAINMODE_E>>
	'''
	returnCode, gainMode = CLIENT_pkg_boson_GetGainMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, gainMode)
# End of GetGainMode()


def bosonWriteDynamicHeaderToFlash():
	'''Usage: returnCode = WriteDynamicHeaderToFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_WriteDynamicHeaderToFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of WriteDynamicHeaderToFlash()


def bosonReadDynamicHeaderFromFlash():
	'''Usage: returnCode = ReadDynamicHeaderFromFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_ReadDynamicHeaderFromFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of ReadDynamicHeaderFromFlash()


def bosonRestoreFactoryDefaultsFromFlash():
	'''Usage: returnCode = RestoreFactoryDefaultsFromFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_RestoreFactoryDefaultsFromFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of RestoreFactoryDefaultsFromFlash()


def bosonRestoreFactoryBadPixelsFromFlash():
	'''Usage: returnCode = RestoreFactoryBadPixelsFromFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_RestoreFactoryBadPixelsFromFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of RestoreFactoryBadPixelsFromFlash()


def bosonWriteBadPixelsToFlash():
	'''Usage: returnCode = WriteBadPixelsToFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_WriteBadPixelsToFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of WriteBadPixelsToFlash()


def bosonGetSoftwareRev():
	'''Usage: returnCode, major, minor, patch = GetSoftwareRev()
		Output_00 returnCode <FLR_RESULT>
		Output_01 major <class 'int'> <<UINT_32>>
		Output_02 minor <class 'int'> <<UINT_32>>
		Output_03 patch <class 'int'> <<UINT_32>>
	'''
	returnCode, major, minor, patch = CLIENT_pkg_boson_GetSoftwareRev()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None, None)
	
	return ( returnCode, major, minor, patch)
# End of GetSoftwareRev()


def bosonSetBadPixelLocation(row, col):
	'''Usage: returnCode = SetBadPixelLocation(row, col)
		Input_01 row <class 'int'> <<UINT_32>>
		Input_02 col <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetBadPixelLocation(row, col)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetBadPixelLocation()


def bosonlookupFPATempDegCx10():
	'''Usage: returnCode, data = lookupFPATempDegCx10()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<INT_16>>
	'''
	returnCode, data = CLIENT_pkg_boson_lookupFPATempDegCx10()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of lookupFPATempDegCx10()


def bosonlookupFPATempDegKx10():
	'''Usage: returnCode, data = lookupFPATempDegKx10()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_boson_lookupFPATempDegKx10()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of lookupFPATempDegKx10()


def bosonWriteLensNvFfcToFlash():
	'''Usage: returnCode = WriteLensNvFfcToFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_WriteLensNvFfcToFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of WriteLensNvFfcToFlash()


def bosonWriteLensGainToFlash():
	'''Usage: returnCode = WriteLensGainToFlash()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_WriteLensGainToFlash()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of WriteLensGainToFlash()


def bosonSetLensNumber(lensNumber):
	'''Usage: returnCode = SetLensNumber(lensNumber)
		Input_01 lensNumber <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetLensNumber(lensNumber)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetLensNumber()


def bosonGetLensNumber():
	'''Usage: returnCode, lensNumber = GetLensNumber()
		Output_00 returnCode <FLR_RESULT>
		Output_01 lensNumber <class 'int'> <<UINT_32>>
	'''
	returnCode, lensNumber = CLIENT_pkg_boson_GetLensNumber()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, lensNumber)
# End of GetLensNumber()


def bosonSetTableNumber(tableNumber):
	'''Usage: returnCode = SetTableNumber(tableNumber)
		Input_01 tableNumber <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetTableNumber(tableNumber)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetTableNumber()


def bosonGetTableNumber():
	'''Usage: returnCode, tableNumber = GetTableNumber()
		Output_00 returnCode <FLR_RESULT>
		Output_01 tableNumber <class 'int'> <<UINT_32>>
	'''
	returnCode, tableNumber = CLIENT_pkg_boson_GetTableNumber()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, tableNumber)
# End of GetTableNumber()


def bosonGetSensorPN():
	'''Usage: returnCode, sensorPN = GetSensorPN()
		Output_00 returnCode <FLR_RESULT>
		Output_01 sensorPN FLR_BOSON_SENSOR_PARTNUMBER_T <<FLR_BOSON_SENSOR_PARTNUMBER_T>>
	'''
	returnCode, sensorPN = CLIENT_pkg_boson_GetSensorPN()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, sensorPN)
# End of GetSensorPN()


def bosonSetGainSwitchParams(parm_struct):
	'''Usage: returnCode = SetGainSwitchParams(parm_struct)
		Input_01 parm_struct FLR_BOSON_GAIN_SWITCH_PARAMS_T <<FLR_BOSON_GAIN_SWITCH_PARAMS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetGainSwitchParams(parm_struct)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetGainSwitchParams()


def bosonGetGainSwitchParams():
	'''Usage: returnCode, parm_struct = GetGainSwitchParams()
		Output_00 returnCode <FLR_RESULT>
		Output_01 parm_struct FLR_BOSON_GAIN_SWITCH_PARAMS_T <<FLR_BOSON_GAIN_SWITCH_PARAMS_T>>
	'''
	returnCode, parm_struct = CLIENT_pkg_boson_GetGainSwitchParams()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, parm_struct)
# End of GetGainSwitchParams()


def bosonGetSwitchToHighGainFlag():
	'''Usage: returnCode, switchToHighGainFlag = GetSwitchToHighGainFlag()
		Output_00 returnCode <FLR_RESULT>
		Output_01 switchToHighGainFlag <class 'int'> <<UCHAR>>
	'''
	returnCode, switchToHighGainFlag = CLIENT_pkg_boson_GetSwitchToHighGainFlag()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, switchToHighGainFlag)
# End of GetSwitchToHighGainFlag()


def bosonGetSwitchToLowGainFlag():
	'''Usage: returnCode, switchToLowGainFlag = GetSwitchToLowGainFlag()
		Output_00 returnCode <FLR_RESULT>
		Output_01 switchToLowGainFlag <class 'int'> <<UCHAR>>
	'''
	returnCode, switchToLowGainFlag = CLIENT_pkg_boson_GetSwitchToLowGainFlag()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, switchToLowGainFlag)
# End of GetSwitchToLowGainFlag()


def bosonGetCLowToHighPercent():
	'''Usage: returnCode, cLowToHighPercent = GetCLowToHighPercent()
		Output_00 returnCode <FLR_RESULT>
		Output_01 cLowToHighPercent <class 'int'> <<UINT_32>>
	'''
	returnCode, cLowToHighPercent = CLIENT_pkg_boson_GetCLowToHighPercent()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, cLowToHighPercent)
# End of GetCLowToHighPercent()


def bosonGetMaxNUCTables():
	'''Usage: returnCode, maxNUCTables = GetMaxNUCTables()
		Output_00 returnCode <FLR_RESULT>
		Output_01 maxNUCTables <class 'int'> <<UINT_32>>
	'''
	returnCode, maxNUCTables = CLIENT_pkg_boson_GetMaxNUCTables()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, maxNUCTables)
# End of GetMaxNUCTables()


def bosonGetMaxLensTables():
	'''Usage: returnCode, maxLensTables = GetMaxLensTables()
		Output_00 returnCode <FLR_RESULT>
		Output_01 maxLensTables <class 'int'> <<UINT_32>>
	'''
	returnCode, maxLensTables = CLIENT_pkg_boson_GetMaxLensTables()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, maxLensTables)
# End of GetMaxLensTables()


def bosonGetFfcWaitCloseFrames():
	'''Usage: returnCode, data = GetFfcWaitCloseFrames()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_boson_GetFfcWaitCloseFrames()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFfcWaitCloseFrames()


def bosonSetFfcWaitCloseFrames(data):
	'''Usage: returnCode = SetFfcWaitCloseFrames(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetFfcWaitCloseFrames(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFfcWaitCloseFrames()


def bosonCheckForTableSwitch():
	'''Usage: returnCode = CheckForTableSwitch()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_CheckForTableSwitch()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CheckForTableSwitch()


def bosonGetDesiredTableNumber():
	'''Usage: returnCode, desiredTableNumber = GetDesiredTableNumber()
		Output_00 returnCode <FLR_RESULT>
		Output_01 desiredTableNumber <class 'int'> <<UINT_32>>
	'''
	returnCode, desiredTableNumber = CLIENT_pkg_boson_GetDesiredTableNumber()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, desiredTableNumber)
# End of GetDesiredTableNumber()


def bosonGetFfcStatus():
	'''Usage: returnCode, ffcStatus = GetFfcStatus()
		Output_00 returnCode <FLR_RESULT>
		Output_01 ffcStatus FLR_BOSON_FFCSTATUS_E <<FLR_BOSON_FFCSTATUS_E>>
	'''
	returnCode, ffcStatus = CLIENT_pkg_boson_GetFfcStatus()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, ffcStatus)
# End of GetFfcStatus()


def bosonGetFfcDesired():
	'''Usage: returnCode, ffcDesired = GetFfcDesired()
		Output_00 returnCode <FLR_RESULT>
		Output_01 ffcDesired <class 'int'> <<UINT_32>>
	'''
	returnCode, ffcDesired = CLIENT_pkg_boson_GetFfcDesired()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, ffcDesired)
# End of GetFfcDesired()


def bosonGetSwRevInHeader():
	'''Usage: returnCode, major, minor, patch = GetSwRevInHeader()
		Output_00 returnCode <FLR_RESULT>
		Output_01 major <class 'int'> <<UINT_32>>
		Output_02 minor <class 'int'> <<UINT_32>>
		Output_03 patch <class 'int'> <<UINT_32>>
	'''
	returnCode, major, minor, patch = CLIENT_pkg_boson_GetSwRevInHeader()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None, None)
	
	return ( returnCode, major, minor, patch)
# End of GetSwRevInHeader()


def bosonGetLastFFCFrameCount():
	'''Usage: returnCode, frameCount = GetLastFFCFrameCount()
		Output_00 returnCode <FLR_RESULT>
		Output_01 frameCount <class 'int'> <<UINT_32>>
	'''
	returnCode, frameCount = CLIENT_pkg_boson_GetLastFFCFrameCount()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, frameCount)
# End of GetLastFFCFrameCount()


def bosonGetLastFFCTempDegKx10():
	'''Usage: returnCode, temp = GetLastFFCTempDegKx10()
		Output_00 returnCode <FLR_RESULT>
		Output_01 temp <class 'int'> <<UINT_16>>
	'''
	returnCode, temp = CLIENT_pkg_boson_GetLastFFCTempDegKx10()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, temp)
# End of GetLastFFCTempDegKx10()


def bosonGetTableSwitchDesired():
	'''Usage: returnCode, tableSwitchDesired = GetTableSwitchDesired()
		Output_00 returnCode <FLR_RESULT>
		Output_01 tableSwitchDesired <class 'int'> <<UINT_16>>
	'''
	returnCode, tableSwitchDesired = CLIENT_pkg_boson_GetTableSwitchDesired()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, tableSwitchDesired)
# End of GetTableSwitchDesired()


def bosonGetOverTempThreshold():
	'''Usage: returnCode, temperatureInC = GetOverTempThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 temperatureInC <class 'float'> <<FLOAT>>
	'''
	returnCode, temperatureInC = CLIENT_pkg_boson_GetOverTempThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, temperatureInC)
# End of GetOverTempThreshold()


def bosonGetLowPowerMode():
	'''Usage: returnCode, lowPowerMode = GetLowPowerMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 lowPowerMode <class 'int'> <<UINT_16>>
	'''
	returnCode, lowPowerMode = CLIENT_pkg_boson_GetLowPowerMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, lowPowerMode)
# End of GetLowPowerMode()


def bosonGetOverTempEventOccurred():
	'''Usage: returnCode, overTempEventOccurred = GetOverTempEventOccurred()
		Output_00 returnCode <FLR_RESULT>
		Output_01 overTempEventOccurred <class 'int'> <<UINT_16>>
	'''
	returnCode, overTempEventOccurred = CLIENT_pkg_boson_GetOverTempEventOccurred()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, overTempEventOccurred)
# End of GetOverTempEventOccurred()


def bosonSetPermitThermalShutdownOverride(permitThermalShutdownOverride):
	'''Usage: returnCode = SetPermitThermalShutdownOverride(permitThermalShutdownOverride)
		Input_01 permitThermalShutdownOverride FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetPermitThermalShutdownOverride(permitThermalShutdownOverride)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetPermitThermalShutdownOverride()


def bosonGetPermitThermalShutdownOverride():
	'''Usage: returnCode, permitThermalShutdownOverride = GetPermitThermalShutdownOverride()
		Output_00 returnCode <FLR_RESULT>
		Output_01 permitThermalShutdownOverride FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, permitThermalShutdownOverride = CLIENT_pkg_boson_GetPermitThermalShutdownOverride()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, permitThermalShutdownOverride)
# End of GetPermitThermalShutdownOverride()


def bosonGetMyriadTemp():
	'''Usage: returnCode, myriadTemp = GetMyriadTemp()
		Output_00 returnCode <FLR_RESULT>
		Output_01 myriadTemp <class 'float'> <<FLOAT>>
	'''
	returnCode, myriadTemp = CLIENT_pkg_boson_GetMyriadTemp()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, myriadTemp)
# End of GetMyriadTemp()


def bosonGetNvFFCNucTableNumberLens0():
	'''Usage: returnCode, nvFFCNucTableNumberLens0 = GetNvFFCNucTableNumberLens0()
		Output_00 returnCode <FLR_RESULT>
		Output_01 nvFFCNucTableNumberLens0 <class 'int'> <<INT_32>>
	'''
	returnCode, nvFFCNucTableNumberLens0 = CLIENT_pkg_boson_GetNvFFCNucTableNumberLens0()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, nvFFCNucTableNumberLens0)
# End of GetNvFFCNucTableNumberLens0()


def bosonGetNvFFCNucTableNumberLens1():
	'''Usage: returnCode, nvFFCNucTableNumberLens1 = GetNvFFCNucTableNumberLens1()
		Output_00 returnCode <FLR_RESULT>
		Output_01 nvFFCNucTableNumberLens1 <class 'int'> <<INT_32>>
	'''
	returnCode, nvFFCNucTableNumberLens1 = CLIENT_pkg_boson_GetNvFFCNucTableNumberLens1()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, nvFFCNucTableNumberLens1)
# End of GetNvFFCNucTableNumberLens1()


def bosonGetNvFFCFPATempDegKx10Lens0():
	'''Usage: returnCode, nvFFCFPATempDegKx10Lens0 = GetNvFFCFPATempDegKx10Lens0()
		Output_00 returnCode <FLR_RESULT>
		Output_01 nvFFCFPATempDegKx10Lens0 <class 'int'> <<UINT_16>>
	'''
	returnCode, nvFFCFPATempDegKx10Lens0 = CLIENT_pkg_boson_GetNvFFCFPATempDegKx10Lens0()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, nvFFCFPATempDegKx10Lens0)
# End of GetNvFFCFPATempDegKx10Lens0()


def bosonGetNvFFCFPATempDegKx10Lens1():
	'''Usage: returnCode, nvFFCFPATempDegKx10Lens1 = GetNvFFCFPATempDegKx10Lens1()
		Output_00 returnCode <FLR_RESULT>
		Output_01 nvFFCFPATempDegKx10Lens1 <class 'int'> <<UINT_16>>
	'''
	returnCode, nvFFCFPATempDegKx10Lens1 = CLIENT_pkg_boson_GetNvFFCFPATempDegKx10Lens1()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, nvFFCFPATempDegKx10Lens1)
# End of GetNvFFCFPATempDegKx10Lens1()


def bosonSetFFCWarnTimeInSecx10(ffcWarnTime):
	'''Usage: returnCode = SetFFCWarnTimeInSecx10(ffcWarnTime)
		Input_01 ffcWarnTime <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetFFCWarnTimeInSecx10(ffcWarnTime)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFFCWarnTimeInSecx10()


def bosonGetFFCWarnTimeInSecx10():
	'''Usage: returnCode, ffcWarnTime = GetFFCWarnTimeInSecx10()
		Output_00 returnCode <FLR_RESULT>
		Output_01 ffcWarnTime <class 'int'> <<UINT_16>>
	'''
	returnCode, ffcWarnTime = CLIENT_pkg_boson_GetFFCWarnTimeInSecx10()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, ffcWarnTime)
# End of GetFFCWarnTimeInSecx10()


def bosonGetOverTempEventCounter():
	'''Usage: returnCode, overTempEventCounter = GetOverTempEventCounter()
		Output_00 returnCode <FLR_RESULT>
		Output_01 overTempEventCounter <class 'int'> <<UINT_32>>
	'''
	returnCode, overTempEventCounter = CLIENT_pkg_boson_GetOverTempEventCounter()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, overTempEventCounter)
# End of GetOverTempEventCounter()


def bosonSetOverTempTimerInSec(overTempTimerInSec):
	'''Usage: returnCode = SetOverTempTimerInSec(overTempTimerInSec)
		Input_01 overTempTimerInSec <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetOverTempTimerInSec(overTempTimerInSec)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOverTempTimerInSec()


def bosonGetOverTempTimerInSec():
	'''Usage: returnCode, overTempTimerInSec = GetOverTempTimerInSec()
		Output_00 returnCode <FLR_RESULT>
		Output_01 overTempTimerInSec <class 'int'> <<UINT_16>>
	'''
	returnCode, overTempTimerInSec = CLIENT_pkg_boson_GetOverTempTimerInSec()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, overTempTimerInSec)
# End of GetOverTempTimerInSec()


def bosonUnloadCurrentLensCorrections():
	'''Usage: returnCode = UnloadCurrentLensCorrections()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_UnloadCurrentLensCorrections()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of UnloadCurrentLensCorrections()


def bosonSetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs):
	'''Usage: returnCode = SetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs)
		Input_01 timeForQuickFFCsInSecs <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetTimeForQuickFFCsInSecs()


def bosonGetTimeForQuickFFCsInSecs():
	'''Usage: returnCode, timeForQuickFFCsInSecs = GetTimeForQuickFFCsInSecs()
		Output_00 returnCode <FLR_RESULT>
		Output_01 timeForQuickFFCsInSecs <class 'int'> <<UINT_32>>
	'''
	returnCode, timeForQuickFFCsInSecs = CLIENT_pkg_boson_GetTimeForQuickFFCsInSecs()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, timeForQuickFFCsInSecs)
# End of GetTimeForQuickFFCsInSecs()


def bosonReloadCurrentLensCorrections():
	'''Usage: returnCode = ReloadCurrentLensCorrections()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_ReloadCurrentLensCorrections()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of ReloadCurrentLensCorrections()


def bosonGetBootTimestamps():
	'''Usage: returnCode, FirstLight, StartInit, BosonExecDone, Timestamp4 = GetBootTimestamps()
		Output_00 returnCode <FLR_RESULT>
		Output_01 FirstLight <class 'float'> <<FLOAT>>
		Output_02 StartInit <class 'float'> <<FLOAT>>
		Output_03 BosonExecDone <class 'float'> <<FLOAT>>
		Output_04 Timestamp4 <class 'float'> <<FLOAT>>
	'''
	returnCode, FirstLight, StartInit, BosonExecDone, Timestamp4 = CLIENT_pkg_boson_GetBootTimestamps()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None, None, None)
	
	return ( returnCode, FirstLight, StartInit, BosonExecDone, Timestamp4)
# End of GetBootTimestamps()


def bosonSetExtSyncMode(mode):
	'''Usage: returnCode = SetExtSyncMode(mode)
		Input_01 mode FLR_BOSON_EXT_SYNC_MODE_E <<FLR_BOSON_EXT_SYNC_MODE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_boson_SetExtSyncMode(mode)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetExtSyncMode()


def bosonGetExtSyncMode():
	'''Usage: returnCode, mode = GetExtSyncMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 mode FLR_BOSON_EXT_SYNC_MODE_E <<FLR_BOSON_EXT_SYNC_MODE_E>>
	'''
	returnCode, mode = CLIENT_pkg_boson_GetExtSyncMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, mode)
# End of GetExtSyncMode()


def dvoSetAnalogVideoState(analogVideoState):
	'''Usage: returnCode = SetAnalogVideoState(analogVideoState)
		Input_01 analogVideoState FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetAnalogVideoState(analogVideoState)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetAnalogVideoState()


def dvoGetAnalogVideoState():
	'''Usage: returnCode, analogVideoState = GetAnalogVideoState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 analogVideoState FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, analogVideoState = CLIENT_pkg_dvo_GetAnalogVideoState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, analogVideoState)
# End of GetAnalogVideoState()


def dvoSetOutputFormat(format):
	'''Usage: returnCode = SetOutputFormat(format)
		Input_01 format FLR_DVO_OUTPUT_FORMAT_E <<FLR_DVO_OUTPUT_FORMAT_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetOutputFormat(format)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOutputFormat()


def dvoGetOutputFormat():
	'''Usage: returnCode, format = GetOutputFormat()
		Output_00 returnCode <FLR_RESULT>
		Output_01 format FLR_DVO_OUTPUT_FORMAT_E <<FLR_DVO_OUTPUT_FORMAT_E>>
	'''
	returnCode, format = CLIENT_pkg_dvo_GetOutputFormat()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, format)
# End of GetOutputFormat()


def dvoSetOutputYCbCrSettings(settings):
	'''Usage: returnCode = SetOutputYCbCrSettings(settings)
		Input_01 settings FLR_DVO_YCBCR_SETTINGS_T <<FLR_DVO_YCBCR_SETTINGS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetOutputYCbCrSettings(settings)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOutputYCbCrSettings()


def dvoGetOutputYCbCrSettings():
	'''Usage: returnCode, settings = GetOutputYCbCrSettings()
		Output_00 returnCode <FLR_RESULT>
		Output_01 settings FLR_DVO_YCBCR_SETTINGS_T <<FLR_DVO_YCBCR_SETTINGS_T>>
	'''
	returnCode, settings = CLIENT_pkg_dvo_GetOutputYCbCrSettings()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, settings)
# End of GetOutputYCbCrSettings()


def dvoSetOutputRGBSettings(settings):
	'''Usage: returnCode = SetOutputRGBSettings(settings)
		Input_01 settings FLR_DVO_RGB_SETTINGS_T <<FLR_DVO_RGB_SETTINGS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetOutputRGBSettings(settings)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOutputRGBSettings()


def dvoGetOutputRGBSettings():
	'''Usage: returnCode, settings = GetOutputRGBSettings()
		Output_00 returnCode <FLR_RESULT>
		Output_01 settings FLR_DVO_RGB_SETTINGS_T <<FLR_DVO_RGB_SETTINGS_T>>
	'''
	returnCode, settings = CLIENT_pkg_dvo_GetOutputRGBSettings()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, settings)
# End of GetOutputRGBSettings()


def dvoApplyCustomSettings():
	'''Usage: returnCode = ApplyCustomSettings()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_ApplyCustomSettings()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of ApplyCustomSettings()


def dvoSetDisplayMode(displayMode):
	'''Usage: returnCode = SetDisplayMode(displayMode)
		Input_01 displayMode FLR_DVO_DISPLAY_MODE_E <<FLR_DVO_DISPLAY_MODE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetDisplayMode(displayMode)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDisplayMode()


def dvoGetDisplayMode():
	'''Usage: returnCode, displayMode = GetDisplayMode()
		Output_00 returnCode <FLR_RESULT>
		Output_01 displayMode FLR_DVO_DISPLAY_MODE_E <<FLR_DVO_DISPLAY_MODE_E>>
	'''
	returnCode, displayMode = CLIENT_pkg_dvo_GetDisplayMode()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, displayMode)
# End of GetDisplayMode()


def dvoSetType(tap):
	'''Usage: returnCode = SetType(tap)
		Input_01 tap FLR_DVO_TYPE_E <<FLR_DVO_TYPE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetType(tap)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetType()


def dvoGetType():
	'''Usage: returnCode, tap = GetType()
		Output_00 returnCode <FLR_RESULT>
		Output_01 tap FLR_DVO_TYPE_E <<FLR_DVO_TYPE_E>>
	'''
	returnCode, tap = CLIENT_pkg_dvo_GetType()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, tap)
# End of GetType()


def dvoSetVideoStandard(videoStandard):
	'''Usage: returnCode = SetVideoStandard(videoStandard)
		Input_01 videoStandard FLR_DVO_VIDEO_STANDARD_E <<FLR_DVO_VIDEO_STANDARD_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetVideoStandard(videoStandard)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetVideoStandard()


def dvoGetVideoStandard():
	'''Usage: returnCode, videoStandard = GetVideoStandard()
		Output_00 returnCode <FLR_RESULT>
		Output_01 videoStandard FLR_DVO_VIDEO_STANDARD_E <<FLR_DVO_VIDEO_STANDARD_E>>
	'''
	returnCode, videoStandard = CLIENT_pkg_dvo_GetVideoStandard()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, videoStandard)
# End of GetVideoStandard()


def dvoSetCheckVideoDacPresent(checkVideoDacPresent):
	'''Usage: returnCode = SetCheckVideoDacPresent(checkVideoDacPresent)
		Input_01 checkVideoDacPresent FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dvo_SetCheckVideoDacPresent(checkVideoDacPresent)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetCheckVideoDacPresent()


def dvoGetCheckVideoDacPresent():
	'''Usage: returnCode, checkVideoDacPresent = GetCheckVideoDacPresent()
		Output_00 returnCode <FLR_RESULT>
		Output_01 checkVideoDacPresent FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, checkVideoDacPresent = CLIENT_pkg_dvo_GetCheckVideoDacPresent()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, checkVideoDacPresent)
# End of GetCheckVideoDacPresent()


def captureSingleFrame():
	'''Usage: returnCode = SingleFrame()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_capture_SingleFrame()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SingleFrame()


def captureFrames(data):
	'''Usage: returnCode = Frames(data)
		Input_01 data FLR_CAPTURE_SETTINGS_T <<FLR_CAPTURE_SETTINGS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_capture_Frames(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Frames()


def captureSingleFrameWithSrc(data):
	'''Usage: returnCode = SingleFrameWithSrc(data)
		Input_01 data FLR_CAPTURE_SRC_E <<FLR_CAPTURE_SRC_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_capture_SingleFrameWithSrc(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SingleFrameWithSrc()


def captureSingleFrameToFile():
	'''Usage: returnCode = SingleFrameToFile()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_capture_SingleFrameToFile()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SingleFrameToFile()


def scnrSetEnableState(data):
	'''Usage: returnCode = SetEnableState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetEnableState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetEnableState()


def scnrGetEnableState():
	'''Usage: returnCode, data = GetEnableState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetEnableState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetEnableState()


def scnrSetThColSum(data):
	'''Usage: returnCode = SetThColSum(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetThColSum(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetThColSum()


def scnrGetThColSum():
	'''Usage: returnCode, data = GetThColSum()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetThColSum()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetThColSum()


def scnrSetThPixel(data):
	'''Usage: returnCode = SetThPixel(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetThPixel(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetThPixel()


def scnrGetThPixel():
	'''Usage: returnCode, data = GetThPixel()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetThPixel()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetThPixel()


def scnrSetMaxCorr(data):
	'''Usage: returnCode = SetMaxCorr(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetMaxCorr(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetMaxCorr()


def scnrGetMaxCorr():
	'''Usage: returnCode, data = GetMaxCorr()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetMaxCorr()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxCorr()


def scnrGetThPixelApplied():
	'''Usage: returnCode, data = GetThPixelApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetThPixelApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetThPixelApplied()


def scnrGetMaxCorrApplied():
	'''Usage: returnCode, data = GetMaxCorrApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetMaxCorrApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxCorrApplied()


def scnrSetThColSumSafe(data):
	'''Usage: returnCode = SetThColSumSafe(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetThColSumSafe(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetThColSumSafe()


def scnrGetThColSumSafe():
	'''Usage: returnCode, data = GetThColSumSafe()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetThColSumSafe()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetThColSumSafe()


def scnrSetThPixelSafe(data):
	'''Usage: returnCode = SetThPixelSafe(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetThPixelSafe(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetThPixelSafe()


def scnrGetThPixelSafe():
	'''Usage: returnCode, data = GetThPixelSafe()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetThPixelSafe()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetThPixelSafe()


def scnrSetMaxCorrSafe(data):
	'''Usage: returnCode = SetMaxCorrSafe(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scnr_SetMaxCorrSafe(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetMaxCorrSafe()


def scnrGetMaxCorrSafe():
	'''Usage: returnCode, data = GetMaxCorrSafe()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_scnr_GetMaxCorrSafe()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxCorrSafe()


def agcSetPercentPerBin(data):
	'''Usage: returnCode = SetPercentPerBin(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0) or (data > 100):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetPercentPerBin(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetPercentPerBin()


def agcGetPercentPerBin():
	'''Usage: returnCode, data = GetPercentPerBin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetPercentPerBin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetPercentPerBin()


def agcSetLinearPercent(data):
	'''Usage: returnCode = SetLinearPercent(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0) or (data > 100):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetLinearPercent(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetLinearPercent()


def agcGetLinearPercent():
	'''Usage: returnCode, data = GetLinearPercent()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetLinearPercent()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetLinearPercent()


def agcSetOutlierCut(data):
	'''Usage: returnCode = SetOutlierCut(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0) or (data > 49):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetOutlierCut(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOutlierCut()


def agcGetOutlierCut():
	'''Usage: returnCode, data = GetOutlierCut()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetOutlierCut()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetOutlierCut()


def agcGetDrOut():
	'''Usage: returnCode, data = GetDrOut()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetDrOut()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDrOut()


def agcSetMaxGain(data):
	'''Usage: returnCode = SetMaxGain(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0.25) or (data > 8):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetMaxGain(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetMaxGain()


def agcGetMaxGain():
	'''Usage: returnCode, data = GetMaxGain()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetMaxGain()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxGain()


def agcSetdf(data):
	'''Usage: returnCode = Setdf(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0) or (data > 100):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_Setdf(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Setdf()


def agcGetdf():
	'''Usage: returnCode, data = Getdf()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_Getdf()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of Getdf()


def agcSetGamma(data):
	'''Usage: returnCode = SetGamma(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0.5) or (data > 4):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetGamma(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetGamma()


def agcGetGamma():
	'''Usage: returnCode, data = GetGamma()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetGamma()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetGamma()


def agcGetFirstBin():
	'''Usage: returnCode, data = GetFirstBin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetFirstBin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFirstBin()


def agcGetLastBin():
	'''Usage: returnCode, data = GetLastBin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetLastBin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetLastBin()


def agcSetDetailHeadroom(data):
	'''Usage: returnCode = SetDetailHeadroom(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0) or (data > 127):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetDetailHeadroom(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDetailHeadroom()


def agcGetDetailHeadroom():
	'''Usage: returnCode, data = GetDetailHeadroom()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetDetailHeadroom()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDetailHeadroom()


def agcSetd2br(data):
	'''Usage: returnCode = Setd2br(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0.0) or (data > 8):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_Setd2br(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Setd2br()


def agcGetd2br():
	'''Usage: returnCode, data = Getd2br()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_Getd2br()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of Getd2br()


def agcSetSigmaR(data):
	'''Usage: returnCode = SetSigmaR(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 1) or (data > 100000):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetSigmaR(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetSigmaR()


def agcGetSigmaR():
	'''Usage: returnCode, data = GetSigmaR()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetSigmaR()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSigmaR()


def agcSetUseEntropy(data):
	'''Usage: returnCode = SetUseEntropy(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_agc_SetUseEntropy(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetUseEntropy()


def agcGetUseEntropy():
	'''Usage: returnCode, data = GetUseEntropy()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetUseEntropy()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetUseEntropy()


def agcSetROI(roi):
	'''Usage: returnCode = SetROI(roi)
		Input_01 roi FLR_ROI_T <<FLR_ROI_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_agc_SetROI(roi)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetROI()


def agcGetROI():
	'''Usage: returnCode, roi = GetROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 roi FLR_ROI_T <<FLR_ROI_T>>
	'''
	returnCode, roi = CLIENT_pkg_agc_GetROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, roi)
# End of GetROI()


def agcGetMaxGainApplied():
	'''Usage: returnCode, data = GetMaxGainApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetMaxGainApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxGainApplied()


def agcGetSigmaRApplied():
	'''Usage: returnCode, data = GetSigmaRApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetSigmaRApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSigmaRApplied()


def agcSetOutlierCutBalance(data):
	'''Usage: returnCode = SetOutlierCutBalance(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	if (data < 0.0) or (data > 2.0):
		return ( FLR_RESULT['FLR_RANGE_ERROR'])
	returnCode = CLIENT_pkg_agc_SetOutlierCutBalance(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetOutlierCutBalance()


def agcGetOutlierCutBalance():
	'''Usage: returnCode, data = GetOutlierCutBalance()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_agc_GetOutlierCutBalance()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetOutlierCutBalance()


def agcGetOutlierCutApplied():
	'''Usage: returnCode, percentHigh, percentLow = GetOutlierCutApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 percentHigh <class 'float'> <<FLOAT>>
		Output_02 percentLow <class 'float'> <<FLOAT>>
	'''
	returnCode, percentHigh, percentLow = CLIENT_pkg_agc_GetOutlierCutApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None)
	
	return ( returnCode, percentHigh, percentLow)
# End of GetOutlierCutApplied()


def tfSetEnableState(data):
	'''Usage: returnCode = SetEnableState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_tf_SetEnableState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetEnableState()


def tfGetEnableState():
	'''Usage: returnCode, data = GetEnableState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetEnableState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetEnableState()


def tfSetDelta_nf(data):
	'''Usage: returnCode = SetDelta_nf(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_tf_SetDelta_nf(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDelta_nf()


def tfGetDelta_nf():
	'''Usage: returnCode, data = GetDelta_nf()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetDelta_nf()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDelta_nf()


def tfSetTHDeltaMotion(data):
	'''Usage: returnCode = SetTHDeltaMotion(data)
		Input_01 data <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_tf_SetTHDeltaMotion(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetTHDeltaMotion()


def tfGetTHDeltaMotion():
	'''Usage: returnCode, data = GetTHDeltaMotion()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetTHDeltaMotion()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetTHDeltaMotion()


def tfSetWLut(data):
	'''Usage: returnCode = SetWLut(data)
		Input_01 data FLR_TF_WLUT_T <<FLR_TF_WLUT_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_tf_SetWLut(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetWLut()


def tfGetWLut():
	'''Usage: returnCode, data = GetWLut()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_TF_WLUT_T <<FLR_TF_WLUT_T>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetWLut()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetWLut()


def tfGetMotionCount():
	'''Usage: returnCode, data = GetMotionCount()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetMotionCount()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMotionCount()


def tfSetMotionThreshold(data):
	'''Usage: returnCode = SetMotionThreshold(data)
		Input_01 data <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_tf_SetMotionThreshold(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetMotionThreshold()


def tfGetMotionThreshold():
	'''Usage: returnCode, data = GetMotionThreshold()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetMotionThreshold()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMotionThreshold()


def tfGetDelta_nfApplied():
	'''Usage: returnCode, data = GetDelta_nfApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetDelta_nfApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDelta_nfApplied()


def tfGetTHDeltaMotionApplied():
	'''Usage: returnCode, data = GetTHDeltaMotionApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_16>>
	'''
	returnCode, data = CLIENT_pkg_tf_GetTHDeltaMotionApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetTHDeltaMotionApplied()


def memReadCapture(bufferNum, offset, sizeInBytes):
	'''Usage: returnCode, data = ReadCapture(bufferNum, offset, sizeInBytes)
		Input_01 bufferNum <class 'int'> <<UCHAR>>
		Input_02 offset <class 'int'> <<UINT_32>>
		Input_03 sizeInBytes <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'bytearray'> <<BYTEARRAY>>
	'''
	returnCode, data = CLIENT_pkg_mem_ReadCapture(bufferNum, offset, sizeInBytes)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of ReadCapture()


def memGetCaptureSize():
	'''Usage: returnCode, bytes, rows, columns = GetCaptureSize()
		Output_00 returnCode <FLR_RESULT>
		Output_01 bytes <class 'int'> <<UINT_32>>
		Output_02 rows <class 'int'> <<UINT_16>>
		Output_03 columns <class 'int'> <<UINT_16>>
	'''
	returnCode, bytes, rows, columns = CLIENT_pkg_mem_GetCaptureSize()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None, None)
	
	return ( returnCode, bytes, rows, columns)
# End of GetCaptureSize()


def memWriteFlash(location, index, offset, sizeInBytes, data):
	'''Usage: returnCode = WriteFlash(location, index, offset, sizeInBytes, data)
		Input_01 location FLR_MEM_LOCATION_E <<FLR_MEM_LOCATION_E>>
		Input_02 index <class 'int'> <<UCHAR>>
		Input_03 offset <class 'int'> <<UINT_32>>
		Input_04 sizeInBytes <class 'int'> <<UINT_16>>
		Input_05 data <class 'bytearray'> <<BYTEARRAY>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_mem_WriteFlash(location, index, offset, sizeInBytes, data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of WriteFlash()


def memReadFlash(location, index, offset, sizeInBytes):
	'''Usage: returnCode, data = ReadFlash(location, index, offset, sizeInBytes)
		Input_01 location FLR_MEM_LOCATION_E <<FLR_MEM_LOCATION_E>>
		Input_02 index <class 'int'> <<UCHAR>>
		Input_03 offset <class 'int'> <<UINT_32>>
		Input_04 sizeInBytes <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'bytearray'> <<BYTEARRAY>>
	'''
	returnCode, data = CLIENT_pkg_mem_ReadFlash(location, index, offset, sizeInBytes)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of ReadFlash()


def memGetFlashSize(location):
	'''Usage: returnCode, bytes = GetFlashSize(location)
		Input_01 location FLR_MEM_LOCATION_E <<FLR_MEM_LOCATION_E>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 bytes <class 'int'> <<UINT_32>>
	'''
	returnCode, bytes = CLIENT_pkg_mem_GetFlashSize(location)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, bytes)
# End of GetFlashSize()


def memEraseFlash(location, index):
	'''Usage: returnCode = EraseFlash(location, index)
		Input_01 location FLR_MEM_LOCATION_E <<FLR_MEM_LOCATION_E>>
		Input_02 index <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_mem_EraseFlash(location, index)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of EraseFlash()


def memEraseFlashPartial(location, index, offset, length):
	'''Usage: returnCode = EraseFlashPartial(location, index, offset, length)
		Input_01 location FLR_MEM_LOCATION_E <<FLR_MEM_LOCATION_E>>
		Input_02 index <class 'int'> <<UCHAR>>
		Input_03 offset <class 'int'> <<UINT_32>>
		Input_04 length <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_mem_EraseFlashPartial(location, index, offset, length)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of EraseFlashPartial()


def memReadCurrentGain(offset, sizeInBytes):
	'''Usage: returnCode, data = ReadCurrentGain(offset, sizeInBytes)
		Input_01 offset <class 'int'> <<UINT_32>>
		Input_02 sizeInBytes <class 'int'> <<UINT_16>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'bytearray'> <<BYTEARRAY>>
	'''
	returnCode, data = CLIENT_pkg_mem_ReadCurrentGain(offset, sizeInBytes)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of ReadCurrentGain()


def memGetGainSize():
	'''Usage: returnCode, bytes, rows, columns = GetGainSize()
		Output_00 returnCode <FLR_RESULT>
		Output_01 bytes <class 'int'> <<UINT_32>>
		Output_02 rows <class 'int'> <<UINT_16>>
		Output_03 columns <class 'int'> <<UINT_16>>
	'''
	returnCode, bytes, rows, columns = CLIENT_pkg_mem_GetGainSize()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None, None)
	
	return ( returnCode, bytes, rows, columns)
# End of GetGainSize()


def colorLutSetControl(data):
	'''Usage: returnCode = SetControl(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_colorLut_SetControl(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetControl()


def colorLutGetControl():
	'''Usage: returnCode, data = GetControl()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_colorLut_GetControl()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetControl()


def colorLutSetId(data):
	'''Usage: returnCode = SetId(data)
		Input_01 data FLR_COLORLUT_ID_E <<FLR_COLORLUT_ID_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_colorLut_SetId(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetId()


def colorLutGetId():
	'''Usage: returnCode, data = GetId()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_COLORLUT_ID_E <<FLR_COLORLUT_ID_E>>
	'''
	returnCode, data = CLIENT_pkg_colorLut_GetId()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetId()


def spnrSetEnableState(data):
	'''Usage: returnCode = SetEnableState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetEnableState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetEnableState()


def spnrGetEnableState():
	'''Usage: returnCode, data = GetEnableState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_spnr_GetEnableState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetEnableState()


def spnrGetState():
	'''Usage: returnCode, data = GetState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_SPNR_STATE_E <<FLR_SPNR_STATE_E>>
	'''
	returnCode, data = CLIENT_pkg_spnr_GetState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetState()


def spnrSetFrameDelay(data):
	'''Usage: returnCode = SetFrameDelay(data)
		Input_01 data <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetFrameDelay(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFrameDelay()


def spnrGetFrameDelay():
	'''Usage: returnCode, data = GetFrameDelay()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_spnr_GetFrameDelay()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFrameDelay()


def spnrGetSFApplied():
	'''Usage: returnCode, sf = GetSFApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 sf <class 'float'> <<FLOAT>>
	'''
	returnCode, sf = CLIENT_pkg_spnr_GetSFApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, sf)
# End of GetSFApplied()


def spnrSetPSDKernel(data):
	'''Usage: returnCode = SetPSDKernel(data)
		Input_01 data FLR_SPNR_PSD_KERNEL_T <<FLR_SPNR_PSD_KERNEL_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetPSDKernel(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetPSDKernel()


def spnrGetPSDKernel():
	'''Usage: returnCode, data = GetPSDKernel()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_SPNR_PSD_KERNEL_T <<FLR_SPNR_PSD_KERNEL_T>>
	'''
	returnCode, data = CLIENT_pkg_spnr_GetPSDKernel()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetPSDKernel()


def spnrSetSFMin(sfmin):
	'''Usage: returnCode = SetSFMin(sfmin)
		Input_01 sfmin <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetSFMin(sfmin)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetSFMin()


def spnrGetSFMin():
	'''Usage: returnCode, sfmin = GetSFMin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 sfmin <class 'float'> <<FLOAT>>
	'''
	returnCode, sfmin = CLIENT_pkg_spnr_GetSFMin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, sfmin)
# End of GetSFMin()


def spnrSetSFMax(sfmax):
	'''Usage: returnCode = SetSFMax(sfmax)
		Input_01 sfmax <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetSFMax(sfmax)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetSFMax()


def spnrGetSFMax():
	'''Usage: returnCode, sfmax = GetSFMax()
		Output_00 returnCode <FLR_RESULT>
		Output_01 sfmax <class 'float'> <<FLOAT>>
	'''
	returnCode, sfmax = CLIENT_pkg_spnr_GetSFMax()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, sfmax)
# End of GetSFMax()


def spnrSetDFMin(dfmin):
	'''Usage: returnCode = SetDFMin(dfmin)
		Input_01 dfmin <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetDFMin(dfmin)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDFMin()


def spnrGetDFMin():
	'''Usage: returnCode, dfmin = GetDFMin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 dfmin <class 'float'> <<FLOAT>>
	'''
	returnCode, dfmin = CLIENT_pkg_spnr_GetDFMin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, dfmin)
# End of GetDFMin()


def spnrSetDFMax(dfmax):
	'''Usage: returnCode = SetDFMax(dfmax)
		Input_01 dfmax <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetDFMax(dfmax)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDFMax()


def spnrGetDFMax():
	'''Usage: returnCode, dfmax = GetDFMax()
		Output_00 returnCode <FLR_RESULT>
		Output_01 dfmax <class 'float'> <<FLOAT>>
	'''
	returnCode, dfmax = CLIENT_pkg_spnr_GetDFMax()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, dfmax)
# End of GetDFMax()


def spnrSetNormTarget(normTarget):
	'''Usage: returnCode = SetNormTarget(normTarget)
		Input_01 normTarget <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_spnr_SetNormTarget(normTarget)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetNormTarget()


def spnrGetNormTarget():
	'''Usage: returnCode, normTarget = GetNormTarget()
		Output_00 returnCode <FLR_RESULT>
		Output_01 normTarget <class 'float'> <<FLOAT>>
	'''
	returnCode, normTarget = CLIENT_pkg_spnr_GetNormTarget()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, normTarget)
# End of GetNormTarget()


def spnrGetNormTargetApplied():
	'''Usage: returnCode, normTargetApplied = GetNormTargetApplied()
		Output_00 returnCode <FLR_RESULT>
		Output_01 normTargetApplied <class 'float'> <<FLOAT>>
	'''
	returnCode, normTargetApplied = CLIENT_pkg_spnr_GetNormTargetApplied()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, normTargetApplied)
# End of GetNormTargetApplied()


def scalerGetMaxZoom():
	'''Usage: returnCode, zoom = GetMaxZoom()
		Output_00 returnCode <FLR_RESULT>
		Output_01 zoom <class 'int'> <<UINT_32>>
	'''
	returnCode, zoom = CLIENT_pkg_scaler_GetMaxZoom()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, zoom)
# End of GetMaxZoom()


def scalerSetZoom(zoomParams):
	'''Usage: returnCode = SetZoom(zoomParams)
		Input_01 zoomParams FLR_SCALER_ZOOM_PARAMS_T <<FLR_SCALER_ZOOM_PARAMS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scaler_SetZoom(zoomParams)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetZoom()


def scalerGetZoom():
	'''Usage: returnCode, zoomParams = GetZoom()
		Output_00 returnCode <FLR_RESULT>
		Output_01 zoomParams FLR_SCALER_ZOOM_PARAMS_T <<FLR_SCALER_ZOOM_PARAMS_T>>
	'''
	returnCode, zoomParams = CLIENT_pkg_scaler_GetZoom()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, zoomParams)
# End of GetZoom()


def scalerSetFractionalZoom(zoomNumerator, zoomDenominator, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable):
	'''Usage: returnCode = SetFractionalZoom(zoomNumerator, zoomDenominator, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable)
		Input_01 zoomNumerator <class 'int'> <<UINT_32>>
		Input_02 zoomDenominator <class 'int'> <<UINT_32>>
		Input_03 zoomXCenter <class 'int'> <<UINT_32>>
		Input_04 zoomYCenter <class 'int'> <<UINT_32>>
		Input_05 inChangeEnable FLR_ENABLE_E <<FLR_ENABLE_E>>
		Input_06 zoomOutXCenter <class 'int'> <<UINT_32>>
		Input_07 zoomOutYCenter <class 'int'> <<UINT_32>>
		Input_08 outChangeEnable FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scaler_SetFractionalZoom(zoomNumerator, zoomDenominator, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFractionalZoom()


def scalerSetIndexZoom(zoomIndex, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable):
	'''Usage: returnCode = SetIndexZoom(zoomIndex, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable)
		Input_01 zoomIndex <class 'int'> <<UINT_32>>
		Input_02 zoomXCenter <class 'int'> <<UINT_32>>
		Input_03 zoomYCenter <class 'int'> <<UINT_32>>
		Input_04 inChangeEnable FLR_ENABLE_E <<FLR_ENABLE_E>>
		Input_05 zoomOutXCenter <class 'int'> <<UINT_32>>
		Input_06 zoomOutYCenter <class 'int'> <<UINT_32>>
		Input_07 outChangeEnable FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_scaler_SetIndexZoom(zoomIndex, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetIndexZoom()


def sysctrlSetFreezeState(data):
	'''Usage: returnCode = SetFreezeState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sysctrl_SetFreezeState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFreezeState()


def sysctrlGetFreezeState():
	'''Usage: returnCode, data = GetFreezeState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_sysctrl_GetFreezeState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFreezeState()


def sysctrlGetCameraFrameRate():
	'''Usage: returnCode, frameRate = GetCameraFrameRate()
		Output_00 returnCode <FLR_RESULT>
		Output_01 frameRate <class 'int'> <<UINT_32>>
	'''
	returnCode, frameRate = CLIENT_pkg_sysctrl_GetCameraFrameRate()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, frameRate)
# End of GetCameraFrameRate()


def testRampSetType(index, data):
	'''Usage: returnCode = SetType(index, data)
		Input_01 index <class 'int'> <<UCHAR>>
		Input_02 data FLR_TESTRAMP_TYPE_E <<FLR_TESTRAMP_TYPE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_testRamp_SetType(index, data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetType()


def testRampGetType(index):
	'''Usage: returnCode, data = GetType(index)
		Input_01 index <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_TESTRAMP_TYPE_E <<FLR_TESTRAMP_TYPE_E>>
	'''
	returnCode, data = CLIENT_pkg_testRamp_GetType(index)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetType()


def testRampSetSettings(index, data):
	'''Usage: returnCode = SetSettings(index, data)
		Input_01 index <class 'int'> <<UCHAR>>
		Input_02 data FLR_TESTRAMP_SETTINGS_T <<FLR_TESTRAMP_SETTINGS_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_testRamp_SetSettings(index, data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetSettings()


def testRampGetSettings(index):
	'''Usage: returnCode, data = GetSettings(index)
		Input_01 index <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_TESTRAMP_SETTINGS_T <<FLR_TESTRAMP_SETTINGS_T>>
	'''
	returnCode, data = CLIENT_pkg_testRamp_GetSettings(index)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetSettings()


def testRampSetMotionState(data):
	'''Usage: returnCode = SetMotionState(data)
		Input_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_testRamp_SetMotionState(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetMotionState()


def testRampGetMotionState():
	'''Usage: returnCode, data = GetMotionState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, data = CLIENT_pkg_testRamp_GetMotionState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMotionState()


def testRampSetIndex(data):
	'''Usage: returnCode = SetIndex(data)
		Input_01 data <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_testRamp_SetIndex(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetIndex()


def testRampGetIndex():
	'''Usage: returnCode, data = GetIndex()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UCHAR>>
	'''
	returnCode, data = CLIENT_pkg_testRamp_GetIndex()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetIndex()


def testRampGetMaxIndex():
	'''Usage: returnCode, data = GetMaxIndex()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UCHAR>>
	'''
	returnCode, data = CLIENT_pkg_testRamp_GetMaxIndex()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetMaxIndex()


def symbologySetEnable(draw_symbols):
	'''Usage: returnCode = SetEnable(draw_symbols)
		Input_01 draw_symbols FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_SetEnable(draw_symbols)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetEnable()


def symbologyCreateBitmap(ID, pos_X, pos_Y, width, height):
	'''Usage: returnCode = CreateBitmap(ID, pos_X, pos_Y, width, height)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateBitmap(ID, pos_X, pos_Y, width, height)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateBitmap()


def symbologySendData(ID, size, text):
	'''Usage: returnCode = SendData(ID, size, text)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 size <class 'int'> <<INT_16>>
		Input_03 text[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_SendData(ID, size, text)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SendData()


def symbologyCreateArc(ID, pos_X, pos_Y, width, height, start_angle, end_angle, color):
	'''Usage: returnCode = CreateArc(ID, pos_X, pos_Y, width, height, start_angle, end_angle, color)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Input_06 start_angle <class 'float'> <<FLOAT>>
		Input_07 end_angle <class 'float'> <<FLOAT>>
		Input_08 color <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateArc(ID, pos_X, pos_Y, width, height, start_angle, end_angle, color)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateArc()


def symbologyCreateText(ID, pos_X, pos_Y, width, height, font, size, alignment, color, text):
	'''Usage: returnCode = CreateText(ID, pos_X, pos_Y, width, height, font, size, alignment, color, text)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Input_06 font <class 'int'> <<CHAR>>
		Input_07 size <class 'int'> <<INT_16>>
		Input_08 alignment FLR_SYMBOLOGY_TEXT_ALIGNMENT_E <<FLR_SYMBOLOGY_TEXT_ALIGNMENT_E>>
		Input_09 color <class 'int'> <<UINT_32>>
		Input_10 text[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateText(ID, pos_X, pos_Y, width, height, font, size, alignment, color, text)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateText()


def symbologyMoveSprite(ID, pos_X, pos_Y):
	'''Usage: returnCode = MoveSprite(ID, pos_X, pos_Y)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_MoveSprite(ID, pos_X, pos_Y)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of MoveSprite()


def symbologyAddToGroup(ID, group_ID):
	'''Usage: returnCode = AddToGroup(ID, group_ID)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 group_ID <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_AddToGroup(ID, group_ID)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of AddToGroup()


def symbologyRemoveFromGroup(ID, group_ID):
	'''Usage: returnCode = RemoveFromGroup(ID, group_ID)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 group_ID <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_RemoveFromGroup(ID, group_ID)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of RemoveFromGroup()


def symbologyUpdateAndShow(ID, visible):
	'''Usage: returnCode = UpdateAndShow(ID, visible)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 visible <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_UpdateAndShow(ID, visible)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of UpdateAndShow()


def symbologyUpdateAndShowGroup(group_ID, visible):
	'''Usage: returnCode = UpdateAndShowGroup(group_ID, visible)
		Input_01 group_ID <class 'int'> <<UCHAR>>
		Input_02 visible <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_UpdateAndShowGroup(group_ID, visible)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of UpdateAndShowGroup()


def symbologyDelete(ID):
	'''Usage: returnCode = Delete(ID)
		Input_01 ID <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_Delete(ID)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Delete()


def symbologyDeleteGroup(group_ID):
	'''Usage: returnCode = DeleteGroup(group_ID)
		Input_01 group_ID <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_DeleteGroup(group_ID)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of DeleteGroup()


def symbologyCreateFilledRectangle(ID, pos_X, pos_Y, width, height, color):
	'''Usage: returnCode = CreateFilledRectangle(ID, pos_X, pos_Y, width, height, color)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Input_06 color <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateFilledRectangle(ID, pos_X, pos_Y, width, height, color)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateFilledRectangle()


def symbologyCreateOutlinedRectangle(ID, pos_X, pos_Y, width, height, color):
	'''Usage: returnCode = CreateOutlinedRectangle(ID, pos_X, pos_Y, width, height, color)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Input_06 color <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateOutlinedRectangle(ID, pos_X, pos_Y, width, height, color)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateOutlinedRectangle()


def symbologyCreateBitmapFromPng(ID, pos_X, pos_Y, size):
	'''Usage: returnCode = CreateBitmapFromPng(ID, pos_X, pos_Y, size)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 size <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateBitmapFromPng(ID, pos_X, pos_Y, size)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateBitmapFromPng()


def symbologyCreateCompressedBitmap(ID, pos_X, pos_Y, width, height):
	'''Usage: returnCode = CreateCompressedBitmap(ID, pos_X, pos_Y, width, height)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateCompressedBitmap(ID, pos_X, pos_Y, width, height)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateCompressedBitmap()


def symbologyCreateBitmapFromPngFile(ID, pos_X, pos_Y, path):
	'''Usage: returnCode = CreateBitmapFromPngFile(ID, pos_X, pos_Y, path)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateBitmapFromPngFile(ID, pos_X, pos_Y, path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateBitmapFromPngFile()


def symbologyResetWritePosition(ID):
	'''Usage: returnCode = ResetWritePosition(ID)
		Input_01 ID <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_ResetWritePosition(ID)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of ResetWritePosition()


def symbologyMoveByOffset(ID, off_X, off_Y):
	'''Usage: returnCode = MoveByOffset(ID, off_X, off_Y)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 off_X <class 'int'> <<INT_16>>
		Input_03 off_Y <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_MoveByOffset(ID, off_X, off_Y)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of MoveByOffset()


def symbologyMoveGroupByOffset(ID, off_X, off_Y):
	'''Usage: returnCode = MoveGroupByOffset(ID, off_X, off_Y)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 off_X <class 'int'> <<INT_16>>
		Input_03 off_Y <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_MoveGroupByOffset(ID, off_X, off_Y)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of MoveGroupByOffset()


def symbologyCreateFilledEllipse(ID, pos_X, pos_Y, width, height, color):
	'''Usage: returnCode = CreateFilledEllipse(ID, pos_X, pos_Y, width, height, color)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 width <class 'int'> <<INT_16>>
		Input_05 height <class 'int'> <<INT_16>>
		Input_06 color <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateFilledEllipse(ID, pos_X, pos_Y, width, height, color)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateFilledEllipse()


def symbologyCreateLine(ID, pos_X, pos_Y, pos_X2, pos_Y2, color):
	'''Usage: returnCode = CreateLine(ID, pos_X, pos_Y, pos_X2, pos_Y2, color)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 pos_X <class 'int'> <<INT_16>>
		Input_03 pos_Y <class 'int'> <<INT_16>>
		Input_04 pos_X2 <class 'int'> <<INT_16>>
		Input_05 pos_Y2 <class 'int'> <<INT_16>>
		Input_06 color <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_CreateLine(ID, pos_X, pos_Y, pos_X2, pos_Y2, color)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of CreateLine()


def symbologySetZorder(ID, zorder):
	'''Usage: returnCode = SetZorder(ID, zorder)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 zorder <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_SetZorder(ID, zorder)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetZorder()


def symbologySaveConfiguration():
	'''Usage: returnCode = SaveConfiguration()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_SaveConfiguration()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SaveConfiguration()


def symbologyReloadConfiguration():
	'''Usage: returnCode = ReloadConfiguration()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_ReloadConfiguration()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of ReloadConfiguration()


def symbologyGetEnable():
	'''Usage: returnCode, draw_symbols = GetEnable()
		Output_00 returnCode <FLR_RESULT>
		Output_01 draw_symbols FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, draw_symbols = CLIENT_pkg_symbology_GetEnable()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, draw_symbols)
# End of GetEnable()


def symbologySetClonesNumber(ID, numberOfClones):
	'''Usage: returnCode = SetClonesNumber(ID, numberOfClones)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 numberOfClones <class 'int'> <<UCHAR>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_SetClonesNumber(ID, numberOfClones)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetClonesNumber()


def symbologyMoveCloneByOffset(ID, cloneID, pos_X, pos_Y):
	'''Usage: returnCode = MoveCloneByOffset(ID, cloneID, pos_X, pos_Y)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 cloneID <class 'int'> <<UCHAR>>
		Input_03 pos_X <class 'int'> <<INT_16>>
		Input_04 pos_Y <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_MoveCloneByOffset(ID, cloneID, pos_X, pos_Y)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of MoveCloneByOffset()


def symbologyMoveCloneSprite(ID, cloneID, pos_X, pos_Y):
	'''Usage: returnCode = MoveCloneSprite(ID, cloneID, pos_X, pos_Y)
		Input_01 ID <class 'int'> <<UCHAR>>
		Input_02 cloneID <class 'int'> <<UCHAR>>
		Input_03 pos_X <class 'int'> <<INT_16>>
		Input_04 pos_Y <class 'int'> <<INT_16>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_symbology_MoveCloneSprite(ID, cloneID, pos_X, pos_Y)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of MoveCloneSprite()


def fileOpsDir():
	'''Usage: returnCode, dirent = Dir()
		Output_00 returnCode <FLR_RESULT>
		Output_01 dirent[<class 'int'>] 128 <<UCHAR*128>>
	'''
	returnCode, dirent = CLIENT_pkg_fileOps_Dir()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, dirent)
# End of Dir()


def fileOpsCd(path):
	'''Usage: returnCode, pwd = Cd(path)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 pwd[<class 'int'>] 128 <<UCHAR*128>>
	'''
	returnCode, pwd = CLIENT_pkg_fileOps_Cd(path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, pwd)
# End of Cd()


def fileOpsMd(path):
	'''Usage: returnCode = Md(path)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Md(path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Md()


def fileOpsFopen(path, mode):
	'''Usage: returnCode, id = Fopen(path, mode)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Input_02 mode[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 id <class 'int'> <<UINT_32>>
	'''
	returnCode, id = CLIENT_pkg_fileOps_Fopen(path, mode)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, id)
# End of Fopen()


def fileOpsFclose(id):
	'''Usage: returnCode = Fclose(id)
		Input_01 id <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Fclose(id)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Fclose()


def fileOpsFread(id, length):
	'''Usage: returnCode, buf, ret = Fread(id, length)
		Input_01 id <class 'int'> <<UINT_32>>
		Input_02 length <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 buf[<class 'int'>] 128 <<UCHAR*128>>
		Output_02 ret <class 'int'> <<UINT_32>>
	'''
	returnCode, buf, ret = CLIENT_pkg_fileOps_Fread(id, length)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None)
	
	return ( returnCode, buf, ret)
# End of Fread()


def fileOpsFwrite(id, length, buf):
	'''Usage: returnCode, ret = Fwrite(id, length, buf)
		Input_01 id <class 'int'> <<UINT_32>>
		Input_02 length <class 'int'> <<UINT_32>>
		Input_03 buf[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 ret <class 'int'> <<UINT_32>>
	'''
	returnCode, ret = CLIENT_pkg_fileOps_Fwrite(id, length, buf)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, ret)
# End of Fwrite()


def fileOpsFtell(id):
	'''Usage: returnCode, offset = Ftell(id)
		Input_01 id <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 offset <class 'int'> <<UINT_32>>
	'''
	returnCode, offset = CLIENT_pkg_fileOps_Ftell(id)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, offset)
# End of Ftell()


def fileOpsFseek(id, offset, origin):
	'''Usage: returnCode = Fseek(id, offset, origin)
		Input_01 id <class 'int'> <<UINT_32>>
		Input_02 offset <class 'int'> <<UINT_32>>
		Input_03 origin <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Fseek(id, offset, origin)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Fseek()


def fileOpsFtruncate(id, length):
	'''Usage: returnCode = Ftruncate(id, length)
		Input_01 id <class 'int'> <<UINT_32>>
		Input_02 length <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Ftruncate(id, length)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Ftruncate()


def fileOpsRmdir(path):
	'''Usage: returnCode = Rmdir(path)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Rmdir(path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Rmdir()


def fileOpsRm(path):
	'''Usage: returnCode = Rm(path)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Rm(path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Rm()


def fileOpsRename(oldpath, newpath):
	'''Usage: returnCode = Rename(oldpath, newpath)
		Input_01 oldpath[<class 'int'>] 128 <<UCHAR*128>>
		Input_02 newpath[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_fileOps_Rename(oldpath, newpath)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Rename()


def fileOpsGetFileSize(path):
	'''Usage: returnCode, fileLength = GetFileSize(path)
		Input_01 path[<class 'int'>] 128 <<UCHAR*128>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 fileLength <class 'int'> <<UINT_32>>
	'''
	returnCode, fileLength = CLIENT_pkg_fileOps_GetFileSize(path)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, fileLength)
# End of GetFileSize()


def jffs2Mount():
	'''Usage: returnCode = Mount()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_jffs2_Mount()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Mount()


def jffs2Unmount():
	'''Usage: returnCode = Unmount()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_jffs2_Unmount()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of Unmount()


def jffs2GetState():
	'''Usage: returnCode, state = GetState()
		Output_00 returnCode <FLR_RESULT>
		Output_01 state FLR_JFFS2_STATE_E <<FLR_JFFS2_STATE_E>>
	'''
	returnCode, state = CLIENT_pkg_jffs2_GetState()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, state)
# End of GetState()


def splashScreenSetDuration(screen_num, periodMs):
	'''Usage: returnCode = SetDuration(screen_num, periodMs)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Input_02 periodMs <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_splashScreen_SetDuration(screen_num, periodMs)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDuration()


def splashScreenSetDataType(screen_num, filetype):
	'''Usage: returnCode = SetDataType(screen_num, filetype)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Input_02 filetype FLR_SPLASHSCREEN_FILETYPE_E <<FLR_SPLASHSCREEN_FILETYPE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_splashScreen_SetDataType(screen_num, filetype)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDataType()


def splashScreenSetBackground(screen_num, backgroundColor):
	'''Usage: returnCode = SetBackground(screen_num, backgroundColor)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Input_02 backgroundColor <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_splashScreen_SetBackground(screen_num, backgroundColor)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetBackground()


def splashScreenGetDuration(screen_num):
	'''Usage: returnCode, periodMs = GetDuration(screen_num)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 periodMs <class 'int'> <<UINT_32>>
	'''
	returnCode, periodMs = CLIENT_pkg_splashScreen_GetDuration(screen_num)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, periodMs)
# End of GetDuration()


def splashScreenGetDataType(screen_num):
	'''Usage: returnCode, filetype = GetDataType(screen_num)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 filetype FLR_SPLASHSCREEN_FILETYPE_E <<FLR_SPLASHSCREEN_FILETYPE_E>>
	'''
	returnCode, filetype = CLIENT_pkg_splashScreen_GetDataType(screen_num)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, filetype)
# End of GetDataType()


def splashScreenGetBackground(screen_num):
	'''Usage: returnCode, backgroundColor = GetBackground(screen_num)
		Input_01 screen_num <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 backgroundColor <class 'int'> <<UINT_32>>
	'''
	returnCode, backgroundColor = CLIENT_pkg_splashScreen_GetBackground(screen_num)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, backgroundColor)
# End of GetBackground()


def systemSymbolsGetID(symbol):
	'''Usage: returnCode, id, id_type = GetID(symbol)
		Input_01 symbol FLR_SYSTEMSYMBOLS_SYMBOL_E <<FLR_SYSTEMSYMBOLS_SYMBOL_E>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 id <class 'int'> <<UCHAR>>
		Output_02 id_type FLR_SYSTEMSYMBOLS_ID_TYPE_E <<FLR_SYSTEMSYMBOLS_ID_TYPE_E>>
	'''
	returnCode, id, id_type = CLIENT_pkg_systemSymbols_GetID(symbol)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None, None)
	
	return ( returnCode, id, id_type)
# End of GetID()


def systemSymbolsSetID(symbol, id, id_type):
	'''Usage: returnCode = SetID(symbol, id, id_type)
		Input_01 symbol FLR_SYSTEMSYMBOLS_SYMBOL_E <<FLR_SYSTEMSYMBOLS_SYMBOL_E>>
		Input_02 id <class 'int'> <<UCHAR>>
		Input_03 id_type FLR_SYSTEMSYMBOLS_ID_TYPE_E <<FLR_SYSTEMSYMBOLS_ID_TYPE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_systemSymbols_SetID(symbol, id, id_type)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetID()


def systemSymbolsGetEnable(symbol):
	'''Usage: returnCode, enabled = GetEnable(symbol)
		Input_01 symbol FLR_SYSTEMSYMBOLS_SYMBOL_E <<FLR_SYSTEMSYMBOLS_SYMBOL_E>>
		Output_00 returnCode <FLR_RESULT>
		Output_01 enabled FLR_ENABLE_E <<FLR_ENABLE_E>>
	'''
	returnCode, enabled = CLIENT_pkg_systemSymbols_GetEnable(symbol)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, enabled)
# End of GetEnable()


def systemSymbolsSetEnable(symbol, enabled):
	'''Usage: returnCode = SetEnable(symbol, enabled)
		Input_01 symbol FLR_SYSTEMSYMBOLS_SYMBOL_E <<FLR_SYSTEMSYMBOLS_SYMBOL_E>>
		Input_02 enabled FLR_ENABLE_E <<FLR_ENABLE_E>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_systemSymbols_SetEnable(symbol, enabled)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetEnable()


def sffcGetScaleFactor():
	'''Usage: returnCode, data = GetScaleFactor()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetScaleFactor()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetScaleFactor()


def sffcGetDeltaTempLinearCoeff():
	'''Usage: returnCode, data = GetDeltaTempLinearCoeff()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetDeltaTempLinearCoeff()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDeltaTempLinearCoeff()


def sffcSetDeltaTempLinearCoeff(data):
	'''Usage: returnCode = SetDeltaTempLinearCoeff(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sffc_SetDeltaTempLinearCoeff(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDeltaTempLinearCoeff()


def sffcGetDeltaTempOffsetCoeff():
	'''Usage: returnCode, data = GetDeltaTempOffsetCoeff()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetDeltaTempOffsetCoeff()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDeltaTempOffsetCoeff()


def sffcSetDeltaTempOffsetCoeff(data):
	'''Usage: returnCode = SetDeltaTempOffsetCoeff(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sffc_SetDeltaTempOffsetCoeff(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDeltaTempOffsetCoeff()


def sffcGetFpaTempLinearCoeff():
	'''Usage: returnCode, data = GetFpaTempLinearCoeff()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetFpaTempLinearCoeff()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFpaTempLinearCoeff()


def sffcSetFpaTempLinearCoeff(data):
	'''Usage: returnCode = SetFpaTempLinearCoeff(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sffc_SetFpaTempLinearCoeff(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFpaTempLinearCoeff()


def sffcGetFpaTempOffsetCoeff():
	'''Usage: returnCode, data = GetFpaTempOffsetCoeff()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'float'> <<FLOAT>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetFpaTempOffsetCoeff()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetFpaTempOffsetCoeff()


def sffcSetFpaTempOffsetCoeff(data):
	'''Usage: returnCode = SetFpaTempOffsetCoeff(data)
		Input_01 data <class 'float'> <<FLOAT>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sffc_SetFpaTempOffsetCoeff(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetFpaTempOffsetCoeff()


def sffcGetDeltaTempTimeLimitInSecs():
	'''Usage: returnCode, data = GetDeltaTempTimeLimitInSecs()
		Output_00 returnCode <FLR_RESULT>
		Output_01 data <class 'int'> <<UINT_32>>
	'''
	returnCode, data = CLIENT_pkg_sffc_GetDeltaTempTimeLimitInSecs()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, data)
# End of GetDeltaTempTimeLimitInSecs()


def sffcSetDeltaTempTimeLimitInSecs(data):
	'''Usage: returnCode = SetDeltaTempTimeLimitInSecs(data)
		Input_01 data <class 'int'> <<UINT_32>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_sffc_SetDeltaTempTimeLimitInSecs(data)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetDeltaTempTimeLimitInSecs()


def imageStatsGetTotalHistPixelsInROI():
	'''Usage: returnCode, totalPixelsInROI = GetTotalHistPixelsInROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 totalPixelsInROI <class 'int'> <<UINT_32>>
	'''
	returnCode, totalPixelsInROI = CLIENT_pkg_imageStats_GetTotalHistPixelsInROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, totalPixelsInROI)
# End of GetTotalHistPixelsInROI()


def imageStatsGetPopBelowLowToHighThresh():
	'''Usage: returnCode, popBelowLowToHighThresh = GetPopBelowLowToHighThresh()
		Output_00 returnCode <FLR_RESULT>
		Output_01 popBelowLowToHighThresh <class 'int'> <<UINT_32>>
	'''
	returnCode, popBelowLowToHighThresh = CLIENT_pkg_imageStats_GetPopBelowLowToHighThresh()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, popBelowLowToHighThresh)
# End of GetPopBelowLowToHighThresh()


def imageStatsGetPopAboveHighToLowThresh():
	'''Usage: returnCode, popAboveHighToLowThresh = GetPopAboveHighToLowThresh()
		Output_00 returnCode <FLR_RESULT>
		Output_01 popAboveHighToLowThresh <class 'int'> <<UINT_32>>
	'''
	returnCode, popAboveHighToLowThresh = CLIENT_pkg_imageStats_GetPopAboveHighToLowThresh()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, popAboveHighToLowThresh)
# End of GetPopAboveHighToLowThresh()


def imageStatsSetROI(roi):
	'''Usage: returnCode = SetROI(roi)
		Input_01 roi FLR_ROI_T <<FLR_ROI_T>>
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_imageStats_SetROI(roi)
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of SetROI()


def imageStatsGetROI():
	'''Usage: returnCode, roi = GetROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 roi FLR_ROI_T <<FLR_ROI_T>>
	'''
	returnCode, roi = CLIENT_pkg_imageStats_GetROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, roi)
# End of GetROI()


def imageStatsGetFirstBin():
	'''Usage: returnCode, firstBin = GetFirstBin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 firstBin <class 'int'> <<UINT_16>>
	'''
	returnCode, firstBin = CLIENT_pkg_imageStats_GetFirstBin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, firstBin)
# End of GetFirstBin()


def imageStatsGetLastBin():
	'''Usage: returnCode, lastBin = GetLastBin()
		Output_00 returnCode <FLR_RESULT>
		Output_01 lastBin <class 'int'> <<UINT_16>>
	'''
	returnCode, lastBin = CLIENT_pkg_imageStats_GetLastBin()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, lastBin)
# End of GetLastBin()


def imageStatsGetMean():
	'''Usage: returnCode, mean = GetMean()
		Output_00 returnCode <FLR_RESULT>
		Output_01 mean <class 'int'> <<UINT_16>>
	'''
	returnCode, mean = CLIENT_pkg_imageStats_GetMean()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, mean)
# End of GetMean()


def imageStatsGetFirstBinInROI():
	'''Usage: returnCode, firstBinInROI = GetFirstBinInROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 firstBinInROI <class 'int'> <<UINT_16>>
	'''
	returnCode, firstBinInROI = CLIENT_pkg_imageStats_GetFirstBinInROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, firstBinInROI)
# End of GetFirstBinInROI()


def imageStatsGetLastBinInROI():
	'''Usage: returnCode, lastBinInROI = GetLastBinInROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 lastBinInROI <class 'int'> <<UINT_16>>
	'''
	returnCode, lastBinInROI = CLIENT_pkg_imageStats_GetLastBinInROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, lastBinInROI)
# End of GetLastBinInROI()


def imageStatsGetMeanInROI():
	'''Usage: returnCode, meanInROI = GetMeanInROI()
		Output_00 returnCode <FLR_RESULT>
		Output_01 meanInROI <class 'int'> <<UINT_16>>
	'''
	returnCode, meanInROI = CLIENT_pkg_imageStats_GetMeanInROI()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode, None)
	
	return ( returnCode, meanInROI)
# End of GetMeanInROI()


def dummyBadCommand():
	'''Usage: returnCode = BadCommand()
		Output_00 returnCode <FLR_RESULT>
	'''
	returnCode = CLIENT_pkg_dummy_BadCommand()
	
	# Check for any errorcode
	if (returnCode.value):
		return ( returnCode)
	
	return ( returnCode)
# End of BadCommand()


