from .osCommands import *
from .xo import *

import platform, sys
import subprocess

'''
# pip install anything
# xo.cmd("python3.7 -m pip install xo-gd")
# import from many folder
# import sys;
# sys.path.append('/path/to/application/app/folder'); import filename
# xo.cmd("python3.7 -m pip install xo-gd")
'''

def openDB(path = ""):
	if path is "" or path is None:
		path = xo.home()
	print(" ::: Opening xo.home DB folder :::",path)
	if platform.system() == "Windows":
		os.startfile(path)
	elif platform.system() == "Darwin":
		subprocess.Popen(["open", path])
		# xo.cmd("open "+path)
	else:
		subprocess.Popen(["xdg-open", path])
		# xo.cmd("xdg-open "+path)

# def openDB():
# 	path = xo.home()
# 	print(" ::: Opening xo.home DB folder :::",path)
# 	if sys.platform == 'darwin':
# 	    def openFolder(path):
# 	        subprocess.check_call(['open', '--', path])
# 	elif sys.platform == 'linux2':
# 	    def openFolder(path):
# 	        subprocess.check_call(['xdg-open', '--', path])
# 	elif sys.platform == 'win32':
# 	    def openFolder(path):
# 	        subprocess.check_call(['explorer', path])

def processCMD(*args, **kwargs):
	print(f" ::: Processing Data from CMD ::: data length {len(str(args))}\n\n")

# REPOSIZE
# curl https://api.github.com/repos/fire17/AlphaENG 2> /dev/null | grep size | tr -dc '[:digit:]'

# TODO: Fix *args **kwargs
# def osCommand(cmd = ['ping -c100 www.google.com',False], callback = processCMD):
def osCommand(cmd = ["",'ping -c100 www.google.com',False, processCMD, "cmd.res"]):
	oneLine, location, cmd, asyn, callback, autoPub = cmd
	# location = "/home/magic/xo-gd/main"
	# cmd = "rm -rf fire17_AlphaENG && git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	# cmd = "git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	if location and not asyn:
		currDir = os.getcwd()
		os.chdir(location)
		newDir = os.getcwd()
		print(" ::: CD TO",location)
	# print("RUNNING 1")
	# res =
	# print("ASYN", asyn)
	if not asyn or True:
		if not oneLine or True:
			cmd = cmd.strip(" ").split(' ')
			# print("bbbbbbbbbbbbbbbbbbb")
		else:
			cmd = [cmd.strip(" ")]
		res = []
		try:
			print (f" ::: Running Command ::: {' '.join(cmd)} \n ::: you can break (ctrl+c) and get the results :::  \n")
			for line in os_command(cmd, print_output=True):
				print(line)
				res.append(line)
		except Exception as e:
			traceback.print_exc()
			print(" ::: STOPING CMD !!! :::")
			pass #so you can break and also get the results

		if callback is not None:
			print(" ::: Sending results to callback !!! :::", callback)
			callback(res)
		if autoPub is not None and autoPub is not "":
			if "list" not in str(type(autoPub)):
				autoPub = [autoPub]
			for a in autoPub:
				x = xo.GetXO(a)
				if x:
					x.set(res)
		# xo.res = res
		return res
	# #######################################################################
	# Below Not Running

	res = []
	for cmdA in cmd.split(" && ")[1:]:
		if not oneLine:
			cmdA = cmdA.split(' ')
			# print("bbbbbbbbbbbbbbbbbbb")
		else:
			cmdA = [cmdA]
			# print("AAAAAAAAAAAAAAAAAAAAAAAAAAA",cmdA)
		resA = run_os_command(cmdA, print_output=False)
		# print("BBBBBBBBBBBBBBBBBBBBBBBBBBB",resA)
		res.append(resA)

	# print("RRRRRRRR",res)
	if location:
		os.chdir(currDir)
		resDir = os.getcwd()
		print(" ::: currDir == resDir",currDir == resDir," BACK TO ",resDir)

	if callback is not None:
		callback(res)
	if autoPub is not None and autoPub is not "" and autoPub is not []:
		if "list" not in str(type(autoPub)):
			autoPub = [autoPub]
		for a in autoPub:
			x = xo.GetXO(a)
			if x:
				x.set(res)
	# xo.res = res
	# print("RUNNING ASYNC DONE")
	# xo.res = line
	# # line = process.stdout.readline().rstrip()
	# # yield line
	# print("............DONE")
	return True


