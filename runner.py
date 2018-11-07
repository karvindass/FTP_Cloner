from git import Repo
import os
import subprocess

repo = Repo(os.getcwd() + "/website")
print("Pulling from Git Repo...")
repo.remotes['origin'].pull()
print("Pulled from Git Repo")

print("Building website using Jekyll...")
p = subprocess.Popen(["jekyll","build"], cwd=os.getcwd() + "/website")
p.wait()
print("Built website using Jekyll")