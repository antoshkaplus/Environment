import subprocess

subprocess.Popen("watch -n1 'echo \"scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192\" | bc'", shell=True)
subprocess.Popen("sudo turbostat -s PkgWatt")
subprocess.Popen("s-tui")
subprocess.Popen("./mprime -m")