# def command(cmd = , asyn = False):
# def command(cmd = "ping 8.8.8.8",location ="", asyn = True):
# def command(cmd = "ping 8.8.8.8",location ="/home/magic/xo-gd/main", asyn = True):
# def command(cmd = "git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG ",location ="", asyn = True):
def command(cmd = "ping 8.8.8.8",location ="", oneLine=True, asyn = True):
	# print("XXXXXD")
	xo._osCMD = osCommand
	if asyn:
		xo._osCMD([oneLine, location, cmd, asyn, processCMD,"cmd.res"], asyn = asyn)
	else:
		xo._osCMD([oneLine, location, cmd, asyn, processCMD,"cmd.res"])
	# print("XXXXXD2")

def cloneCommand(repo):
	path = xo.home.value() + "_".join(repo.split(".git")[0].split(".com/")[-1].split("/")[:2])
	cmd = f"git clone {repo} {path}"
	xo.cmd(cmd)

### SPECIAL FEATURES
#
# def _runF(func, *args, **kwargs):
# 	return func(*args,**kwargs)
#
def testF(given, optional = True, *args, **kwargs):
	print("TTTTTTTTTTTTTTTTTTTTTTT")
	time.sleep(1)
	print("GIVEN",given,"Optional",optional,"args",args,"kwargs",kwargs)

def testAsyn():
	print("1111")
	xo.asyn(testF, *["yes"], **{"optional":"fuckyea","extra":"awesome"})
	print("1111")

def asyn(func, *args, **kwargs):
	# print(args,kwargs)
	xo["_f"][str(func)] = func
	xo["_f"][str(func)](*args, **kwargs,asyn = True)

def pnr(data = "", msg = None):
	if msg is None:
		msg = ""
	msg += " "+str(data)
	if xo.helper.debug == True or xo._firstTime() :
		print(" ::: PrintAndReturn Data :::",msg)
	else:
		print(msg)
	return data

def sleepAnd(t,runFunc, _comeback=False, *args, **kwargs):
	print("Wait",t)
	if not _comeback and ("asyn" not in kwargs or kwargs["asyn"] != False):
		if "asyn" in kwargs:
			kwargs.pop("asyn")
		print("aaaaaa",args,kwargs)

		return xo.asyn(comeback,sleepAnd, t=t,runFunc = runFunc, _comeback = True, *args, **kwargs)
		# return xo.asyn(,t = t)
	time.sleep(t)
	print("HERE!!!!!!!!!!!!!!")
	return runFunc(*args, **kwargs)

def fAnd(func,funcB, *args, **kwargs):
	func(*args, **kwargs)
	funcB(*args, **kwargs)

def hello():
	print("hello")
	return "hello!!!!!!!!!!!!"

	# def timer(func = lambda *args, **kwargs: print("Hello from timer"), t = 1, limit = -1, autoRestart = False, asy = False, stopKey = "timer.run2", *args, **kwargs):
def timer(func, t = 1, limit = -1, autoRestart = False, asy = False, stopKey = "timer.run", *args, **kwargs):
	if asy:
		print("TIMER")
		xo.asyn(timerA, func = func, t = t, limit = limit, autoRestart = autoRestart, asy = asy, stopKey = stopKey, *args, **kwargs)
		# xo.asyn(timerA, *args, **kwargs)
	else:
		# xo.asyn(timerA, *args, **kwargs)
		return timerA(func , t = t, limit = limit, autoRestart = autoRestart, asy = asy, stopKey = stopKey, *args, **kwargs)

