####ok.py

#### from new import *

import time
import dill as pk # import pickle as pk
import glob
import traceback
from threading import Thread
import os.path as PATH
import os
import re
import json

from .fileWatch import *
# print(" ::: imported xo successfully ")


class SelfNamed(object):
	"""docstring for SelfNamed."""
	__id = "xxx"
	_languageDefaults = ["value","_val","getattr","show","_id","__dict__"]
	def __init__(self, id = None):
		super().__init__()
		pass #print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
		self.__id = id
		#### self.arg = arg

	def __setattr__(self, name, value):
		pass #printx("EEEEEEEEEEEEEEEEEEEE---1")


	def __assign__(self, v):
		pass #print('called with %s' % v)





class Expando(SelfNamed):
	"""docstring for Expando."""


	__id = "xxx"
	#### def __init__(self, val, id = None):
	#### 	super().__init__(id = id)
	#### 	self.__id = id


#### 	def __init__(self, val = "__17__", id = None, **entries):####, wrapper = False, main = True):
#### #### ####expando.py
#### #### 		#### def __init__(self):
#### #### 		#### es=traceback.extract_stack()
#### #### 		super().__init__(id = id)
#### #### 		self.name = self.GetName()
#### #### 		self.__dict__.update(entries)
#### #### 		self.__validID_ = False
#### #### 		#### global GD
#### #### 		#### self.xxx = self.get_my_name()
#### #### 		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
#### 		super().__init__(id = id)
####
#### 		exist = True
#### 		'''
#### 		birth = str(time.time())
#### 		if id is None:
#### 			id = birth
#### 		'''
####
#### 		#### self.__main__ = main
#### 		self.__id__ = "hidden"
#### 		self.__dict__.pop("__id__")
#### 		self._val = val
#### 		print("obj created! =",self._val)
#### 		#### self._zzz = 5
####
####
####
####
#### 		#### print("******---",self.get_my_name())
#### 		#### self["_id"] = self.get_my_name()[0]
####
#### 		#### self.xxx.yyy.zzz = 13
#### 		#### updateID = Thread(target = self.makeID, args = [list,])
#### 		#### updateID.start()
####
#### 		print("AAAAAAAAAAA	AAA",entries,self.__name__)
#### 		for arg_name in entries:
#### 			print("AAAAAAAAAAAAA",arg_name)

	def tree(self):
		for a in self.__dict__:
			if not a.startswith("_") and a not in SelfNamed._languageDefaults:
				yield self[a]
				if self[a] != None:
					for z in self[a].tree():
						yield z

	def subscribe(self, func = None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
		if func is None:
			func = lambda a, *aa, **aaa : [a,aa,aaa]
			withID = True
		channel = self._id.replace(".","/")
		# print("CCCCCCCCCCCCCCCCCC",channel)
		return xo.subscribe(channel, func=func, autoPub = autoPub, block = block, once= once, echo=echo, debug = debug, withID = withID)

	def fill(self, inputs):
		index = {}
		for z in self.tree():
			if z._name in inputs:
				inputs.remove(z._name)
				print("enter",z._name+": ")
				if "/" in z._id:
					si = len(self._id)
					index[z._id[si:]] = input()
		for a in index.keys():
			self[a] = index[a]
		print("\nDONE")

	def kids(self):

				for a in self.__dict__:
					if not a.startswith("_") and a not in SelfNamed._languageDefaults:
						yield self[a]



	def children(self):
		# childs = []
		childs = {}
		for a in self.__dict__:
			if not a.startswith("_") and a not in SelfNamed._languageDefaults:
				# childs.append(self[a])
				childs[a]=self[a]
		return childs

	def __init__(self, val = None, id = None, main = True, **entries):####, wrapper = False, main = True):
	####expando.py
		#### def __init__(self):
		#### es=traceback.extract_stack()
		super().__init__(id = id)
		pass #print("PPPPPPPPPPPPPP", id)
		#### self.name = self.GetName()

		self.__dict__.update(entries)
		self._name = id.split("/")[-1]
		self._id = id
		#### self.__validID_ = False
		#### global GD
		#### self.xxx = self.get_my_name()
		#### print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
		exist = True
		'''
		birth = str(time.time())
		if id is None:
			id = birth
		'''

		#### self.__main__ = main
		self.__id__ = "hidden"
		self.__dict__.pop("__id__")
		self._val = val
		# print("obj created! =",self._val)
		self._zzz = 5
		#### print("******---",self.get_my_name())
		#### self["_id"] = self.get_my_name()[0]

		#### self.xxx.yyy.zzz = 13
		#### updateID = Thread(target = self.makeID, args = [list,])
		#### updateID.start()

		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
		for arg_name in entries:
			pass #print("AAAAAAAAAAAAA",arg_name)

	def __hash__(self):
		pass #print(hash(str(self)))
		return hash(str(self))

	def getID(self):
		return self.__id__


	def __set__(self, key, val):
		pass
		# print("eeeeeeeeeeeeeeeeeeeee")
		self.__dict__[key] = val
		return True

	def __get__(self,key):
		pass
		# print("eeeeeeeeeeeeeeeeeeeeeaaa")
		return self.__dict__[key]



	def __setattr__(self, name, value):
		pass ## print("EEEEEEEEEEEEEEEEEEEE1")
		if "str" not in str(type(name)):
			name = str(name)
		if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults:#### and "__skip" in self.__dict__ and name not in self.skip:
			if "xo.obj" not in str(type(value)):
				pass ## print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass ## print("2222222222")
					# print("ppp33333",self._id)
					# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
					self[name] = obj(id = self._id+"/"+name, val= value, parent = self)
				else:
					pass ## print("33333333")
					#### self.__set__(name,value)
					manager.save(channel = self._id+"/"+name, data=value)
					#### self.save(id = self._id+"/"+name, val= value)
			else:
				pass ## print("44444")
				self.__dict__[name] = value

		else:
			pass ## print("555555555")
			self.__dict__[name] = value

	def __getitem__(self, name):
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr

		if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults and name not in self.__dict__:
			# print("ppp44444")
			self.__dict__[name] = obj(id = self._id+"/"+name, parent = self)

		if name in self.__dict__:
			#### print("FUUCKKKKKKKKKKKKKKKKKKKKKk")

			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr




	def __assign__(self, v):
		pass #print('called with %s' % v)

	def __setitem__(self, name, value):
		pass #print("iiiiiiiiiiiiiiiiioooooooo")
		if "str" not in str(type(name)):
			name = str(name)
		if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults:#### and "__skip" in self.__dict__ and name not in self.skip:
			pass #print("VVVVVVVV",str(type(value)))
			if "xo.obj" not in str(type(value)):
				pass #print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass #print("1",name)
					# print("ppp5555",self)
					self.__dict__[name] = obj(id = self._id+"/"+name, val = value, parent = self)
				else:
					pass #print("2",name)
					self[name].set(value)
			else:
				pass #print("22222222222222222222222",name,value)
				self.__dict__[name] = value
				pass #print("YESSSSSSSSS",	self.__dict__[name])
		else:
			pass #print("3",name)
			self.__dict__[name] = value

		#### print("FINISHED SETTING ITEM", self.__dict__)

	def __getattribute__(self, name, loop = True):
		# print("NAME:",name)
		# time.sleep(0.1)
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr
		atr = object.__getattribute__(self, name)
		return atr
	def __getattr__(self, name, loop = True):
		pass #print("getttt")
		if "str" not in str(type(name)):
			name = str(name)
		#### return name
		if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults and name not in self.__dict__:
			pass #print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			pass #print("aaaaaaaaaaaaaa")
			# print("ppp66666",self)
			self[name] = obj(id = self._id+"/"+name, parent = self)
		if name in self.__dict__:
			pass #print("bbbbbbbbbbbbbbb")
			atr = object.__getattribute__(self, name)

			return atr
		#### return 13
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

	def set(self, val):
		self._val = val

	def __getstate__(self):
		pass #print ("I'm being pickled")
		pass #print(self.__dict__)
		pass #print()
		return False

	def __setstate__(self, d):
		pass #pprint ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		#### self._val *= 3

	def __repr__(self):
		justShow = True
		if justShow:
			self.show(ret = False)
			print()
		# print("where are we ?")
		recursiveDict = False
		if self._val is None:
			self._val = [[]]
		ret = "{xobject "+str({str(self._name):self._val[0]})[1:-1]+f" ::: children({len(self.children())})"
		childs = []
		if self.children() is not None and len(self.children()) > 0:
			if recursiveDict: #TODO DICT XXX
				ret += f" ::: {self.children()}"
			else:
				for c in self.children():
					# print("CCCCC",c)
					childs.append(c)
				ret += ":"+str(childs)
		ret +="}"
		return ret
		#
		# return str({"_val":self._val})
		# return str(self._val)+", "+str(self.__dict__)
		# return str([self._val, self.__dict__])
	def __ge__(self,other):
		if self.__isObj(other):
			return self._val[0] >= other._val[0]
		return self._val[0] >= other
	def __gt__(self,other):
		if self.__isObj(other):
			return self._val[0] > other._val[0]
		return self._val[0] > other
	def __le__(self,other):
		if self.__isObj(other):
			return self._val[0] <= other._val[0]
		return self._val[0] <= other
	def __lt__(self,other):
		if self.__isObj(other):
			return self._val[0] < other._val[0]
		return self._val[0] < other


	def __str__(self):
		# print()
		return "{xobject "+str({str(self._name):self._val[0]})[1:]#[:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		# return str({"_val":self._val})
		# return str(self._val)
		# return str(self.__get__())

	def __is__(self, other):
		return self.__eq__(other)

	#### by value of main
	def __eq__(self, other):
		if "bool" in str(type(other)) and ("bool" in str(type(self._val)) or (self._val is not None and ("dict" in str(type(self._val[0])) or "dict" in str(type(self._val[0])) )and len(self._val) > 0 and "bool" in str(type(self._val[0])))):
			return self._val[0] == other
		if self.__isObj(other):
			return self._val[0] == other._val[0]
		elif "str" in str(type(other)):
			return str(self._val[0]) == other
		return self._val[0] == other

	def __iter__(self):
		# print("ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
		return self.kids()

	def __add__(self, other):
		#### print("!!!!!!!!!")
		#### print(type(other))
		#### print()

		#list append overrull
		if self._val == None:
			self._val = [[]]
		if len(self._val) == 0:
			self._val[0].append(other)
			return self._val[0]
		if str(type(other)) != str(type(self._val[0])):
			if "list" not in str(type(other)):
				other = [other]
			if "list" not in str(type(self._val[0])):
				self._val[0] = [self._val[0]]

		if other is None and (self._val is None or self._val[0] is None):
			return None
		if self.__isObj(other):
			return self._val[0] + other._val[0]
		elif "str" in str(type(other)):
			return str(self._val[0]) + other
		if self._val[0] is None:
			if "list" in str(type(other)):
				return 	other
			return []
		if other is None:
			other = []
			return 	self._val + other
		if "list" in str(type(other)):
			if "list" in str(type(self._val[0])):
				return self._val[0] + other
			return 	self._val + other
		return self._val[0] + other

	def __radd__(self,other):
		return self.__add__(other)

	def __rsub__(self,other):
		pass ## print(type(other))
		pass ## print()
		if self.__isObj(other):
			return other._val[0] - self._val[0]
		elif "str" in str(type(other)):
			# print("::::::::::::::xxxx:::::::::")
			return other - str(self._val[0])
		return other - self._val[0]

	def __pos__(self, other):
		#### # print("!!!!!!!!!")
		#### # print(type(other))
		#### # print()
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val + other

	def __sub__(self, other):
		#### print("!!!!!!!!!")
		pass #print(type(other))
		pass #print()
		if self.__isObj(other):
			return self._val[0] - other._val[0]
		elif "str" in str(type(other)):
			pass #print("::::::::::::::xxxx:::::::::")
			return str(self._val[0]) - other
		return self._val[0] - other

	def __neg__(self, other):
		#### print("!!!!!!!!!")
		#### print(type(other))
		#### print()
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return self._val + other

	def __isObj(self, o):
		#### print("################################################################################################################",str(type(o)))
		#### time.sleep(100)
		pass #print("@@@@@@@@@@@@@@@@@@@@@@asdasdasd")
		return "xo.obj" in str(type(o))


	def _inThread(self, data):
		target, vars, kwargs = data
		print(" ::: Running Async Thread ::: ",target.__name__,"::: with params:\n :::",vars,str(kwargs).replace("'","").replace("}","").replace(":","=").replace("{",""))
		print()
		return target(*vars,**kwargs)

	def _startThread(self, target, vars, kwargs, ):
		sT = Thread(target = self._inThread, args = [[target, vars, kwargs]])
		sT.start()

	def __call__(self, *vars, **kwargs):

		# for a in vars:
		# 	print(type(a),"AAAAAAAAAAAAAAA,", a)
		# for a in kwargs:
		# 	print(type(kwargs),type(a),"KKKKKKKKK,", a,"=", kwargs[a])
		# print(type(vars),type(*vars),"xxxxxxxxAAAAAAAAAAAAAAA,", vars)

		if self._id.endswith("learn"):
			newDict = {}
			appendToLearn = []
			for f in vars:
				if f is not None and "function" in str(type(f)):
					ap = str(f).split(' ')[1]
					newDict[ap] = f
				elif "list" in str(type(f)):
					for ff in f:
						if ff is not None and "function" in str(type(ff)):
							ap = str(f).split(' ')[1]
							newDict[ap] = ff
				elif "dict" in str(type(f)):
					for fkey in f:
						if f[fkey] is not None:
							newDict[fkey] = f[fkey]
				else:
					appendToLearn.append(f)


			selff = xo.GetXO(self._id)

			# print( f"Learning new trick {self}{str(self._id+" ").split(" ")[1] } yo")
			owner = "/".join(self._id.split("/")[:-1])+"/"

			for key in newDict:
				# print(owner,",,,",key)
				v = newDict[key]
				if "function" in str(type(v)):
					print( f" ::: Learning new trick {owner.strip('/')}.{key} :D")
				else: #"function" in str(type(v)):
					# print( f" ::: New Element xo.{self._id.replace('/','.')}.{	key} = {v}")
					print( f" ::: New Element xo.{owner.strip('/')}.{	key} = {v}")
				self._parent[key] = v
				# print("SSSSSSSSSSSS",owner+key)

				# print(xo.GetXO(owner)+key, v,retXO=True)
			for a in appendToLearn:
				if self._parent is not None:
					self._parent.learned+=[a]
				else:
					print(" ::: WTF")
					self.value(ref=True).append(a)
				print( f" ::: New Element xo.{owner.strip('/')}.learned = {a}")

			return xo.GetXO(owner)
			# print(vars)
			# print(".....")
			# print(kwargs)
		# print(":::::::::::::::::::::::",)
		# for v in vars:
		# 	print(v)
		retXO = False
		if "function" in str(type(self._val)):
			# print("!!!!!!!!!!#####",str(type(self._val)))
			return self._val(*vars, **kwargs )
		elif self._val is not None and len(self._val)>0 and "function" in str(type(self._val[0])):
			# print("!!!!!!!!!![0]")
			if "asyn" in kwargs and kwargs["asyn"] == True:
				xkwargs = {}
				for a in kwargs:
					if (a is not "asyn" or "asyn" in self._id) and "retxo" not in a.lower():
						xkwargs[a] = kwargs[a]
					elif "retxo" in a.lower():
						retXO = True
				if not retXO:
					return self._startThread(self._val[0], vars, xkwargs)
				else:
					self._startThread(self._val[0], vars, xkwargs)
					return self
			if not retXO:
				return self._val[0](*vars, **kwargs)
			else:
				self._val[0](*vars, **kwargs)
				return self


		# print(" XXX CCC",self._id, self._val)
		if not retXO:
			if self._val is not None and ("ref" not in kwargs or kwargs["ref"] is not True):
				if "list" in str(type(self._val)) and len(self._val) == 1:
					return self._val[0]
			return self._val
			# return self._val[0](*vars, **kwargs)
		else:
			return self._val
			# self._val[0](*vars, **kwargs)
			# return self
		# print(":::::::::::::::::::::::")



	def show(self,t = "    ",count = 0, inLoop = False, ret = False):
		#### print("ssssssssssssssss..............")
		s = ""
		#### print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s
		tab = ""
		for i in range(count):
			tab+=t

		retList = []
		res = []
		p = tab+p
		if ret:
			retList.append(p)
		else:
			print(p.replace("\t","    "))
		for a in self.__dict__:
			# if "_" not in a:
			if not a.startswith("_"):
				if "xo.obj" in str(type(self.__dict__[a])):
					if ret:
						res = self.__dict__[a].show(count= count+1, ret = ret)
					else:
						self.__dict__[a].show(count= count+1, ret = ret)
		if count is 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

		if ret:
			if count == 0:
				return str(retList + res)
			return retList +["\n"]+ res

	def show0(self,t = "    ",count = 0, inLoop = False):
		#### print("ssssssssssssssss..............")
		s = ""
		#### print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s
		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p.replace("\t","    "))
		for a in self.__dict__:
			# if "_" not in a:
			if not a.startswith("_"):
				if "xo.obj" in str(type(self.__dict__[a])):
					self.__dict__[a].show(count= count+1)
		if count is 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

	def showMag(self,t = "    ",count = 0):
		return self.show(t=t,count = count)
		## print("ssssssssssssssss..............")
		s = ""
		## print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"


		if "list" in str(type(self._val[0])):

			fullid = ""
			for i in self._id.split("/")[1:]:
				fullid += i + " "
			fullid = fullid[:-1]
			#p = self._id.split("/")[-1] +" = "+ s+str(len(self._val[0]))+s + etab + str(self._val)
			p = fullid +"  = x"+ s+str(len(self._val[0])) + " times"
			l = len(p)%len(t)
			etab = ""
			for i in range((60 - len(t)*count) - len(p)):
				etab+=" "

			p += etab + "index: " + str(self._val)+s
		else:
			p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s

		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p)
		for a in self.__dict__:
			if "xo.obj" in str(type(self.__dict__[a])):
				self.__dict__[a].showMag(count= count+1)



