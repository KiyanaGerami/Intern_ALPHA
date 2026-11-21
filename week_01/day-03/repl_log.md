Guess vs Reality

**round(2.675, 2)**

my guess is 2.68
but actual output is 2.67
because 2.675 cannot be stored in binary and actually is sorted as 2.67499999... so python rounds down to 2.67

 **0.1 + 0.2**
 
my guess is 0.3
but actual output is 0.30000000000000004
because 0.1 and 0.2 are repeating fractions in binary. 

**Root Cause**
python uses IEEE 754 (floating point) to store decimals.
therefore floating point numbers are approximations not exact value
