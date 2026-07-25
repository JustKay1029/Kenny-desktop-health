# 🤖 Kenny — Jarvis Laptop Health MCP Server

**Kenny** is a lightweight local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server built with Python, `FastMCP`, and `psutil`.

It gives AI clients (like Claude Desktop) real-time visibility into your computer’s health — CPU usage, memory usage, and top memory-consuming processes — through MCP tools.

---

## 📚 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Prerequisites](#️-prerequisites)
- [🚀 Quickstart](#-quickstart)
- [🧪 Local Testing](#-local-testing)
- [🔍 Debugging with MCP Inspector](#-debugging-with-mcp-inspector)
- [⚙️ Claude Desktop Integration](#️-claude-desktop-integration)
- [🧰 Tools Offered](#-tools-offered)
- [📂 Project Structure](#-project-structure)
- [⚠️ Troubleshooting](#️-troubleshooting)
- [🧭 Roadmap Ideas](#-roadmap-ideas)
- [📄 License](#-license)

---

## ✨ Features

- **Live Vitals Diagnostic**
  - `get_system_vitals`
  - Returns live CPU usage and RAM usage (used vs total in GB).

- **Process Inspection**
  - `get_top_processes`
  - Returns top processes sorted by memory usage.

- **MCP Standard Protocol**
  - Runs over `stdio` using the MCP specification.
  - Easy to plug into MCP-compatible clients.

---

## 🏗️ Architecture

```text
+------------------------+         MCP over stdio         +-----------------------------+
| AI Client / Host       | <----------------------------> | Kenny MCP Server            |
| (e.g., Claude Desktop) |                                | (FastMCP + psutil)          |
+------------------------+                                +-----------------------------+
                                                                  |
                                                                  v
                                                        +----------------------+
                                                        | Local OS Metrics     |
                                                        | CPU / RAM / Processes|
                                                        +----------------------+
```

---

## 🛠️ Prerequisites

- **Python 3.10+**
- `pip`
- **Node.js** (optional, only needed for MCP Inspector)

---

## 🚀 Quickstart

### 1) Clone repository

```bash
git clone https://github.com/JustKay1029/Kenny-desktop-health.git
cd Kenny-desktop-health
```

### 2) Install dependencies

```bash
pip install mcp psutil
```

---

## 🧪 Local Testing

Run standalone hardware diagnostics:

```bash
python test_health.py
```

Run the MCP server in stdio mode:

```bash
python server.py
```

> Note: In stdio mode, the server waits silently for JSON-RPC/MCP messages on standard input/output.

---

## 🔍 Debugging with MCP Inspector

Use MCP Inspector for interactive local testing:

```bash
npx @modelcontextprotocol/inspector python server.py
```

Then open the localhost URL shown in your terminal and manually run:

- `get_system_vitals`
- `get_top_processes`

---

## ⚙️ Claude Desktop Integration

Add Kenny to your Claude Desktop MCP config:

```json
{
  "mcpServers": {
    "kenny-jarvis": {
      "command": "python",
      "args": [
        "C:\\path\\to\\Kenny-desktop-health\\server.py"
      ]
    }
  }
}
```

Then restart Claude Desktop.

You can now ask things like:

- “Jarvis, check my laptop vitals.”
- “What are the top 3 processes eating my RAM right now?”

---

## 🧰 Tools Offered

| Tool Name | Parameters | Description |
|---|---|---|
| `get_system_vitals` | None | Returns live CPU percentage and RAM usage (`used / total` in GB). |
| `get_top_processes` | `count: int = 3` | Returns top memory-consuming processes. |

### Example Output: `get_system_vitals`

```json
{
  "cpu_percent": 18.4,
  "memory": {
    "used_gb": 9.72,
    "total_gb": 15.83
  }
}
```

### Example Output: `get_top_processes`

```json
[
  { "pid": 1244, "name": "chrome.exe", "memory_mb": 842.6 },
  { "pid": 988, "name": "Code.exe", "memory_mb": 512.4 },
  { "pid": 4320, "name": "python.exe", "memory_mb": 201.1 }
]
```

---

## 📂 Project Structure

```text
Kenny-desktop-health/
├── server.py        # Main FastMCP server
├── test_health.py   # Standalone local health test script
└── README.md        # Project documentation
```

---

## ⚠️ Troubleshooting

### `ModuleNotFoundError: No module named 'mcp'`
Install dependencies again:

```bash
pip install mcp psutil
```

If needed, use:

```bash
python -m pip install mcp psutil
```

### `python` command not found
Use `python3` instead:

```bash
python3 server.py
```

Or add Python to PATH.

### Claude cannot connect to server
- Verify the path to `server.py` is correct.
- Confirm `python` is available in your environment.
- Restart Claude Desktop after updating config.
- Run `python server.py` manually to ensure it starts without errors.

### Process list appears incomplete
Some processes may be restricted by OS/user permissions. Run with appropriate permissions if needed.

---

## 🧭 Roadmap Ideas

- Add disk usage and temperature sensors (where supported)
- Add per-core CPU metrics
- Add historical snapshots/trend summaries
- Export metrics as structured logs
- Add optional alert thresholds (high RAM / high CPU)

---

## 📄 License

Choose a license and add it here (for example: MIT).
