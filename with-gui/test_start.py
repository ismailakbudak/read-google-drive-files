
import os, subprocess

#os.system("gnome-terminal -e 'ls -al'")
#os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")

os.system("gnome-terminal -e 'zsh -c \"python manager1.py; zsh;\"'")
os.system("gnome-terminal -e 'zsh -c \"python manager2.py; zsh;\"'")
os.system("gnome-terminal -e 'zsh -c \"python nymph1.py; zsh;\"'")