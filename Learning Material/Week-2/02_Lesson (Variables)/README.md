# Python Variable Naming Rules

## Rules

1. **Start with a Letter or Underscore**: Variable names must start with a letter (a-z, A-Z) or an underscore (_). They cannot start with a digit (0-9).
   - Valid: `myVariable`, `_my_variable`
   - Invalid: `1variable`, `9name`

2. **Follow with Letters, Digits, or Underscores**: After the first character, variable names can contain letters, digits, or underscores.
   - Valid: `myVariable1`, `variable_2`
   - Invalid: `my-variable`, `my variable`

3. **Case Sensitivity**: Variable names are case-sensitive, meaning `myVariable` and `myvariable` are considered different variables.

4. **No Spaces**: Variable names cannot contain spaces. Use underscores to separate words.
   - Valid: `my_variable`
   - Invalid: `my variable`

5. **Reserved Words**: Avoid using Python reserved words or keywords as variable names (e.g., `class`, `for`, `if`, `else`, `True`, `False`, etc.). These words have special meanings in Python and cannot be used as variable names.
