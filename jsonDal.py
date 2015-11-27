import json

class JsonDal(object):
    def __init__(self):

        with open('example.json') as data_file:
            self.jsonData = json.load(data_file)
            data_file.close()

    def getJsonData(self, dict):

        for k, v in dict.items():
            if k == "web-app":
                yield v
            elif isinstance(v, dict):
                for id_val in self.getJsonData(self, v):
                    yield id_val

    def getByServletName(self, psln):
        wp = self.jsonData["web-app"]
        servlet = wp["servlet"]

        for sln in servlet:
            if psln == sln["servlet-name"]:
                print "servlet-name is : " + sln["servlet-name"] + " " + \
                      "servlet-class is : " + sln["servlet-class"] + \
                      "\ninit-params are : "
                for subkey, value in sln["init-param"].iteritems():
                    print subkey, value
            else:
                print 'not found..'

    def ServletNameAndIparamValExist(self, psln, iprm):
        wp = self.jsonData["web-app"]
        servlet = wp["servlet"]

        iprmFlag = 0

        for sln in servlet:
            if psln == sln["servlet-name"]:
                #servletdetails = "servlet-name is : " + sln["servlet-name"] + " " + \
                                 #"servlet-class is : " + sln["servlet-class"] + \
                                 #"\ninit-params are : "

                for subkey, value in sln["init-param"].iteritems():

                    if subkey == iprm:
                        iprmFlag = 1
                        return iprmFlag

                #if iprmFlag == 1:
                    #print servletdetails
                    #for subkey, value in sln["init-param"].iteritems():
                    #    print subkey, value
                #else:
                    #print 'not found..'
        #if iprmFlag == 0:
            #print 'not found..'
        return iprmFlag

    def printJson(self):

        for jd in self.getJsonData(self.jsonData):
            print(jd)
