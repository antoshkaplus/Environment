# Must run with root privalages for turbostat to work.

import subprocess

subprocess.Popen("gnome-terminal --title=Vcore -- watch -n1 'echo \"scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192\" | bc'", shell=True)
subprocess.Popen("gnome-terminal --title=Watt -- turbostat -s PkgWatt", shell=True)
subprocess.Popen("gnome-terminal --title=Temp/Freq -- s-tui", shell=True)
subprocess.Popen("./mprime -m", shell=True)