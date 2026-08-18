# ===========================================================
# Practical No. 1
# Simple Reflex Agent
# ===========================================================

import random
import time
import os
import datetime

# Display Program Title
print("=" * 60)
print(" SIMPLE REFLEX AGENT")
print("=" * 60)

# Display Current Date and Time
current_time = datetime.datetime.now()

print("\nCurrent Date :", current_time.strftime("%d-%m-%Y"))
print("Current Time :", current_time.strftime("%H:%M:%S"))

# Display Operating System
print("\nOperating System :", os.name)

# Generate Random Room Status
room_status = random.choice(["Dirty", "Clean"])

print("\nChecking Room Status...")

# AI Thinking Delay
time.sleep(2)

print("\nRoom Status :", room_status)

# Reflex Agent Decision
if room_status == "Dirty":
    print("\nAI Decision : Start Cleaning")
    time.sleep(2)
    print("Action : Room Cleaned Successfully")
else:
    print("\nAI Decision : No Cleaning Required")
    print("Action : Room is Already Clean")

# Program End
print("\nTask Completed Successfully.")
print("=" * 60)