def helloTimer(*args, **kwargs):
	print("Hello from timer")
	print(f"kwargs:{kwargs}")
	print()

# def time(*args, ):
#     print()
#     return time.time()
def sleep(t, *args, **kwargs):
	return time.sleep(t)

def takesXsecs(*args, **kwargs): # Needs s =
	print(f" ::: THIS WILL TAKE {kwargs['s']} SECONDS")
	sleep(kwargs["s"])
	print(f" ::: DONE ::: ")
	# sleep(s)

def takes1sec(*args, **kwargs):
	print(" ::: Takes 1 Seconds")
	sleep(1)
	print(" ::: Takes 1 Seconds - FIN")

def takes3sec(*args, **kwargs):
	print(" ::: Takes 3 Seconds")
	sleep(3)
	print(" ::: Takes 3 Seconds - FIN")


def comeback(f, *args, **kwargs):
	print("cccccccomeback")
	return f(*args, **kwargs)

def measureDuration(runFunc = takesXsecs, asy = False ,autoPub = "", _comeBack = False, *args, **kwargs):
	ap = str(runFunc)
	if not asy or _comeBack:
		if autoPub is "":
			# print("....",autoPub)
			ap = "_".join(str(runFunc).split(" ")[1:2])
			autoPub = f"timer.measure.{ap}.last"

		t0 = time.time()
		res = runFunc(*args, **kwargs)
		tF = time.time()-t0
		# print("TTTTTTT",tF)
		if autoPub is None:
			print(f" ::: Function {ap} finished. took {tF} seconds")
			return tF
		# print(autoPub)
		xo.SetValue(autoPub,tF)
		print(f" ::: Function {ap} finished. took {xo.GetXO(autoPub)} seconds")
		print(f" ::: Results autoPubish to",autoPub, ":::")
		return tF
	else:
		return xo.asyn(comeback,measureDuration,runFunc = runFunc, asy = asy ,autoPub = autoPub, _comeBack = True, *args, **kwargs)



def timerA(runFunc, t = 1, limit = -1, autoRestart = False, asy = True, stopKey = "timer.run", *args, **kwargs):
	c = 0
	print(f" ::: Running timer for runFunc:{str(runFunc)}  ::: asy = {asy} ::: timeout = {t}  ::: limit = {limit}  ::: autoRestart = {autoRestart}\n::: stopKey = xo.{stopKey}")
	print("ASS",asy)
	xo.GetXO(stopKey, allow_creation=True).set( True )
	autoReset = True
	res = None
	try:
		while autoReset:
			if not autoRestart:
				autoReset = False
			# try:
			if True:
				while(xo.GetXO(stopKey, allow_creation=True).value() is not False and (limit==-1 or c<limit)):
					res = runFunc(*args, **kwargs)
					time.sleep(t)
					c+=1
	except:
		print(f" ::: Exception in timer for runFunc:{str(runFunc)}  ::: asyc = {asy} ::: timeout = {t}  ::: limit = {limit}  ::: autoRestart = {autoRestart} ::: stopKey xo.{stopKey}")
		traceback.print_exc()
		print()
	print(f" ::: Timer Finished for runFunc:{str(runFunc)}  ::: asyc = {asy} ::: timeout = {t}  ::: limit = {limit}  ::: autoRestart = {autoRestart} ::: stopKey xo.{stopKey}")


	return res

