
from mecom import MeCom, ResponseException, WrongChecksum
from example import MeerstetterTEC

self = MeCom;
MeCom.channel = 1;
MeCom.session = MeCom;

MeerstetterTEC.set_temp(self,20.0)
    

