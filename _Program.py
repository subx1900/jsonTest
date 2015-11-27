from jsonDal import JsonDal

myJsonRun = JsonDal()

res = myJsonRun.ServletNameAndIparamValExist("cofaxTools", "removePageCache")
print res

srvn = raw_input('Enter servlet-name : ')
iprm = raw_input('Now enter init-param : ')

print myJsonRun.ServletNameAndIparamValExist(srvn, iprm)

#myJsonRun.printJson()