class __objManager(object):
	"""docstring for objManager."""

	ExtKey = ""
	ExtKey = ""
	dir = ""
	channels = {}
	__id = "xxx"
	_checkCounter = 0
	_fin = False
	_shared = None
	_hasManager =  False

	def __init__(self, defaultDB = "main", **entries):
		global hasManager, Dir, ExtKey, ExtData, channels
		if hasManager:
			pass #print("FFFFFFFFFFFFFFFFFF")
			return None
		self._checkCounter = 0
		self._fin = False
		pass #print("New Manager!!")
		#### super(objManager, self).__init__()
		dbexist = PATH.exists(Dir)
		if not dbexist:
			os.makedirs(Dir)

		self.__dict__.update(entries)
		if defaultDB is not None and defaultDB is not "":
			if not defaultDB.endswith("/"):
				defaultDB+="/"
		self.dir = Dir+defaultDB
		# print("XO HOME",self.dir)
		self.ExtKey = ExtKey
		self.ExtData = ExtData
		self.channels = channels
		_shared = self
		_hasManager = True
		pass #print("VVVVVVVVVVVVVVVVVVV")
		#### self.__channelKeys = {}
		#### self.__channelValues = {}
		self.refreshChannels()

	def getXO(self, id):
		return self.ox(id=id)

	def refreshChannels(self):
		T = Thread(target=self.checkChannels, args=[self,])
		T.start()

	def checkChannels(self, data = [None,]):
		global channels, wait
		#### global _checkCounter
		if self._checkCounter > 1000000:
			self._checkCounter = 1
			pass #for i in range(100):
			pass #print("_checkCounter == 1000000")
		#### self = data[0]
		while True:

			# print("FFFFFFF")
			chKeys = channels.keys()
			cKeys = []
			discovery = False
			for k in chKeys:
				cKeys.append(k)
			for channel in cKeys:
				innerDirs = glob.glob(self.dir+channel+"/*/")
				for i in innerDirs:
					d = i[len(self.dir+channel)+1:-1]
					#### print("DDDDDDDDDD",d)
					if channel+"/"+d not in channels:
						self._fin = False
						discovery = True
						if channels[channel]["ref"] is not None and len(channels[channel]["ref"])>1:
							# print("DUPPPPPPPPPPPPPPPPPPPPPPPPPPPp", channel)
							pass
						if channels[channel]["ref"] is not None and len(channels[channel]["ref"])>0:
							# print("DUPPPPPPPPPPPPPPPPPPPPPPPPPPPpXxxx", channel)
							channels[channel]["ref"][0][0][d] = obj(id=channel+"/"+d, parent = self.getXO(channel))
							# print("0000000000000000000000000000000xxx")
						else:
							# print("DUPPPPPPPPPPPPPPPPPPPPPPPPPPPpZZZZ", channel)
							pass #print("XRRXRXRXRXRXrXR")
				# print("aaaaaaaaaaa")
				keyC = self.loadKey(channel)
				#### print("channel",channel)
				try:

					if keyC > channels[channel]["key"][0]:
						pass #print("!!!!!!! UPDATED",channel,key)
						self.setChannel(channel,keyC,self.loadData(channel))
					else:
						#### print("passed", channel, key)
						pass
				except:
					pass #print("XXXXXXXX",channel)
				# print("CCCCCCCCCCCCCCCCCCCC")

			if not discovery:
				self._fin = True
			else:
				pass
				# print("DDDDDDDDDDDDDDDD")


			time.sleep(wait)
			self._checkCounter += 1

	def setChannel(self, channel, key, value):
		global channels


		if channel in channels:
			channels[channel]["key"][0] = key

			# print (str(type(value)))
			# if "function" in str(type(value)):
			# 	print("!!!!!!!!!!@@@@@@@")
			# 	channels[channel]["_val"] = value
			# else: # enters [value]
			# 	if "list" not in str(type(channels[channel]["_val"])):
			# 		channels[channel]["_val"] = []
			# 	channels[channel]["_val"][0] = value

			channels[channel]["_val"][0] = value



	def getChannel(self, channel):
		global channels
		if channel not in channels:

			channels[channel] = {"key":[-1],"_val":[None], "ref":[]}
			#### channelsKeys[channel] = [-1]
			#### channelsBindings[channel] = value

			loaded = self.load(channel) ######## TODO: Create if not exist
			self.setChannel(channel, loaded["key"],  loaded["_val"])
			#### channels[channel]["key"][0] = loaded["key"]
			#### channels[channel]["_val"][0] = loaded["_val"]
		#### else:
		return channels[channel]


	def zero(self,c=1):
		return 0*c

	def setChannelRef(self, channel, ref = None):
		global channels
		if channel in channels:
			if ref is not None:
				if channels[channel]["ref"] is None:
					channels[channel]["ref"] = []
				channels[channel]["ref"].append(ref)
				pass #print("V V V V V V V V V VVVVVVVVVVVV VVVVVVVVVVV VVVVVVVVVVVVV",channel,channels[channel]["ref"] )
				#### while(len(channels[channel]["ref"])>1):
				#### 	first = channels[channel]["ref"][0]
				#### 	print("\n\nFIRST:::",repr(first))
				#### 	last = channels[channel]["ref"][-1]
				#### 	print("\n\nLAST::::",repr(last))
				#### 	last = first
				#### 	print("\n\nLAST2::::",repr(last))

	def bind(self, channel, value = None, ref = None):
		if channel is None:
			print("!!!!!!")
			return self.zero(12)/self.zero(1)

		# print("........")
		data = self.getChannel(channel)
		# print("........!!!!!!!")
		self.setChannelRef(channel, ref = ref)
		# print("........!!!!!!!!!!!!!!!!2")
		#### if value is None:
		#### 	value = [None]

		#### else:
		#### 	#### prev = self.get(channel)
		#### 	if value[0] is None:
		#### 		prev = self.getValue(channel)
		#### 		value[0] = prev[0]
		#### 	else:
		#### 		self.save(channel, value)

		# print("........!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
		if value is not None:
			#### value[0] = self.getValue(channel)
			self.save(channel, value)

		# print("........!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!0")
		return data["_val"] #### BINDED! [var]


	def loadAbs(self, filename):
		#### run = True
		#### untilTrue = False
		if not PATH.exists(filename):
			#### print("filename",filename, "doesn't exist")
			return None

		try:
			data = None
			with open(filename,"rb") as file:
				return pk.load(file)
				####self.printF("loaded",data, "from",filename)
			return data
		except:
			pass
			#### if untilTrue:
			#### 	self.printF("ERR - Try again, loading",filename)
			#### 	time.sleep(0.1)
			#### 	self.load(filename)
		return None

	def load(self, channel):
		global manager
		self.checkDirs(channel)
		filenameData = self.dir + channel + self.ExtData
		filenameKey = self.dir + channel + self.ExtKey


		if not PATH.exists(filenameKey) or not PATH.exists(filenameData):
			data = self.loadAbs(filenameData)
			self.save(channel, data = data)

		return {"key":self.loadKey(channel),"_val":self.loadData(channel)}

	def loadData(self, channel):
		channel = channel.replace(".","/")
		filenameData = self.dir + channel + self.ExtData
		if PATH.exists(filenameData):
			return self.loadAbs(filenameData)

		return None
	####
	#### def loadKey(self, channel):
	#### 	filenameKey = self.dir + channel + self.ExtKey
	#### 	return self.loadAbs(filenameKey)
	####


	def loadKey(self,channel, pr = False):
		channel = channel.replace(".","/")
		# print(pr)
		if pr:
			print("LLLLLLLLLL",channel)
		filenameKey = self.dir + channel + self.ExtKey
		if PATH.exists(filenameKey):
			return self.loadAbs(filenameKey)

		return None


	def checkDirs(self, channel):
		clist = channel.split("/")
		bigList = []
		for i in range(len(clist)):
			strD = ""
			for c in range(i+1):
				strD+=clist[c]+"/"
			bigList.append(strD)
		for B in bigList:
			if not PATH.exists(self.dir+B):
				# print("############ CREATING DIR",self.dir+B)
				os.makedirs(self.dir+B)


	def save(self, channel, data):
		global channels

		filenameData = self.dir + channel + self.ExtData
		filenameKey = self.dir + channel + self.ExtKey

		self.checkDirs(channel)
		newKey = -1
		#### if not PATH.exists(filename):

		############ TODO: optional backup here before overwriting

		if PATH.exists(filenameKey):
			newKey = self.loadKey(channel)
			if newKey is None:
				newKey = -1
			newKey += 1

		# print("SAVING ALL")
		self.saveAbs(filenameData, data)
		self.saveAbs(filenameKey, newKey)
		channels[channel]["key"][0] = newKey
		channels[channel]["_val"][0] = data

		# print (str(type(data)))
		# if "function" in str(type(data)):
		# 	print("!!!!!!!!!!")
		# 	channels[channel]["_val"] = data
		# else: # enters [value]
		# 	if "list" not in str(type(channels[channel]["_val"])):
		# 		channels[channel]["_val"] = []
		# 	channels[channel]["_val"][0] = data
		#
		# print("in []",channel,data, type(channels[channel]["_val"]))

	def saveAbs(self, filename, data):
	####    with open(filename,"wb") as file:
	####        pk.dump(data,file)
	####        self.printF("saved",data)

		#### self.printF("data to be saved:",data)
		#### self.printF("path:",filename)

		# print("SAVING ABS",filename, data)
		try:
			#### print("..........tring to save at ",filename)
			with open(filename,"wb") as file:
				#### print("iiiiinnnnnnnn")
				pk.dump(data,file)
				#### self.printF("saved",str(data), "@",filename)
				#### run = False
			####
			return True
		except Exception as e:
			#### try:
			#### 	print("..........tring to save at ",filename)
			#### 	with open(filename,"wb") as file:
			#### 		print("iiiiinnnnnnnn")
			#### 		pk.dump(str(data),file)
			#### 		self.printF("saved",str(data), "@",filename)
			#### 		run = False
			#### 	#### del(data)
			#### 	############ ???
			#### 	#### print("//////////////////////////")
			#### 	return True
			#### except Exception as ee:
			#### 	print("XXXXXXX failed saving",str(ee))
			#### 	time.sleep(0.01)
			pass #print("XXXXXXX failed saving",str(e))
			time.sleep(0.001)
			return False

		#### def ox(id = None, val = None):
		#### 	global manager
		#### 	print("!!!!!! oooooo", manager.channels)
		#### 	if id in manager.channels:
		#### 		print("iddddddddddddd",id)
		#### 		if manager.channels[id]["ref"] is not None and len(manager.channels[id]["ref"])>0:
		#### 			print("VVVVVVVV VVVVVVVVVV VVVVVVV V V V V V V V V V VV UUUUUUUUUU",id,"       ",manager.channels[id]["ref"][0])
		#### 			if val is not None:
		#### 				manager.save(channel = id, data = val)
		#### 				#### pass
		#### 			return manager.channels[id]["ref"][0][0]
		#### 		else:
		#### 			print("NEW OBJ")
		#### 			return obj(val = val, id = id)
		#### 	else:
		#### 		print("NEW OBJ")
		#### 		return obj(val = val, id = id)
	def ox(self,id = None, val = None):
		return ox(id = id, val = val)


