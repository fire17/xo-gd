from .gd import *
import requests
import git
from git import Repo
# import fileWatch
from .xo import *

import builtins as __builtin__

# xo.working = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYEP"

'''
# PUB PAHO IN REQS
'''
####### Client
import paho.mqtt.client as mqtt
import dill as pk # import pickle as pk

# MQTT_BROKER_HOST = 'mqtt.eclipse.org'
# MQTT_BROKER_PORT = 1883
# MQTT_KEEP_ALIVE_INTERVAL = 60
# class MQTT(object):
def on_connect(client, userdata, flags, rc):
    # print()
    print(" ::: MQTT Subscribing To",xo.mqtt.settings.newSub.value())
    extra =  "(failed)"
    if rc == 0:
        extra =  "(success)"
    print(" ::: MQTT Connected with result code " + str(rc),extra)
    print()
    client.subscribe(xo.mqtt.settings.newSub.value())
    return rc == 0

# xo.mqtt.mainKey = "U(Y&Y*GN&(B6t097mTN(&^NT&(*))))"
# def sub(mqttChannel = None, func = lambda *args,**kw :xo.pnr([' ::: xo.mqtt INCOMMING !!! ',args,kw]), autoPub = "mqtt"):
def sub(mqttChannel = None, func = None, autoPub = "mqtt"):
    if func is None:
        func = lambda a, *aa, **aaa : [a,aa,aaa]

    server = xo.mqtt.settings.server.value()
    port = xo.mqtt.settings.port.value()
    keepAlive = xo.mqtt.settings.keepAlive.value()
    try:
        # print(xo.settings)
        if mqttChannel is None:
            mqttChannel = xo.mqtt.mainKey.value()

        if mqttChannel is None:
            print(" ::: Please set MQTT Main Key with xo.mqtt.mainKey = \"YourSecretChannel\"")
            return False
        xo.mqtt.settings.newSub = mqttChannel
        # print()
        xo.mqtt.settings[mqttChannel] = autoPub
        xo.subsc1ribe(autoPub,func)
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(server,port,keepAlive)
        # print("PPPPPPPPPPPPPPPPPPPPPPPP",server, port,keepAlive)
        # client.on_message = lambda *args,**kw: func(*args, **kw)
        client.loop_start()
        # print()
        # print(f" ::: Subsctibing To MQTT ::: {mqttChannel} ::: autoPub is {autoPub}")
        # print()
        # return True
    except :
        print()
        print(" ::: Exception while subscribing to MQTT, are you connected to the internet ?")
        print(f" ::: MQTT Server server = \"{server}\", port = {port} , keepAlive = {keepAlive}")
        print(f" ::: Connection Failed ::: to enable exeption prints use xo.settings.debug = True")
        if xo.settings.debug == True:
            print()
            traceback.print_exc()
        print()
        return None
    return True

#pub(package("AAAX", cmdDict = {"subscribe":"newValue","run":lambda a, *qa,**b:print(f" III new value is{xo.later}"), "saveAt":"newValue"}, yo = "YO YO"))
# xo.mqtt.skip.time = 1
def pub(data = None, mqttChannel = None, autoPackage = True, ping = False, *ar ,**kw):
    du = 'PID ' + str(os.getpid())
    if xo.mqtt.username.value() is not None:
        du = xo.mqtt.username.value()
    if data is None:
        data =f" @@@ Hello World! from {du}"
    msg = data
    if ping:
        data =f" @@@ Ping from {du}"
    if "bytes" not in str(type(data)) and autoPackage:
        data = package(data,*ar,**kw )
    if mqttChannel is None:
        mqttChannel = xo.mqtt.mainKey.value()
    kw["mqttChannel"] = mqttChannel

    if "silent" not in kw or kw["silent"] is not True:
        print(f" ::: Sending Data ::: {str(msg[:30])} ... to Channel \"{mqttChannel}\" ::: len(data) = {len(data)}\n")
    if xo.log.value() == True or True:
        xo.log += f"Sending data to \"{mqttChannel}\""
    client = mqtt.Client()
    client.connect(xo.mqtt.settings.server.value(), xo.mqtt.settings.port.value(), xo.mqtt.settings.keepAlive.value())
    # if mqttChannel in xo.mqtt.subscribed:
    #     xo.mqtt.skip += mqttChannel
    #     xo.mqtt.skip += mqttChannel
    username = str(os.getpid())
    if xo.mqtt.username.value() is not None:
        username = xo.mqtt.username.value()
    ##########
    final = [username,str(os.getpid()), kw, data]
    client.publish(mqttChannel, pk.dumps(final));
    client.loop_start()
    # client.disconnect();



