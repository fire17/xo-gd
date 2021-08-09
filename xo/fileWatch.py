#!/usr/bin/python
import time, os
from datetime import *
from gd import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
	def __init__(self, path, autoPub, xo, delta = 1):
		self.last_modified = datetime.now()
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

	def on_modified(self, event):
		interesting = False
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
			if datetime.now() - self.last_modified < timedelta(seconds=self.delta):
				return
			else:
				self.last_modified = datetime.now()
			# print("PPPPPPP",self.autoPub)
			auto = self.xo.GetXO(self.autoPub)
			auto["changes"] = event.key
			print(" ::: File/Folder Modified :::",event.key)
			# print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes" , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available

# xo.mock.interested = ["AEsales.xlsx"]
# xo.mock.interested = [""]
# xo.mock.interested.ignore = ["~"]

#test

def watchFiles(path, callback, xoKey, xo):
	# if not xoKey.endswith(".changes"):
	# 	xoKey += ".changes"
	# print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",path,callback,xoKey)
	event_handler = MyHandler(path, xoKey, xo)
	observer = Observer()
	xo[xoKey + ".changes"].subscribe(callback)

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
def watchF(path, callback, xoKey, xo):
	# print("KKKKKKKKKKKKKK",xoKey)
	xo._watchFile = watchFiles
	xo._watchFile(path, callback, xoKey, xo, asyn=True)


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
