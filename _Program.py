from jsonDal import JsonDal

myJsonRun = JsonDal()
myJsonRun.getByServletName("cofaxCDS")
myJsonRun.getByServletNameAndIparamVal("cofaxTools", "toolstemplates/")
#myJsonRun.printJson()
