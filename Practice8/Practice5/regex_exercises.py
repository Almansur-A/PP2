import re

# 1. 'a' followed by zero or more 'b'
def match_a_b0(s):
    pattern = r"ab*"
    return bool(re.fullmatch(pattern, s))

# 2. 'a' followed by two to three 'b'
def match_a_b23(s):
    pattern = r"ab{2,3}"
    return bool(re.fullmatch(pattern, s))

# 3. sequences of lowercase letters joined with underscore
def find_lowercase_underscore(s):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, s)

# 4. one uppercase letter followed by lowercase letters
def find_capital_words(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)

# 5. 'a' followed by anything ending in 'b'
def match_a_any_b(s):
    pattern = r"a.*b$"
    return bool(re.match(pattern, s))

# 6. replace space, comma, or dot with colon
def replace_symbols(s):
    return re.sub(r"[ ,\.]", ":", s)

# 7. snake_case → camelCase
def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), s)

# 8. split string at uppercase letters
def split_at_uppercase(s):
    return re.split(r"(?=[A-Z])", s)

# 9. insert spaces between words starting with capital letters
def insert_spaces(s):
    return re.sub(r"([A-Z])", r" \1", s).strip()

# 10. camelCase → snake_case
def camel_to_snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower()

# Example tests
if __name__ == "__main__":
    print(match_a_b0("abbb"))
    print(match_a_b23("abb"))
    print(find_lowercase_underscore("hello_world test_case"))
    print(find_capital_words("Hello World Python"))
    print(match_a_any_b("a123b"))
    print(replace_symbols("Hello, world. Python"))
    print(snake_to_camel("hello_world_test"))
    print(split_at_uppercase("HelloWorldPython"))
    print(insert_spaces("HelloWorldPython"))
    print(camel_to_snake("helloWorldTest"))