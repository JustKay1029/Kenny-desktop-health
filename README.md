# 🤖 Kenny — Jarvis Laptop Health MCP Server

**Kenny** is a lightweight, local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server built in Python using `FastMCP` and `psutil`. It acts as an extensible "Jarvis-style" hardware diagnostic engine, allowing AI assistants (like Claude Desktop, Cursor, or local LLMs) to securely monitor and inspect your laptop's real-time hardware vitals and running processes.

---

## 🌟 Features

* **Live Vitals Diagnostic:** Exposes a tool (`get_system_vitals`) that retrieves real-time CPU usage percentages and memory consumption (Used vs. Total in GB).
* **Process Inspection:** Exposes a tool (`get_top_processes`) that scans active operating system processes, sorts them by memory consumption, and returns the top resource hogs.
* **Standard Protocol:** Communicates via standard I/O (`stdio`) following the official Model Context Protocol specification.

---

## 🛠️ Project Architecture

+--------------------------+       MCP Protocol       +------------------------------------+|  AI Client / Host        | <----------------------> |  Kenny (MCP Server)                ||  (e.g., Claude Desktop)  |        (Stdio)           |  (server.py / FastMCP)             |+--------------------------+                          +------------------------------------+│▼+------------------------------------+|  System Vitals & Processes         ||  (psutil hardware bindings)        |+------------------------------------+
---

## 🚀 Quickstart & Setup

### Prerequisites

* **Python 3.10+**
* **Node.js** *(Optional, required if using the MCP Inspector for debugging)*

### 1. Installation

Clone your repository and install the required dependencies:

```bash
# Install required dependencies
pip install mcp psutil
2. Testing LocallyYou can test the raw hardware diagnostic script:Bashpython test_health.py
To run the MCP server directly in stdio mode:Bashpython server.py
Note: The server will listen silently for JSON-RPC messages over standard input/output.🧪 Debugging with MCP InspectorTo test the server visual interface without connecting a full AI client:Bashnpx @modelcontextprotocol/inspector python server.py
Open the generated localhost link in your browser to manually execute the get_system_vitals and get_top_processes tools.⚙️ Client Integration (Claude Desktop)To connect Kenny to Claude Desktop, add the following entry to your claude_desktop_config.json file:Location on Windows: %APPDATA%\Claude\claude_desktop_config.jsonJSON{
  "mcpServers": {
    "kenny-jarvis": {
      "command": "python",
      "args": [
        "C:\\path\\to\\your\\folder\\kenny\\server.py"
      ]
    }
  }
}
Restart Claude Desktop, and you will be able to ask natural language questions like:"Jarvis, check my laptop vitals.""What are the top 3 processes eating my RAM right now?"📂 File StructurePlaintextkenny/
├── server.py        # Main MCP Server implementation using FastMCP
├── test_health.py   # Standalone hardware diagnostic script
└── README.md        # Project documentation
🧰 Tools OfferedTool NameParametersDescriptionget_system_vitalsNoneReturns live CPU % and formatted RAM usage (Used / Total GB).get_top_processescount (int, default=3)Returns the top memory-hogging processes running on the machine with PID and memory %.