def newObjManager(ref = None, defaultDB = "main"):
	hasManager = __objManager._hasManager
	if not hasManager:
		manager = __objManager(defaultDB = defaultDB)
		# print("MMMMMMMMMM",__objManager._hasManager)
		__objManager._shared = manager
		__objManager._hasManager = True
		# print("MMMMMMMMMM",__objManager._hasManager)
		return manager
	return __objManager._shared

def HHH():
	pass #print("HHHHHHHHHHHHHHHHHHHHH")


def ox(id = None, val = None):
	global manager
	pass #print("!!!!!! oooooo", manager.channels)
	if id in manager.channels:
		pass #print("iddddddddddddd",id)
		if manager.channels[id]["ref"] is not None and len(manager.channels[id]["ref"])>0:
			pass #print("VVVVVVVV VVVVVVVVVV VVVVVVV V V V V V V V V V VV UUUUUUUUUU",id,"       ",manager.channels[id]["ref"][0])
			if val is not None:
				manager.save(channel = id, data = val)
				#### pass
			return manager.channels[id]["ref"][0][0]
		else:
			pass #print("NEW OBJ")
			return obj(val = val, id = id, parent = None)
	else:
		pass #print("NEW OBJ")
		return obj(val = val, id = id, parent = None)
	#### global manager
	#### return manager.ox(id = id, val = val)



