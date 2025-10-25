from datetime import datetime
import random

# File that will be updated every time
filename = "daily_log.txt"

# Generate a new line entry with timestamp and random number
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
entry = f"{now} — Auto update #{random.randint(1000, 9999)}\n"

# Append to file (or create if it doesn’t exist)
with open(filename, "a") as f:
    f.write(entry)

print(f"✅ Updated {filename} with new entry at {now}")
