from mcp.server.fastmcp import FastMCP
import psutil

# 1. Initialize the MCP Server
mcp = FastMCP("Kenny-Laptop-Health")

# 2. Convert your vitals function into an MCP Tool
@mcp.tool()
def get_system_vitals() -> str:
    """Returns live CPU usage percentage and RAM usage (Used vs Total in GB)."""
    cpu = psutil.cpu_percent(interval=1)
    vmem = psutil.virtual_memory()
    total_gb = vmem.total / (1024**3)
    used_gb = vmem.used / (1024**3)
    return f"CPU: {cpu}% | RAM: {used_gb:.2f} GB / {total_gb:.2f} GB ({vmem.percent}% Used)"

# 3. Convert your processes function into an MCP Tool
@mcp.tool()
def get_top_processes(count: int = 3) -> str:
    """Returns a list of the top memory-hogging processes running on the laptop."""
    processes = []
    
    # ✅ Make sure parentheses () are present here!
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
            
    # Sort processes by memory usage descending
    sorted_procs = sorted(processes, key=lambda p: p['memory_percent'] or 0, reverse=True)
    
    # Format into a clean string
    output = []
    for proc in sorted_procs[:count]:
        output.append(
            f"PID: {proc['pid']} | Name: {proc['name']} | RAM Usage: {proc['memory_percent']:.2f}%"
        )
        
    return "\n".join(output)

# 4. Run the server using standard I/O (stdio)
if __name__ == "__main__":
    mcp.run(transport="stdio")

#npx @modelcontextprotocol/inspector python server.py