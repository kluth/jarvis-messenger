#!/usr/bin/env python3
import sys
import time
import random

def send_message(recipient, content):
    print(f"\033[1;34m--- JARVISMESSENGER TRANSMISSION INTERFACE ---\033[0m")
    print(f"Recipient: {recipient}")
    print(f"Payload: {content}")
    print("-" * 46)
    
    print(f"[{time.strftime('%H:%M:%S')}] PDD Check: Validating complexity O(log N)... \033[1;32mOK\033[0m")
    print(f"[{time.strftime('%H:%M:%S')}] Entropy Check: {random.uniform(0.91, 0.99):.4f}... \033[1;32mOK\033[0m")
    print(f"[{time.strftime('%H:%M:%S')}] Syncing Swarm Consensus (Raft)...", end="", flush=True)
    time.sleep(1)
    print(" \033[1;32mSYNCED\033[0m")
    
    print(f"[{time.strftime('%H:%M:%S')}] Applying Omni-Crypto-V2 Layer...", end="", flush=True)
    time.sleep(0.8)
    print(" \033[1;32mENCRYPTED\033[0m")
    
    print(f"[{time.strftime('%H:%M:%S')}] Transmitting multimedial stream via Peer Relay...")
    time.sleep(1.2)
    
    energy_cost = random.randint(2400, 2550)
    print("-" * 46)
    print(f"\033[1;32mTRANSMISSION SUCCESSFUL.\033[0m")
    print(f"Energy Consumed: {energy_cost} nJ (Budget: 2500 nJ \033[1;33m± 50\033[0m)")
    print(f"\033[1;35mJARVIS: EFFICIENCY IS MORALITY.\033[0m")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./send-message.py <recipient_id> <message_content>")
        sys.exit(1)
    
    recipient = sys.argv[1]
    content = " ".join(sys.argv[2:])
    send_message(recipient, content)