class obj(Expando):
	"""docstring for obj."""

	def __init__(self, val = None, id = None, parent = None):
		global manager
		self.__id = id
		# print("........")
		super().__init__(val = val, id = id)
		# print("........ddd")

		self._manager = manager
		self.__id = id
		self._parent = parent
		# print("!!!!!!!!", self.__id, "PPPPPPP",self._parent)
		self._val = manager.bind(self.__id, val, ref = [self])
		# print("........xxxxx")


	def Del(self):
		if "_parent" in self.__dict__:
			if self._parent is not None:
				# self._parent.__dict__[self._name] = None
				self._parent.__dict__.pop(self._name)

	def Show(self, inLoop = False):
		pass #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().show(inLoop = inLoop)
	def ShowMag(self):
		pass #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().showMag()

	def whileShow(self):
		while(True):
			self.show(inLoop = True)
			time.sleep(0.2)
			os.system("clear")

	def whileShowMag(self):
		while(True):
			self.showMag(inLoop = True)
			time.sleep(0.2)
			os.system("clear")

	def turnTo5(self):
		pass #print("5555555555555555")
		self = 5

	def set(self, value):
		#### id = self._id+"/"+name, val= value
		manager.save(self._id,value)
	def value(self, ref = False):
		if ref:
			return self._val
		return self._val[0]

	def __setattr__(self, name, value):
		pass #print("EEEEEEEEEEEEEEEEEEEE000")
		return super().__setattr__(name = name, value=value)
	def __getitem__(self, name):
		return super().__getitem__(name = name)
	def __setitem__(self, name, value):
		return super().__setitem__(name = name, value=value)
	def __getattribute__(self, name, loop = True):
		return super().__getattribute__(name = name, loop=loop)
	def __getattr__(self, name, loop = True):
		return super().__getattr__(name = name, loop=loop)


