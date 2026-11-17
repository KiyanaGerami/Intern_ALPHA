# Bug log: Binary 

#Bug 1 :zero input in 'to_binary' function

Symptom: The function returned an empty string `""` when the input was `0`. The expected output was the string `"0"`.
Hypothesis: The `while n > 0:` loop does not execute for the number zero. Therefore, the `bits` variable, initialized as an empty string, is returned without any changes.
Experiment: Ran `print(to_binary(0))` in the Python environment and confirmed the output was empty.
Root cause: The function lacked a base case (edge case) handling for the number zero before entering the loop.
Fix: Added an `if n == 0:` condition at the beginning of the function to return `"0"` immediately.
Lesson: Always consider edge cases (like `0`, negative numbers, or empty inputs) when writing loops or recursive functions.
