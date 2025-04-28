# Python_Mininet_Simulator

Mininet Simulator written in Python

---

## 1. Setup and Execution

### Clone the Repository

Clone the repository using the following command:

```
git clone https://github.com/50516021/Python_P2P_fileshare.git
```

### Environment Setup

Install the required dependencies using `requirements.txt`:

```
pip install -r requirements.txt
```

---

## 2. Running the Application

The main script, `main.py`, provides peer discovery, file sharing, and file downloading functionality.  
**Note:** Open multiple terminals to simulate different peers.

### 2.1 Starting the Application

Run the following command to start the P2P file-sharing system:

```
python main.py [TRANSFER_PORT]
```

- `TRANSFER_PORT` (optional): The port number for file transfers. Defaults to `10000`.
  (port 10000 is for two machines)

---

## 3. Layer 3 Network Simulation

The `layer3_network_code.py` script simulates a Layer 3 network using Mininet. It creates a topology with three routers and multiple hosts connected to each router.

### 3.1 Network Topology

- **Routers**: `rA`, `rB`, `rC`
- **Hosts**:
  - LAN A: `hA1 (20.10.172.1/26)`, `hA2 (20.10.172.2/26)`
  - LAN B: `hB1 (20.10.172.65/25)`, `hB2 (20.10.172.66/25)`
  - LAN C: `hC1 (20.10.172.129/27)`, `hC2 (20.10.172.130/27)`
- **Router Interconnections**:
  - `rA ↔ rB`: `20.10.100.1/24` (rA), `20.10.100.4/24` (rB)
  - `rB ↔ rC`: `20.10.100.3/24` (rB), `20.10.100.6/24` (rC)
  - `rC ↔ rA`: `20.10.100.5/24` (rC), `20.10.100.2/24` (rA)

### 3.2 Running the Simulation

Run the following command to start the network simulation:

```
sudo python layer3_network_code.py
```

### 3.3 Features

- **IP Configuration**: Each router and host is manually configured with IP addresses.
- **IP Forwarding**: Enabled on all routers to allow packet forwarding.
- **Connectivity Testing**: The script tests basic LAN connectivity using `pingAll`.

### 3.4 Interactive CLI

After starting the simulation, an interactive Mininet CLI is available for further testing and debugging.

---

## 4. Notes

- Ensure that Mininet is installed on your system.
- Run the scripts with `sudo` to avoid permission issues.
- Use the Mininet CLI to test connectivity or modify the network dynamically.

---

## 5. Author

**Akira Takeuchi**

- [GitHub](https://github.com/50516021)
- [Official Homepage](https://akiratakeuchi.com/)

---
