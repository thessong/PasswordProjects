# PasswordProjects
### Crack_common_pw: 
- Checks for password against a dictionary of common passwords
- Accepts either argument or hidden password
```
python crack_common_pw.py [password] [args]
```

### Word_gen: 
- Creates random passwords 
- Selects random words from a dictionary
```
python word_gen.py
```
| Argument  | Outcome |
|:-------------:|:-------------:|
|-w| Generate random words|

### Crack_1word_pw: 
- Checks English dictionary for aword
- Tries with a symbol at the end
- Uncomment code line to add more symbols
- Brute force password with character iteration loop
- Accepts either argument or hidden password
```
python crack_1word_pw.py [password] [args]
```
| Argument  | Outcome |
|:-------------:|:-------------:|
|-s| Evaluate with symbols at end|
|-v| Password hidden in output|
|-c| Brute force all letter combinations|

### Crack_2word_pw: 
- Checks English dictionary for two words put together
- Tries with symbol at the end
- Uncomment code line to add more symbols
- Accepts either argument or hidden password
```
python crack_2word_pw.py [password] [args]
```
| Argument  | Outcome |
|:-------------:|:-------------:|
|-s| Evaluate with symbols at end|
|-v| Password hidden in output|