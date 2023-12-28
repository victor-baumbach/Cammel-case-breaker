from re import sub

def solution(s):
    return sub(r"([a-z])([A-Z])", r"\1 \2", s)

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
