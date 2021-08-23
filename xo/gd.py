#gd.py


# print()
# from new import *
# from sync import *

import time, random, sys, os, traceback

from .xoHelper import *

withGitSync = False
if withGitSync:
	from .sync import *
else:
    from .xo import *

# print("subing")
# xo.subscribe("settings.autoSync",lambda a: print(" ::: autoSync is True ::: ", xo.watcher.syncRepos(asyn = True), xo.watcher.run.setValue(True)) if a == True else False, autoPub="settings.autoRun")
# # print("subing")
# # xo.subscribe("home",watchF)
# if xo.settings.autoSync.value() == True:
# 	xo.settings.autoSync = True

isInitBefore = xo.GetXO("_init_")
firstTime = False
if isInitBefore is None:
	firstTime = True
	xo._firstTime = True
else:
	xo._firstTime = False

xo["_init_"] = True


def processRES(data):
	print("\n ::: xo.res has changed ::: xo.res =",data)
def processRESCMD(data):
	print("\n ::: CMD RESULTS :::",data)

xo.subscribe("res",processRES)#, autoPub="settings.autoRun")
xo.subscribe("cmd.res",processRESCMD)#, autoPub="settings.autoRun")


print(" ::: Loading History ")
# xo.test()


# xo.Helper = showHelper
xo.helper.basic = "use xo. to create new xobjects"
xo.helper.basic.newXO = "xo.adam = 'init person'"
xo.helper.basic.newXO.var = "xo.adam.height = '1.75m'"
xo.helper.basic.newXO.func = "xo.adam.run = manRuns 			# def manRuns(man):"
xo.helper.basic.GetXO = "xo.GetXO('adam.height')     	# gets adam.height xo"
xo.helper.basic.save_functions = "xo.myFunc = Foo ; xo.myFunc() 	# runs def Foo()"
xo.helper.basic.save_functions.withParams = "xo.myFunc = Foo ; xo.myFunc('hey') # runs def Foo(msg)"
xo.helper.basic.save_functions.lambdas = "xo.myFunc = lambda a,b,c : [print(a,b,c) for i in range(3)]"
xo.helper.mainFuncs = "These functions will help you with the following"
xo.helper.mainFuncs.cmd = "Run commands like the terminal"
xo.helper.mainFuncs.cmd.runCommand = "xo.cmd('ping 8.8.8.8')"
xo.helper.mainFuncs.cmd.getResults = "xo.cmd('ping 8.8.8.8', autoPub = 'pingData') # data is saved to xo.pingData "
xo.helper.mainFuncs.asyn = "Run functions in async thread"
xo.helper.mainFuncs.asyn.headers = "xo.asyn(func), *param, **params) run functions in async thread"
xo.helper.mainFuncs.asyn = "xo.asyn(func, *param, **params) supports any header variable"
xo.helper.mainFuncs.asyn.example = "xo.asyn(xo.f.takes3secs); print('this will run before takes3secs() finishes')"
xo.helper.mainFuncs.measure  = "Measure the time it take a function to run												"
xo.helper.mainFuncs.measure.example  = "xo.measure(xo.f.takes3) 				# will output 3 at "
xo.helper.mainFuncs.measure.example2  = "xo.measure(xo.f.takesX, s = 4, asyn = True) # will run async takesX(s=4) and measure time"
# xo.helper.mainFuncs.asyn.ex2 = "	xo.asyn(xo.f.takes3secs); print('this will run before takes3secs() finishes')"
# xo.helper.mainFuncs.asyn.ex3 = "	xo.asyn(xo.f.takes3secs);print('this will run before takes3secs() finishes')"
# xo.helper.mainFuncs.asyn.ex4 = "	xo.asyn(xo.f.takes3secs);print('this will run before takes3secs() finishes')"
xo.helper.explore.openDB = "Use xo.openDB() to open the main db folder"
xo.helper.explore.awaitExe = "Use xo.awaitExe( t, func, param='yo') to await t seconds and runs function with params, asyn=True by default"
xo.helper.explore.awaitExe.example = "xo.awaitExe(3,lambda:print('yesss'))"
xo.helper.explore.pnr = "Print and Return "
xo.helper.explore.timer = "runs a function loop with delay"
xo.helper.explore.timer.example = "xo.timer( lambda: xo.pnr(' ::: Timer :D '),asyn = True) ; xo.awaitExe( 3, lambda: xo.timer.run.set(False) )"

# xo.helper.explore.openDB = "		xo.openDB() to open the main db folder"
xo.helper.adv.classicVariable = "	xo.adam._classicType = 3 # will be saved as int(3)"
# xo.helper.adv.hiddenVariable = "xo.adam[_hiddenKey] = use ['_'+key] to create hidden xo "

# check
#
if xo.helper.onstartup == True:
	xo.helper()

xo.helper = showHelper

# if firstTime:
	# xo.helper.debug = True

xo.cmd = command
xo.asyn = asyn
xo.timer = timer
xo.measure = measureDuration
xo.awaitExe = sleepAnd
xo.pnr = pnr
xo.openDB = openDB
## xo.adam.learn(toWalk)
## xo.seq = [func1,func2, func3]
## xo.chain = [func1,func2, func3]
xo.f.fnf = fAnd
xo.f.takes3 = takes3sec
xo.f.takesX = takesXsecs
xo.f._repoSize = lambda a = "https://github.com/fire17/Projects":print(a,"Size is",xo.cmd(f"curl {a} 2> /dev/null | grep size | tr -dc '[:digit:]'",asyn = False),"MBs")

from .sync import *
# from .sync import MQTT as mq
# print("ccccc",sub)
xo.settings = "Here we save Settings"
xo.mqtt.settings.server = "broker.hivemq.com"
xo.mqtt.settings.port = 1883
xo.mqtt.settings.keepAlive = 60
# xo.mqtt.mainKey = "U(Y&Y*GN&(B6t097mTN(&^NT&(*))))"
sub()

xo.subscribe("mqtt.mainKey", sub)

xo.msub = sub
xo.mpub = pub

xo.__version__ = "Starlight 3.2.1 MQTT HEAVEN "
# print("ccccc")
print(" ::: Init Done ")

print()
if xo._firstTime():
	pass
else:
	pass #print()

print(" ::::::::::::::::::::::::::::::::::::::::")
print(" :::                                  :::")
print(" :::        xObject is ready          :::")
print(" :::                                  :::")
print(" :::   Please run     or just use     :::")
print(" :::  xo = xo.ok()   from xo import * :::")
print(" :::                                  :::")
print(" ::::::::::::::::::::::::::::::::::::::::")
print()


# print(" ::: Welcome to xObject  ")
# print(" ::: run xo.helper() to see new features and possible commands")
# print()
# print(" ::: Please use                    	:::")
# print(" :::    from xo import *             :::")
# print(" ::: or                           	:::")
# print(" :::    import xo; xo = ok()"        :::")
# print(" :::    xo = ok()                    :::")
# print()


# xo.test = testAsyn
# xo.f.sleepAnd = sleepAnd
# xo.f.waitAnd = sleepAnd


# import sync
# import fileWatch

# print("manager",manager)
# xoManager = xo.__objManager._shared


# xo.alive = True


# xo.watchRepo = githubWatcher.watchRepo
# xo.syncRepo = sync.syncRepo
# xo.watchFiles = fileWatch.watchFiles


# xo.watchXO

# print("YO")

# from akeyo import *
# print("oooooooo",ox)
# print()
# print()
