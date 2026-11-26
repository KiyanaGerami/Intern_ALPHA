# Time Conversion Project



**Input: `200000`** ➔ **Output:** `2 days 07:33:20`
**Input: `59`** ➔ **Output:** `0 days 00:00:59`
**Input: `3600`** ➔ **Output:** `0 days 01:00:00`
**Input: `86400`** ➔ **Output:** `1 days 00:00:00`

Trace Table (Input: 200000)

| Line | Code / Operation | Variable Values |
| :--- | :--- | :--- |
| 1 | `seconds = int(input("enter seconds: "))` | `seconds = 200000` |
| 2 | `days, rest = divmod(seconds, 86400)` | `days = 2`, `rest = 27200` |
| 3 | `hour, rest = divmod(rest, 3600)` | `hour = 7`, `rest = 2000` |
| 4 | `minute, rest = divmod(rest, 60)` | `minute = 33`, `rest = 20` |
| 5 | `second = rest` | `second = 20` |
| 7 | `print(...)` | Output: `2 days 07:33:20` |
