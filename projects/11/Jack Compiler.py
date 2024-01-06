# Author: R7CKB@qq.com
# divide it into five parts: JackTokenizer, JackCompiler, CompilationEngine, SymbolTable, VMWriter
# This is for project 11.
# I've written project 10 with reference to project 10.
# You can look at my past projects to get more information
"""
This project is partly based on https://github.com/sherrydang/Nand2Tetris/blob/master/project11/CompilationEngine.py
I made modifications to this project and made some optimizations. This project is based on project 10. What you need
to do is just to replace the corresponding statement in project 10 with the new statement which generates the VM
code.
The problem is that the function | method | constructor parameter is depended on the corresponding var
variables, instead of the parameter number.
When you call these functions, you need to find the local(var) argument and
count their number, which is the right function number.
"""
import glob
import os.path
import re
from enum import Enum


class KeyWordType(Enum):
    CLASS = 1
    METHOD = 2
    FUNCTION = 3
    CONSTRUCTOR = 4
    INT = 5
    BOOLEAN = 6
    CHAR = 7
    VOID = 8
    VAR = 9
    STATIC = 10
    FIELD = 11
    LET = 12
    DO = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    NULL = 10
    THIS = 21


class TokenType(Enum):
    KEYWORD = 1
    SYMBOL = 2
    IDENTIFIER = 3
    INT_CONSTANT = 4
    STRING_CONSTANT = 5


