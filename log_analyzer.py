# log_analyzer.py

# Read sample log file
with open("sample.log", "r") as file:
    logs = file.readlines()

# Detect failed logins
failed_ips = {}
for line in logs:
    if "Failed login" in line:
        print("Alert detected:", line.strip())
        # Extract IP (assumes last part of line is IP)
        ip = line.strip().split()[-1]
        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

# Print summary
print("\nSummary of failed logins by IP:")
for ip, count in failed_ips.items():
    print(f"{ip}: {count} failed attempts")


