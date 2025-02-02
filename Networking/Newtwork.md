# DevOps and Networking Notes

## OSI Model (Open Systems Interconnection)

### Application Layer
- Provides network services to end users.
- Protocols:
  - **HTTP**: Default port 80 (HTTP) or 443 (HTTPS).
  - **FTP**: Port 20/21 (File Transfer).
  - **SMTP**: Port 25 (Simple Mail Transfer Protocol).

### Presentation Layer
- Handles encoding and encryption.
  - **Encoding**: Uses algorithms.
  - **Encryption**: Uses algorithms and keys provided by the encrypting party.

### Session Layer
- Manages connections:
  - Establishes, maintains, and terminates connections.

### Transport Layer (TCP - Transmission Control Protocol)
- Manages end-to-end communication, data transfer, and error handling.
- TCP is connection-oriented; it waits for a response after sending data.

### Network Layer
- Handles routing and forwarding of data packets (e.g., IP).

### Data Link Layer
- Divides data into frames.
- Responsible for node-to-node delivery, error detection/correction, and encoding/decoding.
- Technologies: Ethernet.

### Physical Layer
- Transfers data in the form of bits (0s and 1s) using cables.
- Deals with hardware transmission (e.g., cables, switches).

---

## Network Types

### LAN (Local Area Network)
- Connects devices in a small area (e.g., home, office).
- Devices: Computers, printers.

### WAN (Wide Area Network)
- Spans large geographic areas (e.g., cities, countries).
- Example: The internet.

### MAN (Metropolitan Area Network)
- Covers a city or large campus.

### PAN (Personal Area Network)
- Connects personal devices within a few meters (e.g., Bluetooth).

---

## Networking Devices

### Nodes
- Any device like a computer or laptop.

### Host
- Only computers.

### Protocols
- Set of rules for data transfer.
  - **SSH**: Port 22.
  - **DNS**: Port 53.
  - **HTTP**: Port 80.
  - **HTTPS**: Port 443.
  - **MySQL**: Port 3306.

### Sockets
- Combination of IP address and port.

### Port
- Identifies specific processes or services.

---

## MODEM and ROUTER

### MODEM
- **Function**: Translates signals (analog to digital and vice versa).
- **Purpose**: Connects to the network via LAN.

### ROUTER
- **Function**: Forwards data between different networks.
- **Purpose**: Distributes the network.

---

## DNS (Domain Name System)
- Converts domain names (e.g., `www.google.com`) to IP addresses (e.g., `190.263.22.9.0`).

---

## HTTP Overview

### HTTP Methods
- **200 OK**: Successful request.
- **201 Created**: Resource created (POST).
- **204 No Content**: No content to return.
- **301 Moved Permanently**: Resource moved permanently.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: Server error.

---

## VPN (Virtual Private Network)
- Allows secure and private connections to a private network.
- Types:
  - **Remote Access VPN**: For remote users.
  - **Site-to-Site VPN**: Connects networks of different locations.
  - **Cloud VPN**: Securely connects to cloud infrastructure.
  - **Mobile VPN**: Securely connects mobile devices.
  - **SSL VPN**: Uses SSL protocol for secure connections.

---

## Checksum
- Error detection method.
- Uses a checksum generator (sender) and checker (receiver).

---

## Cookies
- Small text files stored by websites to remember user preferences or login status.
- Types:
  - **Session Cookies**: Deleted when the browser is closed.
  - **Persistent Cookies**: Stored for a longer duration.

---

## Scalability and Elasticity

### Scalability
- Ability to handle growing workloads.
  - **Vertical Scaling**: Adding resources to a single machine.
  - **Horizontal Scaling**: Adding more machines to the network.

### Elasticity
- Ability to dynamically adjust resources based on demand.

---

## Network Topologies

### Bus Topology
- Single central cable connects all devices.

### Star Topology
- All devices connected to a central hub.

### Ring Topology
- Devices connected in a circular manner.

### Mesh Topology
- Every device connected to every other device.

### Hybrid Topology
- Combination of two or more topologies.

---

## TCP/IP Model

### Application Layer
- Protocols: HTTP, FTP, SMTP, DNS.

### Transport Layer
- Protocols: TCP, UDP.

### Internet Layer
- Protocols: IP, ICMP, ARP.

### Network Access Layer
- Protocols: Ethernet, Wi-Fi.

---

## Networking Protocols

### TCP (Transmission Control Protocol)
- Connection-oriented, reliable data transfer.

### UDP (User Datagram Protocol)
- Connectionless, fast data transfer.

### IP (Internet Protocol)
- Handles logical addressing and routing.

### Ethernet
- Used in LANs for data framing and transmission.

### Wi-Fi
- Wireless networking protocol.

---

## IP Addressing and Subnetting

### IPv4 vs IPv6
- **IPv4**: 32-bit address (e.g., `192.168.1.1`).
- **IPv6**: 128-bit address (e.g., `2001:0db8:85a3::`).

### Subnetting
- Divides a network into smaller subnets for efficient IP address usage.

---

## Network Services

### DHCP (Dynamic Host Configuration Protocol)
- Automatically assigns IP addresses to devices.

### HTTP (Hypertext Transfer Protocol)
- Used for web page transmission.

### FTP (File Transfer Protocol)
- Used for file transfers.

### SMTP (Simple Mail Transfer Protocol)
- Used for sending emails.

### POP3/IMAP
- Used for retrieving emails.

---

## Network Architectures

### Client-Server Architecture
- Centralized server handles requests from multiple clients.

### Peer-to-Peer (P2P) Architecture
- Devices act as both clients and servers.

### Service-Oriented Architecture (SOA)
- Breaks applications into reusable services.

### Microservices Architecture
- Divides applications into small, independent services.

---

## 3-Way Handshake (TCP Connection Establishment)
1. **SYN**: Client sends a synchronization request.
2. **SYN-ACK**: Server acknowledges the request.
3. **ACK**: Client confirms the connection.

---

## Firewall
- Monitors and controls incoming/outgoing traffic based on security rules.

---

## Symmetric vs Asymmetric Encryption

### Symmetric Encryption
- Uses the same key for encryption and decryption (e.g., AES).

### Asymmetric Encryption
- Uses a public key for encryption and a private key for decryption (e.g., RSA).

---

## IPSec (Internet Protocol Security)
- Secures IP communications through encryption and authentication.

---

## Reverse Proxy
- Sits between clients and backend servers to forward requests.

---

## References
- [Types of Virtual Private Network (VPN) and its Protocols - GeeksforGeeks](https://www.geeksforgeeks.org/types-of-virtual-private-network-vpn-and-its-protocols/)