# def cool():
#     print("COOOOOOOOOOOOOOL!")
#     xo.cool = "FUCK YEA"
#     xo.test()
#     return xo.pnr(" ...... last mqtt was"+str(xo.mqtt.value()))

# cmdDict = {"saveAt":"mqtt.incoming","run":lambda *args, **kw: print(f" ::: X Injected {[args,kw]}")},
def package(data, cmdDict = None, saveAt = None, run = None, subscribe = None,  *args, **kw):
    # if cmdDict is None:
    #     cmdDict = {"saveAt":"mqtt.incoming","run":lambda *args, **kw: print(f" ::: X Injected {[args,kw]}")},
    # print(f"!!!!!!!!!!,cmdDict{cmdDict}")
    pack = {}
    pack["cmdDict"] = cmdDict
    if pack["cmdDict"] is None or "dict" not in str(type(pack["cmdDict"])):
        pack["cmdDict"] = {}

    if saveAt is not None:
        pack["cmdDict"]["saveAt"] = saveAt
    if run is not None:
        pack["cmdDict"]["run"] = run
    if subscribe is not None:
        pack["cmdDict"]["subscribe"] = subscribe

    for k in kw:
        pack["cmdDict"][k] = kw[k]




    pack["data"] = data
    pack["args"] = args
    pack["kw"] = kw

    return pk.dumps(pack)

def on_message(client, userdata, msg):
    mqttChannel = msg.topic
    # print("USERDATA",userdata)
    msgData = {}
    for key in ["topic","payload","timestamp"]:
        msgData[key] = msg.__getattribute__(key)
    if "payload" in msgData:
        # user, payload = msgData["payload"]
        # print("!!!!!!!!!!!!!!!!!!!!!!!!", msgData["payload"])
        # print("!!!!!!!!!!!!!!!!!!!!!!!!", payload)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!", user)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!")
        # print("!!!!!!!!!!!!!!!!!!!!!!!!")
        # print("!!!!!!!!!!!!!!!!!!!!!!!!")
        user = "unknown"
        silent = False
        try: ## unpackaging msg
            user,pid,params, bin= unpackage(msg)
            if "silent" in params and params["silent"] == True:
                silent = True
            if str(pid) == str(os.getpid()):
                if not silent:
                    print(" ::: MQTT Message Published successfully ")
                    print()
                pass # SKIP self-sent message!
            else:
                if not silent:
                    print()
                    print(f" ::: Incoming New MQTT Message on Channel \"{msgData['topic']}\" :::")#" ::: From User {user}")
                # print()
                user,pid,params, data = unpackage(msg, body = True)
                msgData["payload"] = {"user":user,"data":data}
        except :
            if not silent:
                print()
                print(f" ::: Exception while unpackaging msg ::: Binary data was saved to xo.mqtt.{user}.bin")
                print(f" ::: To enable exeption prints use xo.settings.debug = True")
                print()
                if xo.settings.debug == True:
                    print()
                    traceback.print_exc()
                print()


        # print("UUUUUUUUUUUUUUUUUUUU",user)
        # print("UUUUUUUUUUUUUUUUUUUU",user)
        # print("UUUUUUUUUUUUUUUUUUUU",user)
        # print("UUUUUUUUUUUUUUUUUUUU",user)
    saveAt = xo.mqtt.settings[mqttChannel].value()
    xo.SetValue(saveAt, msgData)
    # print()
    # print(" ::: New MQTT Message ::: ")
    # print(f" ::: Msg Data :::",msgData["payload"],"::: saved to",saveAt)
    # print()

    # xo.res = [msg.payload]  # until i read the channel name then ; xo.mqtt.settings[]
    # print("::: MQTT Channel MSG A" + str(xo.res))
    # print("::: MQTT Channel MSG B" + str(msg.payload.decode()))
    # client.subsc1ribe(xo.mqtt.mainKey.value())
    # print("Message Recieved. ", msg.payload.decode())


