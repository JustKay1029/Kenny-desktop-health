import psutil

cpu = (psutil.cpu_percent(interval=1))
vmem= psutil.virtual_memory() #VMEM returns a tuple, to access elements I have used dot notation, indexing can be used too.
iter= psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])

# Formatting specs in a better/more readable form
def get_system_vitals():
    total_gb = (vmem.total)/(1024**3)
    available_gb = (vmem.available)/(1024**3)
    used_gb = (vmem.used)/(1024**3)
    free_gb = (vmem.free)/(1024**3)
    return f"CPU: {cpu}% | RAM: {used_gb :.2f} GB / {total_gb :.2f} GB ({vmem.percent}% Used)"

# Finding the top 3 "memory-hogging" processes
def get_top_processes(count=3):
    processes = []
    # Re-instantiate the generator so it fetches fresh data when called
    for proc in iter:
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
    # Sort by memory usage descending
    sorted_procs = sorted(processes, key=lambda p: p['memory_percent'] or 0, reverse=True)
    
    # Format the top items into a clean string
    output = []
    for proc in sorted_procs[:count]:
        output.append(f"PID: {proc['pid']} | Name: {proc['name']} | RAM Usage: {proc['memory_percent']:.2f}%")
        
    return "\n".join(output)

print(get_system_vitals())
print(get_top_processes())