//  /////////////////////////////////////////////////////
//  // DO NOT EDIT.  This is a machine generated file. //
//  /////////////////////////////////////////////////////
/******************************************************************************/
/*                                                                            */
/*  Copyright (C) 2018, FLIR Systems                                          */
/*  All rights reserved.                                                      */
/*                                                                            */
/*  This document is controlled to FLIR Technology Level 2. The information   */
/*  contained in this document pertains to a dual use product controlled for  */
/*  export by the Export Administration Regulations (EAR). Diversion contrary */
/*  to US law is prohibited. US Department of Commerce authorization is not   */
/*  required prior to export or transfer to foreign persons or parties unless */
/*  otherwise prohibited.                                                     */
/*                                                                            */
/******************************************************************************/


#include "Client_API.h"

static const uint16_t MaxMemoryChunk = 256;

FLR_RESULT gaoSetGainState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetGainState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetGainState()

FLR_RESULT gaoGetGainState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetGainState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetGainState()

FLR_RESULT gaoSetFfcState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetFfcState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFfcState()

FLR_RESULT gaoGetFfcState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetFfcState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcState()

FLR_RESULT gaoSetTempCorrectionState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetTempCorrectionState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTempCorrectionState()

FLR_RESULT gaoGetTempCorrectionState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetTempCorrectionState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTempCorrectionState()