def unpackage(msg, body = False):
    if "xo.obj" in str(type(msg)):
        msg = msg.value()

    if not body:
        return unpackageL1(msg)
    else:
        username, pid, params,bin = unpackageL1(msg)
        pid = str(pid)
        # username = user
        knownUser = False
        for c in xo.mqtt.users.children():
            if username == c:
                username = xo.mqtt.users[c].value()
                knownUser = True

        # if user in xo.mqtt.users.children():
        #     username = xo.mqtt.users[user].value()
        xo.mqtt[username].bin = bin
        display = str(username)
        if not knownUser:
            display = "User "+display
        elif str(pid) == str(display):
            username = xo.mqtt.users[pid].value()
            display = str(username)
        if "silent" not in params:
            print(f" ::: From {display} ::: len(data) is {len(bin)} ::: Binary saved to xo.{xo.mqtt[username].bin._id.replace('/','.')}")
        return [username, pid, params ,unpackageBody(bin)]


def unpackageL1(msg):
    if "xo.obj" in str(type(msg)):
            msg = msg.value()
    # print("ggggggg")
    # print("ffffff bin",bin)
    bin = msg.payload
    ob = pk.loads(bin)
    if "list" in str(type(ob)):
        user, pid, params, data = ob
        return user, pid, params, data
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@@@@@@@@")
        # print("@@@@@@@@@@@@@@@@@@@@@")
    return "???"

def unpackageBody(data):
    if "xo.obj" in str(type(data)):
        msg = msg.value()
    # print("ggggggg")
    bin = data
    # print("ffffff")
    ob = pk.loads(bin)
    # print("eeeeee")
    triggered = False
    if ob is not None and "dict" in str(type(ob)):
        # print("dddddd",ob)
        if "cmdDict" in ob:
            # print(type(xo.f.children()),"ccccccc",xo.f.children())
            # print("CCCCCCCCCCCCCCCCCC")
            # print()
            for key in ob["cmdDict"]:
                # print("KEY IS",key)
                # print("bbbbbb",key, key in xo.f.children())
                if key in xo.f.children():
                    # print(f" ::: ::: Running func {key}")
                    triggered = True
                    try:
                        xo.f[key]([ob["data"],ob["cmdDict"], ob["args"], ob["kw"]]) # runs function (packList)
                    except :
                        print()
                        print(f" ::: Exception while running func {key} from mqtt")
                        print(f" ::: To enable exeption prints use xo.settings.debug = True")
                        print()
                        if xo.settings.debug == True:
                            print()
                            traceback.print_exc()
                        print()
                    # change to append to xo.mqtt.updates
    if not triggered:
        print(f" ::: DATA ::: {ob['data']}")
    return ob



def saveAt(data, appenD = False):
    # print(" ::: Injected Save ::: ")
    data, cmdDict, args, kw = data
    correct = False
    if "saveAt" in cmdDict and cmdDict["saveAt"] is not None:
        print(f" ::: Save Request ::: {cmdDict['saveAt']} ::: {data}")
        if not appenD:
            xo.GetXO(cmdDict["saveAt"], allow_creation=True).set(data)
        else:
            o = xo.GetXO(cmdDict["saveAt"], allow_creation=True)
            o += data
        correct = True
    else:
        print(" ::: wwtf saveAt ::: ")
    print()
    return correct
xo.f.saveAt = saveAt

def appenD(data):
    # print(" ::: Injected Save ::: ")
    data, cmdDict, args, kw = data
    correct = False
    if "saveAt" in cmdDict and cmdDict["saveAt"] is not None:
        print(f" ::: Save Request ::: {cmdDict['saveAt']} ::: {data}")
        xo.GetXO(cmdDict["saveAt"], allow_creation=True).set(data)
        correct = True
    else:
        print(" ::: wwtf saveAt ::: ")
    print()
    return correct

xo.f.append = appenD

def subscribe(data):
    # print(" ::: Injected Subscribe ::: ")
    correct = False
    data, cmdDict, args, kw = data
    print()
    print(f" ::: Subscribe Request ::: {cmdDict['subscribe']} ::: {data}")
    if "subscribe" in cmdDict and cmdDict["subscribe"] is not None:
        f = lambda *a,**b: print(f" ::: Subscribed to {cmdDict['subscribe']} with Injection ::: ")
        if "run" in cmdDict and cmdDict["run"] is not None and "func" in str(type(cmdDict["run"])):
            f = cmdDict["run"]
        xo.subscribe(cmdDict["subscribe"],f)
        correct = True
    else:
        print(" ::: wwtf subscribe ::: ")
    return correct

# print("AAAAAAAAAAAA")
xo.f.subscribe = subscribe

