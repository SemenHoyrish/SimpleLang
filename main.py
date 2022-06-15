# TODO: tests! 
# TODO: report error when try to access to undefined variable
# TODO: add some debug features, like:
#                                #dump_vars
#                                #dump a

# TODO: OR AND operations
# TODO: LOOP

import sys
import functools

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIGNS = "+-/*=<>|&"

def report_error(text: str):
    print("[ERROR] " + text)

class Type:
    name: str = "type"
    default_value = None

class Integer(Type):
    name: str = "integer"
    default_value = 0

class String(Type):
    name: str = "string"
    default_value = ""

class Boolean(Type):
    name: str = "boolean"
    default_value = False

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
        elif self.type == String:
            self.value = str(value)
            return True
        elif self.type == Boolean:
            if str(value).lower() == "false":
                self.value = False
                return True
            elif str(value).lower() == "true":
                self.value = True
                return True
            return False
        else:
            return False

    def get_str(self) -> str:
        if self.type == String:
            return self.value
        if self.type == Integer:
            return str(self.value)
        if self.type == Boolean:
            if self.value == True:
                return "true"
            else:
                return "false"
        return ""

types = {
    "int": Integer,
    "str": String,
    "bool": Boolean,
}

vars = {}


last_value = Variable(Type, None)


class Token:
    value = None
    def __init__(self, value):
        self.value = value

class ValueToken(Token):
    pass

class NumberToken(ValueToken):
    def __init__(self, value):
        super().__init__(int(value))
class StringToken(ValueToken):
    def __init__(self, value):
        super().__init__(str(value))
class BooleanToken(ValueToken):
    def __init__(self, value):
        if str(value).lower() == "true":
            super().__init__(True)
        elif str(value).lower() == "false":
            super().__init__(False)

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
            # print(vars)
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
            self.result = left_res // right_res
        if type(self) == EqualsEqualsToken:
            self.result = left_res == right_res
        if type(self) == LessToken:
            self.result = left_res < right_res
        if type(self) == BiggerToken:
            self.result = left_res > right_res
        if type(self) == AndToken:
            self.result = left_res and right_res
        if type(self) == OrToken:
            self.result = left_res or right_res
    

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
class EqualsEqualsToken(SignToken):
    def __init__(self):
        super().__init__("==")
class BiggerToken(SignToken):
    def __init__(self):
        super().__init__(">")
class LessToken(SignToken):
    def __init__(self):
        super().__init__("<")
class AndToken(SignToken):
    def __init__(self):
        super().__init__("&")
class OrToken(SignToken):
    def __init__(self):
        super().__init__("|")

signs_priority = {
    StarToken: 3,
    SlashToken: 3,
    PlusToken: 2,
    MinusToken: 2,
    EqualsEqualsToken: 1,
    BiggerToken: 1,
    LessToken: 1,
    AndToken: 0,
    OrToken: 0
}


