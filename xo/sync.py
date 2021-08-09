from gd import *
import requests
import git
from git import Repo
# import fileWatch
from .xo import *

from .osCommands import os_command
from .osCommands import *

from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
#multiples = [prod(pair) for pair in zip(*[[1,2,3,4],[3,2,1,4],[5.67,1,.5,16]])]# ; multiples
#sum = [sum(pair) for pair in zip(*[[1,2,3,4],[3,2,1,4],[5.67,1,.5,16]])]# ; multiples
# x * [1,2,3]

# print("..........")

from git import RemoteProgress
from tqdm import tqdm
#!/usr/bin/python
# import time, os
from datetime import datetime
from datetime import timedelta
# from gd import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
	def __init__(self, path, autoPub, delta = 1):
		self.last_modified = datetime.now()
		# self.interested = xo.mock.interested.value()
		self.ignore = ["~"]
		self.interested = []
		self.path = path
		self.autoPub = autoPub
		self.delta = delta

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
			auto = xo.GetXO(self.autoPub)
			auto["changes"] = event.key

			print("!!!!!!!!!!! NEW CHANGES !!!!!!!!!!!!!!!!!!", self.autoPub+".changes","event.is_directory:",event.is_directory , event)
			# print(f'Event type: {event.event_type}  path : {event.src_path}')
			# print(event.is_directory) # This attribute is also available

# xo.mock.interested = ["AEsales.xlsx"]
# xo.mock.interested = [""]
# xo.mock.interested.ignore = ["~"]


def watchFiles(path, xoKey, callback):
	# if not xoKey.endswith(".changes"):
	# 	xoKey += ".changes"
	event_handler = MyHandler(path, xoKey)
	observer = Observer()
	xoKey = (xoKey + ".changes").replace("/",".")
	xo.GetXO(xoKey, allow_creation=True).subscribe(callback)

	# cwd = os.getcwd()
	print(" ::: Watching Files:",path, xoKey)
	observer.schedule(event_handler, path=path, recursive=True)
	observer.start()

	try:
		while (xo.watcher.run == True):
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()



class CloneProgress(RemoteProgress):
	def __init__(self):
		super().__init__()
		self.pbar = tqdm()

	def update(self, op_code, cur_count, max_count=None, message=''):
		self.pbar.total = max_count
		self.pbar.n = cur_count
		self.pbar.refresh()


# class github():
def shortRepo(url):
	if ".com" in url:
		return ("_".join(url.split('.com/')[-1].split("/")[:2]))#.replace("/","_")
	return url

def longRepo(url):
	if ".com" not in url:
		return "https://github.com/"+url.replace(".","/").replace("_","/") + "/"
	return url

def fetchLastUpdate(url):
	response = requests.get(url).text
	if response is not None and len(response) > 0:
		# print("!!!"+response)
		dateStr = None
		try:
			if "<updated>" in response:
				dateStr = response.split("<updated>")[1].split("</updated>")[0]
		except:
			print()
			print("URL",url)
			print("300 chars or response:", response[:300])
			print()
			traceback.print_exc()
		return dateStr
	return None

#!!!!!!!!

def checkForUpdates(delay = 0.5, callback = lambda a: print("Repo was updated!",a)):
	finishURL = "commits/master.atom"
	print("\n ::: Checking Github for updates, if you wish hto stop, enter:\n ::: xo.watcher.run = False\n")
	xo.watcher.run = True
	xo.watcher.subscribed = []
	while (xo.watcher.run == True):
		repos = []
		for repo in xo.watcher.repos.value():
			repos.append(repo)
		subscribed = xo.watcher.subscribed.value()
		changed = False
		for repo in repos:
			short = shortRepo(repo)
			if repo not in subscribed:
				subscribed.append(repo)
				channel = "watcher.repos."+short
				# xo.subscribe(channel, callback, withID=True)
				xo[channel].subscribe(callback, withID=True)
				#Subscribe to autoPub
				changed = True
		if changed:
			xo.watcher.subscribed = subscribed
		for repo in repos:
			short = shortRepo(repo)
			lastUpdate = xo.watcher.repos[short].value()
			new = fetchLastUpdate(repo+finishURL)
			if new is not None and len(new) > 0 and new != lastUpdate:
				xo.watcher.repos[short] = new
				print(" ::: ID:",xo.watcher.repos[short]._id)
			else:
				pass
				# print("same",repo)
			time.sleep(delay)

def handleRepoChange(data):
	print("##################################")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("##################################")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print(data)
	data, xoKey = data
	print(xoKey, data)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("##################################")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("##################################")

def watchGithubRepo(repo, callback):
	# print("##################################G")
	# if xo.watcher.repos is None:
	# 	xo.watcher.repos = []
	while(xo.watcher.repos.value() is None):
		xo.watcher.repos = []
		time.sleep(1)
	if repo not in xo.watcher.repos.value():
		xo.watcher.repos.value().append(repo)
	checkForUpdates(callback = callback)
	print("Done Checking for repo changes")
	return None




