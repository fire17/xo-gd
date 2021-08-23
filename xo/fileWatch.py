#!/usr/bin/python
import time, os
from datetime import *
from .gd import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
	def __init__(self, path, autoPub, xo, delta = 1):
		self.last_modified = [datetime.now(), []]
		# self.interested = xo.mock.interested.value()
		self.ignore = ["~"]
		self.interested = []
		self.path = path
		self.autoPub = autoPub
		self.delta = delta
		self.xo = xo

	# ::::::::::: OPTIONS
	# FFF.dispatch(      FFF.on_any_event(  FFF.on_created(    FFF.on_modified(
	# FFF.mro(           FFF.on_closed(     FFF.on_deleted(    FFF.on_moved(


# xo.subscribe('/home/magic/AlphaENG/data' ,lambda *a,**aa:"###################### YEA ##","aa")
	def on_modified(self, event):
		interesting = True
		skip = False
		if len(self.interested) == 0:
			interesting = True
		for i in self.interested:
			if i in str(event.src_path):
				for s in self.ignore:
					if s in str(event.src_path):
						skip = False
				if not skip:
					interesting = True

		if interesting:
			if datetime.now() - self.last_modified[0] < timedelta(seconds=self.delta):
				if event.src_path in self.last_modified[1]:
					return
				self.last_modified = [datetime.now(), self.last_modified[1] + [event.src_path]]
			else:
				self.last_modified[0] = datetime.now()
				if event.src_path in self.last_modified[1]:
					self.last_modified[1] += [event.src_path]
				else:
					self.last_modified[1] = [event.src_path]
			# # print("PPPPPPP",self.autoPub)
			# print("PPPPPPP",self.autoPub)
			# print("PPPPPPPPPP",self.xo.GetXO(self.autoPub))
			self.xo.GetXO(self.autoPub,allow_creation=True).set(event.src_path)
			# # self.xo.GetXO(self.autoPub+".changes",allow_creation=True).set(event.src_path)
			# print("PPPPPPPPPP",self.xo.GetXO(self.autoPub))
			#
			# self.xo.GetXO(self.autoPub).SetValue(event.src_path)
			print(f" ::: File/Folder Modified ::: xo.{self.autoPub.replace('/','.')} :::",event.src_path)
			# print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes" , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available
	def on_createdx(self, event):
		interesting = True
		skip = False
		if len(self.interested) == 0:
			interesting = True
		for i in self.interested:
			if i in str(event.src_path):
				for s in self.ignore:
					if s in str(event.src_path):
						skip = False
				if not skip:
					interesting = True

		if interesting:
			if False and datetime.now() - self.last_modified[0] < timedelta(seconds=self.delta):
				return
			else:
				self.last_modified[0] = datetime.now()
			print("PPPPPPP",self.autoPub)
			print("PPPPPPPPPP",self.xo.GetXO(self.autoPub))
			self.xo.GetXO(self.autoPub).SetValue(event.src_path)
			print("PPPPPPPPPP",self.xo.GetXO(self.autoPub))
			print(f" ::: File/Folder Created ::: xo.{self.autoPub.replace('/','.')} :::",event.src_path)
			# print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes" , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available
	def on_moved0(self, event):
		interesting = True
		skip = False
		if len(self.interested) == 0:
			interesting = True
		for i in self.interested:
			if i in str(event.src_path):
				for s in self.ignore:
					if s in str(event.src_path):
						skip = False
				if not skip:
					interesting = True

		if interesting:
			if False and datetime.now() - self.last_modified < timedelta(seconds=self.delta):
				return
			else:
				self.last_modified = datetime.now()
			# print("PPPPPPP",self.autoPub)
			auto = self.xo.GetXO(self.autoPub)
			auto["changes"] = event.src_path
			print(f" ::: File/Folder Moved ::: xo.{self.autoPub.replace('/','.')} :::",event.src_path)
			# print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes" , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available
	def on_deleted0(self, event):
		interesting = True
		skip = False
		if len(self.interested) == 0:
			interesting = True
		for i in self.interested:
			if i in str(event.src_path):
				for s in self.ignore:
					if s in str(event.src_path):
						skip = False
				if not skip:
					interesting = True

		if interesting:
			if False and datetime.now() - self.last_modified < timedelta(seconds=self.delta):
				return
			else:
				self.last_modified = datetime.now()
			# print("PPPPPPP",self.autoPub)
			auto = self.xo.GetXO(self.autoPub)
			auto["changes"] = event.src_path
			print(f" ::: File/Folder Deleted ::: xo.{self.autoPub.replace('/','.')} :::",event.src_path)
			# print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes" , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available

# xo.mock.interested = ["AEsales.xlsx"]
# xo.mock.interested = [""]
# xo.mock.interested.ignore = ["~"]

#test
# xo.subscribe('/home/magic/AlphaENG/data' ,lambda *a,**aa:"###################### YEA ##","aa")

def watchFiles(path, callback, xoKey, xo, resID = None):
	# if not xoKey.endswith(".changes"):
	# 	xoKey += ".changes"
	# print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",path,callback,xoKey)
	# xoKey += ".changes"
	event_handler = MyHandler(path, xoKey, xo)
	observer = Observer()
	xo.GetXO(xoKey,allow_creation=True).subscribe(callback, autoPub = xoKey.split(".changes")[0])

	# cwd = os.getcwd()
	print("Watching Files:",path, xoKey, callback)
	observer.schedule(event_handler, path=path, recursive=True)
	observer.start()

	try:
		while (xo.watcher.run == True):
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

# 2
def watchF(path, callback, xoKey, xo, res = None):
	# print("KKKKKKKKKKKKKK",xoKey)
	# xo._watchFile = watchFiles
	xo.asyn(watchFiles, path, callback, xoKey, xo, resID = res)


'''
################################################################################################
path = "/home/magic/AlphaENG/xo-gd/";
xo.subscribe(path, lambda a : print(" ::: File/Folder Changed :",a), "res")
# xo.subscribe(folderOrFile, function(data), xoKey for updates)
################################################################################################
#
# “OSError: [Errno 24] inotify instance limit reached” Code Answer
#
# OSError: [Errno 24] inotify instance limit reachedshell by BlueMoon         on Mar 26 2021 Comment
# 1
# cat /proc/sys/fs/inotify/max_user_watches
# 1
# Programs that sync files such as dropbox, git etc use inotify to notice changes to the file system. The limit can be see by
# 2
# ​
# 3
# cat /proc/sys/fs/inotify/max_user_watches
# 4
# If you are running Debian, RedHat, or another similar Linux distribution, run the following in a terminal:
# 5
################################################################################################
# echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
################################################################################################
# 6
# ​
# 7
# If you are running ArchLinux, run the following command instead (see here for why):
# 8
# echo fs.inotify.max_user_watches=524288 | sudo tee /etc/sysctl.d/40-max-user-watches.conf && sudo sysctl --system
# 9
# ​
# 10
# close terminal and open against
'''
