'''
questions={
    "q1":"what is the extension of python file",
    "options" :{"A":".sp", "B":".cpp","C":".os","D":".py"},
    "correct" :"D"
    }
for i in questions:
    print(questions["q1"])
    print(questions["options"])
    print(questions["correct"])


questions = [
    {
        "q1": "what is the extension of python file",
        "options": {"A": ".sp", "B": ".cpp", "C": ".os", "D": ".py"},
        "correct": "D"
    },
    {
        "q1": "what is default data type of input in python",
        "options": {"A": "int", "B": "float", "C": "str", "D": "bool"},
        "correct": "C"
    },
    {
        "q1": "which keyword is used to define a function in python",
        "options": {"A": "func", "B": "def", "C": "function", "D": "define"},
        "correct": "B"
    },
    {
        "q1": "which symbol is used for comments in python",
        "options": {"A": "//", "B": "/* */", "C": "#", "D": "<!-- -->"},
        "correct": "C"
    },
    {
        "q1": "which data type is used to store multiple values",
        "options": {"A": "int", "B": "float", "C": "list", "D": "str"},
        "correct": "C"
    },
    {
        "q1": "what is the output of print(type(10))",
        "options": {"A": "<class 'str'>", "B": "<class 'int'>", "C": "<class 'float'>", "D": "<class 'bool'>"},
        "correct": "B"
    },
    {
        "q1": "which loop is used to iterate over a sequence",
        "options": {"A": "while", "B": "do-while", "C": "for", "D": "switch"},
        "correct": "C"
    },
    {
        "q1": "how do you take input from the user in python",
        "options": {"A": "scan()", "B": "cin", "C": "input()", "D": "read()"},
        "correct": "C"
    },
    {
        "q1": "which operator is used for exponentiation",
        "options": {"A": "^", "B": "**", "C": "//", "D": "%"},
        "correct": "B"
    },
    {
        "q1": "which keyword is used to check a condition",
        "options": {"A": "if", "B": "when", "C": "check", "D": "case"},
        "correct": "A"
    }
]
ans =0
for i in questions:
    print(i["q1"])
    print("options are :")
    print(f" A: {i["options"]["A"]} \n")
    print(f" B:{ i["options"]["B"]} \n")
    print(f" c: {i["options"]["C"]} \n")
    print(f" D : {i["options"]["D"]} \n")
    m = input("enter the option \n")
    if(m==i["correct"]):
        ans = ans+1
        print("yeah correct answer")
        
    else:
        print("sorry wrong answer")
print(f"your total score is {ans}")
    '''




questions = {
    1: {
        "q1": "what is the extension of python file",
        "options": {"A": ".exe", "B": ".java", "C": ".py", "D": ".html"},
        "correct": "C"
    },
    2: {
        "q1": "what is the default data type returned by input()",
        "options": {"A": "int", "B": "float", "C": "bool", "D": "str"},
        "correct": "D"
    },
    3: {
        "q1": "which keyword is used to define a function in python",
        "options": {"A": "function", "B": "def", "C": "fun", "D": "define"},
        "correct": "B"
    },
    4: {
        "q1": "which symbol is used for single line comment in python",
        "options": {"A": "//", "B": "/* */", "C": "#", "D": "--"},
        "correct": "C"
    },
    5: {
        "q1": "which data type is used to store multiple values in python",
        "options": {"A": "int", "B": "float", "C": "list", "D": "str"},
        "correct": "C"
    },
    6: {
        "q1": "what is the output of print(type(5))",
        "options": {"A": "<class 'str'>", "B": "<class 'float'>", "C": "<class 'int'>", "D": "<class 'bool'>"},
        "correct": "C"
    },
    7: {
        "q1": "which loop is used to iterate over a sequence in python",
        "options": {"A": "while", "B": "for", "C": "do while", "D": "switch"},
        "correct": "B"
    },
    8: {
        "q1": "which function is used to take input from the user",
        "options": {"A": "scan()", "B": "cin", "C": "input()", "D": "read()"},
        "correct": "C"
    },
    9: {
        "q1": "which operator is used for exponentiation in python",
        "options": {"A": "^", "B": "*", "C": "**", "D": "//"},
        "correct": "C"
    },
    10: {
        "q1": "which keyword is used for decision making in python",
        "options": {"A": "if", "B": "when", "C": "case", "D": "switch"},
        "correct": "A"
    }
}

ans =0
for i in questions:
    print(questions[i]["q1"])
    print(questions[i]["options"])
    print(questions[i]["correct"])
    m = input("enter the option \n")
    if(m==questions[i]["correct"]):
        ans = ans+1
        print("yeah correct answer")
        
    else:
        print("sorry wrong answer")










































