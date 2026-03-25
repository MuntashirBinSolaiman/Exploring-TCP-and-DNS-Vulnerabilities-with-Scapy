# Exploring-TCP-and-DNS-Vulnerabilities-with-Scapy

## What
In this project, I explored **TCP and DNS attacks**, focusing on their mechanisms and how to exploit vulnerabilities in network systems. The tasks involved launching various attacks using **Scapy** within a virtualized environment. These attacks were performed within containers (server, client, and attacker) to simulate real-world attack scenarios.

The primary focus was on:
- **TCP Reset Attacks** (disrupting SSH sessions).
- **TCP Session Hijacking** (injecting malicious packets into Telnet and SSH communications).
- **DNS Spoofing** (manipulating DNS queries and responses to redirect traffic).

I also documented the steps taken, explained the attacks, and proposed countermeasures to secure systems against such threats.

## How
### Environment Setup
- **VM Configuration**: I used a virtual machine set up in Lab Week 7, ensuring that the network adapter was configured for internet connectivity.
- **Container Access**: I accessed three containers (server, client, and attacker) using SSH and terminal commands to execute the attacks.
  
For each task, I followed these steps:
1. **TCP Reset Attacks**:
   - I connected to the server container from the client container using SSH.
   - Then, I used **Scapy** on the attacker container to launch a **TCP RST** attack, aiming to disconnect the SSH session.
   
2. **TCP Session Hijacking**:
   - I established a Telnet connection between the client and server containers.
   - Using Scapy, I injected packets to hijack the session, create a directory on the server, and establish a reverse shell to the attacker container.
   - I attempted the same on SSH connections and documented success/failure reasons.

3. **DNS Attacks**:
   - **Local DNS Attack**: Using **Scapy**, I modified the authority nameserver for `example.net`, redirecting traffic to the attacker's DNS server and observing the changes using Wireshark.
   - **Remote DNS Attack**: I configured the DNS server and the attacker container for a **Kaminsky DNS spoofing attack**. After crafting malicious DNS queries, I captured network traffic to demonstrate the attack's success.

### Documentation and Deliverables
- **Code**: All scripts used for attacks were documented, including custom Scapy code for each attack.
- **Screenshots**: I took screenshots of terminal outputs, network traffic captures (using Wireshark), and attack results.
- **Video Demonstrations**: I recorded and shared videos demonstrating the attacks and their outcomes, showcasing the malicious traffic and its effects on the target systems.

## Why
This project was an opportunity to gain **hands-on experience with network attacks** and understand how attackers can exploit vulnerabilities in TCP and DNS protocols. By using **Scapy**, I gained practical experience with tools used in network manipulation and analysis, which are essential for securing modern network systems.

The key learnings include:
- Understanding how **TCP RST attacks** can disrupt active sessions.
- Learning how **session hijacking** works and its implications for sensitive communications.
- Gaining insights into **DNS spoofing** and the risks of domain name hijacking.

These attacks highlight the importance of securing network communications, ensuring that systems are resilient against manipulation, and applying the right countermeasures to mitigate these risks.
