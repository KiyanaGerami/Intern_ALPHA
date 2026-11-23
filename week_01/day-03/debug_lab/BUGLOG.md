# BUGLOG

## Bug 1: in_virtualenv
Symptom: returns False even inside a venv
Cause: inverted comparison (== instead of !=)
Fix: prefix != base_prefix

## Bug 2: check_version
Symptom: "3.10" is reported as "too old"
Cause: string comparison ("1" < "9"), not numeric
Fix: convert the version to a tuple of ints before comparing

## Bug 3: hnit typo
Symptom: NameError when the version is too old
Cause: variable misspelled (hnit instead of hint)
Fix: use the correct variable name, hint

## Bug 4: describe_interpreter
Symptom: Symptom: in the REPL the f-string line printed the right sentence, but in a script the function returns just "3.12" instead of a full sentence
Cause: the f-string was built but never returned
Fix: return f"interpreter: Python {version} at {path}"

## Lesson: REPL vs Script
In the REPL, the value of every expression is printed automatically, so a
bare f-string line on its own shows output and seems to "work". In a script,
nothing is printed automatically, so that line does nothing visible. Also, a
script only runs the lines its control flow reaches, so the hnit typo stays
hidden until the "too old" branch actually executes, and then the script
crashes with a NameError. The REPL hides these problems because it echoes
results and you test one line at a time. A script reveals them because it runs
the whole flow with no automatic echo.