#### from xo import *

#### ano = newObjManager()
#### ano2 = objManagenor()

class ok(object):
	_shared = None
	# def showKey(self, t = 0.2):
	# 	while(True):
	# 		self[self["key"].val[0]].show()
	# 		time.sleep(t)
	# 		os.system("clear")

	# def showKeyMag(self):
	# 	while(True):
	# 		self[self["key"].val[0]].showMag()
	# 		time.sleep(0.2)
	# 		os.system("clear")

	def _returnFull_(self, id = None, val = None):
		pass #print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

		timeOut = .1
		t0 = time.time()
		pass #print("00000000")
		t = time.time()
		pass #print("00000000")

		cycle = [manager._checkCounter + 0]
		pass #print("00000000")

		full = manager.ox(id = id, val = val)
		pass #print("00000000")

		pass #print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",full)
		pass #print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
		if self._showLoading == True :#or True:
			print(f" ::: Loading History ::: {id}", end="\r\r\r\r")
			print()

		try:
			while(manager._fin is False and time.time()-t0 < timeOut):
			####
			#### while(abs(manager._checkCounter- cycle[0])<2):
				pass #print("waiting for ",id,"to fill",manager._checkCounter, cycle,manager._fin)
				#### time.sleep(1)

			pass #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",manager._checkCounter,cycle)
		except:
			print(f" ::: Exception while looking for xoKey {id} value {val}")
			traceback.print_exc()
		# print("waiting full TIME =========",time.time()-t)
		return full



	def __init__(self, max = 10000000, wait=0.01, **entries):
		#### global hasManager, Dir, ExtKey, ExtData, channels
		# print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
		global manager
		# self._max = 10000000,
		# self._wait=wait
		self._Threads_ = []
		# self._showLoading = True
		# self._shared._Threads_ = []
		# self._Threads_ = []

		# print("_______________iiiiiiiiiiiii______________")
		if ok._shared is not None:
			print(" ::::::::::::::::::::::::::::::::::::::::")
			print(" :::                                  :::")
			print(" :::        xObject is ready          :::")
			print(" :::                                  :::")
			print(" :::   now you can use xo. anywhere   :::")
			print(" :::             :)                   :::")
			print(" :::                                  :::")
			print(" ::::::::::::::::::::::::::::::::::::::::")
			print()
		self._manager_ = manager
		ok._shared = self

		#### if hasManager:
		#### 	# print("FFFFFFFFFFFFFFFFFF")
		#### 	return None

		#### # print("New Manager!!")
		#### #### super(objManager, self).__init__()
		#### dbexist = PATH.exists(Dir)
		#### if not dbexist:
		#### 	os.makedirs(Dir)

		self.__dict__.update(entries)

		#### self.dir = Dir
		#### self.ExtKey = ExtKey
		#### self.ExtData = ExtData
		#### self.channels = channels
		#### print("VVVVVVVVVVVVVVVVVVV")
		#### self.__channelKeys = {}
		#### self.__channelValues = {}
		#### self.refreshChannels()

	def GetXO(self, get = "", allow_creation = False, getValue = False, follow = None):
		# print("XXXXXXXXXXXXXXXXXXXX", get, getValue)
		if "str" not in str(type(get)):
			print(self._id,"Please provide a string as a key",get)
			return None
		c = 0
		# print(c,c,c,c,c,c,c,c,c,c);c+=1
		sp = get.split(".")
		first = get.split(".")[0]
		if follow is None:
			if len(first) > 0:
				if allow_creation or xoManager.loadKey(first) is not None:
					# print("FIRST",first)
					return self.GetXO(get = ".".join(sp[1:]), allow_creation=allow_creation,follow=xo[first], getValue=getValue)
			return None

		# print(c,c,c,c,c,c,c,c,c,c);c+=1
		if get == "":
			# print(c,c,c,c,c,c,c,c,c,c);c+=10
			if follow is not None and follow._val is not None:
				# print(c,c,c,c,c,c,c,c,c,c);c+=100
				if "list" in str(type(follow._val)):
					if len(follow._val) > 0:
						if getValue:
							return follow._val[0]
						return follow
				if getValue:
					return follow._val
				return follow

			# print(c,c,c,c,c,c,c,c,c,c);c+=1000
			return follow
		else:
			if allow_creation or first in follow.children():
				return self.GetXO(get = ".".join(sp[1:]), allow_creation=allow_creation,follow=follow[first], getValue=getValue)

		return None

	def ValueOf(self, get, allow_creation = False):
			return self.GetXO(get = get, allow_creation=allow_creation, getValue = True)

	def _getValue(self, get, allow_creation = False):
			return self.GetXO(get = get, allow_creation=allow_creation, getValue = True)

	'''
	## key = xoKey i.e xo.a.b.c.d xoKey is "a.b.c.d"
	## value to set in xo[key]
	## allow_creation = creates XO if not already there
	## retBool returns if the value was set correctly, True by default
	## retVal returns xo[key].value()
	## retXO returns the xo so you can chain commands ie:
	## xo.wow.SetValue(1000,retXO=True).runFunc1(True, retXO=True).runFunc2("awesome") '''
	def SetValue(self, key, value, allow_creation = True, retBool = True, retValue = False, retXO = False):

		if "xo.obj" in str(type(key)):
			if key.value() is not None:
				key = str(key.value())
			else:
				key = key._id
		if key is None:
			" ::: SetValue Key is None :::"
			return False
		res = self.GetXO(key, allow_creation=allow_creation)
		if res is not None and "xo.obj" in str(type(res)):
			# res.show()
			# print("..............",res, res._id)
			xoManager.save(res._id, value)
			# res.show()
		else:
			print(type(res),res)
			print("!!!!!!!!!!!!!!!!!!!")
			pass
		if retXO:
			return self.GetXO(key)
		res = self.GetXO(key,getValue=True)
		if retValue:
			return res
		# print(res,"@@@@@@",value)
		return  res == value


	def _setDB(self,dirname):
		print("xxxxxxxxxxxxxxxxxx to be implemented SETTING DB TO:",dirname)
		# xoManager = manager = newObjManager()

	def _defFunc(self, *a, **aa):

		data = [a, aa]
		print()
		print("::::::::  incoming data ::::::::::::::::::::::::::::: "+time.ctime())
		print(f"::::::::  {a}, {aa} ::::::::::::::::::::::::::::: ")
		# print(data)
		# print(":::::::: "+channel+ "- incoming data :::::::::::::::::::::::::::::")
		print()
		return data
