# Must run with root privalages for turbostat to work.

import subprocess

# gnome-terminal does not understand `~`.
# It opens user home by default though.
prime_path = 'Tools/Prime95'

subprocess.Popen("gnome-terminal --title=Vcore -- watch -n1 'echo \"scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192\" | bc'", shell=True)
subprocess.Popen("gnome-terminal --title=Watt -- turbostat -s PkgWatt", shell=True)
subprocess.Popen("gnome-terminal --title=Temp/Freq -- s-tui", shell=True)
subprocess.Popen(f"gnome-terminal --working-directory={prime_path} --title=Prime95 -- ./mprime -m", shell=True)
tail = subprocess.Popen(f"tail -f ~/{prime_path}/results.txt", shell=True)
tail.communicate()