FLR_RESULT gaoSetIConstL(const int16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetIConstL(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetIConstL()

FLR_RESULT gaoGetIConstL(int16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetIConstL(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetIConstL()

FLR_RESULT gaoSetIConstM(const int16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetIConstM(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetIConstM()

FLR_RESULT gaoGetIConstM(int16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetIConstM(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetIConstM()

FLR_RESULT gaoSetAveragerState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetAveragerState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetAveragerState()

FLR_RESULT gaoGetAveragerState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetAveragerState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetAveragerState()

FLR_RESULT gaoSetNumFFCFrames(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetNumFFCFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetNumFFCFrames()

FLR_RESULT gaoGetNumFFCFrames(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetNumFFCFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNumFFCFrames()

FLR_RESULT gaoGetAveragerThreshold(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetAveragerThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetAveragerThreshold()

FLR_RESULT gaoSetRnsState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsState()

FLR_RESULT gaoGetRnsState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsState()

FLR_RESULT gaoSetTestRampState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetTestRampState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTestRampState()

FLR_RESULT gaoGetTestRampState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetTestRampState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTestRampState()

FLR_RESULT gaoSetSffcState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetSffcState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSffcState()

FLR_RESULT gaoGetSffcState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetSffcState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSffcState()

FLR_RESULT gaoSetNucType(const FLR_GAO_NUC_TYPE_E nucType){
    FLR_RESULT returncode = CLIENT_pkgGaoSetNucType(nucType);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetNucType()

FLR_RESULT gaoGetNucType(FLR_GAO_NUC_TYPE_E *nucType){
    FLR_RESULT returncode = CLIENT_pkgGaoGetNucType(nucType);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNucType()

FLR_RESULT gaoSetFfcZeroMeanState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetFfcZeroMeanState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFfcZeroMeanState()

FLR_RESULT gaoGetFfcZeroMeanState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetFfcZeroMeanState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcZeroMeanState()

FLR_RESULT gaoSetCombineMeansEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetCombineMeansEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetCombineMeansEnableState()

FLR_RESULT gaoGetCombineMeansEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetCombineMeansEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCombineMeansEnableState()

FLR_RESULT gaoSetRnsPopThreshold(const uint16_t threshold){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsPopThreshold(threshold);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsPopThreshold()

FLR_RESULT gaoGetRnsPopThreshold(uint16_t *threshold){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsPopThreshold(threshold);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsPopThreshold()

FLR_RESULT gaoSetRnsCloseThreshold(const uint16_t threshold){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsCloseThreshold(threshold);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsCloseThreshold()

FLR_RESULT gaoGetRnsCloseThreshold(uint16_t *threshold){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsCloseThreshold(threshold);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsCloseThreshold()

FLR_RESULT gaoSetRnsTooFewQuit(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsTooFewQuit(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsTooFewQuit()

FLR_RESULT gaoGetRnsTooFewQuit(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsTooFewQuit(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsTooFewQuit()

FLR_RESULT gaoSetRnsTooFew(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsTooFew(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsTooFew()

FLR_RESULT gaoGetRnsTooFew(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsTooFew(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsTooFew()

FLR_RESULT gaoSetRnsMinCorrection(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsMinCorrection(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsMinCorrection()

FLR_RESULT gaoGetRnsMinCorrection(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsMinCorrection(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsMinCorrection()

FLR_RESULT gaoSetRnsDamping(const uint8_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsDamping(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsDamping()

FLR_RESULT gaoGetRnsDamping(uint8_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsDamping(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsDamping()

FLR_RESULT gaoSetRnsFrameHysteresis(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsFrameHysteresis(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsFrameHysteresis()

FLR_RESULT gaoGetRnsFrameHysteresis(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsFrameHysteresis(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsFrameHysteresis()

FLR_RESULT gaoSetRnsBadDamping(const uint8_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsBadDamping(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsBadDamping()

FLR_RESULT gaoGetRnsBadDamping(uint8_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsBadDamping(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsBadDamping()

FLR_RESULT gaoSetRnsNumGoodDampingThreshold(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgGaoSetRnsNumGoodDampingThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRnsNumGoodDampingThreshold()

FLR_RESULT gaoGetRnsNumGoodDampingThreshold(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsNumGoodDampingThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsNumGoodDampingThreshold()

FLR_RESULT gaoGetRnsFfcDesired(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetRnsFfcDesired(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnsFfcDesired()

FLR_RESULT gaoGetAveragerDesiredState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgGaoGetAveragerDesiredState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetAveragerDesiredState()

FLR_RESULT roicGetFPATemp(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPATemp(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPATemp()

FLR_RESULT roicGetFrameCount(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFrameCount(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFrameCount()

FLR_RESULT roicGetActiveNormalizationTarget(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetActiveNormalizationTarget(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetActiveNormalizationTarget()

FLR_RESULT roicSetFPARampState(const FLR_ENABLE_E state){
    FLR_RESULT returncode = CLIENT_pkgRoicSetFPARampState(state);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFPARampState()

FLR_RESULT roicGetFPARampState(FLR_ENABLE_E *state){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPARampState(state);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPARampState()

FLR_RESULT roicGetSensorADC1(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetSensorADC1(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSensorADC1()

FLR_RESULT roicGetSensorADC2(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetSensorADC2(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSensorADC2()

FLR_RESULT roicSetFPATempOffset(const int16_t data){
    FLR_RESULT returncode = CLIENT_pkgRoicSetFPATempOffset(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFPATempOffset()

FLR_RESULT roicGetFPATempOffset(int16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPATempOffset(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPATempOffset()

FLR_RESULT roicSetFPATempMode(const FLR_ROIC_TEMP_MODE_E data){
    FLR_RESULT returncode = CLIENT_pkgRoicSetFPATempMode(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFPATempMode()

FLR_RESULT roicGetFPATempMode(FLR_ROIC_TEMP_MODE_E *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPATempMode(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPATempMode()

FLR_RESULT roicGetFPATempTable(FLR_ROIC_FPATEMP_TABLE_T *table){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPATempTable(table);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPATempTable()

FLR_RESULT roicSetFPATempValue(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgRoicSetFPATempValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFPATempValue()

FLR_RESULT roicGetFPATempValue(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgRoicGetFPATempValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFPATempValue()

FLR_RESULT roicGetPreambleError(uint32_t *preambleError){
    FLR_RESULT returncode = CLIENT_pkgRoicGetPreambleError(preambleError);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPreambleError()

FLR_RESULT roicInducePreambleError(const uint32_t everyNthFrame){
    FLR_RESULT returncode = CLIENT_pkgRoicInducePreambleError(everyNthFrame);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of InducePreambleError()

FLR_RESULT roicGetRoicStarted(FLR_ENABLE_E *roicStarted){
    FLR_RESULT returncode = CLIENT_pkgRoicGetRoicStarted(roicStarted);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRoicStarted()

FLR_RESULT bprGetState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgBprGetState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetState()

FLR_RESULT bprSetState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgBprSetState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetState()

FLR_RESULT bprGetStats(uint32_t *threeby, uint32_t *fiveby, uint32_t *rows, uint32_t *budget, uint32_t *used){
    FLR_RESULT returncode = CLIENT_pkgBprGetStats(threeby, fiveby, rows, budget, used);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetStats()

FLR_RESULT bprGetDisplayMode(FLR_BPR_DISPLAY_MODE_E *data){
    FLR_RESULT returncode = CLIENT_pkgBprGetDisplayMode(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDisplayMode()

FLR_RESULT bprSetDisplayMode(const FLR_BPR_DISPLAY_MODE_E data){
    FLR_RESULT returncode = CLIENT_pkgBprSetDisplayMode(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDisplayMode()

FLR_RESULT bprGetDisplayModeMinValue(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBprGetDisplayModeMinValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDisplayModeMinValue()

FLR_RESULT bprSetDisplayModeMinValue(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBprSetDisplayModeMinValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDisplayModeMinValue()

FLR_RESULT bprGetDisplayModeMaxValue(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBprGetDisplayModeMaxValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDisplayModeMaxValue()

FLR_RESULT bprSetDisplayModeMaxValue(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBprSetDisplayModeMaxValue(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDisplayModeMaxValue()

FLR_RESULT bprGetWorkBufIndex(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgBprGetWorkBufIndex(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetWorkBufIndex()

FLR_RESULT bprSetWorkBufIndex(const uint32_t data){
    FLR_RESULT returncode = CLIENT_pkgBprSetWorkBufIndex(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetWorkBufIndex()

FLR_RESULT bprGetWorkBufStats(uint32_t *threeby, uint32_t *fiveby, uint32_t *rows, uint32_t *budget, uint32_t *used){
    FLR_RESULT returncode = CLIENT_pkgBprGetWorkBufStats(threeby, fiveby, rows, budget, used);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetWorkBufStats()

FLR_RESULT telemetrySetState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgTelemetrySetState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetState()

FLR_RESULT telemetryGetState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgTelemetryGetState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetState()

FLR_RESULT telemetrySetLocation(const FLR_TELEMETRY_LOC_E data){
    FLR_RESULT returncode = CLIENT_pkgTelemetrySetLocation(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetLocation()

FLR_RESULT telemetryGetLocation(FLR_TELEMETRY_LOC_E *data){
    FLR_RESULT returncode = CLIENT_pkgTelemetryGetLocation(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLocation()

FLR_RESULT telemetrySetPacking(const FLR_TELEMETRY_PACKING_E data){
    FLR_RESULT returncode = CLIENT_pkgTelemetrySetPacking(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetPacking()

FLR_RESULT telemetryGetPacking(FLR_TELEMETRY_PACKING_E *data){
    FLR_RESULT returncode = CLIENT_pkgTelemetryGetPacking(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPacking()

FLR_RESULT bosonGetCameraSN(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetCameraSN(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCameraSN()

FLR_RESULT bosonGetCameraPN(FLR_BOSON_PARTNUMBER_T *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetCameraPN(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCameraPN()

FLR_RESULT bosonGetSensorSN(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSensorSN(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSensorSN()

FLR_RESULT bosonRunFFC(){
    FLR_RESULT returncode = CLIENT_pkgBosonRunFFC();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of RunFFC()

FLR_RESULT bosonSetFFCTempThreshold(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFFCTempThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFFCTempThreshold()

FLR_RESULT bosonGetFFCTempThreshold(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFFCTempThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFFCTempThreshold()

FLR_RESULT bosonSetFFCFrameThreshold(const uint32_t data){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFFCFrameThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFFCFrameThreshold()

FLR_RESULT bosonGetFFCFrameThreshold(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFFCFrameThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFFCFrameThreshold()

FLR_RESULT bosonGetFFCInProgress(int16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFFCInProgress(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFFCInProgress()

FLR_RESULT bosonReboot(){
    FLR_RESULT returncode = CLIENT_pkgBosonReboot();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Reboot()

FLR_RESULT bosonSetFFCMode(const FLR_BOSON_FFCMODE_E ffcMode){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFFCMode(ffcMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFFCMode()

FLR_RESULT bosonGetFFCMode(FLR_BOSON_FFCMODE_E *ffcMode){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFFCMode(ffcMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFFCMode()

FLR_RESULT bosonSetGainMode(const FLR_BOSON_GAINMODE_E gainMode){
    FLR_RESULT returncode = CLIENT_pkgBosonSetGainMode(gainMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetGainMode()

FLR_RESULT bosonGetGainMode(FLR_BOSON_GAINMODE_E *gainMode){
    FLR_RESULT returncode = CLIENT_pkgBosonGetGainMode(gainMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetGainMode()

FLR_RESULT bosonWriteDynamicHeaderToFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteDynamicHeaderToFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteDynamicHeaderToFlash()

FLR_RESULT bosonReadDynamicHeaderFromFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonReadDynamicHeaderFromFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReadDynamicHeaderFromFlash()

FLR_RESULT bosonRestoreFactoryDefaultsFromFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonRestoreFactoryDefaultsFromFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of RestoreFactoryDefaultsFromFlash()

FLR_RESULT bosonRestoreFactoryBadPixelsFromFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonRestoreFactoryBadPixelsFromFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of RestoreFactoryBadPixelsFromFlash()

FLR_RESULT bosonWriteBadPixelsToFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteBadPixelsToFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteBadPixelsToFlash()

FLR_RESULT bosonGetSoftwareRev(uint32_t *major, uint32_t *minor, uint32_t *patch){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSoftwareRev(major, minor, patch);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSoftwareRev()

FLR_RESULT bosonSetBadPixelLocation(const uint32_t row, const uint32_t col){
    FLR_RESULT returncode = CLIENT_pkgBosonSetBadPixelLocation(row, col);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetBadPixelLocation()

FLR_RESULT bosonlookupFPATempDegCx10(int16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonlookupFPATempDegCx10(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of lookupFPATempDegCx10()

FLR_RESULT bosonlookupFPATempDegKx10(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonlookupFPATempDegKx10(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of lookupFPATempDegKx10()

FLR_RESULT bosonWriteLensNvFfcToFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteLensNvFfcToFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteLensNvFfcToFlash()

FLR_RESULT bosonWriteLensGainToFlash(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteLensGainToFlash();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteLensGainToFlash()

FLR_RESULT bosonSetLensNumber(const uint32_t lensNumber){
    FLR_RESULT returncode = CLIENT_pkgBosonSetLensNumber(lensNumber);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetLensNumber()

FLR_RESULT bosonGetLensNumber(uint32_t *lensNumber){
    FLR_RESULT returncode = CLIENT_pkgBosonGetLensNumber(lensNumber);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLensNumber()

FLR_RESULT bosonSetTableNumber(const uint32_t tableNumber){
    FLR_RESULT returncode = CLIENT_pkgBosonSetTableNumber(tableNumber);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTableNumber()

FLR_RESULT bosonGetTableNumber(uint32_t *tableNumber){
    FLR_RESULT returncode = CLIENT_pkgBosonGetTableNumber(tableNumber);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTableNumber()

FLR_RESULT bosonGetSensorPN(FLR_BOSON_SENSOR_PARTNUMBER_T *sensorPN){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSensorPN(sensorPN);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSensorPN()

FLR_RESULT bosonSetGainSwitchParams(const FLR_BOSON_GAIN_SWITCH_PARAMS_T parm_struct){
    FLR_RESULT returncode = CLIENT_pkgBosonSetGainSwitchParams(parm_struct);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetGainSwitchParams()

FLR_RESULT bosonGetGainSwitchParams(FLR_BOSON_GAIN_SWITCH_PARAMS_T *parm_struct){
    FLR_RESULT returncode = CLIENT_pkgBosonGetGainSwitchParams(parm_struct);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetGainSwitchParams()

FLR_RESULT bosonGetSwitchToHighGainFlag(uint8_t *switchToHighGainFlag){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSwitchToHighGainFlag(switchToHighGainFlag);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSwitchToHighGainFlag()

FLR_RESULT bosonGetSwitchToLowGainFlag(uint8_t *switchToLowGainFlag){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSwitchToLowGainFlag(switchToLowGainFlag);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSwitchToLowGainFlag()

FLR_RESULT bosonGetCLowToHighPercent(uint32_t *cLowToHighPercent){
    FLR_RESULT returncode = CLIENT_pkgBosonGetCLowToHighPercent(cLowToHighPercent);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCLowToHighPercent()

FLR_RESULT bosonGetMaxNUCTables(uint32_t *maxNUCTables){
    FLR_RESULT returncode = CLIENT_pkgBosonGetMaxNUCTables(maxNUCTables);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxNUCTables()

FLR_RESULT bosonGetMaxLensTables(uint32_t *maxLensTables){
    FLR_RESULT returncode = CLIENT_pkgBosonGetMaxLensTables(maxLensTables);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxLensTables()

FLR_RESULT bosonGetFfcWaitCloseFrames(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFfcWaitCloseFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcWaitCloseFrames()

FLR_RESULT bosonSetFfcWaitCloseFrames(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFfcWaitCloseFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFfcWaitCloseFrames()

FLR_RESULT bosonCheckForTableSwitch(){
    FLR_RESULT returncode = CLIENT_pkgBosonCheckForTableSwitch();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CheckForTableSwitch()

FLR_RESULT bosonGetDesiredTableNumber(uint32_t *desiredTableNumber){
    FLR_RESULT returncode = CLIENT_pkgBosonGetDesiredTableNumber(desiredTableNumber);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDesiredTableNumber()

FLR_RESULT bosonGetFfcStatus(FLR_BOSON_FFCSTATUS_E *ffcStatus){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFfcStatus(ffcStatus);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcStatus()

FLR_RESULT bosonGetFfcDesired(uint32_t *ffcDesired){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFfcDesired(ffcDesired);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcDesired()

FLR_RESULT bosonGetSwRevInHeader(uint32_t *major, uint32_t *minor, uint32_t *patch){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSwRevInHeader(major, minor, patch);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSwRevInHeader()

FLR_RESULT bosonGetLastFFCFrameCount(uint32_t *frameCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGetLastFFCFrameCount(frameCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastFFCFrameCount()

FLR_RESULT bosonGetLastFFCTempDegKx10(uint16_t *temp){
    FLR_RESULT returncode = CLIENT_pkgBosonGetLastFFCTempDegKx10(temp);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastFFCTempDegKx10()

FLR_RESULT bosonGetTableSwitchDesired(uint16_t *tableSwitchDesired){
    FLR_RESULT returncode = CLIENT_pkgBosonGetTableSwitchDesired(tableSwitchDesired);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTableSwitchDesired()

FLR_RESULT bosonGetOverTempThreshold(float *temperatureInC){
    FLR_RESULT returncode = CLIENT_pkgBosonGetOverTempThreshold(temperatureInC);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOverTempThreshold()

FLR_RESULT bosonGetLowPowerMode(uint16_t *lowPowerMode){
    FLR_RESULT returncode = CLIENT_pkgBosonGetLowPowerMode(lowPowerMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLowPowerMode()

FLR_RESULT bosonGetOverTempEventOccurred(uint16_t *overTempEventOccurred){
    FLR_RESULT returncode = CLIENT_pkgBosonGetOverTempEventOccurred(overTempEventOccurred);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOverTempEventOccurred()

FLR_RESULT bosonSetPermitThermalShutdownOverride(const FLR_ENABLE_E permitThermalShutdownOverride){
    FLR_RESULT returncode = CLIENT_pkgBosonSetPermitThermalShutdownOverride(permitThermalShutdownOverride);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetPermitThermalShutdownOverride()

FLR_RESULT bosonGetPermitThermalShutdownOverride(FLR_ENABLE_E *permitThermalShutdownOverride){
    FLR_RESULT returncode = CLIENT_pkgBosonGetPermitThermalShutdownOverride(permitThermalShutdownOverride);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPermitThermalShutdownOverride()

FLR_RESULT bosonGetMyriadTemp(float *myriadTemp){
    FLR_RESULT returncode = CLIENT_pkgBosonGetMyriadTemp(myriadTemp);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMyriadTemp()

FLR_RESULT bosonGetNvFFCNucTableNumberLens0(int32_t *nvFFCNucTableNumberLens0){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCNucTableNumberLens0(nvFFCNucTableNumberLens0);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCNucTableNumberLens0()

FLR_RESULT bosonGetNvFFCNucTableNumberLens1(int32_t *nvFFCNucTableNumberLens1){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCNucTableNumberLens1(nvFFCNucTableNumberLens1);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCNucTableNumberLens1()

FLR_RESULT bosonGetNvFFCFPATempDegKx10Lens0(uint16_t *nvFFCFPATempDegKx10Lens0){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCFPATempDegKx10Lens0(nvFFCFPATempDegKx10Lens0);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCFPATempDegKx10Lens0()

FLR_RESULT bosonGetNvFFCFPATempDegKx10Lens1(uint16_t *nvFFCFPATempDegKx10Lens1){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCFPATempDegKx10Lens1(nvFFCFPATempDegKx10Lens1);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCFPATempDegKx10Lens1()

FLR_RESULT bosonSetFFCWarnTimeInSecx10(const uint16_t ffcWarnTime){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFFCWarnTimeInSecx10(ffcWarnTime);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFFCWarnTimeInSecx10()

FLR_RESULT bosonGetFFCWarnTimeInSecx10(uint16_t *ffcWarnTime){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFFCWarnTimeInSecx10(ffcWarnTime);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFFCWarnTimeInSecx10()

FLR_RESULT bosonGetOverTempEventCounter(uint32_t *overTempEventCounter){
    FLR_RESULT returncode = CLIENT_pkgBosonGetOverTempEventCounter(overTempEventCounter);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOverTempEventCounter()

FLR_RESULT bosonSetOverTempTimerInSec(const uint16_t overTempTimerInSec){
    FLR_RESULT returncode = CLIENT_pkgBosonSetOverTempTimerInSec(overTempTimerInSec);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOverTempTimerInSec()

FLR_RESULT bosonGetOverTempTimerInSec(uint16_t *overTempTimerInSec){
    FLR_RESULT returncode = CLIENT_pkgBosonGetOverTempTimerInSec(overTempTimerInSec);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOverTempTimerInSec()

FLR_RESULT bosonUnloadCurrentLensCorrections(){
    FLR_RESULT returncode = CLIENT_pkgBosonUnloadCurrentLensCorrections();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of UnloadCurrentLensCorrections()

FLR_RESULT bosonSetTimeForQuickFFCsInSecs(const uint32_t timeForQuickFFCsInSecs){
    FLR_RESULT returncode = CLIENT_pkgBosonSetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTimeForQuickFFCsInSecs()

FLR_RESULT bosonGetTimeForQuickFFCsInSecs(uint32_t *timeForQuickFFCsInSecs){
    FLR_RESULT returncode = CLIENT_pkgBosonGetTimeForQuickFFCsInSecs(timeForQuickFFCsInSecs);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTimeForQuickFFCsInSecs()

FLR_RESULT bosonReloadCurrentLensCorrections(){
    FLR_RESULT returncode = CLIENT_pkgBosonReloadCurrentLensCorrections();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReloadCurrentLensCorrections()

FLR_RESULT bosonGetBootTimestamps(float *FirstLight, float *StartInit, float *BosonExecDone, float *Timestamp4){
    FLR_RESULT returncode = CLIENT_pkgBosonGetBootTimestamps(FirstLight, StartInit, BosonExecDone, Timestamp4);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetBootTimestamps()

FLR_RESULT bosonSet2ptResponsivityHighLimit(const float responsivityHighLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptResponsivityHighLimit(responsivityHighLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptResponsivityHighLimit()

FLR_RESULT bosonGet2ptResponsivityHighLimit(float *responsivityHighLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptResponsivityHighLimit(responsivityHighLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptResponsivityHighLimit()

FLR_RESULT bosonSet2ptResponsivityLowLimit(const float responsivityLowLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptResponsivityLowLimit(responsivityLowLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptResponsivityLowLimit()

FLR_RESULT bosonGet2ptResponsivityLowLimit(float *responsivityLowLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptResponsivityLowLimit(responsivityLowLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptResponsivityLowLimit()

FLR_RESULT bosonGet2ptResponsivityHighLimitErrorCount(uint32_t *responsivityHighLimitErrorCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptResponsivityHighLimitErrorCount(responsivityHighLimitErrorCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptResponsivityHighLimitErrorCount()

FLR_RESULT bosonGet2ptResponsivityLowLimitErrorCount(uint32_t *responsivityLowLimitErrorCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptResponsivityLowLimitErrorCount(responsivityLowLimitErrorCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptResponsivityLowLimitErrorCount()

FLR_RESULT bosonGet2ptPixelHighLimit(uint32_t *pixelHighLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptPixelHighLimit(pixelHighLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptPixelHighLimit()

FLR_RESULT bosonSet2ptPixelHighLimit(const uint32_t pixelHighLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptPixelHighLimit(pixelHighLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptPixelHighLimit()

FLR_RESULT bosonGet2ptPixelLowLimit(uint32_t *pixelLowLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptPixelLowLimit(pixelLowLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptPixelLowLimit()

FLR_RESULT bosonSet2ptPixelLowLimit(const uint32_t pixelLowLimit){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptPixelLowLimit(pixelLowLimit);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptPixelLowLimit()

FLR_RESULT bosonGet2ptPixelHighLimitErrorCount(uint32_t *pixelHighLimitErrorCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptPixelHighLimitErrorCount(pixelHighLimitErrorCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptPixelHighLimitErrorCount()

FLR_RESULT bosonGet2ptPixelLowLimitErrorCount(uint32_t *pixelLowLimitErrorCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptPixelLowLimitErrorCount(pixelLowLimitErrorCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptPixelLowLimitErrorCount()

FLR_RESULT bosonGet2ptTotalBadPixelErrorCount(uint32_t *totalBadPixelErrorCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptTotalBadPixelErrorCount(totalBadPixelErrorCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptTotalBadPixelErrorCount()

FLR_RESULT bosonGet2ptNucStatusState(uint32_t *statusState, uint32_t *statusStringLength){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptNucStatusState(statusState, statusStringLength);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptNucStatusState()

FLR_RESULT bosonSet2ptNucStatusState(const uint32_t statusState){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptNucStatusState(statusState);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptNucStatusState()

FLR_RESULT bosonReset2ptNucStatusState(){
    FLR_RESULT returncode = CLIENT_pkgBosonReset2ptNucStatusState();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Reset2ptNucStatusState()

FLR_RESULT bosonGet2ptNucStatusStateString(const uint32_t statusState, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptNucStatusStateString(statusState, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptNucStatusStateString()

FLR_RESULT bosonGet2ptNucResultCode(uint32_t *resultCode, uint32_t *resultStringLength){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptNucResultCode(resultCode, resultStringLength);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptNucResultCode()

FLR_RESULT bosonGet2ptNucResultString(const uint32_t resultNumber, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptNucResultString(resultNumber, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptNucResultString()

FLR_RESULT boson2ptNucStart(){
    FLR_RESULT returncode = CLIENT_pkgBoson2ptNucStart();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of 2ptNucStart()

FLR_RESULT boson2ptNucNext(){
    FLR_RESULT returncode = CLIENT_pkgBoson2ptNucNext();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of 2ptNucNext()

FLR_RESULT boson2ptNucAbort(){
    FLR_RESULT returncode = CLIENT_pkgBoson2ptNucAbort();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of 2ptNucAbort()

FLR_RESULT bosonSetExtSyncMode(const FLR_BOSON_EXT_SYNC_MODE_E mode){
    FLR_RESULT returncode = CLIENT_pkgBosonSetExtSyncMode(mode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetExtSyncMode()

FLR_RESULT bosonGetExtSyncMode(FLR_BOSON_EXT_SYNC_MODE_E *mode){
    FLR_RESULT returncode = CLIENT_pkgBosonGetExtSyncMode(mode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetExtSyncMode()

FLR_RESULT bosonGetLastCommand(uint32_t *sequenceNum, uint32_t *cmdID){
    FLR_RESULT returncode = CLIENT_pkgBosonGetLastCommand(sequenceNum, cmdID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastCommand()

FLR_RESULT bosonSet2ptFrameStdClipValue(const float frameStdClipValue){
    FLR_RESULT returncode = CLIENT_pkgBosonSet2ptFrameStdClipValue(frameStdClipValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Set2ptFrameStdClipValue()

FLR_RESULT bosonGet2ptFrameStdClipValue(float *frameStdClipValue){
    FLR_RESULT returncode = CLIENT_pkgBosonGet2ptFrameStdClipValue(frameStdClipValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Get2ptFrameStdClipValue()

FLR_RESULT bosonGetSensorHostCalVersion(uint32_t *version){
    FLR_RESULT returncode = CLIENT_pkgBosonGetSensorHostCalVersion(version);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSensorHostCalVersion()

FLR_RESULT bosonSetDesiredStartupTableNumber(const int32_t table){
    FLR_RESULT returncode = CLIENT_pkgBosonSetDesiredStartupTableNumber(table);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDesiredStartupTableNumber()

FLR_RESULT bosonGetDesiredStartupTableNumber(int32_t *table){
    FLR_RESULT returncode = CLIENT_pkgBosonGetDesiredStartupTableNumber(table);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDesiredStartupTableNumber()

FLR_RESULT bosonSetNvFFCMeanValueLens0(const float meanValue){
    FLR_RESULT returncode = CLIENT_pkgBosonSetNvFFCMeanValueLens0(meanValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetNvFFCMeanValueLens0()

FLR_RESULT bosonGetNvFFCMeanValueLens0(float *meanValue){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCMeanValueLens0(meanValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCMeanValueLens0()

FLR_RESULT bosonSetNvFFCMeanValueLens1(const float meanValue){
    FLR_RESULT returncode = CLIENT_pkgBosonSetNvFFCMeanValueLens1(meanValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetNvFFCMeanValueLens1()

FLR_RESULT bosonGetNvFFCMeanValueLens1(float *meanValue){
    FLR_RESULT returncode = CLIENT_pkgBosonGetNvFFCMeanValueLens1(meanValue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNvFFCMeanValueLens1()

FLR_RESULT bosonSetInvertImage(const FLR_ENABLE_E invertImage){
    FLR_RESULT returncode = CLIENT_pkgBosonSetInvertImage(invertImage);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetInvertImage()

FLR_RESULT bosonGetInvertImage(FLR_ENABLE_E *invertImage){
    FLR_RESULT returncode = CLIENT_pkgBosonGetInvertImage(invertImage);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetInvertImage()

FLR_RESULT bosonSetRevertImage(const FLR_ENABLE_E revertImage){
    FLR_RESULT returncode = CLIENT_pkgBosonSetRevertImage(revertImage);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetRevertImage()

FLR_RESULT bosonGetRevertImage(FLR_ENABLE_E *revertImage){
    FLR_RESULT returncode = CLIENT_pkgBosonGetRevertImage(revertImage);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRevertImage()

FLR_RESULT bosonGetTimeStamp(const FLR_BOSON_TIMESTAMPTYPE_E timeStampType, float *timeStamp){
    FLR_RESULT returncode = CLIENT_pkgBosonGetTimeStamp(timeStampType, timeStamp);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTimeStamp()

FLR_RESULT bosonGetISPFrameCount(uint32_t *ispFrameCount){
    FLR_RESULT returncode = CLIENT_pkgBosonGetISPFrameCount(ispFrameCount);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetISPFrameCount()

FLR_RESULT bosonWriteUserBadPixelsToAllTables(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteUserBadPixelsToAllTables();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteUserBadPixelsToAllTables()

FLR_RESULT bosonWriteFactoryBadPixelsToAllTables(){
    FLR_RESULT returncode = CLIENT_pkgBosonWriteFactoryBadPixelsToAllTables();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteFactoryBadPixelsToAllTables()

FLR_RESULT bosonGetTempDiodeStatus(FLR_BOSON_TEMP_DIODE_STATUS_E *status){
    FLR_RESULT returncode = CLIENT_pkgBosonGetTempDiodeStatus(status);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTempDiodeStatus()

FLR_RESULT bosonClearFactoryBadPixelsInDDR(){
    FLR_RESULT returncode = CLIENT_pkgBosonClearFactoryBadPixelsInDDR();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ClearFactoryBadPixelsInDDR()

FLR_RESULT bosonGetFfcWaitOpenFrames(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFfcWaitOpenFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcWaitOpenFrames()

FLR_RESULT bosonSetFfcWaitOpenFrames(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFfcWaitOpenFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFfcWaitOpenFrames()

FLR_RESULT bosonGetFfcWaitOpenFlagSettleFrames(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgBosonGetFfcWaitOpenFlagSettleFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFfcWaitOpenFlagSettleFrames()

FLR_RESULT bosonSetFfcWaitOpenFlagSettleFrames(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgBosonSetFfcWaitOpenFlagSettleFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFfcWaitOpenFlagSettleFrames()

FLR_RESULT dvoSetAnalogVideoState(const FLR_ENABLE_E analogVideoState){
    FLR_RESULT returncode = CLIENT_pkgDvoSetAnalogVideoState(analogVideoState);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetAnalogVideoState()

FLR_RESULT dvoGetAnalogVideoState(FLR_ENABLE_E *analogVideoState){
    FLR_RESULT returncode = CLIENT_pkgDvoGetAnalogVideoState(analogVideoState);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetAnalogVideoState()

FLR_RESULT dvoSetOutputFormat(const FLR_DVO_OUTPUT_FORMAT_E format){
    FLR_RESULT returncode = CLIENT_pkgDvoSetOutputFormat(format);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutputFormat()

FLR_RESULT dvoGetOutputFormat(FLR_DVO_OUTPUT_FORMAT_E *format){
    FLR_RESULT returncode = CLIENT_pkgDvoGetOutputFormat(format);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutputFormat()

FLR_RESULT dvoSetOutputYCbCrSettings(const FLR_DVO_YCBCR_SETTINGS_T settings){
    FLR_RESULT returncode = CLIENT_pkgDvoSetOutputYCbCrSettings(settings);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutputYCbCrSettings()

FLR_RESULT dvoGetOutputYCbCrSettings(FLR_DVO_YCBCR_SETTINGS_T *settings){
    FLR_RESULT returncode = CLIENT_pkgDvoGetOutputYCbCrSettings(settings);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutputYCbCrSettings()

FLR_RESULT dvoSetOutputRGBSettings(const FLR_DVO_RGB_SETTINGS_T settings){
    FLR_RESULT returncode = CLIENT_pkgDvoSetOutputRGBSettings(settings);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutputRGBSettings()

FLR_RESULT dvoGetOutputRGBSettings(FLR_DVO_RGB_SETTINGS_T *settings){
    FLR_RESULT returncode = CLIENT_pkgDvoGetOutputRGBSettings(settings);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutputRGBSettings()

FLR_RESULT dvoApplyCustomSettings(){
    FLR_RESULT returncode = CLIENT_pkgDvoApplyCustomSettings();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ApplyCustomSettings()

FLR_RESULT dvoSetDisplayMode(const FLR_DVO_DISPLAY_MODE_E displayMode){
    FLR_RESULT returncode = CLIENT_pkgDvoSetDisplayMode(displayMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDisplayMode()

FLR_RESULT dvoGetDisplayMode(FLR_DVO_DISPLAY_MODE_E *displayMode){
    FLR_RESULT returncode = CLIENT_pkgDvoGetDisplayMode(displayMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDisplayMode()

FLR_RESULT dvoSetType(const FLR_DVO_TYPE_E tap){
    FLR_RESULT returncode = CLIENT_pkgDvoSetType(tap);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetType()

FLR_RESULT dvoGetType(FLR_DVO_TYPE_E *tap){
    FLR_RESULT returncode = CLIENT_pkgDvoGetType(tap);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetType()

FLR_RESULT dvoSetVideoStandard(const FLR_DVO_VIDEO_STANDARD_E videoStandard){
    FLR_RESULT returncode = CLIENT_pkgDvoSetVideoStandard(videoStandard);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetVideoStandard()

FLR_RESULT dvoGetVideoStandard(FLR_DVO_VIDEO_STANDARD_E *videoStandard){
    FLR_RESULT returncode = CLIENT_pkgDvoGetVideoStandard(videoStandard);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetVideoStandard()

FLR_RESULT dvoSetCheckVideoDacPresent(const FLR_ENABLE_E checkVideoDacPresent){
    FLR_RESULT returncode = CLIENT_pkgDvoSetCheckVideoDacPresent(checkVideoDacPresent);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetCheckVideoDacPresent()

FLR_RESULT dvoGetCheckVideoDacPresent(FLR_ENABLE_E *checkVideoDacPresent){
    FLR_RESULT returncode = CLIENT_pkgDvoGetCheckVideoDacPresent(checkVideoDacPresent);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCheckVideoDacPresent()

FLR_RESULT dvoSetCustomLcdConfig(const FLR_DVO_LCD_CONFIG_ID_E id, const FLR_DVO_LCD_CONFIG_T config){
    FLR_RESULT returncode = CLIENT_pkgDvoSetCustomLcdConfig(id, config);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetCustomLcdConfig()

FLR_RESULT dvoGetCustomLcdConfig(const FLR_DVO_LCD_CONFIG_ID_E id, FLR_DVO_LCD_CONFIG_T *config){
    FLR_RESULT returncode = CLIENT_pkgDvoGetCustomLcdConfig(id, config);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCustomLcdConfig()

FLR_RESULT dvoSetLCDConfig(const FLR_DVO_LCD_CONFIG_ID_E id){
    FLR_RESULT returncode = CLIENT_pkgDvoSetLCDConfig(id);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetLCDConfig()

FLR_RESULT dvoGetLCDConfig(FLR_DVO_LCD_CONFIG_ID_E *id){
    FLR_RESULT returncode = CLIENT_pkgDvoGetLCDConfig(id);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLCDConfig()

FLR_RESULT dvoGetClockInfo(uint32_t *horizontalSyncWidth, uint32_t *verticalSyncWidth, uint32_t *clocksPerRowPeriod, uint32_t *horizontalFrontPorch, uint32_t *horizontalBackPorch, uint32_t *frontTelemetryPixels, uint32_t *rearTelemetryPixels, uint32_t *videoColumns, uint32_t *validColumns, uint32_t *telemetryRows, uint32_t *videoRows, uint32_t *validRows, uint32_t *verticalFrontPorch, uint32_t *verticalBackPorch, uint32_t *rowPeriodsPerFrame, uint32_t *clocksPerFrame, float *clockRateInMHz, float *frameRateInHz, uint32_t *validOnRisingEdge, uint32_t *dataWidthInBits){
    FLR_RESULT returncode = CLIENT_pkgDvoGetClockInfo(horizontalSyncWidth, verticalSyncWidth, clocksPerRowPeriod, horizontalFrontPorch, horizontalBackPorch, frontTelemetryPixels, rearTelemetryPixels, videoColumns, validColumns, telemetryRows, videoRows, validRows, verticalFrontPorch, verticalBackPorch, rowPeriodsPerFrame, clocksPerFrame, clockRateInMHz, frameRateInHz, validOnRisingEdge, dataWidthInBits);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetClockInfo()

FLR_RESULT dvoSetAllCustomLcdConfigs(const FLR_DVO_LCD_CONFIG_T config0, const FLR_DVO_LCD_CONFIG_T config1){
    FLR_RESULT returncode = CLIENT_pkgDvoSetAllCustomLcdConfigs(config0, config1);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetAllCustomLcdConfigs()

FLR_RESULT dvoGetAllCustomLcdConfigs(FLR_DVO_LCD_CONFIG_T *config0, FLR_DVO_LCD_CONFIG_T *config1){
    FLR_RESULT returncode = CLIENT_pkgDvoGetAllCustomLcdConfigs(config0, config1);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetAllCustomLcdConfigs()

FLR_RESULT dvoSetOutputIr16Format(const FLR_DVO_OUTPUT_IR16_FORMAT_E format){
    FLR_RESULT returncode = CLIENT_pkgDvoSetOutputIr16Format(format);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutputIr16Format()

FLR_RESULT dvoGetOutputIr16Format(FLR_DVO_OUTPUT_IR16_FORMAT_E *format){
    FLR_RESULT returncode = CLIENT_pkgDvoGetOutputIr16Format(format);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutputIr16Format()

FLR_RESULT captureSingleFrame(){
    FLR_RESULT returncode = CLIENT_pkgCaptureSingleFrame();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SingleFrame()

FLR_RESULT captureFrames(const FLR_CAPTURE_SETTINGS_T data){
    FLR_RESULT returncode = CLIENT_pkgCaptureFrames(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Frames()

FLR_RESULT captureSingleFrameWithSrc(const FLR_CAPTURE_SRC_E data){
    FLR_RESULT returncode = CLIENT_pkgCaptureSingleFrameWithSrc(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SingleFrameWithSrc()

FLR_RESULT captureSingleFrameToFile(){
    FLR_RESULT returncode = CLIENT_pkgCaptureSingleFrameToFile();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SingleFrameToFile()

FLR_RESULT scnrSetEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnableState()

FLR_RESULT scnrGetEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnableState()

FLR_RESULT scnrSetThColSum(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetThColSum(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThColSum()

FLR_RESULT scnrGetThColSum(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetThColSum(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThColSum()

FLR_RESULT scnrSetThPixel(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetThPixel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThPixel()

FLR_RESULT scnrGetThPixel(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetThPixel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixel()

FLR_RESULT scnrSetMaxCorr(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetMaxCorr(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMaxCorr()

FLR_RESULT scnrGetMaxCorr(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetMaxCorr(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxCorr()

FLR_RESULT scnrGetThPixelApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetThPixelApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixelApplied()

FLR_RESULT scnrGetMaxCorrApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetMaxCorrApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxCorrApplied()

FLR_RESULT scnrSetThColSumSafe(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetThColSumSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThColSumSafe()

FLR_RESULT scnrGetThColSumSafe(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetThColSumSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThColSumSafe()

FLR_RESULT scnrSetThPixelSafe(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetThPixelSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThPixelSafe()

FLR_RESULT scnrGetThPixelSafe(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetThPixelSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixelSafe()

FLR_RESULT scnrSetMaxCorrSafe(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgScnrSetMaxCorrSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMaxCorrSafe()

FLR_RESULT scnrGetMaxCorrSafe(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgScnrGetMaxCorrSafe(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxCorrSafe()

FLR_RESULT agcSetPercentPerBin(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetPercentPerBin(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetPercentPerBin()

FLR_RESULT agcGetPercentPerBin(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetPercentPerBin(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPercentPerBin()

FLR_RESULT agcSetLinearPercent(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetLinearPercent(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetLinearPercent()

FLR_RESULT agcGetLinearPercent(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetLinearPercent(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLinearPercent()

FLR_RESULT agcSetOutlierCut(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetOutlierCut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutlierCut()

FLR_RESULT agcGetOutlierCut(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetOutlierCut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutlierCut()

FLR_RESULT agcGetDrOut(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetDrOut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDrOut()

FLR_RESULT agcSetMaxGain(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetMaxGain(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMaxGain()

FLR_RESULT agcGetMaxGain(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetMaxGain(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxGain()

FLR_RESULT agcSetdf(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetdf(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Setdf()

FLR_RESULT agcGetdf(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetdf(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Getdf()

FLR_RESULT agcSetGamma(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetGamma(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetGamma()

FLR_RESULT agcGetGamma(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetGamma(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetGamma()

FLR_RESULT agcGetFirstBin(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetFirstBin(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFirstBin()

FLR_RESULT agcGetLastBin(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetLastBin(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastBin()

FLR_RESULT agcSetDetailHeadroom(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetDetailHeadroom(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDetailHeadroom()

FLR_RESULT agcGetDetailHeadroom(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetDetailHeadroom(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDetailHeadroom()

FLR_RESULT agcSetd2br(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetd2br(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Setd2br()

FLR_RESULT agcGetd2br(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetd2br(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Getd2br()

FLR_RESULT agcSetSigmaR(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetSigmaR(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSigmaR()

FLR_RESULT agcGetSigmaR(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetSigmaR(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSigmaR()

FLR_RESULT agcSetUseEntropy(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetUseEntropy(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetUseEntropy()

FLR_RESULT agcGetUseEntropy(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetUseEntropy(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetUseEntropy()

FLR_RESULT agcSetROI(const FLR_ROI_T roi){
    FLR_RESULT returncode = CLIENT_pkgAgcSetROI(roi);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetROI()

FLR_RESULT agcGetROI(FLR_ROI_T *roi){
    FLR_RESULT returncode = CLIENT_pkgAgcGetROI(roi);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetROI()

FLR_RESULT agcGetMaxGainApplied(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetMaxGainApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxGainApplied()

FLR_RESULT agcGetSigmaRApplied(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetSigmaRApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSigmaRApplied()

FLR_RESULT agcSetOutlierCutBalance(const float data){
    FLR_RESULT returncode = CLIENT_pkgAgcSetOutlierCutBalance(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutlierCutBalance()

FLR_RESULT agcGetOutlierCutBalance(float *data){
    FLR_RESULT returncode = CLIENT_pkgAgcGetOutlierCutBalance(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutlierCutBalance()

FLR_RESULT agcGetOutlierCutApplied(float *percentHigh, float *percentLow){
    FLR_RESULT returncode = CLIENT_pkgAgcGetOutlierCutApplied(percentHigh, percentLow);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutlierCutApplied()

FLR_RESULT agcGetTfThresholds(uint16_t *tf_thresholdMin, uint16_t *tf_thresholdMax){
    FLR_RESULT returncode = CLIENT_pkgAgcGetTfThresholds(tf_thresholdMin, tf_thresholdMax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTfThresholds()

FLR_RESULT agcSetTfThresholds(const uint16_t tf_thresholdMin, const uint16_t tf_thresholdMax){
    FLR_RESULT returncode = CLIENT_pkgAgcSetTfThresholds(tf_thresholdMin, tf_thresholdMax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTfThresholds()

FLR_RESULT agcGetMode(FLR_AGC_MODE_E *mode){
    FLR_RESULT returncode = CLIENT_pkgAgcGetMode(mode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMode()

FLR_RESULT agcSetMode(const FLR_AGC_MODE_E mode){
    FLR_RESULT returncode = CLIENT_pkgAgcSetMode(mode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMode()

FLR_RESULT tfSetEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgTfSetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnableState()

FLR_RESULT tfGetEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnableState()

FLR_RESULT tfSetDelta_nf(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgTfSetDelta_nf(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDelta_nf()

FLR_RESULT tfGetDelta_nf(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetDelta_nf(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDelta_nf()

FLR_RESULT tfSetTHDeltaMotion(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgTfSetTHDeltaMotion(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTHDeltaMotion()

FLR_RESULT tfGetTHDeltaMotion(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetTHDeltaMotion(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTHDeltaMotion()

FLR_RESULT tfSetWLut(const FLR_TF_WLUT_T data){
    FLR_RESULT returncode = CLIENT_pkgTfSetWLut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetWLut()

FLR_RESULT tfGetWLut(FLR_TF_WLUT_T *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetWLut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetWLut()

FLR_RESULT tfGetMotionCount(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetMotionCount(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMotionCount()

FLR_RESULT tfSetMotionThreshold(const uint32_t data){
    FLR_RESULT returncode = CLIENT_pkgTfSetMotionThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMotionThreshold()

FLR_RESULT tfGetMotionThreshold(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetMotionThreshold(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMotionThreshold()

FLR_RESULT tfGetDelta_nfApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetDelta_nfApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDelta_nfApplied()

FLR_RESULT tfGetTHDeltaMotionApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetTHDeltaMotionApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTHDeltaMotionApplied()

FLR_RESULT tfSetTempSignalCompFactorLut(const FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T data){
    FLR_RESULT returncode = CLIENT_pkgTfSetTempSignalCompFactorLut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTempSignalCompFactorLut()

FLR_RESULT tfGetTempSignalCompFactorLut(FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T *data){
    FLR_RESULT returncode = CLIENT_pkgTfGetTempSignalCompFactorLut(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTempSignalCompFactorLut()

FLR_RESULT tfGetRnf(uint16_t *rnf){
    FLR_RESULT returncode = CLIENT_pkgTfGetRnf(rnf);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetRnf()

FLR_RESULT memReadCapture(const uint8_t bufferNum, const uint32_t offset, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgMemReadCapture(bufferNum, offset, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReadCapture()

FLR_RESULT memGetCaptureSize(uint32_t *bytes, uint16_t *rows, uint16_t *columns){
    FLR_RESULT returncode = CLIENT_pkgMemGetCaptureSize(bytes, rows, columns);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCaptureSize()

FLR_RESULT memWriteFlash(const FLR_MEM_LOCATION_E location, const uint8_t index, const uint32_t offset, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgMemWriteFlash(location, index, offset, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of WriteFlash()

FLR_RESULT memReadFlash(const FLR_MEM_LOCATION_E location, const uint8_t index, const uint32_t offset, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgMemReadFlash(location, index, offset, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReadFlash()

FLR_RESULT memGetFlashSize(const FLR_MEM_LOCATION_E location, uint32_t *bytes){
    FLR_RESULT returncode = CLIENT_pkgMemGetFlashSize(location, bytes);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFlashSize()

FLR_RESULT memEraseFlash(const FLR_MEM_LOCATION_E location, const uint8_t index){
    FLR_RESULT returncode = CLIENT_pkgMemEraseFlash(location, index);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of EraseFlash()

FLR_RESULT memEraseFlashPartial(const FLR_MEM_LOCATION_E location, const uint8_t index, const uint32_t offset, const uint32_t length){
    FLR_RESULT returncode = CLIENT_pkgMemEraseFlashPartial(location, index, offset, length);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of EraseFlashPartial()

FLR_RESULT memReadCurrentGain(const uint32_t offset, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgMemReadCurrentGain(offset, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReadCurrentGain()

FLR_RESULT memGetGainSize(uint32_t *bytes, uint16_t *rows, uint16_t *columns){
    FLR_RESULT returncode = CLIENT_pkgMemGetGainSize(bytes, rows, columns);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetGainSize()

FLR_RESULT memGetCaptureSizeSrc(const FLR_CAPTURE_SRC_E src, uint32_t *bytes, uint16_t *rows, uint16_t *columns){
    FLR_RESULT returncode = CLIENT_pkgMemGetCaptureSizeSrc(src, bytes, rows, columns);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCaptureSizeSrc()

FLR_RESULT memReadCaptureSrc(const FLR_CAPTURE_SRC_E src, const uint8_t bufferNum, const uint32_t offset, const uint16_t sizeInBytes, uint8_t *data){
    if (sizeInBytes > MaxMemoryChunk)
    {
        return FLR_DATA_SIZE_ERROR;
    }
    FLR_RESULT returncode = CLIENT_pkgMemReadCaptureSrc(src, bufferNum, offset, sizeInBytes, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReadCaptureSrc()

FLR_RESULT colorLutSetControl(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgColorlutSetControl(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetControl()

FLR_RESULT colorLutGetControl(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgColorlutGetControl(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetControl()

FLR_RESULT colorLutSetId(const FLR_COLORLUT_ID_E data){
    FLR_RESULT returncode = CLIENT_pkgColorlutSetId(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetId()

FLR_RESULT colorLutGetId(FLR_COLORLUT_ID_E *data){
    FLR_RESULT returncode = CLIENT_pkgColorlutGetId(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetId()

FLR_RESULT colorLutSetOutlineColor(const uint8_t red, const uint8_t green, const uint8_t blue){
    FLR_RESULT returncode = CLIENT_pkgColorlutSetOutlineColor(red, green, blue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutlineColor()

FLR_RESULT colorLutGetOutlineColor(uint8_t *red, uint8_t *green, uint8_t *blue){
    FLR_RESULT returncode = CLIENT_pkgColorlutGetOutlineColor(red, green, blue);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutlineColor()

FLR_RESULT colorLutSetOutlineDisplay(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgColorlutSetOutlineDisplay(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetOutlineDisplay()

FLR_RESULT colorLutGetOutlineDisplay(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgColorlutGetOutlineDisplay(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetOutlineDisplay()

FLR_RESULT spnrSetEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnableState()

FLR_RESULT spnrGetEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnableState()

FLR_RESULT spnrGetState(FLR_SPNR_STATE_E *data){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetState()

FLR_RESULT spnrSetFrameDelay(const uint32_t data){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetFrameDelay(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFrameDelay()

FLR_RESULT spnrGetFrameDelay(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetFrameDelay(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFrameDelay()

FLR_RESULT spnrGetSFApplied(float *sf){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetSFApplied(sf);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSFApplied()

FLR_RESULT spnrSetPSDKernel(const FLR_SPNR_PSD_KERNEL_T data){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetPSDKernel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetPSDKernel()

FLR_RESULT spnrGetPSDKernel(FLR_SPNR_PSD_KERNEL_T *data){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetPSDKernel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPSDKernel()

FLR_RESULT spnrSetSFMin(const float sfmin){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetSFMin(sfmin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSFMin()

FLR_RESULT spnrGetSFMin(float *sfmin){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetSFMin(sfmin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSFMin()

FLR_RESULT spnrSetSFMax(const float sfmax){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetSFMax(sfmax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSFMax()

FLR_RESULT spnrGetSFMax(float *sfmax){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetSFMax(sfmax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSFMax()

FLR_RESULT spnrSetDFMin(const float dfmin){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetDFMin(dfmin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDFMin()

FLR_RESULT spnrGetDFMin(float *dfmin){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetDFMin(dfmin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDFMin()

FLR_RESULT spnrSetDFMax(const float dfmax){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetDFMax(dfmax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDFMax()

FLR_RESULT spnrGetDFMax(float *dfmax){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetDFMax(dfmax);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDFMax()

FLR_RESULT spnrSetNormTarget(const float normTarget){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetNormTarget(normTarget);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetNormTarget()

FLR_RESULT spnrGetNormTarget(float *normTarget){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetNormTarget(normTarget);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNormTarget()

FLR_RESULT spnrGetNormTargetApplied(float *normTargetApplied){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetNormTargetApplied(normTargetApplied);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetNormTargetApplied()

FLR_RESULT spnrSetThPix(const uint16_t th_pix){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetThPix(th_pix);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThPix()

FLR_RESULT spnrGetThPix(uint16_t *th_pix){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetThPix(th_pix);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPix()

FLR_RESULT spnrSetThPixSum(const uint16_t th_pixSum){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetThPixSum(th_pixSum);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThPixSum()

FLR_RESULT spnrGetThPixSum(uint16_t *th_pixSum){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetThPixSum(th_pixSum);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixSum()

FLR_RESULT spnrSetMaxcorr(const uint16_t maxcorr){
    FLR_RESULT returncode = CLIENT_pkgSpnrSetMaxcorr(maxcorr);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMaxcorr()

FLR_RESULT spnrGetMaxcorr(uint16_t *maxcorr){
    FLR_RESULT returncode = CLIENT_pkgSpnrGetMaxcorr(maxcorr);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxcorr()

FLR_RESULT scalerGetMaxZoom(uint32_t *zoom){
    FLR_RESULT returncode = CLIENT_pkgScalerGetMaxZoom(zoom);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxZoom()

FLR_RESULT scalerSetZoom(const FLR_SCALER_ZOOM_PARAMS_T zoomParams){
    FLR_RESULT returncode = CLIENT_pkgScalerSetZoom(zoomParams);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetZoom()

FLR_RESULT scalerGetZoom(FLR_SCALER_ZOOM_PARAMS_T *zoomParams){
    FLR_RESULT returncode = CLIENT_pkgScalerGetZoom(zoomParams);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetZoom()

FLR_RESULT scalerSetFractionalZoom(const uint32_t zoomNumerator, const uint32_t zoomDenominator, const uint32_t zoomXCenter, const uint32_t zoomYCenter, const FLR_ENABLE_E inChangeEnable, const uint32_t zoomOutXCenter, const uint32_t zoomOutYCenter, const FLR_ENABLE_E outChangeEnable){
    FLR_RESULT returncode = CLIENT_pkgScalerSetFractionalZoom(zoomNumerator, zoomDenominator, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFractionalZoom()

FLR_RESULT scalerSetIndexZoom(const uint32_t zoomIndex, const uint32_t zoomXCenter, const uint32_t zoomYCenter, const FLR_ENABLE_E inChangeEnable, const uint32_t zoomOutXCenter, const uint32_t zoomOutYCenter, const FLR_ENABLE_E outChangeEnable){
    FLR_RESULT returncode = CLIENT_pkgScalerSetIndexZoom(zoomIndex, zoomXCenter, zoomYCenter, inChangeEnable, zoomOutXCenter, zoomOutYCenter, outChangeEnable);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetIndexZoom()

FLR_RESULT sysctrlSetFreezeState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgSysctrlSetFreezeState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFreezeState()

FLR_RESULT sysctrlGetFreezeState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgSysctrlGetFreezeState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFreezeState()

FLR_RESULT sysctrlGetCameraFrameRate(uint32_t *frameRate){
    FLR_RESULT returncode = CLIENT_pkgSysctrlGetCameraFrameRate(frameRate);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCameraFrameRate()

FLR_RESULT sysctrlGetUptimeSecs(uint32_t *uptime){
    FLR_RESULT returncode = CLIENT_pkgSysctrlGetUptimeSecs(uptime);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetUptimeSecs()

FLR_RESULT testRampSetType(const uint8_t index, const FLR_TESTRAMP_TYPE_E data){
    FLR_RESULT returncode = CLIENT_pkgTestrampSetType(index, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetType()

FLR_RESULT testRampGetType(const uint8_t index, FLR_TESTRAMP_TYPE_E *data){
    FLR_RESULT returncode = CLIENT_pkgTestrampGetType(index, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetType()

FLR_RESULT testRampSetSettings(const uint8_t index, const FLR_TESTRAMP_SETTINGS_T data){
    FLR_RESULT returncode = CLIENT_pkgTestrampSetSettings(index, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSettings()

FLR_RESULT testRampGetSettings(const uint8_t index, FLR_TESTRAMP_SETTINGS_T *data){
    FLR_RESULT returncode = CLIENT_pkgTestrampGetSettings(index, data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetSettings()

FLR_RESULT testRampSetMotionState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgTestrampSetMotionState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMotionState()

FLR_RESULT testRampGetMotionState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgTestrampGetMotionState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMotionState()

FLR_RESULT testRampSetIndex(const uint8_t data){
    FLR_RESULT returncode = CLIENT_pkgTestrampSetIndex(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetIndex()

FLR_RESULT testRampGetIndex(uint8_t *data){
    FLR_RESULT returncode = CLIENT_pkgTestrampGetIndex(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetIndex()

FLR_RESULT testRampGetMaxIndex(uint8_t *data){
    FLR_RESULT returncode = CLIENT_pkgTestrampGetMaxIndex(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxIndex()

FLR_RESULT symbologySetEnable(const FLR_ENABLE_E draw_symbols){
    FLR_RESULT returncode = CLIENT_pkgSymbologySetEnable(draw_symbols);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnable()

FLR_RESULT symbologyCreateBitmap(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateBitmap(ID, pos_X, pos_Y, width, height);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateBitmap()

FLR_RESULT symbologySendData(const uint8_t ID, const int16_t size, const uint8_t text[]){
    FLR_RESULT returncode = CLIENT_pkgSymbologySendData(ID, size, text);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SendData()

FLR_RESULT symbologyCreateArc(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const float start_angle, const float end_angle, const uint32_t color){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateArc(ID, pos_X, pos_Y, width, height, start_angle, end_angle, color);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateArc()

FLR_RESULT symbologyCreateText(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const int8_t font, const int16_t size, const FLR_SYMBOLOGY_TEXT_ALIGNMENT_E alignment, const uint32_t color, const uint8_t text[]){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateText(ID, pos_X, pos_Y, width, height, font, size, alignment, color, text);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateText()

FLR_RESULT symbologyMoveSprite(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y){
    FLR_RESULT returncode = CLIENT_pkgSymbologyMoveSprite(ID, pos_X, pos_Y);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of MoveSprite()

FLR_RESULT symbologyAddToGroup(const uint8_t ID, const uint8_t group_ID){
    FLR_RESULT returncode = CLIENT_pkgSymbologyAddToGroup(ID, group_ID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of AddToGroup()

FLR_RESULT symbologyRemoveFromGroup(const uint8_t ID, const uint8_t group_ID){
    FLR_RESULT returncode = CLIENT_pkgSymbologyRemoveFromGroup(ID, group_ID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of RemoveFromGroup()

FLR_RESULT symbologyUpdateAndShow(const uint8_t ID, const uint8_t visible){
    FLR_RESULT returncode = CLIENT_pkgSymbologyUpdateAndShow(ID, visible);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of UpdateAndShow()

FLR_RESULT symbologyUpdateAndShowGroup(const uint8_t group_ID, const uint8_t visible){
    FLR_RESULT returncode = CLIENT_pkgSymbologyUpdateAndShowGroup(group_ID, visible);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of UpdateAndShowGroup()

FLR_RESULT symbologyDelete(const uint8_t ID){
    FLR_RESULT returncode = CLIENT_pkgSymbologyDelete(ID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Delete()

FLR_RESULT symbologyDeleteGroup(const uint8_t group_ID){
    FLR_RESULT returncode = CLIENT_pkgSymbologyDeleteGroup(group_ID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of DeleteGroup()

FLR_RESULT symbologyCreateFilledRectangle(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const uint32_t color){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateFilledRectangle(ID, pos_X, pos_Y, width, height, color);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateFilledRectangle()

FLR_RESULT symbologyCreateOutlinedRectangle(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const uint32_t color){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateOutlinedRectangle(ID, pos_X, pos_Y, width, height, color);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateOutlinedRectangle()

FLR_RESULT symbologyCreateBitmapFromPng(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t size){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateBitmapFromPng(ID, pos_X, pos_Y, size);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateBitmapFromPng()

FLR_RESULT symbologyCreateCompressedBitmap(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateCompressedBitmap(ID, pos_X, pos_Y, width, height);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateCompressedBitmap()

FLR_RESULT symbologyCreateBitmapFromPngFile(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const uint8_t path[]){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateBitmapFromPngFile(ID, pos_X, pos_Y, path);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateBitmapFromPngFile()

FLR_RESULT symbologyCreateBitmapFromFile(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const uint8_t path[], const FLR_SYMBOLOGY_IMAGE_TYPE_E imageType){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateBitmapFromFile(ID, pos_X, pos_Y, path, imageType);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateBitmapFromFile()

FLR_RESULT symbologyResetWritePosition(const uint8_t ID){
    FLR_RESULT returncode = CLIENT_pkgSymbologyResetWritePosition(ID);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ResetWritePosition()

FLR_RESULT symbologyMoveByOffset(const uint8_t ID, const int16_t off_X, const int16_t off_Y){
    FLR_RESULT returncode = CLIENT_pkgSymbologyMoveByOffset(ID, off_X, off_Y);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of MoveByOffset()

FLR_RESULT symbologyMoveGroupByOffset(const uint8_t ID, const int16_t off_X, const int16_t off_Y){
    FLR_RESULT returncode = CLIENT_pkgSymbologyMoveGroupByOffset(ID, off_X, off_Y);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of MoveGroupByOffset()

FLR_RESULT symbologyCreateFilledEllipse(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const uint32_t color){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateFilledEllipse(ID, pos_X, pos_Y, width, height, color);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateFilledEllipse()

FLR_RESULT symbologyCreateLine(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t pos_X2, const int16_t pos_Y2, const uint32_t color){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateLine(ID, pos_X, pos_Y, pos_X2, pos_Y2, color);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateLine()

FLR_RESULT symbologySetZorder(const uint8_t ID, const uint8_t zorder){
    FLR_RESULT returncode = CLIENT_pkgSymbologySetZorder(ID, zorder);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetZorder()

FLR_RESULT symbologySaveConfiguration(){
    FLR_RESULT returncode = CLIENT_pkgSymbologySaveConfiguration();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SaveConfiguration()

FLR_RESULT symbologyReloadConfiguration(){
    FLR_RESULT returncode = CLIENT_pkgSymbologyReloadConfiguration();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of ReloadConfiguration()

FLR_RESULT symbologyGetEnable(FLR_ENABLE_E *draw_symbols){
    FLR_RESULT returncode = CLIENT_pkgSymbologyGetEnable(draw_symbols);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnable()

FLR_RESULT symbologySetClonesNumber(const uint8_t ID, const uint8_t numberOfClones){
    FLR_RESULT returncode = CLIENT_pkgSymbologySetClonesNumber(ID, numberOfClones);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetClonesNumber()

FLR_RESULT symbologyMoveCloneByOffset(const uint8_t ID, const uint8_t cloneID, const int16_t pos_X, const int16_t pos_Y){
    FLR_RESULT returncode = CLIENT_pkgSymbologyMoveCloneByOffset(ID, cloneID, pos_X, pos_Y);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of MoveCloneByOffset()

FLR_RESULT symbologyMoveCloneSprite(const uint8_t ID, const uint8_t cloneID, const int16_t pos_X, const int16_t pos_Y){
    FLR_RESULT returncode = CLIENT_pkgSymbologyMoveCloneSprite(ID, cloneID, pos_X, pos_Y);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of MoveCloneSprite()

FLR_RESULT symbologySetTransformation(const FLR_SYMBOLOGY_TRANSFORMATION_E transformation){
    FLR_RESULT returncode = CLIENT_pkgSymbologySetTransformation(transformation);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetTransformation()

FLR_RESULT symbologyUpdateAllVisible(){
    FLR_RESULT returncode = CLIENT_pkgSymbologyUpdateAllVisible();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of UpdateAllVisible()

FLR_RESULT symbologySetSizeAndScalingMode(const uint8_t ID, const int16_t width, const int16_t height, const FLR_SYMBOLOGY_SCALING_MODE_E scalingMode){
    FLR_RESULT returncode = CLIENT_pkgSymbologySetSizeAndScalingMode(ID, width, height, scalingMode);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetSizeAndScalingMode()

FLR_RESULT symbologyCreateLineHVT(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t pos_X2, const int16_t pos_Y2, const uint32_t color1, const uint32_t color2, const uint16_t dashLen, const uint16_t thickness){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateLineHVT(ID, pos_X, pos_Y, pos_X2, pos_Y2, color1, color2, dashLen, thickness);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateLineHVT()

FLR_RESULT symbologyCreateTextHVT(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const int8_t font, const int16_t size, const FLR_SYMBOLOGY_TEXT_ALIGNMENT_E alignment, const uint32_t color1, const uint32_t color2, const uint8_t dashLen, const uint8_t text[]){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateTextHVT(ID, pos_X, pos_Y, width, height, font, size, alignment, color1, color2, dashLen, text);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateTextHVT()

FLR_RESULT symbologyCreateTextBg(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const int8_t font, const int16_t size, const FLR_SYMBOLOGY_TEXT_ALIGNMENT_E alignment, const uint32_t color, const uint32_t bgColor, const uint8_t text[]){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateTextBg(ID, pos_X, pos_Y, width, height, font, size, alignment, color, bgColor, text);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateTextBg()

FLR_RESULT symbologyCreateScaledBitmapFromFile(const uint8_t ID, const int16_t pos_X, const int16_t pos_Y, const int16_t width, const int16_t height, const FLR_SYMBOLOGY_SCALING_MODE_E scalingMode, const uint8_t path[], const FLR_SYMBOLOGY_IMAGE_TYPE_E imageType){
    FLR_RESULT returncode = CLIENT_pkgSymbologyCreateScaledBitmapFromFile(ID, pos_X, pos_Y, width, height, scalingMode, path, imageType);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of CreateScaledBitmapFromFile()

FLR_RESULT fileOpsDir(uint8_t dirent[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsDir(dirent);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Dir()

FLR_RESULT fileOpsCd(const uint8_t path[], uint8_t pwd[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsCd(path, pwd);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Cd()

FLR_RESULT fileOpsMd(const uint8_t path[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsMd(path);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Md()

FLR_RESULT fileOpsFopen(const uint8_t path[], const uint8_t mode[], uint32_t *id){
    FLR_RESULT returncode = CLIENT_pkgFileopsFopen(path, mode, id);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Fopen()

FLR_RESULT fileOpsFclose(const uint32_t id){
    FLR_RESULT returncode = CLIENT_pkgFileopsFclose(id);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Fclose()

FLR_RESULT fileOpsFread(const uint32_t id, const uint32_t length, uint8_t buf[], uint32_t *ret){
    FLR_RESULT returncode = CLIENT_pkgFileopsFread(id, length, buf, ret);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Fread()

FLR_RESULT fileOpsFwrite(const uint32_t id, const uint32_t length, const uint8_t buf[], uint32_t *ret){
    FLR_RESULT returncode = CLIENT_pkgFileopsFwrite(id, length, buf, ret);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Fwrite()

FLR_RESULT fileOpsFtell(const uint32_t id, uint32_t *offset){
    FLR_RESULT returncode = CLIENT_pkgFileopsFtell(id, offset);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Ftell()

FLR_RESULT fileOpsFseek(const uint32_t id, const uint32_t offset, const uint32_t origin){
    FLR_RESULT returncode = CLIENT_pkgFileopsFseek(id, offset, origin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Fseek()

FLR_RESULT fileOpsFtruncate(const uint32_t id, const uint32_t length){
    FLR_RESULT returncode = CLIENT_pkgFileopsFtruncate(id, length);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Ftruncate()

FLR_RESULT fileOpsRmdir(const uint8_t path[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsRmdir(path);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Rmdir()

FLR_RESULT fileOpsRm(const uint8_t path[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsRm(path);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Rm()

FLR_RESULT fileOpsRename(const uint8_t oldpath[], const uint8_t newpath[]){
    FLR_RESULT returncode = CLIENT_pkgFileopsRename(oldpath, newpath);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Rename()

FLR_RESULT fileOpsGetFileSize(const uint8_t path[], uint32_t *fileLength){
    FLR_RESULT returncode = CLIENT_pkgFileopsGetFileSize(path, fileLength);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFileSize()

FLR_RESULT jffs2Mount(){
    FLR_RESULT returncode = CLIENT_pkgJffs2Mount();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Mount()

FLR_RESULT jffs2Unmount(){
    FLR_RESULT returncode = CLIENT_pkgJffs2Unmount();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of Unmount()

FLR_RESULT jffs2GetState(FLR_JFFS2_STATE_E *state){
    FLR_RESULT returncode = CLIENT_pkgJffs2GetState(state);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetState()

FLR_RESULT splashScreenSetDuration(const uint32_t screen_num, const uint32_t periodMs){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenSetDuration(screen_num, periodMs);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDuration()

FLR_RESULT splashScreenSetDataType(const uint32_t screen_num, const FLR_SPLASHSCREEN_FILETYPE_E filetype){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenSetDataType(screen_num, filetype);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDataType()

FLR_RESULT splashScreenSetBackground(const uint32_t screen_num, const uint32_t backgroundColor){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenSetBackground(screen_num, backgroundColor);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetBackground()

FLR_RESULT splashScreenGetDuration(const uint32_t screen_num, uint32_t *periodMs){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenGetDuration(screen_num, periodMs);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDuration()

FLR_RESULT splashScreenGetDataType(const uint32_t screen_num, FLR_SPLASHSCREEN_FILETYPE_E *filetype){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenGetDataType(screen_num, filetype);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDataType()

FLR_RESULT splashScreenGetBackground(const uint32_t screen_num, uint32_t *backgroundColor){
    FLR_RESULT returncode = CLIENT_pkgSplashscreenGetBackground(screen_num, backgroundColor);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetBackground()

FLR_RESULT systemSymbolsGetID(const FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, uint8_t *id, FLR_SYSTEMSYMBOLS_ID_TYPE_E *id_type){
    FLR_RESULT returncode = CLIENT_pkgSystemsymbolsGetID(symbol, id, id_type);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetID()

FLR_RESULT systemSymbolsSetID(const FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, const uint8_t id, const FLR_SYSTEMSYMBOLS_ID_TYPE_E id_type){
    FLR_RESULT returncode = CLIENT_pkgSystemsymbolsSetID(symbol, id, id_type);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetID()

FLR_RESULT systemSymbolsGetEnable(const FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, FLR_ENABLE_E *enabled){
    FLR_RESULT returncode = CLIENT_pkgSystemsymbolsGetEnable(symbol, enabled);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnable()

FLR_RESULT systemSymbolsSetEnable(const FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, const FLR_ENABLE_E enabled){
    FLR_RESULT returncode = CLIENT_pkgSystemsymbolsSetEnable(symbol, enabled);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnable()

FLR_RESULT sffcGetScaleFactor(float *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetScaleFactor(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetScaleFactor()

FLR_RESULT sffcGetDeltaTempLinearCoeff(float *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetDeltaTempLinearCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDeltaTempLinearCoeff()

FLR_RESULT sffcSetDeltaTempLinearCoeff(const float data){
    FLR_RESULT returncode = CLIENT_pkgSffcSetDeltaTempLinearCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDeltaTempLinearCoeff()

FLR_RESULT sffcGetDeltaTempOffsetCoeff(float *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetDeltaTempOffsetCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDeltaTempOffsetCoeff()

FLR_RESULT sffcSetDeltaTempOffsetCoeff(const float data){
    FLR_RESULT returncode = CLIENT_pkgSffcSetDeltaTempOffsetCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDeltaTempOffsetCoeff()

FLR_RESULT sffcGetFpaTempLinearCoeff(float *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetFpaTempLinearCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFpaTempLinearCoeff()

FLR_RESULT sffcSetFpaTempLinearCoeff(const float data){
    FLR_RESULT returncode = CLIENT_pkgSffcSetFpaTempLinearCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFpaTempLinearCoeff()

FLR_RESULT sffcGetFpaTempOffsetCoeff(float *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetFpaTempOffsetCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFpaTempOffsetCoeff()

FLR_RESULT sffcSetFpaTempOffsetCoeff(const float data){
    FLR_RESULT returncode = CLIENT_pkgSffcSetFpaTempOffsetCoeff(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetFpaTempOffsetCoeff()

FLR_RESULT sffcGetDeltaTempTimeLimitInSecs(uint32_t *data){
    FLR_RESULT returncode = CLIENT_pkgSffcGetDeltaTempTimeLimitInSecs(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetDeltaTempTimeLimitInSecs()

FLR_RESULT sffcSetDeltaTempTimeLimitInSecs(const uint32_t data){
    FLR_RESULT returncode = CLIENT_pkgSffcSetDeltaTempTimeLimitInSecs(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetDeltaTempTimeLimitInSecs()

FLR_RESULT imageStatsGetTotalHistPixelsInROI(uint32_t *totalPixelsInROI){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetTotalHistPixelsInROI(totalPixelsInROI);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetTotalHistPixelsInROI()

FLR_RESULT imageStatsGetPopBelowLowToHighThresh(uint32_t *popBelowLowToHighThresh){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetPopBelowLowToHighThresh(popBelowLowToHighThresh);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPopBelowLowToHighThresh()

FLR_RESULT imageStatsGetPopAboveHighToLowThresh(uint32_t *popAboveHighToLowThresh){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetPopAboveHighToLowThresh(popAboveHighToLowThresh);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetPopAboveHighToLowThresh()

FLR_RESULT imageStatsSetROI(const FLR_ROI_T roi){
    FLR_RESULT returncode = CLIENT_pkgImagestatsSetROI(roi);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetROI()

FLR_RESULT imageStatsGetROI(FLR_ROI_T *roi){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetROI(roi);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetROI()

FLR_RESULT imageStatsGetFirstBin(uint16_t *firstBin){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetFirstBin(firstBin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFirstBin()

FLR_RESULT imageStatsGetLastBin(uint16_t *lastBin){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetLastBin(lastBin);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastBin()

FLR_RESULT imageStatsGetMean(uint16_t *mean){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetMean(mean);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMean()

FLR_RESULT imageStatsGetFirstBinInROI(uint16_t *firstBinInROI){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetFirstBinInROI(firstBinInROI);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetFirstBinInROI()

FLR_RESULT imageStatsGetLastBinInROI(uint16_t *lastBinInROI){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetLastBinInROI(lastBinInROI);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetLastBinInROI()

FLR_RESULT imageStatsGetMeanInROI(uint16_t *meanInROI){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetMeanInROI(meanInROI);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMeanInROI()

FLR_RESULT imageStatsGetImageStats(uint16_t *meanIntensity, uint16_t *peakIntensity, uint16_t *baseIntensity){
    FLR_RESULT returncode = CLIENT_pkgImagestatsGetImageStats(meanIntensity, peakIntensity, baseIntensity);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetImageStats()

FLR_RESULT srnrSetEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgSrnrSetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetEnableState()

FLR_RESULT srnrGetEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetEnableState()

FLR_RESULT srnrSetThRowSum(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgSrnrSetThRowSum(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThRowSum()

FLR_RESULT srnrGetThRowSum(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetThRowSum(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThRowSum()

FLR_RESULT srnrSetThPixel(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgSrnrSetThPixel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetThPixel()

FLR_RESULT srnrGetThPixel(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetThPixel(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixel()

FLR_RESULT srnrSetMaxCorr(const uint16_t data){
    FLR_RESULT returncode = CLIENT_pkgSrnrSetMaxCorr(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetMaxCorr()

FLR_RESULT srnrGetMaxCorr(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetMaxCorr(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxCorr()

FLR_RESULT srnrGetThPixelApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetThPixelApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetThPixelApplied()

FLR_RESULT srnrGetMaxCorrApplied(uint16_t *data){
    FLR_RESULT returncode = CLIENT_pkgSrnrGetMaxCorrApplied(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMaxCorrApplied()

FLR_RESULT lfsrSetApplyOffsetEnableState(const FLR_ENABLE_E data){
    FLR_RESULT returncode = CLIENT_pkgLfsrSetApplyOffsetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetApplyOffsetEnableState()

FLR_RESULT lfsrGetApplyOffsetEnableState(FLR_ENABLE_E *data){
    FLR_RESULT returncode = CLIENT_pkgLfsrGetApplyOffsetEnableState(data);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetApplyOffsetEnableState()

FLR_RESULT sysinfoGetMonitorSoftwareRev(uint32_t *major, uint32_t *minor, uint32_t *patch){
    FLR_RESULT returncode = CLIENT_pkgSysinfoGetMonitorSoftwareRev(major, minor, patch);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMonitorSoftwareRev()

FLR_RESULT sysinfoGetMonitorBuildVariant(FLR_SYSINFO_MONITOR_BUILD_VARIANT_T *monitorBuildVariant){
    FLR_RESULT returncode = CLIENT_pkgSysinfoGetMonitorBuildVariant(monitorBuildVariant);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetMonitorBuildVariant()

FLR_RESULT sysinfoGetProductName(uint8_t name[]){
    FLR_RESULT returncode = CLIENT_pkgSysinfoGetProductName(name);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetProductName()

FLR_RESULT sysinfoGetCameraSN(uint8_t number[]){
    FLR_RESULT returncode = CLIENT_pkgSysinfoGetCameraSN(number);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetCameraSN()

FLR_RESULT flashIOSetProtectionState(const FLR_ENABLE_E protectionState){
    FLR_RESULT returncode = CLIENT_pkgFlashioSetProtectionState(protectionState);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of SetProtectionState()

FLR_RESULT flashIOGetProtectionState(FLR_ENABLE_E *protectionState){
    FLR_RESULT returncode = CLIENT_pkgFlashioGetProtectionState(protectionState);
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of GetProtectionState()

FLR_RESULT dummyBadCommand(){
    FLR_RESULT returncode = CLIENT_pkgDummyBadCommand();
    // Check for any errorcode
    if((uint32_t) returncode){
        return returncode;
    }
    return R_SUCCESS;
} // End of BadCommand()

