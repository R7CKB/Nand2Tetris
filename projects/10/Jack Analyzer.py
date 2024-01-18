# Author: R7CKB@qq.com
# Divide it into three parts: JackTokenizer, CompilationEngine, JackAnalyzer.
# This is for project 10, because this doesn't include code generator.
# I've written project 10 with reference to project 8 and 9
# You can look at project 8 and 9 to get more information
"""
This project doesn't like project 8 and 9,you need to recognize each token respectively.
Besides, you need to generate the xxxT.xml, and then generate the xxx.xml.
I use indent to make my generate_code more readable.
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
                    "*") and line:  # //,/* and * are all annotations
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
            # raise IndexError("The List is empty")

    # Returns the type of the current token,as a constant.
    def tokenType(self):
        if self.token in JackTokenizer.keyword_dict:
            self.token_type = TokenType.KEYWORD
        elif self.token in JackTokenizer.symbol_dict:
            self.token_type = TokenType.SYMBOL
        elif self.token.isdigit() and 0 <= int(self.token) <= 32767:
            self.token_type = TokenType.INT_CONSTANT
        # identifier and string constant aren't easy to distinguish
        # isalnum is able to distinguish the punctuation marks
        # I didn't handle the distinction between string and identifier well
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


class CompilationEngine:  # Handles the parsing
    # this initialization method starts the whole procedure
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.indent = ""
        self.tokenizer = JackTokenizer(input_file)
        self.tokenizer.process()
        self.compileClass()

    def add_indent(self):
        self.indent += "  "

    def sub_indent(self):
        self.indent = self.indent[2:]

    # Use class methods to avoid using with open method multiple times
    @classmethod
    def write_method(cls, output_file, string):
        try:
            with open(output_file, "a") as fw:
                fw.write(string)
        except Exception as e:
            print(f"Error: {e}")

    def process(self, string):
        try:
            if self.tokenizer.token == "":  # at first the token is empty
                self.tokenizer.advance()
            if self.tokenizer.token == string:
                if self.tokenizer.token_type == TokenType.KEYWORD:
                    self.write_method(self.output_file, f"{self.indent}<keyword> {self.tokenizer.token} </keyword>\n")
                    self.tokenizer.advance()
                elif self.tokenizer.token_type == TokenType.SYMBOL:
                    self.write_method(self.output_file, f"{self.indent}<symbol> {self.tokenizer.token} </symbol>\n")
                    self.tokenizer.advance()
                elif self.tokenizer.token_type == TokenType.INT_CONSTANT:
                    self.write_method(self.output_file,
                                      f"{self.indent}<integerConstant> {self.tokenizer.token} </integerConstant>\n")
                    self.tokenizer.advance()
                elif self.tokenizer.token_type == TokenType.STRING_CONSTANT:
                    self.write_method(self.output_file,
                                      f"{self.indent}<stringConstant> {self.tokenizer.token} </stringConstant>\n")
                    self.tokenizer.advance()
                elif self.tokenizer.token_type == TokenType.IDENTIFIER:
                    self.write_method(self.output_file,
                                      f"{self.indent}<identifier> {self.tokenizer.token} </identifier>\n")
                    self.tokenizer.advance()
        except Exception as e:
            raise SyntaxError(f"Syntax Error! {e} {self.tokenizer.token}")

    def compileClass(self):
        self.write_method(self.output_file, "<class>\n")
        self.add_indent()
        self.process("class")
        self.process(self.tokenizer.token)  # className
        self.process("{")
        # classVarDec may have serval lines
        while self.tokenizer.token in ("static", "field"):
            self.compileClassVarDec()
        while self.tokenizer.token in ("constructor", "function", "method"):
            self.compileSubroutine()
        self.process("}")
        self.sub_indent()
        self.write_method(self.output_file, "</class>\n")

    def compileClassVarDec(self):
        self.write_method(self.output_file, f"{self.indent}<classVarDec>\n")
        self.add_indent()
        while self.tokenizer.token != ";":  # at the end of the line
            # type varName (',' varName)*
            self.process(self.tokenizer.token)
        self.process(";")  # to tackle the semicolon
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</classVarDec>\n")

    def compileSubroutine(self):
        self.write_method(self.output_file, f"{self.indent}<subroutineDec>\n")
        self.add_indent()
        while self.tokenizer.token != "(":
            # ('void'|type ) subroutineName
            self.process(self.tokenizer.token)
        self.process("(")  # this is for (
        # this is for parameter
        self.compileParameterList()
        self.process(")")  # this is for )
        self.compileSubroutineBody()
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</subroutineDec>\n")

    def compileParameterList(self):
        self.write_method(self.output_file, f"{self.indent}<parameterList>\n")
        self.add_indent()
        while self.tokenizer.token != ")":
            # ((type varName),(',' type varName)*)?
            self.process(self.tokenizer.token)
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</parameterList>\n")

    def compileSubroutineBody(self):
        self.write_method(self.output_file, f"{self.indent}<subroutineBody>\n")
        self.add_indent()
        self.process("{")
        while self.tokenizer.token == "var":
            # varDec*
            self.compileVarDec()
        self.compileStatements()
        self.process("}")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</subroutineBody>\n")

    def compileVarDec(self):
        self.write_method(self.output_file, f"{self.indent}<varDec>\n")
        self.add_indent()
        while self.tokenizer.token != ";":
            # 'var' type varName (',' varName)*
            self.process(self.tokenizer.token)
        self.process(";")  # to tackle the semicolon
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</varDec>\n")

    def compileStatements(self):
        self.write_method(self.output_file, f"{self.indent}<statements>\n")
        self.add_indent()
        while self.tokenizer.token in ("let", "if", "while", "do", "return"):
            if self.tokenizer.token == "let":
                self.compileLet()
            elif self.tokenizer.token == "if":
                self.compileIf()
            elif self.tokenizer.token == "while":
                self.compileWhile()
            elif self.tokenizer.token == "do":
                self.compileDo()
            else:
                self.compileReturn()
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</statements>\n")

    def compileLet(self):
        self.write_method(self.output_file, f"{self.indent}<letStatement>\n")
        self.add_indent()
        self.process("let")
        self.process(self.tokenizer.token)  # varName
        if self.tokenizer.token == "[":  # ([expression])?
            self.process("[")
            self.compileExpression()
            self.process("]")
        self.process("=")
        self.compileExpression()
        self.process(";")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</letStatement>\n")

    def compileIf(self):
        self.write_method(self.output_file, f"{self.indent}<ifStatement>\n")
        self.add_indent()
        self.process("if")
        self.process("(")
        self.compileExpression()
        self.process(")")
        self.process("{")
        self.compileStatements()
        self.process("}")
        if self.tokenizer.token == "else":
            self.process("else")
            self.process("{")
            self.compileStatements()
            self.process("}")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</ifStatement>\n")

    def compileWhile(self):
        self.write_method(self.output_file, f"{self.indent}<whileStatement>\n")
        self.add_indent()
        self.process("while")
        self.process("(")
        self.compileExpression()
        self.process(")")
        self.process("{")
        self.compileStatements()
        self.process("}")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</whileStatement>\n")

    def compileDo(self):
        self.write_method(self.output_file, f"{self.indent}<doStatement>\n")
        self.add_indent()
        self.process("do")
        # the following are subroutineCall
        while self.tokenizer.token != ";":
            self.process(self.tokenizer.token)  # subroutineName | className | varName
            if self.tokenizer.token == ".":
                self.process(".")
                self.process(self.tokenizer.token)  # subroutineName
            self.process("(")
            self.compileExpressionList()
            self.process(")")
        self.process(";")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</doStatement>\n")

    def compileReturn(self):
        self.write_method(self.output_file, f"{self.indent}<returnStatement>\n")
        self.add_indent()
        self.process("return")
        while self.tokenizer.token != ";":
            self.compileExpression()
        self.process(";")
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</returnStatement>\n")

    def compileExpression(self):
        self.write_method(self.output_file, f"{self.indent}<expression>\n")
        self.add_indent()
        self.compileTerm()
        # (op term)*
        while self.tokenizer.token in ("+", "-", "*", "/", "=", "&lt;", "&gt;", "&amp;", "|", "&quote;"):
            self.process(self.tokenizer.token)
            self.compileTerm()
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</expression>\n")

    # you can't use while in this method
    def compileTerm(self):
        self.write_method(self.output_file, f"{self.indent}<term>\n")
        self.add_indent()
        # unaryOp term
        if self.tokenizer.token in ("-", "~"):
            self.process(self.tokenizer.token)  # unary op
            self.compileTerm()
        # expression
        elif self.tokenizer.token == "(":
            self.process("(")
            self.compileExpression()
            self.process(")")
        elif self.tokenizer.token_type == TokenType.IDENTIFIER:
            next_token = self.tokenizer.token_list[0]
            self.process(self.tokenizer.token)
            # varName [expression]
            if next_token == "[":  # array
                self.process("[")
                self.compileExpression()
                self.process("]")
            elif next_token == ".":  # function
                self.process(".")
                self.process(self.tokenizer.token)  # identifier
                self.process("(")
                self.compileExpressionList()
                self.process(")")
            elif next_token == "(":  # method,static method
                self.process("(")
                self.compileExpressionList()
                self.process(")")
        elif self.tokenizer.token_type == TokenType.INT_CONSTANT:
            self.process(self.tokenizer.token)
        elif self.tokenizer.token_type == TokenType.STRING_CONSTANT:
            self.process(self.tokenizer.token)
        elif self.tokenizer.token_type == TokenType.KEYWORD:
            self.process(self.tokenizer.token)
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</term>\n")

    def compileExpressionList(self):
        self.write_method(self.output_file, f"{self.indent}<expressionList>\n")
        self.add_indent()
        # maybe no expressionList
        if self.tokenizer.token != ")":
            # expression
            self.compileExpression()
            # (',' expression)*
            while self.tokenizer.token != ")":
                self.process(self.tokenizer.token)
                self.compileExpression()
        self.sub_indent()
        self.write_method(self.output_file, f"{self.indent}</expressionList>\n")


class JackAnalyzer:  # Drives the translation process.
    def __init__(self, file):
        self.file = file
        self.file_name = ""
        self.isdir = os.path.isdir(self.file)

    @staticmethod
    def get_file_name(file_path) -> str:
        file_name = os.path.basename(file_path)
        index = file_name.find(".")
        return file_name[:index]

    def compile(self):
        if self.isdir:
            files = glob.glob(f'{self.file}/*.jack')
            for file in files:
                self.file_name = os.path.basename(file)
                index = self.file_name.find(".")
                file_name = self.file_name[:index]
                generate_files = CompilationEngine(file, file_name + ".xml")
        # this is for the single file
        else:
            self.file_name = os.path.basename(self.file)
            index = self.file_name.find(".")
            file_name = self.file_name[:index]
            generate_file = CompilationEngine(self.file, file_name + ".xml")

    # This method is able to generate another XML file(T.xml),which only has tokens.
    @staticmethod
    def generate_Token_file(input_file, output_file):
        try:
            with open(output_file, 'a') as fw:
                fw.write("<tokens>\n")
                tokens = JackTokenizer(input_file)
                tokens.process()
                while tokens.hasMoreTokens():
                    tokens.advance()
                    if tokens.token_type == TokenType.KEYWORD:
                        fw.write(f"  <keyword> {tokens.token} </keyword>\n")
                    elif tokens.token_type == TokenType.SYMBOL:
                        fw.write(f"  <symbol> {tokens.token} </symbol>\n")
                    elif tokens.token_type == TokenType.INT_CONSTANT:
                        fw.write(f"  <integerConstant> {tokens.token} </integerConstant>\n")
                    elif tokens.token_type == TokenType.STRING_CONSTANT:
                        fw.write(f"  <stringConstant> {tokens.token} </stringConstant>\n")
                    elif tokens.token_type == TokenType.IDENTIFIER:
                        fw.write(f"  <identifier> {tokens.token} </identifier>\n")
                fw.write("</tokens>")
        except Exception as e:
            print(f"Error: {e}")

    def compileToken(self):
        if self.isdir:
            files = glob.glob(f'{self.file}/*.jack')
            for file in files:
                file_name = self.get_file_name(file)
                output_file = file_name + "T.xml"
                self.generate_Token_file(file, output_file)
        else:
            file_name = self.get_file_name(self.file)
            output_file = file_name + "T.xml"
            self.generate_Token_file(self.file, output_file)


a = JackAnalyzer("Square")
a.compile()
# a.compileToken()
