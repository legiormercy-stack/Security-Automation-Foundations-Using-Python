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

### Code Description

The code performs the following actions:

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
