

# How to setup GlobalData & XObject
''

from gd import *

#myobj = xo.myobj
x = xo.x                  # this will create a xobject object named "x"

x.anything = "anything"   # x's children can be given any value
x.show()                  # shows x's contents

def foo(bar):
    return bar + 10

x.foo = foo               # x's children can be functions !
x.foo = lambda a : a+10   # or lambdas :D

#call functions
x.foo(123)
#call functions ASYNC in another thread
x.foo(123, asyn = True)

#get or set elements by path  
xo._get("path.to.element")
xo._getValue("path.to.element")
xo._setValue("path.to.element", 123)


# iterate over children:
for kid in x.children(): # .children() returns a list
    print(kid)

counter = 0
for kid in x.kids():     # .kids() yield returns (lazy-good)
    kid(counter)         # calls functions like foo
    counter += 1


# Subscribe and AutoPublish
xo.subscribe("xo.element.id", callbackFunction)
xo.subscribe("xo.element.id", callbackFunction, autoPublish = [publishResultFuncA, publishResultFuncB])
>>>
>>>

################################### CODE EXAMPLE!

## XObject: Real Dynamic Coding (using ExpandoObject and more!)
______________________________
# After you import gd-xo you can use **xo.** prefix to create special xobjects
# XObjects automaticly grow as you fill them - so you can do alot in every line

# store data in dict-like structure
xo.foo.settings.brightness = 87

# set and store functions
xo.foo.bar.functions.dim = lambda bright : xo._setValue("foo.settings.brightness",bright)

# subscribe to variable changes and trigger processes subscribe(elementID, callFunction)
xo.subscribe("foo.trigger", xo.foo.bar.functions.dim)
xo.foo.trigger = 55 # will trigger dim(bright=55) and change the brightness to 55

# quick flag to run async in another thread (asyn = True)
def watch():
    c = 0
    while(xo.foo.run == True):
        print("    Brightness =", xo.foo.settings.brightness.value(),"                    ",end="\r")
        time.sleep(0.01); c+=1
    print("    Done Watching                 ")

def stopAfter(t):
    t0 = time.time()
    while(time.time()-t0 < t):
        pass # wait for timeout
    xo.foo.run = False

def change():
    while(xo.foo.run == True):
        move = random.choice([-1,1])
        xo.foo.settings.brightness += move
        if xo.foo.settings.brightness > 100: xo.foo.settings.brightness = 100;
        if xo.foo.settings.brightness < 1: xo.foo.settings.brightness = 0;
        # time.sleep(0.01)

xo.watch, xo.stop, xo.change = watch, stopAfter, change
xo.foo.run = True
xo.change(asyn=True);
xo.watch(asyn=True);
xo.stop(5, asyn=True)



''

#TODO

#lambdas
#x.foo = lambda a: a + 10

#iterate naturally: check!
#for kid in x: #instead of x.kids() check!

#save functions check!
#better deletion

#set / show path

#child report changes to parent to trigger Subscribers

#xo._vars settings
#xo._helper = true
#xo._realtime = false
#xo._debug = false

#string addition "xxx"+xo.n.msg

#Set with dictionary