class JackTokenizer:  # Handles the input
    keyword_dict = {
        'class': KeyWordType.CLASS,
        'constructor': KeyWordType.CONSTRUCTOR,
        'function': KeyWordType.FUNCTION,
        'method': KeyWordType.METHOD,
        'field': KeyWordType.FIELD,
        'static': KeyWordType.STATIC,
        'var': KeyWordType.VAR,
        'int': KeyWordType.INT,
        'char': KeyWordType.CHAR,
        'boolean': KeyWordType.BOOLEAN,
        'void': KeyWordType.VOID,
        'true': KeyWordType.TRUE,
        'false': KeyWordType.FALSE,
        'null': KeyWordType.NULL,
        'this': KeyWordType.THIS,
        'let': KeyWordType.LET,
        'do': KeyWordType.DO,
        'if': KeyWordType.IF,
        'else': KeyWordType.ELSE,
        'while': KeyWordType.WHILE,
        'return': KeyWordType.RETURN,
    }
    symbol_dict = {
        '{': 'symbol',
        '}': 'symbol',
        '[': 'symbol',
        ']': 'symbol',
        '(': 'symbol',
        ')': 'symbol',
        '.': 'symbol',
        ',': 'symbol',
        ';': 'symbol',
        '+': 'symbol',
        '-': 'symbol',
        '*': 'symbol',
        '/': 'symbol',
        '&amp;': 'symbol',
        '|': 'symbol',
        '&lt;': 'symbol',
        '&gt;': 'symbol',
        '=': 'symbol',
        '~': 'symbol',
    }
    conversion_dict = {
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;',
        '"': "&quote;",
    }

    # self.lines load the whole file content and store it in a list
    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            self.lines = f.readlines()
        self.line_list = []
        self.token_list = []
        self.token = ""
        self.token_type = ""

    def process(self):  # this method creates a list so all the tokens in it\
        self.lines = [line.strip() for line in self.lines]
        for index in range(len(self.lines)):
            line = self.lines[index]
            if "//" in line and not line.startswith("//"):  # Post-sentence notes
                comment_index = line.find("//")
                self.lines[index] = self.lines[index][:comment_index].strip()
            elif not line.startswith("//") and not line.startswith("/*") and not line.startswith(
                    "*") and not line.endswith("*/") and line:  # //,/* and * are all annotations
                self.lines[index] = line.strip()
            else:  # For those comments that stand alone
                self.lines[index] = ""  # Remove unnecessary things (ignore space and comments)
            if self.lines[index] != "":  # ignore comments and blank line
                # use regrex regulation to match the all symbols
                delimiters = r'([()\[\]\{\}.,;\+\-\*\/\&\|\>\<\=\~\"])|\s+'  # It's challenging to figure it out
                self.line_list = re.split(delimiters,
                                          self.lines[index].strip())  # to split the line into a single character
                # The next two steps are to clean the dirty data
                self.line_list = list(filter(lambda x: x is not None, self.line_list))  # use the lambda function
                self.line_list = list(filter(lambda x: x != '', self.line_list))
                # Handle cases where strings are present
                if '"' in self.line_list:
                    first_quote_index = self.line_list.index('"')
                    self.line_list.pop(first_quote_index)
                    second_quote_index = self.line_list.index('"')
                    self.line_list.pop(second_quote_index)
                    # pop the string parts and insert a new complete string
                    for i in range(second_quote_index - first_quote_index):
                        self.line_list.pop(first_quote_index)
                    string = re.findall(r'"([^"]*)"', line)[0]  # this is used for match the string
                    self.line_list.insert(first_quote_index, '"' + string + '"')
                self.token_list.extend(self.line_list)
        self.token_list = list(filter(lambda x: x != '', self.token_list))

    # divide the current line into several tokens (use a list to store them).
    def hasMoreTokens(self):
        if len(self.token_list) > 0:
            return True
        return False

    def advance(self):  # Get the next token and make it current_token
        try:
            self.token = self.token_list.pop(0)
            if self.token in self.conversion_dict:
                self.token = self.conversion_dict[self.token]
            self.tokenType()
        except IndexError:
            pass

    # Returns the type of the current token,as a constant.
    def tokenType(self):
        if self.token in JackTokenizer.keyword_dict:
            self.token_type = TokenType.KEYWORD
        elif self.token in JackTokenizer.symbol_dict:
            self.token_type = TokenType.SYMBOL
        elif self.token.isdigit() and 0 <= int(self.token) <= 32767:
            self.token_type = TokenType.INT_CONSTANT
        elif self.token.startswith('"') and self.token.endswith('"'):
            self.token_type = TokenType.STRING_CONSTANT
            self.token = self.token[1:-1]
        # identifier must be the continuous but string can be not continuous
        else:
            self.token_type = TokenType.IDENTIFIER

    # Returns the keyword which is the current token, as a constant.
    def keyWord(self):
        if self.token_type == TokenType.KEYWORD:
            return self.keyword_dict.get(self.token)

    # Returns the character which is the current token.
    def symbol(self):
        if self.token_type == TokenType.SYMBOL:
            return self.token

    # Returns the string which is the current token.
    def identifier(self):
        if self.token_type == TokenType.IDENTIFIER:
            return self.token

    # Returns the integer value of the current token.
    def intVal(self):
        if self.token_type == TokenType.INT_CONSTANT:
            return int(self.token)

    # Returns the string value Of the current token ，
    def stringVal(self):
        if self.token_type == TokenType.STRING_CONSTANT:
            return self.token


