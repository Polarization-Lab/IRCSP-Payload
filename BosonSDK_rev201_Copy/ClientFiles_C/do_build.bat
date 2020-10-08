tcc -v -c -o Client_Dispatcher_64.o Client_Dispatcher.c -I.
tcc -v -c -o Client_API_64.o Client_API.c -I.
tcc -v -c -o Client_Packager_64.o Client_Packager.c -I.
tcc -v -c -o Serializer_BuiltIn_64.o Serializer_BuiltIn.c -I.
tcc -v -c -o Serializer_Struct_64.o Serializer_Struct.c -I.
tcc -v -c -o UART_Connector_64.o UART_Connector.c -I.
tcc -v -shared -m64 -o C_SDK_64.dll Client_API_64.o Client_Dispatcher_64.o Client_Packager_64.o Serializer_BuiltIn_64.o Serializer_Struct_64.o UART_Connector_64.o UART_HalfDuplex64.def -I.
tcc -v Example.c C_SDK_64.def -I. -o Example_64.exe
 

:: gcc -v -c -o Client_Dispatcher_32.o Client_Dispatcher.c -I.
:: gcc -v -c -o Client_API_32.o Client_API.c -I.
:: gcc -v -c -o Client_Packager_32.o Client_Packager.c -I.
:: gcc -v -c -o Serializer_BuiltIn_32.o Serializer_BuiltIn.c -I.
:: gcc -v -c -o Serializer_Struct_32.o Serializer_Struct.c -I.
:: gcc -v -c -o UART_Connector_32.o UART_Connector.c -I.
:: gcc -v -shared -o C_SDK_32.dll Client_API_32.o Client_Dispatcher_32.o Client_Packager_32.o Serializer_BuiltIn_32.o Serializer_Struct_32.o UART_Connector_32.o UART_HalfDuplex64.def -I.