def showHelper():
	print()
	print(" :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print(" ::: xo.helper() :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print(" ::: Use any of the following commands to test xo' functionality :::::::::::::::")
	print(" ::: To run helper again use xo.helper() :::::::::::::::::::::::::::::::::::::::")
	print(" :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print()
	xo.helper.show()

# timer
# measure
# pnr
# waitAnd
#

####### TODO
'''

Use Python Like You Never Have Before, Easy Acces To: Events and Triggers, Realtime MultiProcessing, Instant Dynamic DB, Filesytem & Web Watchdog, Sockets, API Server, Support You Fast Prototyping To Large Scale Systems


Use Python Like You Never Have Before,
Easy Acces To: Events and Triggers
Realtime MultiProcessing
Instant Dynamic DB
Filesytem & Web Watchdog, Sockets, API Server,
From Fast Prototyping To Large Scale Systems

xo.cmd(pip)
xo.map ! Vis of the network !
xo.AJ20.map ! Vis of the network !

# POST TO REDDIT # I've used a bunch of reflections to make python better, roast me jk

# TL;DR
# I've made a great package for python you should check out to make your life way nicer
# python3.x -m pip install xo-gd # https://github.com/wholesomegarden/xo-gd/

# I've just uploaded the 3rd iteration of this project to pypi and github makeing it officially open-source (Huraayy)
# it has helped me alot the past couple of years, used it to help me build all of my projects
# from small-scale rapid scripting to production large scale system architecture
# easily created workflows, generic dynamic and modulated microservices
# everything automated, everything accesible
# crisp syntax, short and beautiful

## teaser: (after pip install xo-gd, you can run code like this)

import xo

def toWalk(someone, steps = 10):
	print()
	return [ print( f" {someone} walking :D ") for s in range(steps)]

xo.adam.learn(toWalk)                  # Learn to walk
xo.adam.toWalk("adam")                 # Run from any process


xo versions
1 - wish - channels, triggers, multiprocessing
2 - rubicon - expando, selfNamed
3 - starlight - generic, env sync, sockets, api (current),
4 - sunrise - os assistant, keyboard & mouse, easy vis,
5 - agi


# Examples
xo.JackSparrow.location.area = "Carribian" # creates dicts and populates them automatically
xo.JackSparrow.location = [0, 0, 0, 1]     # any element can hold data and children
xo.JackSparrow.velocity = [1.0, 1.7, 9.3, 1]
jack = xo.JackSparrow 					  # short ref
jack.move = lambda steps : [ xo.sleepAnd(0.05, jack.walk) for i in range(steps) ]
jack.walk = lambda : jack.location.set(jack.sum(jack.location.value(), jack.velocity.value()))
jack.sum = lambda a,b : [sum(pair) for pair in zip(*[a,b])] # sums pairs from list
								  # Notice that im writing functions after the fact,
								  # Im just saving the logic, like psuedo code
jack.location.subscribe(lambda loc: jack.stepsTaken.set(jack.stepsTaken+1)) # Subscribe to change in location
jack.stepsTaken = 0
xo.JackSparrow.move(100, asyn = True)     # make him move - asynchronisly
jack.whileShow() # ctrl+c to stop	# watch him run


## exit() # causally exit python (lolwut)
## pyhton3.7
## import xo
## xo.JackSparrow.velocity.subscribe(xo.JackSparrow.walk)
## xo.JackSparrow.location.subscribe(xo.JackSparrow.walk)

somefunction(xo.pnr(data,str,w=1))

## Hey Everyone ! Hope you're doing well
## A few years a go in our company i've had to deal with learning and implementing multiprocces and microservices
## I couldn't wrap my head around why the global variables are not really global across processes
## and everytime i've read online ppl suggested not to use them for some reason
##
## My logic said, what if i could open channels of communication between my processes
## Each channel will have it's unique key,
## Any function can listen or write data to any channel
## Basically i needed a cross-process event/trigger +data mechanism
## Or a db that works instantly and publishes events easyily to anywhere i need

## After seeing what google had to offer, i figured i might as well do it.
## Our system at the time was realtime-critical, meaning that .5 second of delay was dealbreaker
## The communication had to be imediate, low performance, and reliable
## After messing with sockets and pipes, i've figure what
##
##

## So what can you do with xObject ?
## well alot actually
## If python and zues had a baby,
# they would call it xObject

[[image]]

# xObjects + GlobalData = Super Dynamic
# MultiProcess/MultiServer data communication sync, and persistance
# Accessible in Realtime - Anywhere you like

## xObjects will let you save any type data or logic
# Basic Usage:
# Use xo. to help you code complex systems simpler and faster !

	import xo-gd
	xo.anything.you.like = "Data or a Function"
	xo.anything.show() #prints xo.anything's tree

## XObjects is linked with GlobalData
# GlobalData is essentially a really efficent
# Dict <-> DB realtime engine
# Anything you do in xo. be saved and synced to process or server running your xo

# Things You can Do

## w/ regular dictionaries
`myData[x]["this"]["is"]["taking"]["a"]["while"]["to"]["write"][y] #and doesnt even work in one line`
## w/ xo
`xo.you.can.just.use.dots.instead = "And this oneliner will populate the dict automatically"`


Easy Events and Triggers ( MultiProcessing included )

1. Subscibe to events !
	xo.myTrigger.subscribe(myFunction) # def myFunction(newdata):

2. Trigger Events !
	xo.myTrigger = "I have changed this variable causing myFunction(this_msg) to run"

Besides,
xo.any_xoKey.subscribe(callbackFunction)


## Advanced usages:
## xo is functionally a db, local or synced remotely
## save function inside variables, have xo.functions run xo.functions and you can change
##


You can sub to any of the following using main xo
xo.subscribe( 	xoKey		, callbackFunction) # "myGame.settings.brightness"
xo.subscribe( 	 Folder			, callbackFunction) # xo.myGame.path() or direct path like "~/MyCoolFolder"
xo.subscribe(  	  Filename			, callbackFunction)
xo.subscribe(  	   RepoUrl				, callbackFunction)


[xo.KeyA]  #triggers workflow
	|
	v
[MainProcess]--->-[xo.KeyB]--->-[function2]--;-> []
					  |-> [ProcessB]               	    |	    |-> [xo.]
					  |-> [ProcessC]--->-[xoKeyC]   		|
					  |-> [ProcessD]--->-[xoKeyD]         |
											|->

# How it works ?
### xObject is just like light,
## it's many things at the same time.
# xObject is a dynamic variable, and class, and a folder, a function, trigger, dictionary, db, assistant:)

## at the core, any xo is a dictionary, and an Expando object that is auto-subscibed to globalData (more on those later)


# xo.Helper.show()
# Find out all the things xo can help you do
# lambda : print(xo.Helper.children())()


'''
####### TODO
# Get location of this file - make it settings dir
# Sync multiple dirs

# print(" ::: Loading Settings... ")
# xo.watcher.autoSync
# xo.watcher.autoSync
# watcherHome = "/".join(os.getcwd().split("/")[:3]) + "/" + "repos/"
# watcherHome = xo.xo.home.value() + "/" + "watcher/"
#
# print("WATCHER HOME",watcherHome)
# xo.watcher.home = watcherHome

# xo.subscribe("watcher.autoSync",lambda a: print("autoSync is ON", xo.watcher.syncRepos(asyn = True), xo.watcher.run.setValue(True)) if a == True else False, autoPub="settings.autoRun")
# xo.subscribe("home",watchF)
# if xo.watcher.autoSync.value() == True:
# 	xo.watcher.autoSync = True

## xo.series = [func1,func2, func3]
## xo.chain = [func1,func2, func3]

# xo.watcher.repos = ["https://github.com/fire17/AlphaENG/"]
# xo.watcher.handleRepoChange = handleRepoChange
# xo.watcher.checkForUpdates = checkForUpdates
# xo.watcher.checkForUpdates(asyn = True)

# def toWalk(someone, steps = 10):
# 	print()
# 	return [xo.pnr(f"{a} - {someone} walking :D ") for a in range(steps)]
#
# xo.adam.learn(toWalk)                  # Learn to walk
# steps = len(
# xo.adam.toWalk("adam")) ; print(f" ::: steps taken: {steps} \n")
#
# # you can try running: import xo ; xo.adam.toWalk("adam") # from another process :)