class SymbolTable:
    # I use a nested list for data storage
    def __init__(self):
        self.static_index = 0
        self.field_index = 0
        self.argument_index = 0
        self.local_index = 0
        self.classTable = []
        self.subroutineTable = []

    # Empties the symbol table, and resets the four indexes to 0.
    def reset(self):
        self.static_index = 0
        self.field_index = 0
        self.argument_index = 0
        self.local_index = 0
        self.subroutineTable = []

    # Defines (adds to the table) a new variable of the given name, type,and kind.
    # Assigns to it the index value of that kind, and adds 1 to the index.
    def define(self, name, data_type, kind):
        if kind == "static":
            self.classTable.append([name, data_type, kind, self.static_index])
            self.static_index += 1
        elif kind == "field":
            self.classTable.append([name, data_type, "this", self.field_index])
            self.field_index += 1
        elif kind == "local":
            self.subroutineTable.append([name, data_type, "local", self.local_index])
            self.local_index += 1
        elif kind == "argument":
            self.subroutineTable.append([name, data_type, "argument", self.argument_index])
            self.argument_index += 1

    # Use list derivation to make the structure more aesthetically pleasing
    def varCount(self, kind) -> int:
        if kind == "static":
            return sum(1 for element in self.classTable if element[2] == "static")
        elif kind == "this":
            return sum(1 for element in self.classTable if element[2] == "this")
        elif kind == "local":
            return sum(1 for element in self.subroutineTable if element[2] == "local")
        elif kind == "argument":
            return sum(1 for element in self.subroutineTable if element[2] == "argument")

    # Returns the kind Of the named identifier.
    # If the identifier isn't found, returns NONE.
    def kindOf(self, name):
        for element in self.subroutineTable:
            if element[0] == name:
                return element[2]
        for element in self.classTable:
            if element[0] == name:
                return element[2]
        return None

    # Returns the type of the named variable.
    def typeOf(self, name) -> str:
        for element in self.subroutineTable:
            if element[0] == name:
                return element[1]
        for element in self.classTable:
            if element[0] == name:
                return element[1]

    # # Returns the index of the named variable.
    def indexOf(self, name) -> int:
        for element in self.subroutineTable:
            if element[0] == name:
                return element[3]
        for element in self.classTable:
            if element[0] == name:
                return element[3]


class VMWriter:
    def __init__(self, output_file):
        self.output_file = output_file
        self.indent = "    "

    @classmethod
    def write_method(cls, output_file, string):
        try:
            with open(output_file, "a") as f:
                f.write(string)
        except Exception as e:
            print(f"Error: {e}")

    def writePush(self, segment, index):
        self.write_method(self.output_file, f"{self.indent}push {segment} {index}\n")

    def writePop(self, segment, index):
        self.write_method(self.output_file, f"{self.indent}pop {segment} {index}\n")

    def writeArithmetic(self, command):
        if command == "+":
            self.write_method(self.output_file, f"{self.indent}add\n")
        elif command == "-":
            self.write_method(self.output_file, f"{self.indent}sub\n")
        elif command == "~":
            self.write_method(self.output_file, f"{self.indent}not\n")
        elif command == "=":
            self.write_method(self.output_file, f"{self.indent}eq\n")
        elif command == "&gt;":
            self.write_method(self.output_file, f"{self.indent}gt\n")
        elif command == "&lt;":
            self.write_method(self.output_file, f"{self.indent}lt\n")
        elif command == "&amp;":
            self.write_method(self.output_file, f"{self.indent}and\n")
        elif command == "|":
            self.write_method(self.output_file, f"{self.indent}or\n")
        elif command == "*":
            self.write_method(self.output_file, f"{self.indent}call Math.multiply 2\n")
        elif command == "/":
            self.write_method(self.output_file, f"{self.indent}call Math.divide 2\n")
        elif command == "neg":
            self.write_method(self.output_file, f"{self.indent}neg\n")

    def writeLabel(self, label):
        self.write_method(self.output_file, f"label {label}\n")

    def writeGoto(self, label):
        self.write_method(self.output_file, f"{self.indent}goto {label}\n")

    def writeIf(self, label):
        self.write_method(self.output_file, f"{self.indent}if-goto {label}\n")

    def writeCall(self, name, nArgs):
        self.write_method(self.output_file, f"{self.indent}call {name} {nArgs}\n")

    def writeFunction(self, name, nVars):
        self.write_method(self.output_file, f"function {name} {nVars}\n")

    def writeReturn(self):
        self.write_method(self.output_file, f"{self.indent}return\n")

    # python use with method will automatically call the close method


