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


using System;
using Boson;
using System.Runtime.InteropServices;

namespace Boson {
	public partial class Camera {
		//Garbage Variable to avoid ever having blank code
		static Boolean NotEmptyC = true;
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_ROI_T {
			public UInt16 rowStart;
			public UInt16 rowStop;
			public UInt16 colStart;
			public UInt16 colStop;
			public static bool operator ==(FLR_ROI_T self, FLR_ROI_T other) {
				return ((self.rowStart == other.rowStart) && (self.rowStop == other.rowStop) && (self.colStart == other.colStart) && (self.colStop == other.colStop));
			}
			public static bool operator !=(FLR_ROI_T self, FLR_ROI_T other) {
				return !(self == other);
			}
		}// end of FLR_ROI_T()
		
		private static FLR_ROI_T byteToFLR_ROI_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_ROI_T outVal;
			outVal.rowStart = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			outVal.rowStop = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			outVal.colStart = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			outVal.colStop = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			return outVal;
		} //end byteToFLR_ROI_T()
		private static void FLR_ROI_TToByte(FLR_ROI_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_16ToByte((inVal.rowStart),outBuff,ptr);
			ptr += 2;
			
			UINT_16ToByte((inVal.rowStop),outBuff,ptr);
			ptr += 2;
			
			UINT_16ToByte((inVal.colStart),outBuff,ptr);
			ptr += 2;
			
			UINT_16ToByte((inVal.colStop),outBuff,ptr);
			ptr += 2;
			
		} //end FLR_ROI_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_ROIC_FPATEMP_TABLE_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=32)]
				public Int16[] value;
			public static bool operator ==(FLR_ROIC_FPATEMP_TABLE_T self, FLR_ROIC_FPATEMP_TABLE_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_ROIC_FPATEMP_TABLE_T self, FLR_ROIC_FPATEMP_TABLE_T other) {
				return !(self == other);
			}
		}// end of FLR_ROIC_FPATEMP_TABLE_T()
		
		private static FLR_ROIC_FPATEMP_TABLE_T byteToFLR_ROIC_FPATEMP_TABLE_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_ROIC_FPATEMP_TABLE_T outVal;
			outVal.value = byteToINT_16Array(inBuff,ptr,(UInt16) 32);
			ptr += 64;
			
			return outVal;
		} //end byteToFLR_ROIC_FPATEMP_TABLE_T()
		private static void FLR_ROIC_FPATEMP_TABLE_TToByte(FLR_ROIC_FPATEMP_TABLE_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			INT_16ArrayToByte((inVal.value),(UInt16) 32,outBuff,ptr);
			ptr += 64;
			
		} //end FLR_ROIC_FPATEMP_TABLE_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_BOSON_PARTNUMBER_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=20)]
				public Byte[] value;
			public static bool operator ==(FLR_BOSON_PARTNUMBER_T self, FLR_BOSON_PARTNUMBER_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_BOSON_PARTNUMBER_T self, FLR_BOSON_PARTNUMBER_T other) {
				return !(self == other);
			}
		}// end of FLR_BOSON_PARTNUMBER_T()
		
		private static FLR_BOSON_PARTNUMBER_T byteToFLR_BOSON_PARTNUMBER_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_BOSON_PARTNUMBER_T outVal;
			outVal.value = byteToUCHARArray(inBuff,ptr,(UInt16) 20);
			ptr += 20;
			
			return outVal;
		} //end byteToFLR_BOSON_PARTNUMBER_T()
		private static void FLR_BOSON_PARTNUMBER_TToByte(FLR_BOSON_PARTNUMBER_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UCHARArrayToByte((inVal.value),(UInt16) 20,outBuff,ptr);
			ptr += 20;
			
		} //end FLR_BOSON_PARTNUMBER_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_BOSON_SENSOR_PARTNUMBER_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=32)]
				public Byte[] value;
			public static bool operator ==(FLR_BOSON_SENSOR_PARTNUMBER_T self, FLR_BOSON_SENSOR_PARTNUMBER_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_BOSON_SENSOR_PARTNUMBER_T self, FLR_BOSON_SENSOR_PARTNUMBER_T other) {
				return !(self == other);
			}
		}// end of FLR_BOSON_SENSOR_PARTNUMBER_T()
		
		private static FLR_BOSON_SENSOR_PARTNUMBER_T byteToFLR_BOSON_SENSOR_PARTNUMBER_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_BOSON_SENSOR_PARTNUMBER_T outVal;
			outVal.value = byteToUCHARArray(inBuff,ptr,(UInt16) 32);
			ptr += 32;
			
			return outVal;
		} //end byteToFLR_BOSON_SENSOR_PARTNUMBER_T()
		private static void FLR_BOSON_SENSOR_PARTNUMBER_TToByte(FLR_BOSON_SENSOR_PARTNUMBER_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UCHARArrayToByte((inVal.value),(UInt16) 32,outBuff,ptr);
			ptr += 32;
			
		} //end FLR_BOSON_SENSOR_PARTNUMBER_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_BOSON_GAIN_SWITCH_PARAMS_T {
			public UInt32 pHighToLowPercent;
			public UInt32 cHighToLowPercent;
			public UInt32 pLowToHighPercent;
			public UInt32 hysteresisPercent;
			public static bool operator ==(FLR_BOSON_GAIN_SWITCH_PARAMS_T self, FLR_BOSON_GAIN_SWITCH_PARAMS_T other) {
				return ((self.pHighToLowPercent == other.pHighToLowPercent) && (self.cHighToLowPercent == other.cHighToLowPercent) && (self.pLowToHighPercent == other.pLowToHighPercent) && (self.hysteresisPercent == other.hysteresisPercent));
			}
			public static bool operator !=(FLR_BOSON_GAIN_SWITCH_PARAMS_T self, FLR_BOSON_GAIN_SWITCH_PARAMS_T other) {
				return !(self == other);
			}
		}// end of FLR_BOSON_GAIN_SWITCH_PARAMS_T()
		
		private static FLR_BOSON_GAIN_SWITCH_PARAMS_T byteToFLR_BOSON_GAIN_SWITCH_PARAMS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_BOSON_GAIN_SWITCH_PARAMS_T outVal;
			outVal.pHighToLowPercent = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.cHighToLowPercent = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.pLowToHighPercent = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.hysteresisPercent = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			return outVal;
		} //end byteToFLR_BOSON_GAIN_SWITCH_PARAMS_T()
		private static void FLR_BOSON_GAIN_SWITCH_PARAMS_TToByte(FLR_BOSON_GAIN_SWITCH_PARAMS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_32ToByte((inVal.pHighToLowPercent),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.cHighToLowPercent),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.pLowToHighPercent),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.hysteresisPercent),outBuff,ptr);
			ptr += 4;
			
		} //end FLR_BOSON_GAIN_SWITCH_PARAMS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_DVO_YCBCR_SETTINGS_T {
			public FLR_DVO_OUTPUT_YCBCR_FORMAT_E ycbcrFormat;
			public FLR_DVO_OUTPUT_CBCR_ORDER_E cbcrOrder;
			public FLR_DVO_OUTPUT_Y_ORDER_E yOrder;
			public static bool operator ==(FLR_DVO_YCBCR_SETTINGS_T self, FLR_DVO_YCBCR_SETTINGS_T other) {
				return ((self.ycbcrFormat == other.ycbcrFormat) && (self.cbcrOrder == other.cbcrOrder) && (self.yOrder == other.yOrder));
			}
			public static bool operator !=(FLR_DVO_YCBCR_SETTINGS_T self, FLR_DVO_YCBCR_SETTINGS_T other) {
				return !(self == other);
			}
		}// end of FLR_DVO_YCBCR_SETTINGS_T()
		
		private static FLR_DVO_YCBCR_SETTINGS_T byteToFLR_DVO_YCBCR_SETTINGS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_DVO_YCBCR_SETTINGS_T outVal;
			outVal.ycbcrFormat =(FLR_DVO_OUTPUT_YCBCR_FORMAT_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.cbcrOrder =(FLR_DVO_OUTPUT_CBCR_ORDER_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.yOrder =(FLR_DVO_OUTPUT_Y_ORDER_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			return outVal;
		} //end byteToFLR_DVO_YCBCR_SETTINGS_T()
		private static void FLR_DVO_YCBCR_SETTINGS_TToByte(FLR_DVO_YCBCR_SETTINGS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			INT_32ToByte((Int32)(inVal.ycbcrFormat),outBuff,ptr);
			ptr += 4;
			
			INT_32ToByte((Int32)(inVal.cbcrOrder),outBuff,ptr);
			ptr += 4;
			
			INT_32ToByte((Int32)(inVal.yOrder),outBuff,ptr);
			ptr += 4;
			
		} //end FLR_DVO_YCBCR_SETTINGS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_DVO_RGB_SETTINGS_T {
			public FLR_DVO_OUTPUT_RGB_FORMAT_E rgbFormat;
			public FLR_DVO_OUTPUT_RGB_ORDER_E rgbOrder;
			public static bool operator ==(FLR_DVO_RGB_SETTINGS_T self, FLR_DVO_RGB_SETTINGS_T other) {
				return ((self.rgbFormat == other.rgbFormat) && (self.rgbOrder == other.rgbOrder));
			}
			public static bool operator !=(FLR_DVO_RGB_SETTINGS_T self, FLR_DVO_RGB_SETTINGS_T other) {
				return !(self == other);
			}
		}// end of FLR_DVO_RGB_SETTINGS_T()
		
		private static FLR_DVO_RGB_SETTINGS_T byteToFLR_DVO_RGB_SETTINGS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_DVO_RGB_SETTINGS_T outVal;
			outVal.rgbFormat =(FLR_DVO_OUTPUT_RGB_FORMAT_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.rgbOrder =(FLR_DVO_OUTPUT_RGB_ORDER_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			return outVal;
		} //end byteToFLR_DVO_RGB_SETTINGS_T()
		private static void FLR_DVO_RGB_SETTINGS_TToByte(FLR_DVO_RGB_SETTINGS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			INT_32ToByte((Int32)(inVal.rgbFormat),outBuff,ptr);
			ptr += 4;
			
			INT_32ToByte((Int32)(inVal.rgbOrder),outBuff,ptr);
			ptr += 4;
			
		} //end FLR_DVO_RGB_SETTINGS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_DVO_LCD_CONFIG_T {
			public UInt32 width;
			public UInt32 hPulseWidth;
			public UInt32 hBackP;
			public UInt32 hFrontP;
			public UInt32 height;
			public UInt32 vPulseWidth;
			public UInt32 vBackP;
			public UInt32 vFrontP;
			public UInt32 outputFormat;
			public UInt32 control;
			public UInt32 rotation;
			public UInt32 pixelClockkHz;
			public static bool operator ==(FLR_DVO_LCD_CONFIG_T self, FLR_DVO_LCD_CONFIG_T other) {
				return ((self.width == other.width) && (self.hPulseWidth == other.hPulseWidth) && (self.hBackP == other.hBackP) && (self.hFrontP == other.hFrontP) && (self.height == other.height) && (self.vPulseWidth == other.vPulseWidth) && (self.vBackP == other.vBackP) && (self.vFrontP == other.vFrontP) && (self.outputFormat == other.outputFormat) && (self.control == other.control) && (self.rotation == other.rotation) && (self.pixelClockkHz == other.pixelClockkHz));
			}
			public static bool operator !=(FLR_DVO_LCD_CONFIG_T self, FLR_DVO_LCD_CONFIG_T other) {
				return !(self == other);
			}
		}// end of FLR_DVO_LCD_CONFIG_T()
		
		private static FLR_DVO_LCD_CONFIG_T byteToFLR_DVO_LCD_CONFIG_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_DVO_LCD_CONFIG_T outVal;
			outVal.width = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.hPulseWidth = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.hBackP = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.hFrontP = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.height = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.vPulseWidth = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.vBackP = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.vFrontP = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.outputFormat = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.control = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.rotation = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.pixelClockkHz = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			return outVal;
		} //end byteToFLR_DVO_LCD_CONFIG_T()
		private static void FLR_DVO_LCD_CONFIG_TToByte(FLR_DVO_LCD_CONFIG_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_32ToByte((inVal.width),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.hPulseWidth),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.hBackP),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.hFrontP),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.height),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.vPulseWidth),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.vBackP),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.vFrontP),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.outputFormat),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.control),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.rotation),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.pixelClockkHz),outBuff,ptr);
			ptr += 4;
			
		} //end FLR_DVO_LCD_CONFIG_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_CAPTURE_SETTINGS_T {
			public FLR_CAPTURE_SRC_E dataSrc;
			public UInt32 numFrames;
			public UInt16 bufferIndex;
			public static bool operator ==(FLR_CAPTURE_SETTINGS_T self, FLR_CAPTURE_SETTINGS_T other) {
				return ((self.dataSrc == other.dataSrc) && (self.numFrames == other.numFrames) && (self.bufferIndex == other.bufferIndex));
			}
			public static bool operator !=(FLR_CAPTURE_SETTINGS_T self, FLR_CAPTURE_SETTINGS_T other) {
				return !(self == other);
			}
		}// end of FLR_CAPTURE_SETTINGS_T()
		
		private static FLR_CAPTURE_SETTINGS_T byteToFLR_CAPTURE_SETTINGS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_CAPTURE_SETTINGS_T outVal;
			outVal.dataSrc =(FLR_CAPTURE_SRC_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.numFrames = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.bufferIndex = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			return outVal;
		} //end byteToFLR_CAPTURE_SETTINGS_T()
		private static void FLR_CAPTURE_SETTINGS_TToByte(FLR_CAPTURE_SETTINGS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			INT_32ToByte((Int32)(inVal.dataSrc),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.numFrames),outBuff,ptr);
			ptr += 4;
			
			UINT_16ToByte((inVal.bufferIndex),outBuff,ptr);
			ptr += 2;
			
		} //end FLR_CAPTURE_SETTINGS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_CAPTURE_FILE_SETTINGS_T {
			public FLR_CAPTURE_FILE_TYPE_E captureFileType;
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=128)]
				public Byte[] filePath;
			public static bool operator ==(FLR_CAPTURE_FILE_SETTINGS_T self, FLR_CAPTURE_FILE_SETTINGS_T other) {
				return ((self.captureFileType == other.captureFileType) && (self.filePath == other.filePath));
			}
			public static bool operator !=(FLR_CAPTURE_FILE_SETTINGS_T self, FLR_CAPTURE_FILE_SETTINGS_T other) {
				return !(self == other);
			}
		}// end of FLR_CAPTURE_FILE_SETTINGS_T()
		
		private static FLR_CAPTURE_FILE_SETTINGS_T byteToFLR_CAPTURE_FILE_SETTINGS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_CAPTURE_FILE_SETTINGS_T outVal;
			outVal.captureFileType =(FLR_CAPTURE_FILE_TYPE_E) byteToINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.filePath = byteToUCHARArray(inBuff,ptr,(UInt16) 128);
			ptr += 128;
			
			return outVal;
		} //end byteToFLR_CAPTURE_FILE_SETTINGS_T()
		private static void FLR_CAPTURE_FILE_SETTINGS_TToByte(FLR_CAPTURE_FILE_SETTINGS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			INT_32ToByte((Int32)(inVal.captureFileType),outBuff,ptr);
			ptr += 4;
			
			UCHARArrayToByte((inVal.filePath),(UInt16) 128,outBuff,ptr);
			ptr += 128;
			
		} //end FLR_CAPTURE_FILE_SETTINGS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_TF_WLUT_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=32)]
				public Byte[] value;
			public static bool operator ==(FLR_TF_WLUT_T self, FLR_TF_WLUT_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_TF_WLUT_T self, FLR_TF_WLUT_T other) {
				return !(self == other);
			}
		}// end of FLR_TF_WLUT_T()
		
		private static FLR_TF_WLUT_T byteToFLR_TF_WLUT_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_TF_WLUT_T outVal;
			outVal.value = byteToUCHARArray(inBuff,ptr,(UInt16) 32);
			ptr += 32;
			
			return outVal;
		} //end byteToFLR_TF_WLUT_T()
		private static void FLR_TF_WLUT_TToByte(FLR_TF_WLUT_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UCHARArrayToByte((inVal.value),(UInt16) 32,outBuff,ptr);
			ptr += 32;
			
		} //end FLR_TF_WLUT_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_TF_NF_LUT_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=17)]
				public UInt16[] value;
			public static bool operator ==(FLR_TF_NF_LUT_T self, FLR_TF_NF_LUT_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_TF_NF_LUT_T self, FLR_TF_NF_LUT_T other) {
				return !(self == other);
			}
		}// end of FLR_TF_NF_LUT_T()
		
		private static FLR_TF_NF_LUT_T byteToFLR_TF_NF_LUT_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_TF_NF_LUT_T outVal;
			outVal.value = byteToUINT_16Array(inBuff,ptr,(UInt16) 17);
			ptr += 34;
			
			return outVal;
		} //end byteToFLR_TF_NF_LUT_T()
		private static void FLR_TF_NF_LUT_TToByte(FLR_TF_NF_LUT_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_16ArrayToByte((inVal.value),(UInt16) 17,outBuff,ptr);
			ptr += 34;
			
		} //end FLR_TF_NF_LUT_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=17)]
				public UInt16[] value;
			public static bool operator ==(FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T self, FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T self, FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T other) {
				return !(self == other);
			}
		}// end of FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T()
		
		private static FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T byteToFLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T outVal;
			outVal.value = byteToUINT_16Array(inBuff,ptr,(UInt16) 17);
			ptr += 34;
			
			return outVal;
		} //end byteToFLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T()
		private static void FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_TToByte(FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_16ArrayToByte((inVal.value),(UInt16) 17,outBuff,ptr);
			ptr += 34;
			
		} //end FLR_TF_TEMP_SIGNAL_COMP_FACTOR_LUT_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_SPNR_PSD_KERNEL_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=64)]
				public Double[] fvalue;
			public static bool operator ==(FLR_SPNR_PSD_KERNEL_T self, FLR_SPNR_PSD_KERNEL_T other) {
				return ((self.fvalue == other.fvalue));
			}
			public static bool operator !=(FLR_SPNR_PSD_KERNEL_T self, FLR_SPNR_PSD_KERNEL_T other) {
				return !(self == other);
			}
		}// end of FLR_SPNR_PSD_KERNEL_T()
		
		private static FLR_SPNR_PSD_KERNEL_T byteToFLR_SPNR_PSD_KERNEL_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_SPNR_PSD_KERNEL_T outVal;
			outVal.fvalue = byteToFLOATArray(inBuff,ptr,(UInt16) 64);
			ptr += 256;
			
			return outVal;
		} //end byteToFLR_SPNR_PSD_KERNEL_T()
		private static void FLR_SPNR_PSD_KERNEL_TToByte(FLR_SPNR_PSD_KERNEL_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			FLOATArrayToByte((inVal.fvalue),(UInt16) 64,outBuff,ptr);
			ptr += 256;
			
		} //end FLR_SPNR_PSD_KERNEL_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_SCALER_ZOOM_PARAMS_T {
			public UInt32 zoom;
			public UInt32 xCenter;
			public UInt32 yCenter;
			public static bool operator ==(FLR_SCALER_ZOOM_PARAMS_T self, FLR_SCALER_ZOOM_PARAMS_T other) {
				return ((self.zoom == other.zoom) && (self.xCenter == other.xCenter) && (self.yCenter == other.yCenter));
			}
			public static bool operator !=(FLR_SCALER_ZOOM_PARAMS_T self, FLR_SCALER_ZOOM_PARAMS_T other) {
				return !(self == other);
			}
		}// end of FLR_SCALER_ZOOM_PARAMS_T()
		
		private static FLR_SCALER_ZOOM_PARAMS_T byteToFLR_SCALER_ZOOM_PARAMS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_SCALER_ZOOM_PARAMS_T outVal;
			outVal.zoom = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.xCenter = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			outVal.yCenter = byteToUINT_32(inBuff,ptr);
			ptr += 4;
			
			return outVal;
		} //end byteToFLR_SCALER_ZOOM_PARAMS_T()
		private static void FLR_SCALER_ZOOM_PARAMS_TToByte(FLR_SCALER_ZOOM_PARAMS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_32ToByte((inVal.zoom),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.xCenter),outBuff,ptr);
			ptr += 4;
			
			UINT_32ToByte((inVal.yCenter),outBuff,ptr);
			ptr += 4;
			
		} //end FLR_SCALER_ZOOM_PARAMS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_TESTRAMP_SETTINGS_T {
			public UInt16 start;
			public UInt16 end;
			public UInt16 increment;
			public static bool operator ==(FLR_TESTRAMP_SETTINGS_T self, FLR_TESTRAMP_SETTINGS_T other) {
				return ((self.start == other.start) && (self.end == other.end) && (self.increment == other.increment));
			}
			public static bool operator !=(FLR_TESTRAMP_SETTINGS_T self, FLR_TESTRAMP_SETTINGS_T other) {
				return !(self == other);
			}
		}// end of FLR_TESTRAMP_SETTINGS_T()
		
		private static FLR_TESTRAMP_SETTINGS_T byteToFLR_TESTRAMP_SETTINGS_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_TESTRAMP_SETTINGS_T outVal;
			outVal.start = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			outVal.end = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			outVal.increment = byteToUINT_16(inBuff,ptr);
			ptr += 2;
			
			return outVal;
		} //end byteToFLR_TESTRAMP_SETTINGS_T()
		private static void FLR_TESTRAMP_SETTINGS_TToByte(FLR_TESTRAMP_SETTINGS_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UINT_16ToByte((inVal.start),outBuff,ptr);
			ptr += 2;
			
			UINT_16ToByte((inVal.end),outBuff,ptr);
			ptr += 2;
			
			UINT_16ToByte((inVal.increment),outBuff,ptr);
			ptr += 2;
			
		} //end FLR_TESTRAMP_SETTINGS_TToByte()
		
		[ StructLayout( LayoutKind.Sequential )]
		public struct FLR_SYSINFO_MONITOR_BUILD_VARIANT_T {
			[MarshalAs(UnmanagedType.ByValArray,SizeConst=50)]
				public Byte[] value;
			public static bool operator ==(FLR_SYSINFO_MONITOR_BUILD_VARIANT_T self, FLR_SYSINFO_MONITOR_BUILD_VARIANT_T other) {
				return ((self.value == other.value));
			}
			public static bool operator !=(FLR_SYSINFO_MONITOR_BUILD_VARIANT_T self, FLR_SYSINFO_MONITOR_BUILD_VARIANT_T other) {
				return !(self == other);
			}
		}// end of FLR_SYSINFO_MONITOR_BUILD_VARIANT_T()
		
		private static FLR_SYSINFO_MONITOR_BUILD_VARIANT_T byteToFLR_SYSINFO_MONITOR_BUILD_VARIANT_T( Byte[] inBuff, UInt16 inPtr) {
			
			UInt16 ptr = inPtr;
			FLR_SYSINFO_MONITOR_BUILD_VARIANT_T outVal;
			outVal.value = byteToUCHARArray(inBuff,ptr,(UInt16) 50);
			ptr += 50;
			
			return outVal;
		} //end byteToFLR_SYSINFO_MONITOR_BUILD_VARIANT_T()
		private static void FLR_SYSINFO_MONITOR_BUILD_VARIANT_TToByte(FLR_SYSINFO_MONITOR_BUILD_VARIANT_T inVal, Byte[] outBuff, UInt16 outPtr) {
			
			UInt16 ptr = outPtr;
			UCHARArrayToByte((inVal.value),(UInt16) 50,outBuff,ptr);
			ptr += 50;
			
		} //end FLR_SYSINFO_MONITOR_BUILD_VARIANT_TToByte()
		
	} // end partial class Camera
} // end namespace Boson