def listen(data):
    # print(" ::: Injected Subscribe ::: ")
    correct = False
    data, cmdDict, args, kw = data
    print()
    print(f" ::: Subscribe To MQTT Request ::: {cmdDict['listen']} ::: {data}")
    if "listen" in cmdDict and cmdDict["listen"] is not None:
        channel = cmdDict["listen"]
        f = None
        if "run" in cmdDict and cmdDict["run"] is not None and "func" in str(type(cmdDict["run"])):
            f = cmdDict["run"]
            print(f" ::: Subscribing to MQTT Channel \"{channel}\" With Function {f}")

        autoPub = "mqtt.res"
        if "saveAt" in cmdDict and cmdDict["saveAt"] is not None:# and "func" in str(type(cmdDict["run"])):
            autoPub = cmdDict["saveAt"]
            print(f" ::: MQTT Channel \"{channel}\" will be saved at {autoPub}")

        sub(channel, f, autoPub)
        correct = True
    else:
        print(" ::: wwtf subscribe ::: ")
    return correct

# print("AAAAAAAAAAAA")
xo.f.listen = listen

def run(data):
    data, cmdDict, args, kw = data
    if not ("silent" in kw and kw["silent"] is True):
        print()
        print(f" ::: Run Request ::: {cmdDict['run']} ::: {data}, ", )
    else: # silent
        pass # does not print
        # print("@@@@@@@@@@@@@@@@@@@@")
        # print(kw)
        # print("@@@@@@@@@@@@@@@@@@@@")

    correct = False
    # f = lambda *a,**b: print(f" ::: Subscribed to {cmdDict["subscribe"]} with Injection ::: ")
    if "run" in cmdDict and cmdDict["run"] is not None and "func" in str(type(cmdDict["run"])):
        f = cmdDict["run"]
        nA = [data]
        for a in args:
            nA.append(a)
        # list(args).append(data)
        correct = False
        f(data, *args, **kw)
    else:
        print(" ::: wwtf run ::: ")
    return correct

xo.f.run = run

def chat():
    print()
    print(f" ::: Entering chat \"{xo.mqtt.mainKey.value()}\"","\n ::: Type your message and press enter to send\n ::: exit() or Ctrl+C to leave\n")
    stop = False
    username = str(os.getpid())
    if xo.mqtt.username.value() is not None:
        username = xo.mqtt.username.value()
    while(not stop):
        try:

            # print("                                                          \n                                                            "
            # +"\n ("+username+"): ",end='')
            print("                                    "#"                                                          \n                                                            "
            +"\n ("+username+"): ",end='')
            res = input()
            print(chr(27)+"[1A"+"\033[F"+f" ::: {username} : {res}")
            if res is "exit" or res is "exit()":
                stop = True
            else:
                xo.msg(res, chat = True, prev = chr(27)+"[2A\n"+"",after = chr(27)+"[1A\n\n")
                # xo.msg(res, chat = True, prev = chr(27)+"[2A\033[F"+"\033[F"+"\033[F\n\n\n")
                # xo.msg(res, chat = True, prev = "")
        except:
            traceback.print_exc()
            stop = True
xo.chat = chat

def ping(msg = "hello from the other side", data = None, *ar, **kw):
    xo.pub(ping = True, run = lambda *a,**aa:xo.pub("hello from the other side"))

xo.ping = ping

def _remoteCMD(cmd, *ar, **kw):
    xo.pub(ping = True, run = lambda *a,**aa:xo.cmd(cmd))

xo._remoteCMD = _remoteCMD

def msg(msg = "", title = None, *ar, **kw):
    username = str(os.getpid())
    if xo.mqtt.username.value() is not None:
        username = xo.mqtt.username.value()
    if not title:
        title = "Msg from "+username+" ::: "
    prev,after = "",""
    if "chat" in kw:
        if "prev" in kw:
            prev = kw["prev"]
        if "after" in kw:
            after = kw["after"]
            # print("pppppppppppppppppppp")
    xo.pub(data = title, run = lambda *a,**aa:xo.pnr(prev+f" ::: {username}: "+msg+after), silent = True)

xo.msg = msg
# print("BBBBBBBBBb")

if xo.settings.auto == True:
    sub()
# print("ccccc")

# xo.mqtt.onconnect = on_connect
# # xo.mqtt.on_message = on_message
# mqtt = xo.mqtt
xo.a.b.c.d.e = 10
xo.pid = os.getpid