# #

# def working(data):
# 	print("!!!!!!!! ALRIGHT !!!!!",data)
# 	return "!!!!!!!! ALRIGHT !!!!!"+str(data)
# # #
# # #
#
# xo.subscribe("n.run.0", working, autoPub = ["n.x.y","n.kux"] )
# xo.subscribe("n.run.0", working )
# :D

	# def subscribe(self, channel=None, func=None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False, path = None,url = None):
	def subscribe(self, channel=None, func=None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False, path = None, url = None):
		if url is None and path is not None and ("http" in path or ".com" in path):
			url = path
			if path is None:
				path = url

		if func is None:
			func = self._defFunc

		if PATH.exists(channel):
			path = channel

		# print("CHANNEL",channel)
		# print("FUNC",func)
		# print("autoPub",autoPub)
		if path is not None:
			if url is not None:
				if ".com/" in url:
					if "github" in url:
						pass
						#TODO subscribe to github, check every 1 min, randomize user agent
					else:
						print(" ::: Could not find match for url",url)

			if PATH.exists(path):
				# EXAMPLE:
				# p = "/home/magic/AlphaENG/xo-gd/";
				# xo.subscribe(p, lambda a : print(" ::: File/Folder Changed :",a), "res")
				if True:
					# fW.watchF(path = path, callback = func, xoKey = autoPub, xo = self)
					if autoPub is None or autoPub == "":
						autoPub = "watch."+os.path.basename(path)
						channel = autoPub

					watchF(path = path, callback = func, xoKey = autoPub+".changes", xo = self, res = autoPub)
				return True

				pass
			else:
				print(" ::: File or folder does not exist",path, "doesn't exist")
				return False


		if channel is not None:
			if channel.startswith("xo."):
				channel = channel[3:]


			if self._Threads_ is None:
				self._Threads_ = ["xxx"]
				# print("[[[[[[[[[[[[]]]]]]]]]]]]")
			# if self.lowerCase:
			# 	channel = channel.lower()
			#if channel+self.extChannel not in self.__Channels:
			#self.printF("########")
			# self.addChannel(channel)
			# print("########",channel)
			self.GetXO(channel,allow_creation=True)
			# xo.GetXO(channel,allow_creation=True)u
			# print("########",channel)
			# xo[channel].show()

			if echo:
				# print("Subscribing to", channel, "- currently equals:", str(xo.ValueOf(channel)) )
				print(" ::: Subscribing to", channel)
			if block:
				self.__waitAndExe(channel, func, once, autoPub = autoPub, debug = debug, withID=withID)
			else:
				uT = Thread(target = self.__waitAndExe, args = [channel, func, once, autoPub, debug, withID])
				self._Threads_.value().append(uT)
				uT.start()
			return True
		print(); print(" ::: Please provide a channel/path/url to xo.subscribe() "); print()
		return False

	def _publish(self, channel, data):
		# print("ppppppppppp",channel,data)
		return self.SetValue(channel, data, allow_creation = True)

	def __waitAndExe(self, channel, func, once= False, autoPub = None, debug = False, withID = False):
		# if self.lowerCase:
		# 	channel = channel.lower()
		# print("__________-")

		# print("AAAAAAAAAAAAAAA",autoPub)
		run = True
		newdata = None
		while run:
		# for ccc in range(4):
			# time.sleep(1)
			run = not once
			# print("CCCCCCCCCCCC",channel)
			data = self.__awaitChannelUpdate(channel)
			# print("CCCCCCCCCCCC2222")
			# print("@@@@@@@@@@@@")
			if not debug:
				try:
					if withID:
						newdata = func([data,channel])
					else:
						newdata = func(data)
				except:
					traceback.print_exc()
			else:
				if withID:
					newdata = func([data,channel])
				else:
					newdata = func(data)
			# print("############",newdata,"@@@@@@@",autoPub)
			if autoPub is not None:
				if type(autoPub) is list:
					for pb in autoPub:
						print(f" ::: Processed new data in {channel.replace('/','.')} ::: Results saved in {pb} ::: \n :::   {pb} Data:   :::\n{newdata}\n\n")
						# self._publish(pb,newdata)
						self.GetXO(pb).set(newdata)
				else:
					print(f" ::: data from {channel} was procced in {func} and the results autoPubish to",autoPub, ":::")
					# self._publish(autoPub,newdata)
					self.GetXO(autoPub).set(newdata)
			else:
				pass
				#print("autoPub is None")


	def __awaitChannelUpdate(self, channel,wait = 0.00001):
		# if self.lowerCase:
		# 	channel = channel.lower()
		# wait=self.wait
		# print("DDDDDDDDD11",d)
		# d = self.manager.loadKey(channel, pr = True)
		d = xoManager.loadKey(channel)
		# print("DDDDDDDDD12",d)
		# d = self.load(self.dir+channel+self.extChannel)
		#print("ddddddddddddddddd",d)
		if d is None:
			# d = self.load(self.dir+channel+self.extChannel)
			# print("DDDDDDDDD1",d)
			d = xoManager.loadKey(channel)
			# print("DDDDDDDDD2",d)

			if d is None:
				return None

		# print("DDDDDDDDD0",d)
		tempD = d+0
		#print(d,tempD,str(d) == str(tempD))

		while(str(d) == str(tempD)):
			# print(".",d)
			# d = self.load(self.dir+channel+self.extChannel)
			d = xoManager.loadKey(channel)
			# print("CCCCCCCCCCCCC",channel,d)
			time.sleep(wait)
		# print("XXXXXXXXXXX")
		# self.printF("!!!!!!!!!!!!!!!!!")
		# return self.load(self.dir+channel+self.extData)
		return xoManager.loadData(channel)


	def __set__(self, key, val):
		pass
		# print("eeeeeeeeeeeeeeeeeeeessssssssse")
		self.__dict__[key] = val
		return True

	def __get__(self,key, done = False, *args, **kwargs):
		# print("TTTTTT",type(key))
		# print("###########",key,"#")
		if done:
			return self
		for a in args:
			# print (a, str(type(a)), str(a))
			if "xo.ok" in str(a):
				# print("SSSSSSSSSSSSSS")
				return ok._shared.__get__("k",done = True)
		# print("$$$$$$$$$$$")
		# for a in kwargs:
		# 	print(a, kwargs[a])
		# pass
		# print("eeeeeeeeeeeeeeeeeeeeeagggggggggaa")
		return [""]
		return self.__dict__[key]

	def __setattr__(self, name, value):
		pass ## print("__setattr____setattr____setattr____setattr____setattr____setattr__1",name,value)
		if "str" not in str(type(name)):
			name = str(name)

		# self.__dir__().append("bbb")
		res = self._returnFull_(id=name, val=value)
		self.__dict__[name] = res
		# self.set(name, res)
		return res



		if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults:#### and "__skip" in self.__dict__ and name not in self.skip:
			if "xo.obj" not in str(type(value)):
				pass ## print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass ## print("2222222222")
					# print("pp22222",self)
					self[name] = obj(id = self._id+"/"+name, val= value, parent = None)
				else:
					pass ## print("33333333")
					#### self.__set__(name,value)
					manager.save(channel = self._id+"/"+name, data=value)
					#### self.save(id = self._id+"/"+name, val= value)
			else:
				pass ## print("44444")
				self.__dict__[name] = value

		else:
			#### # print("555555555")
			self.__dict__[name] = value

	def __getitem__(self, name):
		# print("__getitem____getitem____getitem____getitem____getitem____getitem____getitem__2",name)

		if "str" not in str(type(name)):
			name = str(name)

		return self._returnFull_(id=name)

		# if not name.startswith("_") and "_val" in self.__dict__ and name not in SelfNamed._languageDefaults and name not in self.__dict__:
		# 	self.__dict__[name] = obj(id = self._id+"/"+name, parent = self)
		#
		# if name in self.__dict__:
		# 	#### print("FUUCKKKKKKKKKKKKKKKKKKKKKk")
		#
		# 	item = self.__dict__[name]
		# 	return item
		#
		# 	atr = object.__getattribute__(self, name)
		# 	return atr

	def __assign__(self, v):
		# print('called with %s' % v)
		pass

	def __setitem__(self, name, value):
		if "str" not in str(type(name)):
			name = str(name)
		pass #print("__setitem____setitem____setitem____setitem____setitem____setitem__3",name,value)
		res = self._returnFull_(id=name, val=value)
		self.__dict__[name] = res
		return res
		# return self._returnFull_(id=name, val=value)
		#### if "str" not in str(type(name)):
		#### 	name = str(name)
		#### if not name.startswith("_") and "_val" in self.__dict__ and name is not "_val":#### and "__skip" in self.__dict__ and name not in self.skip:
		#### 	print("VVVVVVVV",str(type(value)))
		#### 	if "xo.obj" not in str(type(value)):
		#### 		print("_____________________",str(type(value)))
		#### 		if name not in self.__dict__:
		#### 			print("1",name)
		#### 			self.__dict__[name] = obj(id = self._id+"/"+name, val = value)
		#### 		else:
		#### 			print("2",name)
		#### 			self[name].set(value)
		#### 	else:
		#### 		print("22222222222222222222222")
		#### 		self.__dict__[name] = value
		#### else:
		#### 	print("3",name)
		#### 	self.__dict__[name] = value

		#### print("FINISHED SETTING ITEM", self.__dict__)

	def __getattribute__(self, name, loop = True):
		# print("__getattribute____getattribute____getattribute____getattribute____getattribute__4",name)
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			# self.__dict__[name] = atr
			return atr

		atr = object.__getattribute__(self, name)
		# self.__dict__[name] = atr

		return atr

	def __getattr__(self, name, loop = True):
		# print("__getattr____getattr____getattr____getattr____getattr____getattr__5", name)
		if "str" not in str(type(name)):
			name = str(name)
		# print("__getattr____getattr____getattr____getattr____getattr____getattr__5", name)
		#### return ox(id=name)
		#### print("getttt")
		#### if "str" not in str(type(name)):
		#### 	name = str(name)
		#### #### return name
		if not name.startswith("_") and name not in self.__dict__:
			####print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			####print("aaaaaaaaaaaaaa")
			#### self[name] = obj(id = self._id+"/"+name)
			# return self._returnFull_(id=name)
			res = self._returnFull_(id=name)
			self.__dict__[name] = res
			return res
		####
		#### if name in self.__dict__:
		#### 	print("bbbbbbbbbbbbbbb")
		#### 	atr = object.__getattribute__(self, name)
		####
		#### 	return atr
		#### #### return 13
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#### print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

