[log_analyzer.py](https://github.com/user-attachments/files/27276126/log_analyzer.py)# Security-Automation-Foundations-Using-Python

## Objective
To develop foundational security automation skills by using Python to parse and analyze log files, detect failed login attempts, and generate summarized security insights for incident detection.


### Skills Learned
- Basic security automation using Python
- Log parsing and analysis
- Pattern detection using string matching
- Identifying failed login attempts (authentication monitoring)
- Writing scripts for SOC task automation
- Extracting and processing IP address data


### Tools Used
- Python for scripting and automation.
- Visual Studio Code for development environment.
- Sample log file (sample.log) for input data for analysis.

## Steps
[Uploading log# log_analyzer.py

#Read sample log file
with open("sample.log", "r") as file:
    logs = file.readlines()

#Detect failed logins
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

#Print summary
print("\nSummary of failed logins by IP:")
for ip, count in failed_ips.items():[sample.log](https://github.com/user-attachments/files/27276144/sample.log)

    print(f"{ip}: {count} failed attempts")


_analyzer.py…]()


[Uploading sample.log…]()
2026-02-19 08:12:45 Failed login from 192.168.1.10
2026-02-19 08:13:00 Successful login from 192.168.1.12
2026-02-19 08:14:21 Failed login from 10.0.0.5
2026-02-19 08:15:00 Failed login from 192.168.1.10

### Code Description

This code performs the following actions:

- Reads log data from a file (sample.log)
- Iterates through each log entry
- Identifies failed login attempts using keyword matching (“Failed login”)
- Extracts IP addresses from each relevant log entry
- Tracks the number of failed attempts per IP address using a dictionary
- 
Outputs:
<img width="1366" height="720" alt="Screenshot (564)" src="https://github.com/user-attachments/assets/b0be735b-175b-4a11-832a-c8c3776dec35" />

- Real-time alerts for each failed login detected
- A summary report showing total failed attempts grouped by IP

This demonstrates the ability to automate basic security monitoring tasks and extract actionable insights from raw log data.

## Key Findings
- Multiple failed login attempts were detected from specific IP addresses.
- Certain IPs showed repeated failures, which may indicate brute-force attempts.
- Automating log analysis significantly reduces manual effort and improves detection speed.
