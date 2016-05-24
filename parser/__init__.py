#coding:utf-8
import os

# NiuParser path
parserPath = "/xxx/NiuParser-v1.3.0-linux/"
# the file which needs to be dealed path
fileprefix = "/xxx/search/src/"

# filename must be encoded by "utf-8" reference to NiuParser Manual 
class Parser:
    def exe(self,com):
        print ("command:"+com)
        res =  os.popen(com).readlines()
        print (res)
    def ws(self,filename):
        com = "cd "+parserPath+"bin && \
        ./NiuParser-v1.3.0-mt-linux --WS -in "+filename+" -out "+filename+".ws"+" -c niuparser.config"
        self.exe(com)
        print ("WS finish")
    def pos(self,filename):
        com = "cd "+parserPath+"bin && \
        ./NiuParser-v1.3.0-mt-linux --POS -in "+filename+".ws"+" -out "+filename+".pos"+" -c niuparser.config"
        self.exe(com)
        print "POS finish"
    def ner(self,filename):
        com = "cd "+parserPath+"bin && \
        ./NiuParser-v1.3.0-mt-linux --NER -in "+filename+".pos"+" -out "+filename+".ner"+" -c niuparser.config"
        self.exe(com)
        print "NER finish"
    def dp(self,filename):
        com = "cd "+parserPath+"bin && \
        ./NiuParser-v1.3.0-mt-linux --DP -in "+filename+".pos"+" -out "+filename+".dp"+" -c niuparser.config"
        self.exe(com)
        print "DP finish"
        
# test as an example 
# parser = Parser()
# parser.ws(fileprefix+"movie.QUERY.DEVSET.txt")
# parser.pos(fileprefix+"movie.QUERY.DEVSET.txt")
# parser.ner(fileprefix+"movie.QUERY.DEVSET.txt") 
# parser.dp(fileprefix+"movie.QUERY.DEVSET.txt") 
