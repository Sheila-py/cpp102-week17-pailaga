# Laboratory Exercise 17
## Simulated Device Monitoring and Alert System

### Project Description
This Python program simulates a device temperature
monitoring system. It stores temperature readings,
classifies them, validates new inputs, and generates
a numerical summary.

### Features
1. View Readings
2. Add Reading
3. Classify Readings
4. Generate Summary
5. Exit

### Classification Rules
- Below 30 degrees Celsius: NORMAL
- 30 to 35 degrees Celsius: WARNING
- Above 35 degrees Celsius: CRITICAL

### Overall Status Rules
- At least one CRITICAL reading: ATTENTION REQUIRED
- Otherwise, at least one WARNING reading: MONITOR
- Otherwise: NORMAL

### How to Run
Run the following command in the terminal:

python device_monitor.py

### Sample Output

MONITORING SUMMARY

Number of readings : 5
Total of readings  : 160
Average temperature: 32.00 °C
Minimum temperature: 28 °C
Maximum temperature: 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED