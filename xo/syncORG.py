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
class MQTT(object):
    def on_connect(client, userdata, flags, rc):
        print()
        print("::: MQTT Connected with result code " + str(rc))
        print("::: MQTT Subscribing To",xo.mqtt.settings.newSub.value())
        print()
        client.subscribe(xo.mqtt.settings.newSub.value())

    def on_message(client, userdata, msg):
        mqttChannel = msg.topic
        # print("USERDATA",userdata)
        msgData = {}
        for key in ["topic","payload","timestamp"]:
            msgData[key] = msg.__getattribute__(key)
        saveAt = xo.mqtt.settings[mqttChannel].value()
        xo.SetValue(saveAt, msgData)
        print()
        print(" ::: New MQTT Message ::: ")
        print(f" ::: Msg Data :::",msgData["payload"],"::: saved to",saveAt)
        print()

        # xo.res = [msg.payload]  # until i read the channel name then ; xo.mqtt.settings[]
        # print("::: MQTT Channel MSG A" + str(xo.res))
        # print("::: MQTT Channel MSG B" + str(msg.payload.decode()))
        # client.subsc1ribe(xo.mqtt.mainKey.value())
        # print("Message Recieved. ", msg.payload.decode())

    def subscribeMQTT(mqttChannel = None, func = lambda *args,**kw :xo.pnr([' ::: xo.mqtt INCOMMING !!! ',args,kw]), autoPub = "mqtt"):
        if mqttChannel is None:
            mqttChannel = xo.mqtt.mainKey.value()
        xo.mqtt.settings.newSub = mqttChannel
        print()
        xo.mqtt.settings[mqttChannel] = autoPub
        xo.subscribe(autoPub,func)
        client = mqtt.Client()
        client.on_connect = MQTT.on_connect
        client.on_message = MQTT.on_message
        client.connect(xo.mqtt.settings.server.value(), xo.mqtt.settings.port.value(), xo.mqtt.settings.keepAlive.value())
        # client.on_message = lambda *args,**kw: func(*args, **kw)
        client.loop_start()
        print()
        print(f" ::: Subsctibing To MQTT ::: {mqttChannel} ::: autoPub is {autoPub}")
        print()
        return True

    def publishMQTT(data, mqttChannel = None):
        if mqttChannel is None:
            mqttChannel = xo.mqtt.mainKey.value()
        print("!!!!!!!!!!! SENDING,{data},{mqttChannel}")
        if xo.log.value() == True or True:
            xo.log += f"Sending {data} to {mqttChannel}"
        client = mqtt.Client()
        client.connect(xo.mqtt.settings.server.value(), xo.mqtt.settings.port.value(), xo.mqtt.settings.keepAlive.value())
        client.publish(mqttChannel, data);
        client.loop_start()
        # client.disconnect();

    # def cool():
    #     print("COOOOOOOOOOOOOOL!")
    #     xo.cool = "FUCK YEA"
    #     xo.test()
    #     return xo.pnr(" ...... last mqtt was"+str(xo.mqtt.value()))


    def package(data, cmdDict = {"saveAt":"mqtt.incoming","run":lambda *args, **kw: print(f" ::: X Injected {[args,kw]}")},  *args, **kw):
        pack = {}
        pack["data"] = data
        pack["cmdDict"] = cmdDict
        pack["args"] = args
        pack["kw"] = kw

        return pk.dumps(pack)


    def unpackage(msg):
        bin = msg["payload"]
        ob = pk.loads(bin)
        if ob is not None and "dict" in str(type(ob)):
            if "cmdData" in ob:
                for key in ob:
                    if key in xo.f.children():
                        xo.f[key]([data,cmdDict, args, kw]) # runs function (packList)
                        # change to append to xo.mqtt.updates


def saveAt(data):
    print(" ::: Injected Save ::: ")
    data, cmdDict, args, kw = data
    correct = False
    if "saveAt" in cmdDict and cmdDict["saveAt"] is not None:
        xo.GetXO(cmdDict["saveAt"], allow_creation=True).set(data)
        correct = True
    else:
        print(" ::: wwtf saveAt ::: ")
    print(f" ::: Injected Saving ({correct}) ::: {cmdDict['saveAt']} ::: {data}")
    return correct

xo.f.saveAt = saveAt

def subscribe():
    print(" ::: Injected Subscribe ::: ")
    correct = False
    data, cmdDict, args, kw = data
    if "subscribe" in cmdDict and cmdDict["subscribe"] is not None:
        f = lambda *a,**b: print(f" ::: Subscribed to {cmdDict['subscribe']} with Injection ::: ")
        if "run" in cmdDict and cmdDict["run"] is not None and "func" in str(type(cmdDict["run"])):
            f = cmdDict["run"]
        xo.subscribe(cmdDict["subscribe"],f)
        correct = True
    else:
        print(" ::: wwtf subscribe ::: ")
    print(f" ::: Injected Subscribing ::: {cmdDict['subscribe']} ::: {data}")
    return correct

print("AAAAAAAAAAAA")
xo.f.subscribe = subscribe

def run():
    print(" ::: Injected Running ::: ")
    data, cmdDict, args, kw = data
    correct = False
    # f = lambda *a,**b: print(f" ::: Subscribed to {cmdDict["subscribe"]} with Injection ::: ")
    if "run" in cmdDict and cmdDict["run"] is not None and "func" in str(type(cmdDict["run"])):
        f = cmdDict["run"]
        args.append(data)
        correct = False
        f(*args, **kw)
    else:
        print(" ::: wwtf run ::: ")
    print(f" ::: Injected Running ::: {cmdDict['run']} ::: {data}")
    return correct

print("BBBBBBBBBb")
xo.f.run = run
print("ccccc")

# xo.mqtt.onconnect = on_connect
# # xo.mqtt.on_message = on_message
# mqtt = xo.mqtt
# xo.a.b.c.d.e = 5



# xo.settings = "Here we save Settings"
# xo.mqtt.settings.server = "broker.hivemq.com"
# xo.mqtt.settings.port = 1883
# xo.mqtt.settings.keepAlive = 60
# xo.mqtt.mainKey = "U(Y&Y*GN&(B6t097mTN(&^NT&(*))))"
