def isValid(s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        for bracket in s:
            if bracket == '(':
                if s.count(')') != s.count(bracket):
                    return False
            elif bracket == '[':
                if s.count(']') != s.count(bracket):
                    return False
            else:
                if s.count('}') != s.count(bracket):
                    return False
        return True

print(isValid("()"))