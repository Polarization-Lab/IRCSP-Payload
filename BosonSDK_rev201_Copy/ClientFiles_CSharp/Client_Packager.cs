//  /////////////////////////////////////////////////////
//  // DO NOT EDIT.  This is a machine generated file. //
//  /////////////////////////////////////////////////////

/******************************************************************************/
/*                                                                            */
/*  Copyright (C) 2016, FLIR Systems                                          */
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


using System;
using Boson;


namespace Boson {
	public partial class Camera{
		internal static class ClientPackager {
			static UInt32 commandCount = 0;
			
			// Begin Module: gao
			public static FLR_RESULT GaoSetGainState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETGAINSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetGainState()
			
			public static FLR_RESULT GaoGetGainState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETGAINSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetGainState()
			
			public static FLR_RESULT GaoSetFfcState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETFFCSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetFfcState()
			
			public static FLR_RESULT GaoGetFfcState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETFFCSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetFfcState()
			
			public static FLR_RESULT GaoSetTempCorrectionState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETTEMPCORRECTIONSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetTempCorrectionState()
			
			public static FLR_RESULT GaoGetTempCorrectionState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETTEMPCORRECTIONSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetTempCorrectionState()
			
			public static FLR_RESULT GaoSetIConstL(Camera parent, Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETICONSTL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetIConstL()
			
			public static FLR_RESULT GaoGetIConstL(Camera parent, out Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Int16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETICONSTL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetIConstL()
			
			public static FLR_RESULT GaoSetIConstM(Camera parent, Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETICONSTM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetIConstM()
			
			public static FLR_RESULT GaoGetIConstM(Camera parent, out Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Int16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETICONSTM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetIConstM()
			
			public static FLR_RESULT GaoSetAveragerState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETAVERAGERSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetAveragerState()
			
			public static FLR_RESULT GaoGetAveragerState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETAVERAGERSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetAveragerState()
			
			public static FLR_RESULT GaoSetNumFFCFrames(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETNUMFFCFRAMES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetNumFFCFrames()
			
			public static FLR_RESULT GaoGetNumFFCFrames(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETNUMFFCFRAMES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetNumFFCFrames()
			
			public static FLR_RESULT GaoGetAveragerThreshold(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETAVERAGERTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetAveragerThreshold()
			
			public static FLR_RESULT GaoGetRnsState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETRNSSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetRnsState()
			
			public static FLR_RESULT GaoSetTestRampState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETTESTRAMPSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetTestRampState()
			
			public static FLR_RESULT GaoGetTestRampState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETTESTRAMPSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetTestRampState()
			
			public static FLR_RESULT GaoSetSffcState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETSFFCSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetSffcState()
			
			public static FLR_RESULT GaoGetSffcState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETSFFCSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetSffcState()
			
			public static FLR_RESULT GaoSetRpmState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETRPMSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetRpmState()
			
			public static FLR_RESULT GaoGetRpmState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETRPMSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetRpmState()
			
			public static FLR_RESULT GaoGetRpmThreshold(Camera parent, out UInt16 threshold) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				threshold = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETRPMTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read threshold from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				threshold = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetRpmThreshold()
			
			public static FLR_RESULT GaoSetFfcZeroMeanState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_SETFFCZEROMEANSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoSetFfcZeroMeanState()
			
			public static FLR_RESULT GaoGetFfcZeroMeanState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.GAO_GETFFCZEROMEANSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgGaoGetFfcZeroMeanState()
			
			// End Module: gao
			
			// Begin Module: lagrange
			// End Module: lagrange
			
			// Begin Module: roic
			public static FLR_RESULT RoicGetFPATemp(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPATEMP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPATemp()
			
			public static FLR_RESULT RoicGetFrameCount(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFRAMECOUNT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFrameCount()
			
			public static FLR_RESULT RoicGetActiveNormalizationTarget(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETACTIVENORMALIZATIONTARGET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetActiveNormalizationTarget()
			
			public static FLR_RESULT RoicSetFPARampState(Camera parent, FLR_ENABLE_E state) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write state to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) state,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_SETFPARAMPSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicSetFPARampState()
			
			public static FLR_RESULT RoicGetFPARampState(Camera parent, out FLR_ENABLE_E state) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				state = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPARAMPSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read state from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				state = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPARampState()
			
			public static FLR_RESULT RoicGetSensorADC1(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETSENSORADC1, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetSensorADC1()
			
			public static FLR_RESULT RoicGetSensorADC2(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETSENSORADC2, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetSensorADC2()
			
			public static FLR_RESULT RoicSetFPATempOffset(Camera parent, Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_SETFPATEMPOFFSET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicSetFPATempOffset()
			
			public static FLR_RESULT RoicGetFPATempOffset(Camera parent, out Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Int16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPATEMPOFFSET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPATempOffset()
			
			public static FLR_RESULT RoicSetFPATempMode(Camera parent, FLR_ROIC_TEMP_MODE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_SETFPATEMPMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicSetFPATempMode()
			
			public static FLR_RESULT RoicGetFPATempMode(Camera parent, out FLR_ROIC_TEMP_MODE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ROIC_TEMP_MODE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPATEMPMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ROIC_TEMP_MODE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPATempMode()
			
			public static FLR_RESULT RoicGetFPATempTable(Camera parent, out FLR_ROIC_FPATEMP_TABLE_T table) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 64;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				table = new FLR_ROIC_FPATEMP_TABLE_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPATEMPTABLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read table from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				table = byteToFLR_ROIC_FPATEMP_TABLE_T(receiveData,inPtr);
				inPtr+=64;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPATempTable()
			
			public static FLR_RESULT RoicSetFPATempValue(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_SETFPATEMPVALUE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicSetFPATempValue()
			
			public static FLR_RESULT RoicGetFPATempValue(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.ROIC_GETFPATEMPVALUE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgRoicGetFPATempValue()
			
			// End Module: roic
			
			// Begin Module: bpr
			public static FLR_RESULT BprSetState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BPR_SETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBprSetState()
			
			public static FLR_RESULT BprGetState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BPR_GETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBprGetState()
			
			// End Module: bpr
			
			// Begin Module: telemetry
			public static FLR_RESULT TelemetrySetState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_SETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetrySetState()
			
			public static FLR_RESULT TelemetryGetState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_GETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetryGetState()
			
			public static FLR_RESULT TelemetrySetLocation(Camera parent, FLR_TELEMETRY_LOC_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_SETLOCATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetrySetLocation()
			
			public static FLR_RESULT TelemetryGetLocation(Camera parent, out FLR_TELEMETRY_LOC_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_TELEMETRY_LOC_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_GETLOCATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_TELEMETRY_LOC_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetryGetLocation()
			
			public static FLR_RESULT TelemetrySetPacking(Camera parent, FLR_TELEMETRY_PACKING_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_SETPACKING, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetrySetPacking()
			
			public static FLR_RESULT TelemetryGetPacking(Camera parent, out FLR_TELEMETRY_PACKING_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_TELEMETRY_PACKING_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TELEMETRY_GETPACKING, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_TELEMETRY_PACKING_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTelemetryGetPacking()
			
			// End Module: telemetry
			
			// Begin Module: boson
			public static FLR_RESULT BosonGetCameraSN(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETCAMERASN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetCameraSN()
			
			public static FLR_RESULT BosonGetCameraPN(Camera parent, out FLR_BOSON_PARTNUMBER_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 20;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_BOSON_PARTNUMBER_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETCAMERAPN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLR_BOSON_PARTNUMBER_T(receiveData,inPtr);
				inPtr+=20;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetCameraPN()
			
			public static FLR_RESULT BosonGetSensorSN(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSENSORSN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSensorSN()
			
			public static FLR_RESULT BosonRunFFC(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_RUNFFC, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonRunFFC()
			
			public static FLR_RESULT BosonSetFFCTempThreshold(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETFFCTEMPTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetFFCTempThreshold()
			
			public static FLR_RESULT BosonGetFFCTempThreshold(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCTEMPTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFFCTempThreshold()
			
			public static FLR_RESULT BosonSetFFCFrameThreshold(Camera parent, UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETFFCFRAMETHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetFFCFrameThreshold()
			
			public static FLR_RESULT BosonGetFFCFrameThreshold(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCFRAMETHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFFCFrameThreshold()
			
			public static FLR_RESULT BosonGetFFCInProgress(Camera parent, out Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Int16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCINPROGRESS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFFCInProgress()
			
			public static FLR_RESULT BosonReboot(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_REBOOT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonReboot()
			
			public static FLR_RESULT BosonSetFFCMode(Camera parent, FLR_BOSON_FFCMODE_E ffcMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ffcMode to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) ffcMode,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETFFCMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetFFCMode()
			
			public static FLR_RESULT BosonGetFFCMode(Camera parent, out FLR_BOSON_FFCMODE_E ffcMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				ffcMode = new FLR_BOSON_FFCMODE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read ffcMode from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ffcMode = (FLR_BOSON_FFCMODE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFFCMode()
			
			public static FLR_RESULT BosonSetGainMode(Camera parent, FLR_BOSON_GAINMODE_E gainMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write gainMode to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) gainMode,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETGAINMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetGainMode()
			
			public static FLR_RESULT BosonGetGainMode(Camera parent, out FLR_BOSON_GAINMODE_E gainMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				gainMode = new FLR_BOSON_GAINMODE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETGAINMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read gainMode from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				gainMode = (FLR_BOSON_GAINMODE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetGainMode()
			
			public static FLR_RESULT BosonWriteDynamicHeaderToFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_WRITEDYNAMICHEADERTOFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonWriteDynamicHeaderToFlash()
			
			public static FLR_RESULT BosonReadDynamicHeaderFromFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_READDYNAMICHEADERFROMFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonReadDynamicHeaderFromFlash()
			
			public static FLR_RESULT BosonRestoreFactoryDefaultsFromFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_RESTOREFACTORYDEFAULTSFROMFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonRestoreFactoryDefaultsFromFlash()
			
			public static FLR_RESULT BosonRestoreFactoryBadPixelsFromFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_RESTOREFACTORYBADPIXELSFROMFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonRestoreFactoryBadPixelsFromFlash()
			
			public static FLR_RESULT BosonWriteBadPixelsToFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_WRITEBADPIXELSTOFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonWriteBadPixelsToFlash()
			
			public static FLR_RESULT BosonGetSoftwareRev(Camera parent, out UInt32 major, out UInt32 minor, out UInt32 patch) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 12;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				major = new UInt32();
				minor = new UInt32();
				patch = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSOFTWAREREV, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read major from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				major = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read minor from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				minor = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read patch from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				patch = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSoftwareRev()
			
			public static FLR_RESULT BosonSetBadPixelLocation(Camera parent, UInt32 row, UInt32 col) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write row to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(row,sendData,outPtr);
				outPtr += 4;
				
				//write col to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(col,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETBADPIXELLOCATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetBadPixelLocation()
			
			public static FLR_RESULT BosonlookupFPATempDegCx10(Camera parent, out Int16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Int16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_LOOKUPFPATEMPDEGCX10, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonlookupFPATempDegCx10()
			
			public static FLR_RESULT BosonlookupFPATempDegKx10(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_LOOKUPFPATEMPDEGKX10, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonlookupFPATempDegKx10()
			
			public static FLR_RESULT BosonWriteLensNvFfcToFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_WRITELENSNVFFCTOFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonWriteLensNvFfcToFlash()
			
			public static FLR_RESULT BosonWriteLensGainToFlash(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_WRITELENSGAINTOFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonWriteLensGainToFlash()
			
			public static FLR_RESULT BosonSetLensNumber(Camera parent, UInt32 lensNumber) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write lensNumber to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(lensNumber,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETLENSNUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetLensNumber()
			
			public static FLR_RESULT BosonGetLensNumber(Camera parent, out UInt32 lensNumber) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				lensNumber = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETLENSNUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read lensNumber from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				lensNumber = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetLensNumber()
			
			public static FLR_RESULT BosonSetTableNumber(Camera parent, UInt32 tableNumber) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write tableNumber to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(tableNumber,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETTABLENUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetTableNumber()
			
			public static FLR_RESULT BosonGetTableNumber(Camera parent, out UInt32 tableNumber) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				tableNumber = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETTABLENUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read tableNumber from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				tableNumber = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetTableNumber()
			
			public static FLR_RESULT BosonGetSensorPN(Camera parent, out FLR_BOSON_SENSOR_PARTNUMBER_T sensorPN) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 32;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				sensorPN = new FLR_BOSON_SENSOR_PARTNUMBER_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSENSORPN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read sensorPN from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				sensorPN = byteToFLR_BOSON_SENSOR_PARTNUMBER_T(receiveData,inPtr);
				inPtr+=32;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSensorPN()
			
			public static FLR_RESULT BosonSetGainSwitchParams(Camera parent, FLR_BOSON_GAIN_SWITCH_PARAMS_T parm_struct) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 16;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write parm_struct to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_BOSON_GAIN_SWITCH_PARAMS_TToByte(parm_struct,sendData,outPtr);
				outPtr += 16;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETGAINSWITCHPARAMS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetGainSwitchParams()
			
			public static FLR_RESULT BosonGetGainSwitchParams(Camera parent, out FLR_BOSON_GAIN_SWITCH_PARAMS_T parm_struct) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 16;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				parm_struct = new FLR_BOSON_GAIN_SWITCH_PARAMS_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETGAINSWITCHPARAMS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read parm_struct from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				parm_struct = byteToFLR_BOSON_GAIN_SWITCH_PARAMS_T(receiveData,inPtr);
				inPtr+=16;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetGainSwitchParams()
			
			public static FLR_RESULT BosonGetSwitchToHighGainFlag(Camera parent, out Byte switchToHighGainFlag) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 1;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				switchToHighGainFlag = new Byte();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSWITCHTOHIGHGAINFLAG, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read switchToHighGainFlag from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				switchToHighGainFlag = byteToUCHAR(receiveData,inPtr);
				inPtr+=1;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSwitchToHighGainFlag()
			
			public static FLR_RESULT BosonGetSwitchToLowGainFlag(Camera parent, out Byte switchToLowGainFlag) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 1;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				switchToLowGainFlag = new Byte();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSWITCHTOLOWGAINFLAG, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read switchToLowGainFlag from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				switchToLowGainFlag = byteToUCHAR(receiveData,inPtr);
				inPtr+=1;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSwitchToLowGainFlag()
			
			public static FLR_RESULT BosonGetCLowToHighPercent(Camera parent, out UInt32 cLowToHighPercent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				cLowToHighPercent = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETCLOWTOHIGHPERCENT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read cLowToHighPercent from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				cLowToHighPercent = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetCLowToHighPercent()
			
			public static FLR_RESULT BosonGetMaxNUCTables(Camera parent, out UInt32 maxNUCTables) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				maxNUCTables = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETMAXNUCTABLES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read maxNUCTables from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				maxNUCTables = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetMaxNUCTables()
			
			public static FLR_RESULT BosonGetMaxLensTables(Camera parent, out UInt32 maxLensTables) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				maxLensTables = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETMAXLENSTABLES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read maxLensTables from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				maxLensTables = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetMaxLensTables()
			
			public static FLR_RESULT BosonGetFfcWaitCloseFrames(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCWAITCLOSEFRAMES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFfcWaitCloseFrames()
			
			public static FLR_RESULT BosonSetFfcWaitCloseFrames(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETFFCWAITCLOSEFRAMES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetFfcWaitCloseFrames()
			
			public static FLR_RESULT BosonCheckForTableSwitch(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_CHECKFORTABLESWITCH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonCheckForTableSwitch()
			
			public static FLR_RESULT BosonGetDesiredTableNumber(Camera parent, out UInt32 desiredTableNumber) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				desiredTableNumber = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETDESIREDTABLENUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read desiredTableNumber from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				desiredTableNumber = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetDesiredTableNumber()
			
			public static FLR_RESULT BosonGetFfcStatus(Camera parent, out FLR_BOSON_FFCSTATUS_E ffcStatus) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				ffcStatus = new FLR_BOSON_FFCSTATUS_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCSTATUS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read ffcStatus from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ffcStatus = (FLR_BOSON_FFCSTATUS_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFfcStatus()
			
			public static FLR_RESULT BosonGetFfcDesired(Camera parent, out UInt32 ffcDesired) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				ffcDesired = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCDESIRED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read ffcDesired from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ffcDesired = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFfcDesired()
			
			public static FLR_RESULT BosonGetSwRevInHeader(Camera parent, out UInt32 major, out UInt32 minor, out UInt32 patch) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 12;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				major = new UInt32();
				minor = new UInt32();
				patch = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETSWREVINHEADER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read major from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				major = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read minor from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				minor = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read patch from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				patch = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetSwRevInHeader()
			
			public static FLR_RESULT BosonGetLastFFCFrameCount(Camera parent, out UInt32 frameCount) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				frameCount = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETLASTFFCFRAMECOUNT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read frameCount from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				frameCount = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetLastFFCFrameCount()
			
			public static FLR_RESULT BosonGetLastFFCTempDegKx10(Camera parent, out UInt16 temp) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				temp = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETLASTFFCTEMPDEGKX10, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read temp from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				temp = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetLastFFCTempDegKx10()
			
			public static FLR_RESULT BosonGetTableSwitchDesired(Camera parent, out UInt16 tableSwitchDesired) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				tableSwitchDesired = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETTABLESWITCHDESIRED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read tableSwitchDesired from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				tableSwitchDesired = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetTableSwitchDesired()
			
			public static FLR_RESULT BosonGetOverTempThreshold(Camera parent, out Double temperatureInC) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				temperatureInC = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETOVERTEMPTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read temperatureInC from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				temperatureInC = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetOverTempThreshold()
			
			public static FLR_RESULT BosonGetLowPowerMode(Camera parent, out UInt16 lowPowerMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				lowPowerMode = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETLOWPOWERMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read lowPowerMode from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				lowPowerMode = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetLowPowerMode()
			
			public static FLR_RESULT BosonGetOverTempEventOccurred(Camera parent, out UInt16 overTempEventOccurred) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				overTempEventOccurred = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETOVERTEMPEVENTOCCURRED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read overTempEventOccurred from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				overTempEventOccurred = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetOverTempEventOccurred()
			
			public static FLR_RESULT BosonSetPermitThermalShutdownOverride(Camera parent, FLR_ENABLE_E permitThermalShutdownOverride) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write permitThermalShutdownOverride to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) permitThermalShutdownOverride,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETPERMITTHERMALSHUTDOWNOVERRIDE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetPermitThermalShutdownOverride()
			
			public static FLR_RESULT BosonGetPermitThermalShutdownOverride(Camera parent, out FLR_ENABLE_E permitThermalShutdownOverride) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				permitThermalShutdownOverride = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETPERMITTHERMALSHUTDOWNOVERRIDE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read permitThermalShutdownOverride from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				permitThermalShutdownOverride = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetPermitThermalShutdownOverride()
			
			public static FLR_RESULT BosonGetMyriadTemp(Camera parent, out Double myriadTemp) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				myriadTemp = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETMYRIADTEMP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read myriadTemp from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				myriadTemp = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetMyriadTemp()
			
			public static FLR_RESULT BosonGetNvFFCNucTableNumberLens0(Camera parent, out Int32 nvFFCNucTableNumberLens0) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				nvFFCNucTableNumberLens0 = new Int32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETNVFFCNUCTABLENUMBERLENS0, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read nvFFCNucTableNumberLens0 from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				nvFFCNucTableNumberLens0 = byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetNvFFCNucTableNumberLens0()
			
			public static FLR_RESULT BosonGetNvFFCNucTableNumberLens1(Camera parent, out Int32 nvFFCNucTableNumberLens1) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				nvFFCNucTableNumberLens1 = new Int32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETNVFFCNUCTABLENUMBERLENS1, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read nvFFCNucTableNumberLens1 from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				nvFFCNucTableNumberLens1 = byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetNvFFCNucTableNumberLens1()
			
			public static FLR_RESULT BosonGetNvFFCFPATempDegKx10Lens0(Camera parent, out UInt16 nvFFCFPATempDegKx10Lens0) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				nvFFCFPATempDegKx10Lens0 = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETNVFFCFPATEMPDEGKX10LENS0, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read nvFFCFPATempDegKx10Lens0 from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				nvFFCFPATempDegKx10Lens0 = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetNvFFCFPATempDegKx10Lens0()
			
			public static FLR_RESULT BosonGetNvFFCFPATempDegKx10Lens1(Camera parent, out UInt16 nvFFCFPATempDegKx10Lens1) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				nvFFCFPATempDegKx10Lens1 = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETNVFFCFPATEMPDEGKX10LENS1, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read nvFFCFPATempDegKx10Lens1 from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				nvFFCFPATempDegKx10Lens1 = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetNvFFCFPATempDegKx10Lens1()
			
			public static FLR_RESULT BosonSetFFCWarnTimeInSecx10(Camera parent, UInt16 ffcWarnTime) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ffcWarnTime to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(ffcWarnTime,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETFFCWARNTIMEINSECX10, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetFFCWarnTimeInSecx10()
			
			public static FLR_RESULT BosonGetFFCWarnTimeInSecx10(Camera parent, out UInt16 ffcWarnTime) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				ffcWarnTime = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETFFCWARNTIMEINSECX10, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read ffcWarnTime from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ffcWarnTime = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetFFCWarnTimeInSecx10()
			
			public static FLR_RESULT BosonGetOverTempEventCounter(Camera parent, out UInt32 overTempEventCounter) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				overTempEventCounter = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETOVERTEMPEVENTCOUNTER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read overTempEventCounter from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				overTempEventCounter = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetOverTempEventCounter()
			
			public static FLR_RESULT BosonSetOverTempTimerInSec(Camera parent, UInt16 overTempTimerInSec) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write overTempTimerInSec to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(overTempTimerInSec,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETOVERTEMPTIMERINSEC, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetOverTempTimerInSec()
			
			public static FLR_RESULT BosonGetOverTempTimerInSec(Camera parent, out UInt16 overTempTimerInSec) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				overTempTimerInSec = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETOVERTEMPTIMERINSEC, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read overTempTimerInSec from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				overTempTimerInSec = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetOverTempTimerInSec()
			
			public static FLR_RESULT BosonUnloadCurrentLensCorrections(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_UNLOADCURRENTLENSCORRECTIONS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonUnloadCurrentLensCorrections()
			
			public static FLR_RESULT BosonSetTimeForQuickFFCsInSecs(Camera parent, UInt32 timeForQuickFFCsInSecs) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write timeForQuickFFCsInSecs to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(timeForQuickFFCsInSecs,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETTIMEFORQUICKFFCSINSECS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetTimeForQuickFFCsInSecs()
			
			public static FLR_RESULT BosonGetTimeForQuickFFCsInSecs(Camera parent, out UInt32 timeForQuickFFCsInSecs) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				timeForQuickFFCsInSecs = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETTIMEFORQUICKFFCSINSECS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read timeForQuickFFCsInSecs from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				timeForQuickFFCsInSecs = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetTimeForQuickFFCsInSecs()
			
			public static FLR_RESULT BosonReloadCurrentLensCorrections(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_RELOADCURRENTLENSCORRECTIONS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonReloadCurrentLensCorrections()
			
			public static FLR_RESULT BosonGetBootTimestamps(Camera parent, out Double FirstLight, out Double StartInit, out Double BosonExecDone, out Double Timestamp4) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 16;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				FirstLight = new Double();
				StartInit = new Double();
				BosonExecDone = new Double();
				Timestamp4 = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETBOOTTIMESTAMPS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read FirstLight from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FirstLight = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				// read StartInit from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				StartInit = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				// read BosonExecDone from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				BosonExecDone = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				// read Timestamp4 from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				Timestamp4 = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetBootTimestamps()
			
			public static FLR_RESULT BosonSetExtSyncMode(Camera parent, FLR_BOSON_EXT_SYNC_MODE_E mode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write mode to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) mode,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_SETEXTSYNCMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonSetExtSyncMode()
			
			public static FLR_RESULT BosonGetExtSyncMode(Camera parent, out FLR_BOSON_EXT_SYNC_MODE_E mode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				mode = new FLR_BOSON_EXT_SYNC_MODE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.BOSON_GETEXTSYNCMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read mode from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				mode = (FLR_BOSON_EXT_SYNC_MODE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgBosonGetExtSyncMode()
			
			// End Module: boson
			
			// Begin Module: dvo
			public static FLR_RESULT DvoSetAnalogVideoState(Camera parent, FLR_ENABLE_E analogVideoState) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write analogVideoState to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) analogVideoState,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETANALOGVIDEOSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetAnalogVideoState()
			
			public static FLR_RESULT DvoGetAnalogVideoState(Camera parent, out FLR_ENABLE_E analogVideoState) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				analogVideoState = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETANALOGVIDEOSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read analogVideoState from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				analogVideoState = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetAnalogVideoState()
			
			public static FLR_RESULT DvoSetOutputFormat(Camera parent, FLR_DVO_OUTPUT_FORMAT_E format) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write format to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) format,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETOUTPUTFORMAT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetOutputFormat()
			
			public static FLR_RESULT DvoGetOutputFormat(Camera parent, out FLR_DVO_OUTPUT_FORMAT_E format) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				format = new FLR_DVO_OUTPUT_FORMAT_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETOUTPUTFORMAT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read format from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				format = (FLR_DVO_OUTPUT_FORMAT_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetOutputFormat()
			
			public static FLR_RESULT DvoSetOutputYCbCrSettings(Camera parent, FLR_DVO_YCBCR_SETTINGS_T settings) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 12;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write settings to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_DVO_YCBCR_SETTINGS_TToByte(settings,sendData,outPtr);
				outPtr += 12;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETOUTPUTYCBCRSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetOutputYCbCrSettings()
			
			public static FLR_RESULT DvoGetOutputYCbCrSettings(Camera parent, out FLR_DVO_YCBCR_SETTINGS_T settings) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 12;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				settings = new FLR_DVO_YCBCR_SETTINGS_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETOUTPUTYCBCRSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read settings from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				settings = byteToFLR_DVO_YCBCR_SETTINGS_T(receiveData,inPtr);
				inPtr+=12;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetOutputYCbCrSettings()
			
			public static FLR_RESULT DvoSetOutputRGBSettings(Camera parent, FLR_DVO_RGB_SETTINGS_T settings) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write settings to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_DVO_RGB_SETTINGS_TToByte(settings,sendData,outPtr);
				outPtr += 8;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETOUTPUTRGBSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetOutputRGBSettings()
			
			public static FLR_RESULT DvoGetOutputRGBSettings(Camera parent, out FLR_DVO_RGB_SETTINGS_T settings) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				settings = new FLR_DVO_RGB_SETTINGS_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETOUTPUTRGBSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read settings from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				settings = byteToFLR_DVO_RGB_SETTINGS_T(receiveData,inPtr);
				inPtr+=8;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetOutputRGBSettings()
			
			public static FLR_RESULT DvoApplyCustomSettings(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_APPLYCUSTOMSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoApplyCustomSettings()
			
			public static FLR_RESULT DvoSetDisplayMode(Camera parent, FLR_DVO_DISPLAY_MODE_E displayMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write displayMode to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) displayMode,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETDISPLAYMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetDisplayMode()
			
			public static FLR_RESULT DvoGetDisplayMode(Camera parent, out FLR_DVO_DISPLAY_MODE_E displayMode) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				displayMode = new FLR_DVO_DISPLAY_MODE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETDISPLAYMODE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read displayMode from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				displayMode = (FLR_DVO_DISPLAY_MODE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetDisplayMode()
			
			public static FLR_RESULT DvoSetType(Camera parent, FLR_DVO_TYPE_E tap) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write tap to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) tap,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETTYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetType()
			
			public static FLR_RESULT DvoGetType(Camera parent, out FLR_DVO_TYPE_E tap) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				tap = new FLR_DVO_TYPE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETTYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read tap from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				tap = (FLR_DVO_TYPE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetType()
			
			public static FLR_RESULT DvoSetVideoStandard(Camera parent, FLR_DVO_VIDEO_STANDARD_E videoStandard) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write videoStandard to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) videoStandard,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETVIDEOSTANDARD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetVideoStandard()
			
			public static FLR_RESULT DvoGetVideoStandard(Camera parent, out FLR_DVO_VIDEO_STANDARD_E videoStandard) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				videoStandard = new FLR_DVO_VIDEO_STANDARD_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETVIDEOSTANDARD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read videoStandard from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				videoStandard = (FLR_DVO_VIDEO_STANDARD_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetVideoStandard()
			
			public static FLR_RESULT DvoSetCheckVideoDacPresent(Camera parent, FLR_ENABLE_E checkVideoDacPresent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write checkVideoDacPresent to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) checkVideoDacPresent,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_SETCHECKVIDEODACPRESENT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoSetCheckVideoDacPresent()
			
			public static FLR_RESULT DvoGetCheckVideoDacPresent(Camera parent, out FLR_ENABLE_E checkVideoDacPresent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				checkVideoDacPresent = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DVO_GETCHECKVIDEODACPRESENT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read checkVideoDacPresent from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				checkVideoDacPresent = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDvoGetCheckVideoDacPresent()
			
			// End Module: dvo
			
			// Begin Module: capture
			public static FLR_RESULT CaptureSingleFrame(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.CAPTURE_SINGLEFRAME, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgCaptureSingleFrame()
			
			public static FLR_RESULT CaptureFrames(Camera parent, FLR_CAPTURE_SETTINGS_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 10;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_CAPTURE_SETTINGS_TToByte(data,sendData,outPtr);
				outPtr += 10;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.CAPTURE_FRAMES, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgCaptureFrames()
			
			public static FLR_RESULT CaptureSingleFrameWithSrc(Camera parent, FLR_CAPTURE_SRC_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.CAPTURE_SINGLEFRAMEWITHSRC, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgCaptureSingleFrameWithSrc()
			
			public static FLR_RESULT CaptureSingleFrameToFile(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.CAPTURE_SINGLEFRAMETOFILE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgCaptureSingleFrameToFile()
			
			// End Module: capture
			
			// Begin Module: scnr
			public static FLR_RESULT ScnrSetEnableState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetEnableState()
			
			public static FLR_RESULT ScnrGetEnableState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetEnableState()
			
			public static FLR_RESULT ScnrSetThColSum(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETTHCOLSUM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetThColSum()
			
			public static FLR_RESULT ScnrGetThColSum(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETTHCOLSUM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetThColSum()
			
			public static FLR_RESULT ScnrSetThPixel(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETTHPIXEL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetThPixel()
			
			public static FLR_RESULT ScnrGetThPixel(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETTHPIXEL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetThPixel()
			
			public static FLR_RESULT ScnrSetMaxCorr(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETMAXCORR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetMaxCorr()
			
			public static FLR_RESULT ScnrGetMaxCorr(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETMAXCORR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetMaxCorr()
			
			public static FLR_RESULT ScnrGetThPixelApplied(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETTHPIXELAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetThPixelApplied()
			
			public static FLR_RESULT ScnrGetMaxCorrApplied(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETMAXCORRAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetMaxCorrApplied()
			
			public static FLR_RESULT ScnrSetThColSumSafe(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETTHCOLSUMSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetThColSumSafe()
			
			public static FLR_RESULT ScnrGetThColSumSafe(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETTHCOLSUMSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetThColSumSafe()
			
			public static FLR_RESULT ScnrSetThPixelSafe(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETTHPIXELSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetThPixelSafe()
			
			public static FLR_RESULT ScnrGetThPixelSafe(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETTHPIXELSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetThPixelSafe()
			
			public static FLR_RESULT ScnrSetMaxCorrSafe(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_SETMAXCORRSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrSetMaxCorrSafe()
			
			public static FLR_RESULT ScnrGetMaxCorrSafe(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCNR_GETMAXCORRSAFE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScnrGetMaxCorrSafe()
			
			// End Module: scnr
			
			// Begin Module: agc
			public static FLR_RESULT AgcSetPercentPerBin(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETPERCENTPERBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetPercentPerBin()
			
			public static FLR_RESULT AgcGetPercentPerBin(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETPERCENTPERBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetPercentPerBin()
			
			public static FLR_RESULT AgcSetLinearPercent(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETLINEARPERCENT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetLinearPercent()
			
			public static FLR_RESULT AgcGetLinearPercent(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETLINEARPERCENT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetLinearPercent()
			
			public static FLR_RESULT AgcSetOutlierCut(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETOUTLIERCUT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetOutlierCut()
			
			public static FLR_RESULT AgcGetOutlierCut(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETOUTLIERCUT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetOutlierCut()
			
			public static FLR_RESULT AgcGetDrOut(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETDROUT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetDrOut()
			
			public static FLR_RESULT AgcSetMaxGain(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETMAXGAIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetMaxGain()
			
			public static FLR_RESULT AgcGetMaxGain(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETMAXGAIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetMaxGain()
			
			public static FLR_RESULT AgcSetdf(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETDF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetdf()
			
			public static FLR_RESULT AgcGetdf(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETDF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetdf()
			
			public static FLR_RESULT AgcSetGamma(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETGAMMA, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetGamma()
			
			public static FLR_RESULT AgcGetGamma(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETGAMMA, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetGamma()
			
			public static FLR_RESULT AgcGetFirstBin(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETFIRSTBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetFirstBin()
			
			public static FLR_RESULT AgcGetLastBin(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETLASTBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetLastBin()
			
			public static FLR_RESULT AgcSetDetailHeadroom(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETDETAILHEADROOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetDetailHeadroom()
			
			public static FLR_RESULT AgcGetDetailHeadroom(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETDETAILHEADROOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetDetailHeadroom()
			
			public static FLR_RESULT AgcSetd2br(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETD2BR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetd2br()
			
			public static FLR_RESULT AgcGetd2br(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETD2BR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetd2br()
			
			public static FLR_RESULT AgcSetSigmaR(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETSIGMAR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetSigmaR()
			
			public static FLR_RESULT AgcGetSigmaR(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETSIGMAR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetSigmaR()
			
			public static FLR_RESULT AgcSetUseEntropy(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETUSEENTROPY, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetUseEntropy()
			
			public static FLR_RESULT AgcGetUseEntropy(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETUSEENTROPY, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetUseEntropy()
			
			public static FLR_RESULT AgcSetROI(Camera parent, FLR_ROI_T roi) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write roi to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_ROI_TToByte(roi,sendData,outPtr);
				outPtr += 8;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetROI()
			
			public static FLR_RESULT AgcGetROI(Camera parent, out FLR_ROI_T roi) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				roi = new FLR_ROI_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read roi from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				roi = byteToFLR_ROI_T(receiveData,inPtr);
				inPtr+=8;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetROI()
			
			public static FLR_RESULT AgcGetMaxGainApplied(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETMAXGAINAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetMaxGainApplied()
			
			public static FLR_RESULT AgcGetSigmaRApplied(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETSIGMARAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetSigmaRApplied()
			
			public static FLR_RESULT AgcSetOutlierCutBalance(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_SETOUTLIERCUTBALANCE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcSetOutlierCutBalance()
			
			public static FLR_RESULT AgcGetOutlierCutBalance(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETOUTLIERCUTBALANCE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetOutlierCutBalance()
			
			public static FLR_RESULT AgcGetOutlierCutApplied(Camera parent, out Double percentHigh, out Double percentLow) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				percentHigh = new Double();
				percentLow = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.AGC_GETOUTLIERCUTAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read percentHigh from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				percentHigh = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				// read percentLow from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				percentLow = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgAgcGetOutlierCutApplied()
			
			// End Module: agc
			
			// Begin Module: tf
			public static FLR_RESULT TfSetEnableState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_SETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfSetEnableState()
			
			public static FLR_RESULT TfGetEnableState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetEnableState()
			
			public static FLR_RESULT TfSetDelta_nf(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_SETDELTA_NF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfSetDelta_nf()
			
			public static FLR_RESULT TfGetDelta_nf(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETDELTA_NF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetDelta_nf()
			
			public static FLR_RESULT TfSetTHDeltaMotion(Camera parent, UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(data,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_SETTHDELTAMOTION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfSetTHDeltaMotion()
			
			public static FLR_RESULT TfGetTHDeltaMotion(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETTHDELTAMOTION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetTHDeltaMotion()
			
			public static FLR_RESULT TfSetWLut(Camera parent, FLR_TF_WLUT_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 32;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_TF_WLUT_TToByte(data,sendData,outPtr);
				outPtr += 32;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_SETWLUT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfSetWLut()
			
			public static FLR_RESULT TfGetWLut(Camera parent, out FLR_TF_WLUT_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 32;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_TF_WLUT_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETWLUT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLR_TF_WLUT_T(receiveData,inPtr);
				inPtr+=32;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetWLut()
			
			public static FLR_RESULT TfGetMotionCount(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETMOTIONCOUNT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetMotionCount()
			
			public static FLR_RESULT TfSetMotionThreshold(Camera parent, UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_SETMOTIONTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfSetMotionThreshold()
			
			public static FLR_RESULT TfGetMotionThreshold(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETMOTIONTHRESHOLD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetMotionThreshold()
			
			public static FLR_RESULT TfGetDelta_nfApplied(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETDELTA_NFAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetDelta_nfApplied()
			
			public static FLR_RESULT TfGetTHDeltaMotionApplied(Camera parent, out UInt16 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TF_GETTHDELTAMOTIONAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTfGetTHDeltaMotionApplied()
			
			// End Module: tf
			
			// Begin Module: mem
			public static FLR_RESULT MemReadCapture(Camera parent, Byte bufferNum, UInt32 offset, UInt16 sizeInBytes, out Byte[] data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 7;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 256;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Byte[sizeInBytes];
				
				//write bufferNum to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(bufferNum,sendData,outPtr);
				outPtr += 1;
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write sizeInBytes to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(sizeInBytes,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_READCAPTURE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUCHARArray(receiveData,inPtr,sizeInBytes);
				inPtr+=sizeInBytes;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemReadCapture()
			
			public static FLR_RESULT MemGetCaptureSize(Camera parent, out UInt32 bytes, out UInt16 rows, out UInt16 columns) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				bytes = new UInt32();
				rows = new UInt16();
				columns = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_GETCAPTURESIZE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read bytes from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				bytes = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read rows from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				rows = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				// read columns from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				columns = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemGetCaptureSize()
			
			public static FLR_RESULT MemWriteFlash(Camera parent, FLR_MEM_LOCATION_E location, Byte index, UInt32 offset, UInt16 sizeInBytes, Byte[] data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = (UInt32) sizeInBytes + 11;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write location to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) location,sendData,outPtr);
				outPtr += 4;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write sizeInBytes to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(sizeInBytes,sendData,outPtr);
				outPtr += 2;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(data,sizeInBytes,sendData,outPtr);
				outPtr += sizeInBytes;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_WRITEFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemWriteFlash()
			
			public static FLR_RESULT MemReadFlash(Camera parent, FLR_MEM_LOCATION_E location, Byte index, UInt32 offset, UInt16 sizeInBytes, out Byte[] data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 11;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 256;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Byte[sizeInBytes];
				
				//write location to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) location,sendData,outPtr);
				outPtr += 4;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write sizeInBytes to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(sizeInBytes,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_READFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUCHARArray(receiveData,inPtr,sizeInBytes);
				inPtr+=sizeInBytes;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemReadFlash()
			
			public static FLR_RESULT MemGetFlashSize(Camera parent, FLR_MEM_LOCATION_E location, out UInt32 bytes) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				bytes = new UInt32();
				
				//write location to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) location,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_GETFLASHSIZE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read bytes from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				bytes = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemGetFlashSize()
			
			public static FLR_RESULT MemEraseFlash(Camera parent, FLR_MEM_LOCATION_E location, Byte index) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 5;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write location to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) location,sendData,outPtr);
				outPtr += 4;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_ERASEFLASH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemEraseFlash()
			
			public static FLR_RESULT MemEraseFlashPartial(Camera parent, FLR_MEM_LOCATION_E location, Byte index, UInt32 offset, UInt32 length) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 13;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write location to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) location,sendData,outPtr);
				outPtr += 4;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write length to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(length,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_ERASEFLASHPARTIAL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemEraseFlashPartial()
			
			public static FLR_RESULT MemReadCurrentGain(Camera parent, UInt32 offset, UInt16 sizeInBytes, out Byte[] data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 6;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 256;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Byte[sizeInBytes];
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write sizeInBytes to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_16ToByte(sizeInBytes,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_READCURRENTGAIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUCHARArray(receiveData,inPtr,sizeInBytes);
				inPtr+=sizeInBytes;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemReadCurrentGain()
			
			public static FLR_RESULT MemGetGainSize(Camera parent, out UInt32 bytes, out UInt16 rows, out UInt16 columns) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				bytes = new UInt32();
				rows = new UInt16();
				columns = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.MEM_GETGAINSIZE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read bytes from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				bytes = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				// read rows from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				rows = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				// read columns from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				columns = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgMemGetGainSize()
			
			// End Module: mem
			
			// Begin Module: colorLut
			public static FLR_RESULT ColorlutSetControl(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.COLORLUT_SETCONTROL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgColorlutSetControl()
			
			public static FLR_RESULT ColorlutGetControl(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.COLORLUT_GETCONTROL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgColorlutGetControl()
			
			public static FLR_RESULT ColorlutSetId(Camera parent, FLR_COLORLUT_ID_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.COLORLUT_SETID, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgColorlutSetId()
			
			public static FLR_RESULT ColorlutGetId(Camera parent, out FLR_COLORLUT_ID_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_COLORLUT_ID_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.COLORLUT_GETID, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_COLORLUT_ID_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgColorlutGetId()
			
			// End Module: colorLut
			
			// Begin Module: spnr
			public static FLR_RESULT SpnrSetEnableState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetEnableState()
			
			public static FLR_RESULT SpnrGetEnableState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETENABLESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetEnableState()
			
			public static FLR_RESULT SpnrGetState(Camera parent, out FLR_SPNR_STATE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_SPNR_STATE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_SPNR_STATE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetState()
			
			public static FLR_RESULT SpnrSetFrameDelay(Camera parent, UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETFRAMEDELAY, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetFrameDelay()
			
			public static FLR_RESULT SpnrGetFrameDelay(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETFRAMEDELAY, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetFrameDelay()
			
			public static FLR_RESULT SpnrGetSFApplied(Camera parent, out Double sf) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				sf = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETSFAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read sf from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				sf = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetSFApplied()
			
			public static FLR_RESULT SpnrSetPSDKernel(Camera parent, FLR_SPNR_PSD_KERNEL_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 256;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_SPNR_PSD_KERNEL_TToByte(data,sendData,outPtr);
				outPtr += 256;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETPSDKERNEL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetPSDKernel()
			
			public static FLR_RESULT SpnrGetPSDKernel(Camera parent, out FLR_SPNR_PSD_KERNEL_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 256;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_SPNR_PSD_KERNEL_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETPSDKERNEL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLR_SPNR_PSD_KERNEL_T(receiveData,inPtr);
				inPtr+=256;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetPSDKernel()
			
			public static FLR_RESULT SpnrSetSFMin(Camera parent, Double sfmin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write sfmin to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(sfmin,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETSFMIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetSFMin()
			
			public static FLR_RESULT SpnrGetSFMin(Camera parent, out Double sfmin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				sfmin = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETSFMIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read sfmin from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				sfmin = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetSFMin()
			
			public static FLR_RESULT SpnrSetSFMax(Camera parent, Double sfmax) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write sfmax to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(sfmax,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETSFMAX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetSFMax()
			
			public static FLR_RESULT SpnrGetSFMax(Camera parent, out Double sfmax) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				sfmax = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETSFMAX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read sfmax from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				sfmax = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetSFMax()
			
			public static FLR_RESULT SpnrSetDFMin(Camera parent, Double dfmin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write dfmin to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(dfmin,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETDFMIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetDFMin()
			
			public static FLR_RESULT SpnrGetDFMin(Camera parent, out Double dfmin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				dfmin = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETDFMIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read dfmin from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				dfmin = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetDFMin()
			
			public static FLR_RESULT SpnrSetDFMax(Camera parent, Double dfmax) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write dfmax to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(dfmax,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETDFMAX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetDFMax()
			
			public static FLR_RESULT SpnrGetDFMax(Camera parent, out Double dfmax) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				dfmax = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETDFMAX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read dfmax from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				dfmax = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetDFMax()
			
			public static FLR_RESULT SpnrSetNormTarget(Camera parent, Double normTarget) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write normTarget to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(normTarget,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_SETNORMTARGET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrSetNormTarget()
			
			public static FLR_RESULT SpnrGetNormTarget(Camera parent, out Double normTarget) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				normTarget = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETNORMTARGET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read normTarget from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				normTarget = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetNormTarget()
			
			public static FLR_RESULT SpnrGetNormTargetApplied(Camera parent, out Double normTargetApplied) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				normTargetApplied = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPNR_GETNORMTARGETAPPLIED, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read normTargetApplied from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				normTargetApplied = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSpnrGetNormTargetApplied()
			
			// End Module: spnr
			
			// Begin Module: scaler
			public static FLR_RESULT ScalerGetMaxZoom(Camera parent, out UInt32 zoom) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				zoom = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCALER_GETMAXZOOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read zoom from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				zoom = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScalerGetMaxZoom()
			
			public static FLR_RESULT ScalerSetZoom(Camera parent, FLR_SCALER_ZOOM_PARAMS_T zoomParams) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 12;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write zoomParams to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_SCALER_ZOOM_PARAMS_TToByte(zoomParams,sendData,outPtr);
				outPtr += 12;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCALER_SETZOOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScalerSetZoom()
			
			public static FLR_RESULT ScalerGetZoom(Camera parent, out FLR_SCALER_ZOOM_PARAMS_T zoomParams) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 12;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				zoomParams = new FLR_SCALER_ZOOM_PARAMS_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCALER_GETZOOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read zoomParams from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				zoomParams = byteToFLR_SCALER_ZOOM_PARAMS_T(receiveData,inPtr);
				inPtr+=12;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScalerGetZoom()
			
			public static FLR_RESULT ScalerSetFractionalZoom(Camera parent, UInt32 zoomNumerator, UInt32 zoomDenominator, UInt32 zoomXCenter, UInt32 zoomYCenter, FLR_ENABLE_E inChangeEnable, UInt32 zoomOutXCenter, UInt32 zoomOutYCenter, FLR_ENABLE_E outChangeEnable) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 32;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write zoomNumerator to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomNumerator,sendData,outPtr);
				outPtr += 4;
				
				//write zoomDenominator to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomDenominator,sendData,outPtr);
				outPtr += 4;
				
				//write zoomXCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomXCenter,sendData,outPtr);
				outPtr += 4;
				
				//write zoomYCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomYCenter,sendData,outPtr);
				outPtr += 4;
				
				//write inChangeEnable to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) inChangeEnable,sendData,outPtr);
				outPtr += 4;
				
				//write zoomOutXCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomOutXCenter,sendData,outPtr);
				outPtr += 4;
				
				//write zoomOutYCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomOutYCenter,sendData,outPtr);
				outPtr += 4;
				
				//write outChangeEnable to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) outChangeEnable,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCALER_SETFRACTIONALZOOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScalerSetFractionalZoom()
			
			public static FLR_RESULT ScalerSetIndexZoom(Camera parent, UInt32 zoomIndex, UInt32 zoomXCenter, UInt32 zoomYCenter, FLR_ENABLE_E inChangeEnable, UInt32 zoomOutXCenter, UInt32 zoomOutYCenter, FLR_ENABLE_E outChangeEnable) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 28;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write zoomIndex to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomIndex,sendData,outPtr);
				outPtr += 4;
				
				//write zoomXCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomXCenter,sendData,outPtr);
				outPtr += 4;
				
				//write zoomYCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomYCenter,sendData,outPtr);
				outPtr += 4;
				
				//write inChangeEnable to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) inChangeEnable,sendData,outPtr);
				outPtr += 4;
				
				//write zoomOutXCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomOutXCenter,sendData,outPtr);
				outPtr += 4;
				
				//write zoomOutYCenter to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(zoomOutYCenter,sendData,outPtr);
				outPtr += 4;
				
				//write outChangeEnable to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) outChangeEnable,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SCALER_SETINDEXZOOM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgScalerSetIndexZoom()
			
			// End Module: scaler
			
			// Begin Module: sysctrl
			public static FLR_RESULT SysctrlSetFreezeState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSCTRL_SETFREEZESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSysctrlSetFreezeState()
			
			public static FLR_RESULT SysctrlGetFreezeState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSCTRL_GETFREEZESTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSysctrlGetFreezeState()
			
			public static FLR_RESULT SysctrlGetCameraFrameRate(Camera parent, out UInt32 frameRate) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				frameRate = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSCTRL_GETCAMERAFRAMERATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read frameRate from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				frameRate = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSysctrlGetCameraFrameRate()
			
			// End Module: sysctrl
			
			// Begin Module: testRamp
			public static FLR_RESULT TestrampSetType(Camera parent, Byte index, FLR_TESTRAMP_TYPE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 5;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_SETTYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampSetType()
			
			public static FLR_RESULT TestrampGetType(Camera parent, Byte index, out FLR_TESTRAMP_TYPE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_TESTRAMP_TYPE_E();
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_GETTYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_TESTRAMP_TYPE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampGetType()
			
			public static FLR_RESULT TestrampSetSettings(Camera parent, Byte index, FLR_TESTRAMP_SETTINGS_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 7;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_TESTRAMP_SETTINGS_TToByte(data,sendData,outPtr);
				outPtr += 6;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_SETSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampSetSettings()
			
			public static FLR_RESULT TestrampGetSettings(Camera parent, Byte index, out FLR_TESTRAMP_SETTINGS_T data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 6;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_TESTRAMP_SETTINGS_T();
				
				//write index to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(index,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_GETSETTINGS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLR_TESTRAMP_SETTINGS_T(receiveData,inPtr);
				inPtr+=6;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampGetSettings()
			
			public static FLR_RESULT TestrampSetMotionState(Camera parent, FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_SETMOTIONSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampSetMotionState()
			
			public static FLR_RESULT TestrampGetMotionState(Camera parent, out FLR_ENABLE_E data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_GETMOTIONSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampGetMotionState()
			
			public static FLR_RESULT TestrampSetIndex(Camera parent, Byte data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(data,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_SETINDEX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampSetIndex()
			
			public static FLR_RESULT TestrampGetIndex(Camera parent, out Byte data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 1;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Byte();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_GETINDEX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUCHAR(receiveData,inPtr);
				inPtr+=1;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampGetIndex()
			
			public static FLR_RESULT TestrampGetMaxIndex(Camera parent, out Byte data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 1;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Byte();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.TESTRAMP_GETMAXINDEX, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUCHAR(receiveData,inPtr);
				inPtr+=1;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgTestrampGetMaxIndex()
			
			// End Module: testRamp
			
			// Begin Module: symbology
			public static FLR_RESULT SymbologySetEnable(Camera parent, FLR_ENABLE_E draw_symbols) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write draw_symbols to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) draw_symbols,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_SETENABLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologySetEnable()
			
			public static FLR_RESULT SymbologyCreateBitmap(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 9;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEBITMAP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateBitmap()
			
			public static FLR_RESULT SymbologySendData(Camera parent, Byte ID, Int16 size, Byte[] text) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 131;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write size to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(size,sendData,outPtr);
				outPtr += 2;
				
				//write text to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(text,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_SENDDATA, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologySendData()
			
			public static FLR_RESULT SymbologyCreateArc(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height, Double start_angle, Double end_angle, UInt32 color) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 21;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				//write start_angle to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(start_angle,sendData,outPtr);
				outPtr += 4;
				
				//write end_angle to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(end_angle,sendData,outPtr);
				outPtr += 4;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEARC, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateArc()
			
			public static FLR_RESULT SymbologyCreateText(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height, SByte font, Int16 size, FLR_SYMBOLOGY_TEXT_ALIGNMENT_E alignment, UInt32 color, Byte[] text) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 146;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				//write font to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				CHARToByte(font,sendData,outPtr);
				outPtr += 1;
				
				//write size to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(size,sendData,outPtr);
				outPtr += 2;
				
				//write alignment to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte((Int16) alignment,sendData,outPtr);
				outPtr += 2;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				//write text to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(text,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATETEXT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateText()
			
			public static FLR_RESULT SymbologyMoveSprite(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 5;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_MOVESPRITE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyMoveSprite()
			
			public static FLR_RESULT SymbologyAddToGroup(Camera parent, Byte ID, Byte group_ID) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write group_ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(group_ID,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_ADDTOGROUP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyAddToGroup()
			
			public static FLR_RESULT SymbologyRemoveFromGroup(Camera parent, Byte ID, Byte group_ID) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write group_ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(group_ID,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_REMOVEFROMGROUP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyRemoveFromGroup()
			
			public static FLR_RESULT SymbologyUpdateAndShow(Camera parent, Byte ID, Byte visible) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write visible to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(visible,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_UPDATEANDSHOW, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyUpdateAndShow()
			
			public static FLR_RESULT SymbologyUpdateAndShowGroup(Camera parent, Byte group_ID, Byte visible) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write group_ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(group_ID,sendData,outPtr);
				outPtr += 1;
				
				//write visible to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(visible,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_UPDATEANDSHOWGROUP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyUpdateAndShowGroup()
			
			public static FLR_RESULT SymbologyDelete(Camera parent, Byte ID) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_DELETE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyDelete()
			
			public static FLR_RESULT SymbologyDeleteGroup(Camera parent, Byte group_ID) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write group_ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(group_ID,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_DELETEGROUP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyDeleteGroup()
			
			public static FLR_RESULT SymbologyCreateFilledRectangle(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height, UInt32 color) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 13;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEFILLEDRECTANGLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateFilledRectangle()
			
			public static FLR_RESULT SymbologyCreateOutlinedRectangle(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height, UInt32 color) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 13;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEOUTLINEDRECTANGLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateOutlinedRectangle()
			
			public static FLR_RESULT SymbologyCreateBitmapFromPng(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 size) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 7;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write size to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(size,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEBITMAPFROMPNG, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateBitmapFromPng()
			
			public static FLR_RESULT SymbologyCreateCompressedBitmap(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 9;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATECOMPRESSEDBITMAP, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateCompressedBitmap()
			
			public static FLR_RESULT SymbologyCreateBitmapFromPngFile(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Byte[] path) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 133;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEBITMAPFROMPNGFILE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateBitmapFromPngFile()
			
			public static FLR_RESULT SymbologyResetWritePosition(Camera parent, Byte ID) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 1;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_RESETWRITEPOSITION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyResetWritePosition()
			
			public static FLR_RESULT SymbologyMoveByOffset(Camera parent, Byte ID, Int16 off_X, Int16 off_Y) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 5;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write off_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(off_X,sendData,outPtr);
				outPtr += 2;
				
				//write off_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(off_Y,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_MOVEBYOFFSET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyMoveByOffset()
			
			public static FLR_RESULT SymbologyMoveGroupByOffset(Camera parent, Byte ID, Int16 off_X, Int16 off_Y) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 5;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write off_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(off_X,sendData,outPtr);
				outPtr += 2;
				
				//write off_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(off_Y,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_MOVEGROUPBYOFFSET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyMoveGroupByOffset()
			
			public static FLR_RESULT SymbologyCreateFilledEllipse(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 width, Int16 height, UInt32 color) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 13;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write width to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(width,sendData,outPtr);
				outPtr += 2;
				
				//write height to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(height,sendData,outPtr);
				outPtr += 2;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATEFILLEDELLIPSE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateFilledEllipse()
			
			public static FLR_RESULT SymbologyCreateLine(Camera parent, Byte ID, Int16 pos_X, Int16 pos_Y, Int16 pos_X2, Int16 pos_Y2, UInt32 color) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 13;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				//write pos_X2 to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X2,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y2 to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y2,sendData,outPtr);
				outPtr += 2;
				
				//write color to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(color,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_CREATELINE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyCreateLine()
			
			public static FLR_RESULT SymbologySetZorder(Camera parent, Byte ID, Byte zorder) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write zorder to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(zorder,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_SETZORDER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologySetZorder()
			
			public static FLR_RESULT SymbologySaveConfiguration(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_SAVECONFIGURATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologySaveConfiguration()
			
			public static FLR_RESULT SymbologyReloadConfiguration(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_RELOADCONFIGURATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyReloadConfiguration()
			
			public static FLR_RESULT SymbologyGetEnable(Camera parent, out FLR_ENABLE_E draw_symbols) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				draw_symbols = new FLR_ENABLE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_GETENABLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read draw_symbols from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				draw_symbols = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyGetEnable()
			
			public static FLR_RESULT SymbologySetClonesNumber(Camera parent, Byte ID, Byte numberOfClones) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 2;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write numberOfClones to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(numberOfClones,sendData,outPtr);
				outPtr += 1;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_SETCLONESNUMBER, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologySetClonesNumber()
			
			public static FLR_RESULT SymbologyMoveCloneByOffset(Camera parent, Byte ID, Byte cloneID, Int16 pos_X, Int16 pos_Y) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 6;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write cloneID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(cloneID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_MOVECLONEBYOFFSET, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyMoveCloneByOffset()
			
			public static FLR_RESULT SymbologyMoveCloneSprite(Camera parent, Byte ID, Byte cloneID, Int16 pos_X, Int16 pos_Y) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 6;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write ID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(ID,sendData,outPtr);
				outPtr += 1;
				
				//write cloneID to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(cloneID,sendData,outPtr);
				outPtr += 1;
				
				//write pos_X to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_X,sendData,outPtr);
				outPtr += 2;
				
				//write pos_Y to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_16ToByte(pos_Y,sendData,outPtr);
				outPtr += 2;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYMBOLOGY_MOVECLONESPRITE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSymbologyMoveCloneSprite()
			
			// End Module: symbology
			
			// Begin Module: fileOps
			public static FLR_RESULT FileopsDir(Camera parent, out Byte[] dirent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 128;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				dirent = new Byte[128];
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_DIR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read dirent from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				dirent = byteToUCHARArray(receiveData,inPtr,128);
				inPtr+=128;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsDir()
			
			public static FLR_RESULT FileopsCd(Camera parent, Byte[] path, out Byte[] pwd) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 128;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 128;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				pwd = new Byte[128];
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_CD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read pwd from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				pwd = byteToUCHARArray(receiveData,inPtr,128);
				inPtr+=128;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsCd()
			
			public static FLR_RESULT FileopsMd(Camera parent, Byte[] path) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 128;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_MD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsMd()
			
			public static FLR_RESULT FileopsFopen(Camera parent, Byte[] path, Byte[] mode, out UInt32 id) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 256;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				id = new UInt32();
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				//write mode to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(mode,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FOPEN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read id from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				id = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFopen()
			
			public static FLR_RESULT FileopsFclose(Camera parent, UInt32 id) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FCLOSE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFclose()
			
			public static FLR_RESULT FileopsFread(Camera parent, UInt32 id, UInt32 length, out Byte[] buf, out UInt32 ret) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 132;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				buf = new Byte[128];
				ret = new UInt32();
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				//write length to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(length,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FREAD, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read buf from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				buf = byteToUCHARArray(receiveData,inPtr,128);
				inPtr+=128;
				
				// read ret from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ret = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFread()
			
			public static FLR_RESULT FileopsFwrite(Camera parent, UInt32 id, UInt32 length, Byte[] buf, out UInt32 ret) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 136;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				ret = new UInt32();
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				//write length to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(length,sendData,outPtr);
				outPtr += 4;
				
				//write buf to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(buf,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FWRITE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read ret from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				ret = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFwrite()
			
			public static FLR_RESULT FileopsFtell(Camera parent, UInt32 id, out UInt32 offset) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				offset = new UInt32();
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FTELL, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read offset from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				offset = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFtell()
			
			public static FLR_RESULT FileopsFseek(Camera parent, UInt32 id, UInt32 offset, UInt32 origin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 12;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				//write offset to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(offset,sendData,outPtr);
				outPtr += 4;
				
				//write origin to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(origin,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FSEEK, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFseek()
			
			public static FLR_RESULT FileopsFtruncate(Camera parent, UInt32 id, UInt32 length) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(id,sendData,outPtr);
				outPtr += 4;
				
				//write length to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(length,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_FTRUNCATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsFtruncate()
			
			public static FLR_RESULT FileopsRmdir(Camera parent, Byte[] path) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 128;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_RMDIR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsRmdir()
			
			public static FLR_RESULT FileopsRm(Camera parent, Byte[] path) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 128;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_RM, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsRm()
			
			public static FLR_RESULT FileopsRename(Camera parent, Byte[] oldpath, Byte[] newpath) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 256;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write oldpath to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(oldpath,128,sendData,outPtr);
				outPtr += 128;
				
				//write newpath to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(newpath,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_RENAME, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsRename()
			
			public static FLR_RESULT FileopsGetFileSize(Camera parent, Byte[] path, out UInt32 fileLength) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 128;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				fileLength = new UInt32();
				
				//write path to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARArrayToByte(path,128,sendData,outPtr);
				outPtr += 128;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.FILEOPS_GETFILESIZE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read fileLength from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				fileLength = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgFileopsGetFileSize()
			
			// End Module: fileOps
			
			// Begin Module: jffs2
			public static FLR_RESULT Jffs2Mount(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.JFFS2_MOUNT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgJffs2Mount()
			
			public static FLR_RESULT Jffs2Unmount(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.JFFS2_UNMOUNT, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgJffs2Unmount()
			
			public static FLR_RESULT Jffs2GetState(Camera parent, out FLR_JFFS2_STATE_E state) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				state = new FLR_JFFS2_STATE_E();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.JFFS2_GETSTATE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read state from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				state = (FLR_JFFS2_STATE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgJffs2GetState()
			
			// End Module: jffs2
			
			// Begin Module: splashScreen
			public static FLR_RESULT SplashscreenSetDuration(Camera parent, UInt32 screen_num, UInt32 periodMs) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				//write periodMs to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(periodMs,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_SETDURATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenSetDuration()
			
			public static FLR_RESULT SplashscreenSetDataType(Camera parent, UInt32 screen_num, FLR_SPLASHSCREEN_FILETYPE_E filetype) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				//write filetype to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) filetype,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_SETDATATYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenSetDataType()
			
			public static FLR_RESULT SplashscreenSetBackground(Camera parent, UInt32 screen_num, UInt32 backgroundColor) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				//write backgroundColor to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(backgroundColor,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_SETBACKGROUND, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenSetBackground()
			
			public static FLR_RESULT SplashscreenGetDuration(Camera parent, UInt32 screen_num, out UInt32 periodMs) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				periodMs = new UInt32();
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_GETDURATION, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read periodMs from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				periodMs = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenGetDuration()
			
			public static FLR_RESULT SplashscreenGetDataType(Camera parent, UInt32 screen_num, out FLR_SPLASHSCREEN_FILETYPE_E filetype) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				filetype = new FLR_SPLASHSCREEN_FILETYPE_E();
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_GETDATATYPE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read filetype from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				filetype = (FLR_SPLASHSCREEN_FILETYPE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenGetDataType()
			
			public static FLR_RESULT SplashscreenGetBackground(Camera parent, UInt32 screen_num, out UInt32 backgroundColor) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				backgroundColor = new UInt32();
				
				//write screen_num to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(screen_num,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SPLASHSCREEN_GETBACKGROUND, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read backgroundColor from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				backgroundColor = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSplashscreenGetBackground()
			
			// End Module: splashScreen
			
			// Begin Module: systemSymbols
			public static FLR_RESULT SystemsymbolsGetID(Camera parent, FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, out Byte id, out FLR_SYSTEMSYMBOLS_ID_TYPE_E id_type) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 5;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				id = new Byte();
				id_type = new FLR_SYSTEMSYMBOLS_ID_TYPE_E();
				
				//write symbol to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) symbol,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSTEMSYMBOLS_GETID, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read id from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				id = byteToUCHAR(receiveData,inPtr);
				inPtr+=1;
				
				// read id_type from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				id_type = (FLR_SYSTEMSYMBOLS_ID_TYPE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSystemsymbolsGetID()
			
			public static FLR_RESULT SystemsymbolsSetID(Camera parent, FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, Byte id, FLR_SYSTEMSYMBOLS_ID_TYPE_E id_type) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 9;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write symbol to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) symbol,sendData,outPtr);
				outPtr += 4;
				
				//write id to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UCHARToByte(id,sendData,outPtr);
				outPtr += 1;
				
				//write id_type to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) id_type,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSTEMSYMBOLS_SETID, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSystemsymbolsSetID()
			
			public static FLR_RESULT SystemsymbolsGetEnable(Camera parent, FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, out FLR_ENABLE_E enabled) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				enabled = new FLR_ENABLE_E();
				
				//write symbol to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) symbol,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSTEMSYMBOLS_GETENABLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read enabled from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				enabled = (FLR_ENABLE_E) byteToINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSystemsymbolsGetEnable()
			
			public static FLR_RESULT SystemsymbolsSetEnable(Camera parent, FLR_SYSTEMSYMBOLS_SYMBOL_E symbol, FLR_ENABLE_E enabled) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write symbol to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) symbol,sendData,outPtr);
				outPtr += 4;
				
				//write enabled to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				INT_32ToByte((Int32) enabled,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SYSTEMSYMBOLS_SETENABLE, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSystemsymbolsSetEnable()
			
			// End Module: systemSymbols
			
			// Begin Module: sffc
			public static FLR_RESULT SffcGetScaleFactor(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETSCALEFACTOR, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetScaleFactor()
			
			public static FLR_RESULT SffcGetDeltaTempLinearCoeff(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETDELTATEMPLINEARCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetDeltaTempLinearCoeff()
			
			public static FLR_RESULT SffcSetDeltaTempLinearCoeff(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_SETDELTATEMPLINEARCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcSetDeltaTempLinearCoeff()
			
			public static FLR_RESULT SffcGetDeltaTempOffsetCoeff(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETDELTATEMPOFFSETCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetDeltaTempOffsetCoeff()
			
			public static FLR_RESULT SffcSetDeltaTempOffsetCoeff(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_SETDELTATEMPOFFSETCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcSetDeltaTempOffsetCoeff()
			
			public static FLR_RESULT SffcGetFpaTempLinearCoeff(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETFPATEMPLINEARCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetFpaTempLinearCoeff()
			
			public static FLR_RESULT SffcSetFpaTempLinearCoeff(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_SETFPATEMPLINEARCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcSetFpaTempLinearCoeff()
			
			public static FLR_RESULT SffcGetFpaTempOffsetCoeff(Camera parent, out Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new Double();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETFPATEMPOFFSETCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToFLOAT(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetFpaTempOffsetCoeff()
			
			public static FLR_RESULT SffcSetFpaTempOffsetCoeff(Camera parent, Double data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLOATToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_SETFPATEMPOFFSETCOEFF, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcSetFpaTempOffsetCoeff()
			
			public static FLR_RESULT SffcGetDeltaTempTimeLimitInSecs(Camera parent, out UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				data = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_GETDELTATEMPTIMELIMITINSECS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read data from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				data = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcGetDeltaTempTimeLimitInSecs()
			
			public static FLR_RESULT SffcSetDeltaTempTimeLimitInSecs(Camera parent, UInt32 data) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 4;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write data to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				UINT_32ToByte(data,sendData,outPtr);
				outPtr += 4;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.SFFC_SETDELTATEMPTIMELIMITINSECS, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgSffcSetDeltaTempTimeLimitInSecs()
			
			// End Module: sffc
			
			// Begin Module: imageStats
			public static FLR_RESULT ImagestatsGetTotalHistPixelsInROI(Camera parent, out UInt32 totalPixelsInROI) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				totalPixelsInROI = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETTOTALHISTPIXELSINROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read totalPixelsInROI from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				totalPixelsInROI = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetTotalHistPixelsInROI()
			
			public static FLR_RESULT ImagestatsGetPopBelowLowToHighThresh(Camera parent, out UInt32 popBelowLowToHighThresh) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				popBelowLowToHighThresh = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETPOPBELOWLOWTOHIGHTHRESH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read popBelowLowToHighThresh from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				popBelowLowToHighThresh = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetPopBelowLowToHighThresh()
			
			public static FLR_RESULT ImagestatsGetPopAboveHighToLowThresh(Camera parent, out UInt32 popAboveHighToLowThresh) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 4;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				popAboveHighToLowThresh = new UInt32();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETPOPABOVEHIGHTOLOWTHRESH, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read popAboveHighToLowThresh from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				popAboveHighToLowThresh = byteToUINT_32(receiveData,inPtr);
				inPtr+=4;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetPopAboveHighToLowThresh()
			
			public static FLR_RESULT ImagestatsSetROI(Camera parent, FLR_ROI_T roi) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 8;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				//write roi to sendData buffer
				if(outPtr >= (sendBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				FLR_ROI_TToByte(roi,sendData,outPtr);
				outPtr += 8;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_SETROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsSetROI()
			
			public static FLR_RESULT ImagestatsGetROI(Camera parent, out FLR_ROI_T roi) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 8;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				roi = new FLR_ROI_T();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read roi from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				roi = byteToFLR_ROI_T(receiveData,inPtr);
				inPtr+=8;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetROI()
			
			public static FLR_RESULT ImagestatsGetFirstBin(Camera parent, out UInt16 firstBin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				firstBin = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETFIRSTBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read firstBin from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				firstBin = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetFirstBin()
			
			public static FLR_RESULT ImagestatsGetLastBin(Camera parent, out UInt16 lastBin) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				lastBin = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETLASTBIN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read lastBin from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				lastBin = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetLastBin()
			
			public static FLR_RESULT ImagestatsGetMean(Camera parent, out UInt16 mean) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				mean = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETMEAN, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read mean from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				mean = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetMean()
			
			public static FLR_RESULT ImagestatsGetFirstBinInROI(Camera parent, out UInt16 firstBinInROI) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				firstBinInROI = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETFIRSTBININROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read firstBinInROI from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				firstBinInROI = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetFirstBinInROI()
			
			public static FLR_RESULT ImagestatsGetLastBinInROI(Camera parent, out UInt16 lastBinInROI) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				lastBinInROI = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETLASTBININROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read lastBinInROI from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				lastBinInROI = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetLastBinInROI()
			
			public static FLR_RESULT ImagestatsGetMeanInROI(Camera parent, out UInt16 meanInROI) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 2;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				// Assign Null values to all receive parameters
				meanInROI = new UInt16();
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.IMAGESTATS_GETMEANINROI, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				// read meanInROI from receiveData buffer
				if(inPtr >= (receiveBytes)){
					return FLR_RESULT.R_SDK_PKG_BUFFER_OVERFLOW;
				}
				meanInROI = byteToUINT_16(receiveData,inPtr);
				inPtr+=2;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgImagestatsGetMeanInROI()
			
			// End Module: imageStats
			
			// Begin Module: dummy
			public static FLR_RESULT DummyBadCommand(Camera parent) {
				// Allocate buffers with space for marshalled data
				UInt32 sendBytes = 0;
				Byte[] sendData = new Byte[sendBytes];
				UInt32 receiveBytes = 0;
				Byte[] receiveData = new Byte[receiveBytes];
				UInt16 outPtr = 0;
				
				FLR_RESULT returncode = parent.dispatcher(commandCount++, FLR_FUNCTION.DUMMY_BADCOMMAND, sendData, sendBytes, receiveData, ref receiveBytes);
				
				// Check for any errorcode
				if(returncode != FLR_RESULT.R_SUCCESS){
					return returncode;
				}
				
				UInt16 inPtr = 0;
				
				return FLR_RESULT.R_SUCCESS;
				
			}// End of CLIENT_pkgDummyBadCommand()
			
			// End Module: dummy
			
		} // End class ClientPackager
	} // End partial class Camera
} // End namespace Boson

