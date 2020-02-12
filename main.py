<<<<<<< HEAD
# This is a task Manager App written by Omar Siddiqi
# Requirements:
# Create an app to capture the System State
# Information like what was deployed on the system,
# where and what was running.
############# random change############

import psutil
import numpy as n

mem = psutil.virtual_memory()
print("Memory Available:", int(n.round(mem[0]/(1024*1024*1024))), "GB")

for proc in psutil.process_iter():
    try:
        procID = proc.pid
        procName = proc.name()
        procUser = proc.username()
        procMem = proc.memory_info

        # procInfo = proc.as_dict(attrs=['pid', 'name', 'username', 'memory_percent'])
        # Alternavitely this can be used, but shows all PID even with unknown names

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    else:
            print("pid:", procID, "| name:", procName, "| user:", procUser, "| mem:", int(n.round(proc.memory_percent()*100)), "% usage")

=======
# This is a task Manager App written by Omar Siddiqi
# Requirements:
# Create an app to capture the System Sate
# Information like what was deployed on the system,
# where and what was running.

import psutil
import numpy as n

mem = psutil.virtual_memory()
print("Memory Available:", int(n.round(mem[0]/(1024*1024*1024))), "GB")

for proc in psutil.process_iter():
    try:
        procID = proc.pid
        procName = proc.name()
        procUser = proc.username()
        procMem = proc.memory_info

        # procInfo = proc.as_dict(attrs=['pid', 'name', 'username', 'memory_percent'])
        # Alternavitely this can be used, but shows all PID even with unknown names

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    else:
            print("pid:", procID, "| name:", procName, "| user:", procUser, "| mem:", int(n.round(proc.memory_percent()*100)), "% usage")


>>>>>>> e3f8629e1106882005411a6bc90b56165e6c7e62
