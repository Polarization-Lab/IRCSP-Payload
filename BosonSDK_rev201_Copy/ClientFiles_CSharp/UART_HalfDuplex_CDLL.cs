
/******************************************************************************/
/*                                                                            */
/*  Copyright (C) 2015, FLIR Systems                                          */
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
using System.Runtime.InteropServices;
using Boson;

namespace Boson {

	partial class Camera{
		
		private class UART{
#if _WIN64
            [DllImport("UART_HalfDuplex64.dll", EntryPoint = "send_to_camera", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _SendToCamera(Int32 PortNum, Byte channelID, UInt32 clientBytes, IntPtr ClientToCam);//, out UInt32 camBytes, IntPtr CamToClient);
            [DllImport("UART_HalfDuplex64.dll", EntryPoint = "open_port", CallingConvention = CallingConvention.Cdecl)]
            private extern static Int32 _OpenPort(Int32 portnum, Int32 baudrate);
            [DllImport("UART_HalfDuplex64.dll", EntryPoint = "close_port", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ClosePort(Int32 portnum);
            [DllImport("UART_HalfDuplex64.dll", EntryPoint = "read_frame", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ReadFrame(Int32 port_num, Byte channel_ID, UInt16 start_byte_ms, ref UInt32 receiveBytes, IntPtr receiveBuffer);
            [DllImport("UART_HalfDuplex64.dll", EntryPoint = "read_unfframed", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ReadUnframed(Int32 port_num, UInt16 start_byte_ms, ref UInt32 receiveBytes, IntPtr receiveBuffer);
#endif
#if _WIN32
            [DllImport("UART_HalfDuplex32.dll", EntryPoint = "send_to_camera", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _SendToCamera(Int32 PortNum, Byte channelID, UInt32 clientBytes, IntPtr ClientToCam);//, out UInt32 camBytes, IntPtr CamToClient);
            [DllImport("UART_HalfDuplex32.dll", EntryPoint = "open_port", CallingConvention = CallingConvention.Cdecl)]
            private extern static Int32 _OpenPort(Int32 portnum, Int32 baudrate);
            [DllImport("UART_HalfDuplex32.dll", EntryPoint = "close_port", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ClosePort(Int32 portnum);
            [DllImport("UART_HalfDuplex32.dll", EntryPoint = "read_frame", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ReadFrame(Int32 port_num, Byte channel_ID, UInt16 start_byte_ms, ref UInt32 receiveBytes, IntPtr receiveBuffer);
            [DllImport("UART_HalfDuplex32.dll", EntryPoint = "read_unfframed", CallingConvention = CallingConvention.Cdecl)]
            private extern static void _ReadUnframed(Int32 port_num, UInt16 start_byte_ms, ref UInt32 receiveBytes, IntPtr receiveBuffer);
#endif
			public Boolean isInitialized { get; set; }
			private int _PortNum;
			public UART(string PortName, UInt32 BaudRate){
				if (int.TryParse(PortName.Substring(3), out _PortNum))
				{
					Int32 result = _OpenPort((Int32) (_PortNum - 1), (Int32) BaudRate);
					if (result == 0)
					{
						isInitialized = true;
						_PortNum = (_PortNum - 1);
					}
					else
					{
						isInitialized = false;
					}
				} 
				else 
				{
					isInitialized = false;
				}
				
			}
			public void Close(){
				_ClosePort((Int32) _PortNum);
			}
			internal void SendToCamera( Byte channelID, UInt32 clientBytes, Byte[] ClientToCam){ //, out UInt32 camBytes, IntPtr CamToClient){
                IntPtr ClientToCamPtr = Marshal.AllocHGlobal((Int32)(ClientToCam.Length));
                Marshal.Copy(ClientToCam, 0, ClientToCamPtr, (Int32)(clientBytes + 12));
				_SendToCamera( (Int32) _PortNum, channelID, clientBytes, ClientToCamPtr);
			}
            internal void ReadFrame(Byte channelID, ref UInt32 receiveBytes, Byte[] receiveBuffer)
            { //, out UInt32 camBytes, IntPtr CamToClient){
                IntPtr receivePtr = Marshal.AllocHGlobal((Int32)(receiveBuffer.Length));
                // hardcoded 1000ms polling delay for now
                _ReadFrame((Int32)_PortNum, channelID, 1000, ref receiveBytes, receivePtr);
                Marshal.Copy(receivePtr, receiveBuffer, 0, (Int32)receiveBytes);
            }
            internal void ReadUnframed(ref UInt32 receiveBytes, byte[] receiveBuffer)
            { //, out UInt32 camBytes, IntPtr CamToClient){
                IntPtr receivePtr = Marshal.AllocHGlobal((Int32)(receiveBuffer.Length));
                // hardcoded 25ms polling delay for now
                _ReadUnframed((Int32)_PortNum, 25, ref receiveBytes,receivePtr);
                Marshal.Copy(receivePtr, receiveBuffer, 0, (Int32)receiveBytes);
            }
		}
		
		private UART myUART = null;
		
		public void Initialize(string PortName, UInt32 BaudRate){
			myUART = new UART(PortName,BaudRate);
			if (!myUART.isInitialized){
				throw new System.IO.IOException("Port initialization failed!");
			}
			
		}
		public void Close(){
			myUART.Close();
		}
        //public void SendToCamera(UInt32 clientBytes,IntPtr ClientToCam,ref UInt32 ReceiveBytes,IntPtr CamToClient){
        //    if (myUART.isInitialized){
        //        myUART.SendToCamera(clientBytes,ClientToCam, out ReceiveBytes, CamToClient);
        //    } else {
        //        throw new System.IO.IOException("Attempting to access closed DLL or COM port!");
        //    }
        //}
        public void SendToCamera(Byte channelID, UInt32 clientBytes, Byte[] ClientToCam)
        { //, out UInt32 camBytes, IntPtr CamToClient){
            if (myUART.isInitialized) 
            {
                myUART.SendToCamera( channelID, clientBytes, ClientToCam);
            } else {
                 throw new System.IO.IOException("Attempting to access closed DLL or COM port!");
            }
        }
        public void ReadFrame(Byte channelID, ref UInt32 receiveBytes, Byte[] receiveBuffer)
        { //, out UInt32 camBytes, IntPtr CamToClient){
            // hardcoded 1000ms polling delay for now
            if (myUART.isInitialized) 
            {
                myUART.ReadFrame(channelID, ref receiveBytes, receiveBuffer);
            } else {
                 throw new System.IO.IOException("Attempting to access closed DLL or COM port!");
            }
        }
        public void ReadUnframed(ref UInt32 receiveBytes, Byte[] receiveBuffer)
        { //, out UInt32 camBytes, IntPtr CamToClient){
            // hardcoded 25ms polling delay for now
            if (myUART.isInitialized) 
            {
                myUART.ReadUnframed( ref receiveBytes, receiveBuffer);
            }
            else
            {
                throw new System.IO.IOException("Attempting to access closed DLL or COM port!");
            }
        }
	}// end internal class FLR_SLP
} // end namespace Boson