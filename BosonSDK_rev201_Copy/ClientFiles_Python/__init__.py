from . import EnumTypes as EE
from . import Client_API as pyClient
from . import Serializer_Struct as SS
from . import __dict__
__all__ = ['pyClient']

for item in EE.__dict__.items():
    if "FLR_" in item[0] and isinstance(item[1],type):
#        print(item[0],item[1].__class__)
        __all__.append(item[0])
        __dict__[item[0]] = item[1]

for item in SS.__dict__.items():
    if "FLR_" in item[0] and isinstance(item[1],type):
#        print(item[0],item[1].__class__)
        __all__.append(item[0])
        __dict__[item[0]] = item[1]
