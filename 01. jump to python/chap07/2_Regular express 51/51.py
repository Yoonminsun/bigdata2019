import re

# 대문자로 시작하는 단어 사이에 공백 넣기
def capital_words_spaces(my_str):
    p = re.compile('((?!^)[A-Z])')
    m = p.sub(' \g<1>',my_str)
    return m
print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

