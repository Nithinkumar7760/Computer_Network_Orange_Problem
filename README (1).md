#  SDN-Based Path Tracing Tool

**Student:** Nithin  
**SRN:** PES1UG25CS829  
**Subject:** Computer Networks  
**Level:** Orange — Problem Statement 20  
**University:** PES University, Bengaluru  

---

##  What is this project?

This is an **SDN-Based Path Tracing Tool** built using POX Controller and Mininet.

When a packet travels from one computer to another in a network, it passes through multiple switches. This tool **automatically detects and displays the exact path** that packet took — like a GPS for network packets! 🗺️⚡

---

##  How does it work?

1. **Mininet** creates a virtual network with switches and hosts inside your laptop
2. **POX Controller** acts as the brain — one central boss controlling all switches
3. Our **path_tracer.py** code runs inside POX and:
   - Learns where each host is located (which switch, which port)
   - Uses **BFS (Breadth First Search)** to find the path between switches
   - Prints the full route every time a packet travels

---

##  Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| Mininet | 2.3.0 | Virtual network emulator |
| POX Controller | 0.7.0 | SDN Controller |
| Python | 3.12 | Programming language |
| Ubuntu | 24.04 | Operating System |

---

##  Network Topology

```
h1 --- Switch1 --- Switch2 --- Switch3 --- h3
                      |
                      h2
```

Linear topology with **3 switches** and **3 hosts**

---

##  How to Run

### Step 1 — Clone this repo
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### Step 2 — Copy code into POX
```bash
cp path_tracer.py ~/pox/ext/
```

### Step 3 — Open Two Terminals

**Terminal 1 — Start POX Controller:**
```bash
cd ~/pox
python3 pox.py path_tracer
```

**Terminal 2 — Start Mininet:**
```bash
sudo mn --controller=remote --topo=linear,3
```

### Step 4 — Run the test
In Terminal 2 type:
```bash
h1 ping h3
```

### Step 5 — See the magic in Terminal 1!! 🎉
```
INFO: path_tracer: PATH FOUND: xx:xx --> xx:xx
INFO: path_tracer: Route: Switch 1 --> Switch 2 --> Switch 3
```

---

##  Screenshots

### Mininet — h1 ping h3 running successfully
![Mininet Output](screenshots/mininet.png)

### POX Controller — Path Tracer showing full route
![POX Output](screenshots/pox_output.png)

---

##  Project Structure

```
├── README.md              ← You are here!!
├── path_tracer.py         ← Main controller code
└── screenshots/
    ├── mininet.png        ← Mininet ping output
    └── pox_output.png     ← Path tracer output
```

---

##  Key Concepts

**SDN (Software Defined Networking)** — One central controller controls all switches. Switches don't make their own decisions.

**POX Controller** — The software that acts as the SDN controller brain.

**Mininet** — A network simulator that creates fake switches and hosts inside your laptop for testing.

**BFS Algorithm** — Breadth First Search — finds the shortest path between two switches in the network map.

---

*Built with by Nithin | PES1UG25CS829 | PES University*