def gitPull(data):
	data, xoKey = data
	print("PULLING CHANGES FROM",xoKey)
	watcherKey = xoKey.split(".")[-1]
	print()
	print("PULLING",watcherKey)
	print()

	xo.GetXO("watcher.repos", allow_creation=True).show()
	print("SSwatcherKeyTT",watcherKey)
	clonePath = xo.GetXO(watcherKey)["clonePath"].value()
	print("Loading repo",clonePath)
	repo = Repo(clonePath)
	print("found repo",repo)
	o = repo.remotes.origin
	print("found origin",o)
	res = o.pull()
	xo.GetXO(watcherKey)["lastPull"] = res
	print("::: Pull Finished - Info saved in", (watcherKey+"."+"lastPull").replace("/","."), res)



def syncRepo(repo = "https://github.com/fire17/AlphaENG/"):
	### GIT CLONE IF NOT THERE
	short = shortRepo(repo)
	clonePath = xo.home.value() + short
	print("SHORT",short,clonePath)

	xo.GetXO("watcher.repos."+short, allow_creation = True)["clonePath"] = clonePath

	repoExists = PATH.exists(clonePath)
	if not repoExists:
		gitUrl = repo + ""
		if not gitUrl.endswith(".git"):
			if gitUrl.endswith("/"):
				gitUrl = gitUrl[:-1]
			gitUrl += ".git"

		print("\n ::: Cloning",gitUrl,"to",clonePath, )
		print("\n ::: If you're having issues, please clone manually with the following :::")

		repoName = '/'.join(clonePath.split('/')[-1:])
		cmd = f"cd {'/'.join(clonePath.split('/')[:-1])}"
		cmd += f" && rm -rf {repoName}"
		# cmd += f" && mkdir {'/'.join(clonePath.split('/')[-1:])}"
		cmd += f" && git clone {gitUrl} {repoName}"
		print(f" ::: {cmd} \n")
		# Repo.clone_from(gitUrl , clonePath, progress=CloneProgress())
		print("\n ::: Depending on the repo this can take a while :::")
		tc = time.time()
		Repo.clone_from(gitUrl , clonePath, branch="master", progress=CloneProgress())
		# git.Git(clonePath).clone(gitUrl, progress=CloneProgress())
		# os.makedirs(clonePath)
		# git.Git("/".join(clonePath.split("/")[:-1])).clone(gitUrl)

		# Repo.clone_from("git@github.com:"+gitUrl.strip("https://").strip("http://") , clonePath, branch="master")
		# git.Git("/your/directory/to/clone").clone(path = "git://gitorious.org/git-python/mainline.git", progress=CloneProgress())

		print(" ::: Cloning Finished. Time:",time.time()-tc,"\n")
		repoExists2 = PATH.exists(clonePath)
		if not repoExists2:
			print(gitUrl, "COULD NOT BE CLONED.................",)
		else:
			print(" ::: SYNC :::", gitUrl.replace("https://", "").replace("http://", ""), "Was Clones Succesfully into",clonePath)
	else:
		print(" ::: No need to clone",short," - ",clonePath, "already exists!")
		# os.makedirs(clonePath)
	### GIT PULL IF UPDATED
	# print("\n 1. watching repo for updates")
	xo.watcher.watchRepo(repo, gitPull)
	print(" ::: SYNC ::: Watching for github changes in",repo)
	# print("DONE.......")


	# GIT PUSH IF LOCAL CHANGES
	# print()
	print(" ::: SYNC ::: Watching for file changes in",clonePath)
	# print("checking for changes.......")
	xo.watcher.watchFiles(clonePath, "watcher.repos."+short, xo)
	print(" ::: SYNC ::: Syncing Repo :::", short)
	return True

def watchR(repo, callback = handleRepoChange):
	watchR = "3333333"
	xo.watcher.githubWatch = watchGithubRepo
	xo.watcher.githubWatch(repo, callback, asyn = True)

def syncR(repos = "https://github.com/fire17/AlphaENG/"):
	if "list" not in str(type(repos)):
		repos = [repos]

	xo._syncR = syncRepo
	for repo in repos:
		xo._syncR(repo, asyn = True)
	print("RRR returning from syncR")
	return True


def changed(data):
	print("UUUUUUUUUUUUUUUUUUUUUUUUUUU")
	print("UUUUUUUUUUUUUUUUUUUUUUUUUUU",data)
	repoPath, event = data
	print("::::",  event)
	print("UUUUUUUUUUUUUUUUUUUUUUUUUUU")
	repo = Repo(repoPath)
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	repo.git.pull()
	repo.git.add(".")
	repo.git.commit("-m","autoCOMMIT"+str(event))
	repo.git.push()
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ DONE!")



# def cloneRepo(repo = "https://github.com/fire17/AlphaENG"):
def cloneRepo(repo = "https://github.com/fire17/Projects"):
	xo._cloneCommand = cloneCommand
	xo._cloneCommand(repo, asyn = True)
	# xo._clone = callCommand:
	# xo._clone([repo, ], asyn = True)


xo.f.cloneRepo = cloneRepo
xo.watcher.watchFiles = watchF
xo.watcher.watchRepo = watchR
xo.watcher.syncRepos = syncR