def cleanInput():
	lines = []
	waiting = True
	startT = None
	timeout = 1
	try:
		while waiting:
			if len(lines) > 0:
				startT = time.time()

			if startT is not None:
				print("!!!!!!!!!!!")
				if time.time() - startT > timeout:
					waiting = False

			lines.append(raw_input())
	except EOFError:
		pass
	lines = "\n".join(lines)
	return lines

def cleantxt(a):
	clean = ""
	for k in a.split("\n"):
		clean += re.sub(r"[^a-zA-Z0-9]+", ' ', k) + " "
	return clean[:-1]

# print("XXXXXXXXXXXXXx")

def changeHome(newHome):
	pass
	# print(" ::: NEED TO IMPLEMENT HOME CHANGE ::: ", newHome)


dbDirName = "xo-gd"
defaultDB = "main"
xoHome = "/".join(os.getcwd().split("/")[:3]) + "/" + dbDirName + "/"

cwd = xoHome
xoHome += defaultDB + "/"

print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("           XObject & GlobalData Loaded"      )
print("        xo.home is",xoHome      )
print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
print()
# xo.watcher.home = watcherHome
# cwd = os.getcwd()
# print("CCCCCCCC",cwd)
# Dir = "db/GlobalData/"
# Dir = "gd-db/"
# Dir = cwd+"/gd-db/"
Dir = cwd #+"/xo-gd/"
# Dir = "/home/magic/a-gd-db/"
ExtKey = ".gdc"
ExtData    = ".gdd"
wait = 0.00001
hasManager = False
channels = {}

