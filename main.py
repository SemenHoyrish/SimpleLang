

from ast import Num
import functools
from traceback import print_tb
from turtle import left
from winsound import PlaySound


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIGNS = "+-/*"

def report_error(text: str):
    print("[ERROR] " + text)

class Type:
    name: str = "type"
    default_value = None

class Integer(Type):
    name: str = "integer"
    default_value = 0

class Variable:
    type: Type = None
    value = None

    def __init__(self, type: Type, value=None) -> None:
        self.type = type
        if value == None:
            self.value = self.type.default_value
        else:
            self.value = value
    
    def parse_value(self, value) -> bool:
        if self.type == Integer:
            try:
                self.value = int(value)
                return True
            except:
                report_error("Incorrect value type")
                return False
        else:
            return False

types = {
    "int": Integer,
}

vars = {}


last_value = None


class Token:
    value = None
    def __init__(self, value):
        self.value = value

class NumberToken(Token):
    pass

class VariableNameToken(Token):
    pass

class SignToken(Token):
    left: Token = None
    right: Token = None
    result = None
    def calc(self):
        left_res = None
        right_res = None

        if type(self.left) == NumberToken:
            left_res = self.left.value
        if type(self.left) == VariableNameToken:
            left_res = vars[self.left.value].value
        if isinstance(self.left, SignToken):
            if self.left.result == None:
                self.left.calc()
            left_res = self.left.result


        if type(self.right) == NumberToken:
            right_res = self.right.value
        if type(self.right) == VariableNameToken:
            right_res = vars[self.right.value].value
        if isinstance(self.right, SignToken):
            if self.right.result == None:
                self.right.calc()
            right_res = self.right.result

        if type(self) == PlusToken:
            self.result = left_res + right_res
        if type(self) == MinusToken:
            self.result = left_res - right_res
        if type(self) == StarToken:
            self.result = left_res * right_res
        if type(self) == SlashToken:
            self.result = left_res / right_res
            

class PlusToken(SignToken):
    def __init__(self):
        super().__init__("+")
class MinusToken(SignToken):
    def __init__(self):
        super().__init__("-")
class StarToken(SignToken):
    def __init__(self):
        super().__init__("*")
class SlashToken(SignToken):
    def __init__(self):
        super().__init__("/")

signs_priority = {
    StarToken: 1,
    SlashToken: 1,
    PlusToken: 0,
    MinusToken: 0
}


def run(text: str):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line.startswith("//"):
            continue

        elif line.startswith("def"):
            line = line.replace("def ", "")
            t, n = line.split(" ")
            t = t.strip()
            n = n.strip()
            vars[n] = Variable(types[t])
        
        elif line.startswith("in"):
            line = line.replace("in ", "")
            n = line.strip()
            if n not in vars.keys():
                report_error("Indefined variable")
                return
            
            inp = input()
            r = vars[n].parse_value(inp)
            if r == False:
                report_error("??")
                return

            last_value = vars[n].value
        
        elif line.strip() == "out":
            print(last_value)

        elif line.startswith("set"):
            line = line.replace("set ", "")
            n = line.strip()
            if n not in vars.keys():
                report_error("Indefined variable")
                return

            r = vars[n].parse_value(last_value)
            if r == False:
                report_error("??/")
                return

        elif line.startswith("get"):
            line = line.replace("get ", "")
            n = line.strip()
            if n not in vars.keys():
                report_error("Indefined variable")
                return

            last_value = vars[n].value

        else:
            symbols = list(line)
            # print(symbols)
            tokens = []
            number_str = ""
            last_symbol_is_digit = False
            var_name = ""
            last_symbol_is_letter = False
            for symbol in symbols:
                if symbol == " ": continue    
                if symbol.isdigit():
                    if last_symbol_is_letter:
                        last_symbol_is_letter = False
                        tokens.append([VariableNameToken(var_name), False])

                    if not last_symbol_is_digit:
                        number_str = ""
                    number_str += symbol
                    last_symbol_is_digit = True

                elif symbol in SIGNS:
                    if last_symbol_is_digit:
                        last_symbol_is_digit = False
                        tokens.append([NumberToken(int(number_str)), False])
                    if last_symbol_is_letter:
                        last_symbol_is_letter = False
                        tokens.append([VariableNameToken(var_name), False])

                    if symbol == "+":
                        tokens.append([PlusToken(), False])
                    elif symbol == "-":
                        tokens.append([MinusToken(), False])
                    elif symbol == "*":
                        tokens.append([StarToken(), False])
                    elif symbol == "/":
                        tokens.append([SlashToken(), False])
                
                else:
                    if last_symbol_is_digit:
                        last_symbol_is_digit = False
                        tokens.append([NumberToken(int(number_str)), False])

                    if not last_symbol_is_letter:
                        var_name = ""
                    var_name += symbol
                    last_symbol_is_letter = True

            if last_symbol_is_digit:
                last_symbol_is_digit = False
                tokens.append([NumberToken(int(number_str)), False])
            if last_symbol_is_letter:
                last_symbol_is_letter = False
                tokens.append([VariableNameToken(var_name), False])

            sign_tokens = []
            for i, [token, used] in enumerate(tokens):
                # print("TOKEN: ", token.value, " with type: ", type(token))
                if isinstance(token, SignToken):
                    sign_tokens.append( [i, token] )
            # print()

            def compare(a, b):
                return signs_priority[type(a[1])] - signs_priority[type(b[1])]

            sign_tokens.sort(key=functools.cmp_to_key(compare), reverse=True)
            for index, token in sign_tokens:
                # print(tokens)
                if not tokens[index - 1][1]:
                    token.left = tokens[index - 1][0]
                    tokens[index - 1][1] = True
                else:
                    tmp = 2
                    while tokens[index - tmp][1]:
                        tmp += 1
                    token.left = tokens[index - tmp][0]
                    tokens[index - tmp][1] = True
                if not tokens[index + 1][1]:
                    token.right = tokens[index + 1][0]
                    tokens[index + 1][1] = True
                else:
                    tmp = 2
                    while tokens[index + tmp][1]:
                        tmp += 1
                    token.right = tokens[index + tmp][0]
                    tokens[index + tmp][1] = True
                

                # print(index, end="  ")
                # print(token, end="  ")
                # print(signs_priority[type(token)], end="  ")
                # print()

            # for index, token in sign_tokens:
            #     print(index)
            #     print(token.value)
            #     print(token.left, token.left.value)
            #     print(token.right, token.right.value)
            #     print()

            sign_tokens.reverse()
            for index, token in sign_tokens:
                token.calc()
                last_value = token.result
                break          



text = """
// def int a
// in a
// out
// 1 + 2 * 4
// out
"""

# run(text)

f = open("test.sl", "r")
run(f.read())
f.close()

