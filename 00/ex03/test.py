from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

NULL_not_found(Nothing)             # Nothing: None <class 'NoneType'>$
NULL_not_found(Garlic)              # Cheese: nan <class 'float'>$
NULL_not_found(Zero)                # Zero: 0 <class 'int'>$
NULL_not_found(Empty)               # Empty: <class 'str'>$
NULL_not_found(Fake)                # Fake: False <class 'bool'>$
print(NULL_not_found("Brian"))      # Type not Found
# 1