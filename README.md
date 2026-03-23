# Iterative Socket Server Project  
Course: CNT4504 - Computer Networks and Distributed Processing  
Students: Cole Parsons & Anthony Nguyen  

---

## Overview  
This project implements a client-server system designed to analyze the performance of an iterative (single-threaded) server. The goal is to observe how handling requests sequentially impacts system efficiency, specifically focusing on turn-around time as the number of client requests increases.

The system consists of:   
* An iterative server that processes on client request at a time - Created by Cole Parsons  
* A multi threaded client capable of generating multiple simultaneous requests - Created by Anthony Nguyen

## Objectives
* Understand how iterative servers handle client requests  
* Measures and analyze system performance under increasing load  
* Compare the effects of multiple client sessions on response time  
* Gain experience with socket programming and system-level command execution

---

## Features  
### Server Capabilities  
The Server supports the following client requests:  
1. Date and Time - Returns the current system date and time  
2. Uptime - Displays how long the system has been running  
3. Memory Use - Shows current memory usage  
4. Netstat - Lists active network connections  
5. Current Users - Displays logged-in users  
6. Running Processes - Lists active processes  

### Client Capabilities  
* Connects to the server using a specified IP address and port  
* Allows selection of requested operation  
* Spawns multiple threads to simulate concurrent clients  
* Supports request loads of: 1, 5, 10, 15, 20, 25  
* Measures:  
-Individual Turn Around Time  
-Total Turn Around Time  
-Average Turn Around Time

---

## System Architecture  
### Iterative Server  
* Uses a single thread  
* Processes one request at a time (FIFO queue via socket backlog)  
* Steps:  
-Listen for incoming connections  
-Accept client request  
-Execute requested operation  
-Send response back to client  
-Close connection  
-Repeat  

### Multi-threaded Client  
* Uses multiple threads to simulate concurrent users  
* Each thread:  
-Connects to server  
-Sends request  
-Waits for response  
-Measures elapsed time

---

## Technologies Used
* Python
* Socket Programming
* Multi-threading
* Linux System Commands