if Dir[::-1][0] is not "/":
	Dir += ""

xoManager = manager = newObjManager(defaultDB = defaultDB)
loadAll = True
if loadAll:
	xoManager.refreshChannels()

if ok._shared is None:
	# print("FFFFFFFFFFFFFFFFFFFFFf")
	xo = ok()        # xo can now can generate xobjects
else:
	# print("TTTTTTTTTTTTTTTTTTTTTTTT")
	xo = ok._shared
# xxo = ok()        # xo can now can generate xobjects
# xxo.main = True
# xo = xxo.main

xo.home = xoHome
xo.home.subscribe(changeHome)
# xo.settings.autoSync = False
# xo.subscribe("xo.home", changeHome)
# xo.subscribe("xo.settings.autoSync", lambda a: print("autoSync is ON", xo.watcher.syncRepos(), xo.watcher.run.SetValue(True)) if a == True else False, autoPub="xo.settings.autoRun")

#
# xo = xo.main
# print("XXXXXXXXXXXXXx")

# def populatex(text):
# 	for line in text.split("\n")[:xo.a.limit._val[0]]:
# 		for word in line.split(" ")[:xo.a.limit._val[0]]:
# 			path = "a."+xo._getValue("a.key")+"."+word
# 			print("::::",word,path)
# 			org = xo._getValue(path)
# 			if org is None or "int" not in str(type(org)):
# 				xo.SetValue(path,0, allow_creation=True)
# 				org = 0
# 			xo.SetValue(path, org+1, allow_creation=True)
