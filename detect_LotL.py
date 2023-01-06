import subprocess

def get_installed_programs():
    # Use the WMIC command to get a list of installed programs
    installed_programs = subprocess.check_output(["wmic", "product", "get", "name"])
    # Split the output into a list of program names
    installed_programs = [p.strip() for p in installed_programs.split("\n") if p.strip()]
    return installed_programs

def get_running_processes():
    # Use the WMIC command to get a list of running processes
    running_processes = subprocess.check_output(["wmic", "process", "get", "name"])
    # Split the output into a list of process names
    running_processes = [p.strip() for p in running_processes.split("\n") if p.strip()]
    return running_processes

def check_for_living_off_the_land(installed_programs, running_processes):
    # Check if any processes are running that are not installed programs
    for process in running_processes:
        if process not in installed_programs:
            print("Possible living off the land activity detected: {} is running but not installed".format(process))

# Get the list of installed programs and running processes
installed_programs = get_installed_programs()
running_processes = get_running_process
