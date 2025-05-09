# Code Quality Analysis Report

### Tasks:

1. Use two static analysis tools (**flake8, pylint, mypy**)
2. Run **line-profiler** to find bottlenecks and fix them
3. Run **code coverage**

## <u>Summary</u>

### **flake8** report:
- (Line 1) Two unused libraries: `math`, `random`
- (Line 5) Local variable 'output' is assigned to but never used
- (Line 11) No newline at end of file

### **pylint** report:
- (Line 1, 5, 12, 19, 26, 28) Missing docstring 
- (Line 33) Final newline missing

### Line Profiler report:
- Bottleneck found in: 
  - `expensive_op`: 
    - Line 7 & 8: 99.8% of total execution time
      - This function caused `slow_func` to be a significant bottleneck while calling `expensive_op`

### Fixes:
  - Removed unused libraries
  - Inner loop inside `expensive_op` replaced with a math formula
  - `slow_func` simplified using list comprehension
  - Removed trailing whitespaces
  - Removed unused variable `output` (directly printed `slow_func` result rather than creating and assigning result to new variable)

### Results (line-profiler):
  - `expensive_op` runs 97% faster after optimizations
    - Before Optimizations: 0.36 seconds
    - After Optimizations: 0.0084 seconds
  - `slow_func` runs 99% faster after optimizations
    - Before Optimizations: 0.72 seconds
    - After Optimizations: 0.011 seconds