class CompilationEngine:  # Handles the parsing
    operators = ["+", "-", "*", "/", "=", "&lt;", "&gt;", "&amp;", "|", "&quote;"]
    unary_operators = ["~", "-"]

    # this initialization method starts the whole procedure
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.classname = ""
        self.while_level = 0
        self.if_level = 0
        self.tokenizer = JackTokenizer(input_file)
        self.tokenizer.process()
        # use dictionary to store the methods
        self.methods = {}
        self.method_list()
        self.vmWriter = VMWriter(output_file)
        self.symbolTable = SymbolTable()
        # must call compileClass first
        self.compileClass()

    def method_list(self):
        for i in range(len(self.tokenizer.token_list)):
            if self.tokenizer.token_list[i] == "method":
                self.methods[self.tokenizer.token_list[i + 2]] = 0

    # Use class methods to avoid using with open method multiple times
    @classmethod
    def write_method(cls, output_file, string):
        try:
            with open(output_file, "a") as fw:
                fw.write(string)
        except Exception as e:
            print(f"Error: {e}")

    # this method is referred with the corresponding method, using advanced method is right
    # it's easy-understanding
    def process(self, token=None):
        if token is None:
            self.tokenizer.advance()
        elif self.tokenizer.token == token:
            self.tokenizer.advance()
        else:
            print(self.tokenizer.token + self.tokenizer.token_list[0] + " syntax error")
            self.tokenizer.advance()

    def compileClass(self):
        self.process()  # let the current token equals class
        self.process("class")
        self.classname = self.tokenizer.token
        self.process()  # process the classname
        self.process("{")
        # classVarDec may have serval lines
        while self.tokenizer.token in ("static", "field", "arg", "var"):
            self.compileClassVarDec()
        while self.tokenizer.token in ("constructor", "function", "method"):
            self.compileSubroutine()
        self.process("}")

    def compileClassVarDec(self):
        kind = self.tokenizer.token  # the variable kind (static | field)
        self.process()  # process the variable kind
        data_type = self.tokenizer.token  # the variable type (int|char|boolean|classname)
        self.process()  # process the variable type
        name = self.tokenizer.token  # the variable name
        self.process()
        self.symbolTable.define(name, data_type, kind)
        while self.tokenizer.token == ",":  # deal with case like "(field | static) int x,y,z,c"
            self.process(",")
            name = self.tokenizer.token
            self.process()  # process the name
            self.symbolTable.define(name, data_type, kind)
        self.process(";")

    # this method is to get the local variable number
    # each method | function | constructor's parameter number is depending on how many 'var' variables are.
    def getParameterNumber(self):
        var_number = 0
        change = 0
        # use foolish method to get the parameter
        # use return to make sure the var variables in the same function,
        return_index = self.tokenizer.token_list.index("return")
        for i in range(return_index):
            if self.tokenizer.token_list[i] == "var":
                var_number += 1
                another_var = self.tokenizer.token_list[i + 3]  # var int key,x,y;
                while another_var != ";":
                    var_number += 1
                    another_var = self.tokenizer.token_list[i + 3 + change]  # skip the ',
                    change += 2
        return var_number

    # this method is to deal with the method | constructor | function three cases
    def compileSubroutine(self):
        # Empties the symbol subroutineTable, and resets the four indexes to O.
        self.symbolTable.reset()
        function_type = self.tokenizer.token
        self.process()  # process the (function|method|constructor)
        self.process()  # process the function type (void | other)
        function_name = self.tokenizer.token
        self.process()  # process the function name

        # such like the (self) in the python
        if function_type == "method":
            self.symbolTable.define("this", self.classname, "argument")
        self.process("(")
        if self.tokenizer.token != ")":
            self.compileParameterList()

        # initialize jump level
        # in each subroutine the level must be reset
        self.if_level = 0
        self.while_level = 0
        self.process(")")

        # get the local variables number
        parameter_number = self.getParameterNumber()

        # function | constructor | method
        self.vmWriter.writeFunction(f"{self.classname}.{function_name}", parameter_number)

        # deal with the method, which is mentioned in the book Figure 11.10
        if function_type == "method":
            self.vmWriter.writePush("argument", 0)
            self.vmWriter.writePop("pointer", 0)

        # deal with the constructor, which is mentioned in the book Figure 11.8
        elif function_type == "constructor":
            # push constant args_count
            class_var_number = self.symbolTable.varCount("this")
            self.vmWriter.writePush("constant", class_var_number)
            # call Memory.alloc
            self.vmWriter.writeCall("Memory.alloc", 1)
            # set this to the base address return by alloc
            self.vmWriter.writePop("pointer", 0)

        self.compileSubroutineBody()

    def compileParameterList(self):
        data_type = self.tokenizer
        self.process()  # process the data_type like int | boolean | char
        name = self.tokenizer.token
        self.symbolTable.define(name, data_type, "argument")
        self.process()  # process the name
        # this can compile arguments like "int ax,int ay,int az"
        if self.tokenizer.token == ",":
            self.process()  # deal with the comma(,)
            self.compileParameterList()

    def compileSubroutineBody(self):
        self.process("{")
        while self.tokenizer.token == "var":
            # varDec*
            self.compileVarDec()
        self.compileStatements()
        self.process("}")

    def compileVarDec(self):
        while self.tokenizer.token != ";":
            self.process("var")
            var_data_type = self.tokenizer.token  # var_data_type
            self.process()  # process the data_type
            var_name = self.tokenizer.token  # var_name
            self.symbolTable.define(var_name, var_data_type, "local")
            self.process()  # process the var_name
            while self.tokenizer.token == ",":
                self.process(",")
                another_name = self.tokenizer.token
                self.symbolTable.define(another_name, var_data_type, "local")
                self.process()  # process the another_name
        self.process(";")

    def compileStatements(self):
        while self.tokenizer.token in ("let", "if", "while", "do", "return"):
            if self.tokenizer.token == "let":
                self.compileLet()
            elif self.tokenizer.token == "if":
                self.compileIf()
            elif self.tokenizer.token == "while":
                self.compileWhile()
            elif self.tokenizer.token == "do":
                self.compileDo()
            elif self.tokenizer.token == "return":
                self.compileReturn()

    def compileLet(self):
        self.process("let")
        var_name = self.tokenizer.token
        self.process()  # process the var_name

        # let var_name [expression1] = expression2
        # such like let a[i] = b[j]
        if self.tokenizer.token == "[":
            # push arr
            self.vmWriter.writePush(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
            self.process("[")
            self.compileExpression()  # call compileExpression to compute and push expression1
            self.process("]")
            # add
            self.vmWriter.writeArithmetic("+")  # top stack value = address of arr[expression1]
            self.process("=")
            self.compileExpression()  # call compileExpression to compute and push expression2
            # mentioned in the book figure11.12, after it
            self.vmWriter.writePop("temp", 0)
            self.vmWriter.writePop("pointer", 1)
            self.vmWriter.writePush("temp", 0)
            self.vmWriter.writePop("that", 0)

        # let var_name = expression
        elif self.tokenizer.token == "=":
            self.process("=")
            self.compileExpression()
            self.vmWriter.writePop(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
        self.process(";")

    # This method isn't easy to understand. It's challenging to Figure out its logic.
    #   Expression will return a value
    #   negative the value
    #   if goto label_false(only the value is negative)
    #   statements
    #   go to label_end
    # label_false
    #   statements
    # label_end
    def compileIf(self):
        self.process("if")
        self.process("(")
        self.compileExpression()
        self.process(")")
        # string is unchangeable, so you need to assign the str the value again
        if_false = f"IF_FALSE{self.if_level}"
        if_end = f"IF_END{self.if_level}"
        self.if_level += 1
        self.vmWriter.writeArithmetic("~")  # not
        self.vmWriter.writeIf(if_false)
        self.process("{")
        self.compileStatements()
        self.process("}")
        self.vmWriter.writeGoto(if_end)
        self.vmWriter.writeLabel(if_false)
        if self.tokenizer.token == "else":
            self.process("else")
            self.process("{")
            self.compileStatements()
            self.process("}")
        self.vmWriter.writeLabel(if_end)

    # the only difficult is to understand the logical sequence
    # label_start
    #   expression will return a value
    #   negative the value
    #   if goto label_end (only the value is negative)
    #   statements
    #   goto label_start
    # label label_end
    def compileWhile(self):
        self.process("while")
        # String is unchangeable, so you need to assign the str the value again.
        # Each time you call this method the while level will increase, and the label will change.
        while_start = f"WHILE_START{self.while_level}"
        while_end = f"WHILE_END{self.while_level}"
        self.while_level += 1
        self.vmWriter.writeLabel(while_start)
        self.process("(")
        self.compileExpression()
        self.process(")")
        self.vmWriter.writeArithmetic("~")  # not
        self.vmWriter.writeIf(while_end)
        self.process("{")
        self.compileStatements()
        self.process("}")
        self.vmWriter.writeGoto(while_start)
        self.vmWriter.writeLabel(while_end)

    def compileDo(self):
        """
        do subroutineName(exp1, exp2, …)
        We recommend handling do subroutineName(…) statements as if they were do expression statements.
        """
        self.process("do")
        self.compileExpression()
        self.vmWriter.writePop("temp", 0)
        self.process(";")

    def compileReturn(self):
        self.process("return")
        if self.tokenizer.token != ";":  # return expression;
            self.compileExpression()
        else:  # only return statement
            self.vmWriter.writePush("constant", 0)
        self.vmWriter.writeReturn()
        self.process(";")

        # done

    # compileExpression we need to transfer the infix notation into postfix notation, which is suitable for the stack.
    # It took on the duty of subroutine-call
    def compileExpression(self):
        # term
        self.compileTerm()  # term

        # (op term)*
        if self.tokenizer.token in self.operators:
            operator = self.tokenizer.token
            self.process()  # process the operators
            self.compileTerm()  # term2
            self.vmWriter.writeArithmetic(operator)

    # you can't use while in this method
    def compileTerm(self):
        next_token = self.tokenizer.token_list[0]
        class_flag = False
        subroutine_flag = False

        # deal with the varName
        for entry in self.symbolTable.subroutineTable:
            if entry[0] == self.tokenizer.token:
                subroutine_flag = True
        for entry in self.symbolTable.classTable:
            if entry[0] == self.tokenizer.token:
                class_flag = True

        # integer_constant
        if self.tokenizer.token_type == TokenType.INT_CONSTANT:
            self.vmWriter.writePush("constant", int(self.tokenizer.token))
            self.process()

        # string_constant
        elif self.tokenizer.token_type == TokenType.STRING_CONSTANT:
            string = self.tokenizer.token
            # I get rid of the double quote in tokenType method
            # string = string[1:-1]  # get rid of double quote
            self.vmWriter.writePush("constant", len(string))
            self.vmWriter.writeCall("String.new", 1)
            for char in string:
                code = ord(char)
                self.vmWriter.writePush("constant", code)
                # the parameter is 2 because call String.new will return a value
                self.vmWriter.writeCall("String.appendChar", 2)
            self.process()

        # keyword_constant
        elif self.tokenizer.token in ("null", "false", "this", "true"):
            if self.tokenizer.token == "null" or self.tokenizer.token == "false":
                self.vmWriter.writePush("constant", 0)
            elif self.tokenizer.token == "true":
                self.vmWriter.writePush("constant", 1)
                self.vmWriter.writeArithmetic("neg")
            elif self.tokenizer.token == "this":
                self.vmWriter.writePush("pointer", 0)
            self.process()  # process the null|false|true|this

        # mentioned in the book figure 11.11
        # array[expression]
        elif next_token == "[":
            var_name = self.tokenizer.token
            self.process()  # process the var_name
            # push array
            self.vmWriter.writePush(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
            self.process("[")
            self.compileExpression()
            self.process("]")
            # add
            self.vmWriter.writeArithmetic("+")
            self.vmWriter.writePop("pointer", 1)
            self.vmWriter.writePush("that", 0)

        # only var_name
        elif subroutine_flag and next_token != ".":
            var_name = self.tokenizer.token
            self.vmWriter.writePush(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
            self.process()  # process the var_name

        # only var_name
        elif class_flag and next_token != ".":
            var_name = self.tokenizer.token
            self.vmWriter.writePush(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
            self.process()  # process the var_name

        # unaryOp term
        elif self.tokenizer.token in self.unary_operators:
            unary_operator = self.tokenizer.token
            self.tokenizer.advance()  # process the unary operator
            self.compileTerm()
            if unary_operator == "-":  # this means neg
                self.vmWriter.writeArithmetic("neg")
            elif unary_operator == "~":  # this means not
                self.vmWriter.writeArithmetic("~")

        # (expression)
        elif self.tokenizer.token == "(":
            self.process("(")
            self.compileExpression()
            self.process(")")

        # the following two steps are subroutineCall
        # deal with the varName.methodName(expression1,expression2...)
        elif next_token == ".":
            var_name = self.tokenizer.token
            self.process()  # process the varname
            self.process('.')
            method_name = self.tokenizer.token
            self.process()  # process the method_name
            var_type = None
            call_text = ""

            # deal with the case like 'field Square square'
            for i in range(len(self.symbolTable.classTable)):
                if self.symbolTable.classTable[i][0] == var_name:
                    var_type = self.symbolTable.typeOf(var_name)
            # deal with the case like 'var SquareGame game'
            for i in range(len(self.symbolTable.subroutineTable)):
                if self.symbolTable.subroutineTable[i][0] == var_name:
                    var_type = self.symbolTable.typeOf(var_name)

            #  mentioned in the book Figure11.9
            if var_type:
                call_text += var_type
                self.vmWriter.writePush(self.symbolTable.kindOf(var_name), self.symbolTable.indexOf(var_name))
            else:
                call_text = var_name

            # varName.methodName
            call_text += "."
            call_text += method_name

            # process expressionList
            self.process('(')
            var_count = self.compileExpressionList()
            self.process(')')

            # call className.methodName n+1
            if var_type:
                var_count += 1
            self.vmWriter.writeCall(call_text, var_count)

        # method(expression1,expression....)
        # like moveSquare()
        elif next_token == "(":
            method_name = self.tokenizer.token
            self.process()  # process the method_name

            self.process("(")
            var_count = 0
            # mentioned in the compiling method calls
            if method_name in self.methods:
                # method(expression1,expression....)  as this.method(expression1,expression....)
                self.vmWriter.writePush("pointer", 0)
                var_count += 1
            var_count += self.compileExpressionList()
            method_name = self.classname + "." + method_name
            self.vmWriter.writeCall(method_name, var_count)
            self.process(")")

    def compileExpressionList(self):
        expression_number = 0
        # maybe no expressionList
        if self.tokenizer.token != ")":
            expression_number += 1
            self.compileExpression()
            while self.tokenizer.token != ")":
                expression_number += 1
                self.tokenizer.advance()  # process the parenthesis(')'),or comma(,)
                self.compileExpression()
        return expression_number


class JackCompiler:  # Drives the translation process.
    def __init__(self, file):
        self.file = file
        self.file_name = ""
        self.isdir = os.path.isdir(self.file)

    @staticmethod
    def get_file_name(file_path) -> str:
        file_name = os.path.basename(file_path)
        index = file_name.find(".")
        return file_name[:index]

    # We're going to compile the main file at the end
    def compile(self):
        if self.isdir:
            files = glob.glob(f'{self.file}/*.jack')
            for file in files:
                self.file_name = os.path.basename(file)
                index = self.file_name.find(".")
                file_name = self.file_name[:index]
                process_files = CompilationEngine(file, file_name + ".vm")
        # this is for the single file
        else:
            self.file_name = os.path.basename(self.file)
            index = self.file_name.find(".")
            file_name = self.file_name[:index]
            process_file = CompilationEngine(self.file, file_name + ".vm")


a = JackCompiler("ComplexArrays")
a.compile()
