# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Sheila Mae Pailaga
Date: October 12, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | | |
| TC02 | Choose 2, enter 33 | Reading added successfully | | |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | | |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | | |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | | |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | | |
| TC07 | Choose 3 | 35 °C -> WARNING | | |
| TC08 | Choose 4 with initial data | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | | |
| TC09 | Enter 9 | Error message; menu shown again | | |
| TC10 | Choose 5 | Exit message; program ends | | |

## Bugs Found and Fixed

Describe at least one bug you found during testing
and how you fixed it.

If you found none, describe the test that was hardest
to pass.