def run(text: str, from_loop: bool = False):
    global last_value
    lines = text.split("\n")


    if_count = 0
    if_truth = []
    else_count = 0
    else_truth = []

    # loop_count = 0
    is_loop = False
    loop = ""
    
    for line_index, line in enumerate(lines):
        raw_line = line
        line = line.strip()

        # print("\n---")
        # print("if_count", if_count)
        # print("if_truth", if_truth)
        # print("else_count", else_count)
        # print("else_truth", else_truth)

        if line.startswith("//"):
            continue


        elif line.strip() == "loop":
            is_loop = True

        
        elif line.strip() == "endloop":
            run(loop, True)
            is_loop = False
            # print("!!!!")
            # print(loop)
            # print("!!!!")
        
        elif is_loop:
            loop += line + "\n"
            continue

        
            
        elif line.strip() == "if":
            # print("-> if")
            # print(last_value.get_str())
            # print(last_value.type)
            # print(last_value.value)
            if last_value.type != Boolean:
                report_error("Incorrect type for if statement!")
                return
            if_count += 1
            if_truth.append(last_value.value)
            else_count += 1
            else_truth.append(not last_value.value)

        elif line.strip() == "else":
            # print("-> else")
            # else_count += 1
            # else_truth.append(not if_truth[if_count - 1])
            if_count -= 1
            del if_truth[if_count]
        
        elif line.strip() == "endif":
            # print("-> endif")
            else_count -= 1
            del else_truth[else_count]

        elif if_count > 0 and if_truth[if_count - 1] == False:
            continue
            
        elif else_count > 0 and else_count > if_count and else_truth[else_count - 1] == False:
            continue


        elif line.strip() == "break":
            loop += line + "\n"
            if from_loop:
                return

        # elif line.strip() == "loop":
        #     loop_count += 1
        #     loops.append(line_index)
        # elif line.strip() == "break":
        #     loop_count -= 1
        #     del loops[loop_count]
        # elif line.strip() == "endloop":
        #     line_index = loops[loop_count - 1]

        

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

            last_value = vars[n]
        
        elif line.strip() == "out":
            print(last_value.get_str().replace("\\n", "\n"), end="")

        elif line.startswith("set"):
            line = line.replace("set ", "")
            n = line.strip()
            if n not in vars.keys():
                report_error("Indefined variable")
                return

            r = vars[n].parse_value(last_value.value)
            if r == False:
                report_error("??")
                return

        elif line.startswith("get"):
            line = line.replace("get ", "")
            n = line.strip()
            if n not in vars.keys():
                report_error("Indefined variable")
                return

            last_value = vars[n]

        else:
            symbols = list(raw_line)
            # print(symbols)
            tokens = []
            number_str = ""
            last_symbol_is_digit = False
            is_str = False
            name = ""
            last_symbol_is_letter = False
            skip = False
            for symbol_index, symbol in enumerate(symbols):
                if skip:
                    skip = False
                    continue
                if symbol == " " and not is_str: continue
                if symbol.isdigit() and not is_str:
                    if last_symbol_is_letter:
                        last_symbol_is_letter = False
                        if name.lower() == "false" or name.lower() == "true":
                            tokens.append([BooleanToken(name), False])
                        elif is_str:
                            is_str = False
                            tokens.append([StringToken(name), False])
                        else:
                            tokens.append([VariableNameToken(name), False])

                    if not last_symbol_is_digit:
                        number_str = ""
                    number_str += symbol
                    last_symbol_is_digit = True

                elif symbol in SIGNS and not is_str:
                    if last_symbol_is_digit:
                        last_symbol_is_digit = False
                        tokens.append([NumberToken(int(number_str)), False])
                    if last_symbol_is_letter:
                        last_symbol_is_letter = False
                        if name.lower() == "false" or name.lower() == "true":
                            tokens.append([BooleanToken(name), False])
                        elif is_str:
                            is_str = False
                            tokens.append([StringToken(name), False])
                        else:
                            tokens.append([VariableNameToken(name), False])

                    if symbol == "+":
                        tokens.append([PlusToken(), False])
                    elif symbol == "-":
                        tokens.append([MinusToken(), False])
                    elif symbol == "*":
                        tokens.append([StarToken(), False])
                    elif symbol == "/":
                        tokens.append([SlashToken(), False])
                    elif symbol == "<":
                        tokens.append([LessToken(), False])
                    elif symbol == ">":
                        tokens.append([BiggerToken(), False])
                    elif symbol == "=" and symbols[symbol_index + 1] == "=":
                        tokens.append([EqualsEqualsToken(), False])
                        skip = True
                    elif symbol == "&":
                        tokens.append([AndToken(), False])
                    elif symbol == "|":
                        tokens.append([OrToken(), False])
                
                else:
                    if last_symbol_is_digit:
                        last_symbol_is_digit = False
                        tokens.append([NumberToken(int(number_str)), False])

                    if symbol == "\"":
                        is_str = True
                        continue

                    if not last_symbol_is_letter:
                        name = ""
                    name += symbol
                    last_symbol_is_letter = True

            if last_symbol_is_digit:
                last_symbol_is_digit = False
                tokens.append([NumberToken(int(number_str)), False])
            if last_symbol_is_letter:
                last_symbol_is_letter = False
                if name.lower() == "false" or name.lower() == "true":
                    tokens.append([BooleanToken(name), False])
                elif is_str:
                    is_str = False
                    tokens.append([StringToken(name), False])
                else:
                    tokens.append([VariableNameToken(name), False])

            if len(tokens) == 1 and isinstance(tokens[0][0], ValueToken):
                # print("Only one token detected!")
                if type(tokens[0][0]) == NumberToken:
                    last_value = Variable(Integer, tokens[0][0].value)
                elif type(tokens[0][0]) == StringToken:
                    last_value = Variable(String, tokens[0][0].value)
                elif type(tokens[0][0]) == BooleanToken:
                    last_value = Variable(Boolean, tokens[0][0].value)

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
                if (token.result == True or token.result == False) and type(token.result) == type(True):
                    last_value = Variable(Boolean, token.result)
                else:
                    last_value = Variable(Integer, token.result)
                break          

    if from_loop:
        run(text, True)


text = """
// def int a
// in a
// out
// 1 + 2 * 4
// out
"""

# run(text)

filename = "test.sl"

for arg in sys.argv:
    if arg.endswith(".sl"):
        filename = arg

f = open(filename, "r")
run(f.read())
# print(vars)
# print(vars['a'].type)
# print(vars['a'].value)
f.close()

