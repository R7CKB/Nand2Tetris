# author:R7CKB@qq.com
# divide it into three segments: Parser,CodeWriter,Main

"""
I'm not an English native speaker,so my sentences maybe wrong sometimes,hope you can understand.
I'm a rookie in the Python,if you can point out my faults,I will appreciate you very much.
In my opinion,this is as same as the Assembler,just a little different.
Besides,I also need to change the Assembler Construction to make it more coherent.
However, When I begin to implement to this project,it is not as easy as seen.
unlike Assembler,it is more difficult.
if you have any questions,please ask me at any time.
I will answer you patiently.
"""

from enum import Enum


class CommandType(Enum):  # use enumerate to make types instead of string
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9


class Parser:  # parses each VM command into its lexical elements
    """
    Parser class is as same as the Assembler,this class is not difficult.
    """

    def __init__(self, sentence):
        self.command = sentence
        self.command_type = ""

    def advance(self):  # Get next instruction and make it current_instruction
        line = self.command
        if "//" in line and not line.startswith("//"):  # For those comments that follow the commands
            index = line.find("//")
            self.command = line[:index]
        if line.startswith("//") or not line:  # For those comments that stands alone
            self.command = ""
        else:
            self.command = line.strip()  # Remove unnecessary things(ignore space and comments)

    """ 
    maybe what I think is wrong,
    but I don't think the has_more_line method is useful (maybe because the Python language? ヾ(•ω•`)o)
    maybe the structure is different?
    """

    def commandType(self):  # classify these commands
        line = self.command
        if line.startswith(("add", "neg", "sub", "eq", "gt", "lt", "and", "or", "not")):
            self.command_type = CommandType.C_ARITHMETIC
        elif line.startswith("push"):
            self.command_type = CommandType.C_PUSH
        elif line.startswith("pop"):
            self.command_type = CommandType.C_POP
        else:
            self.command_type = ""

    def arg1(self):
        if self.command_type == CommandType.C_ARITHMETIC:  # for those commands like add,sub and so on.
            return self.command
        return self.command.split()[1]

    def arg2(self):
        return int(self.command.split()[2])


class CodeWriter:  # writes the assembly code that implements the parsed command
    def __init__(self, file):
        self.file = file
        self.number = 0  # file line number

    # This is not a good solution for this class,but I will implement it with my way.
    # instead of using \n for indicating next line,
    # I use a more readable way to realize it(use """ indicate multiple lines).
    # you must make SP++ after each command.

    def write_arithmetic(self, command):
        assembler_language = ""
        # SP++
        sp_inc = """@SP  // SP++
M=M+1"""
        # SP--
        sp_dec = """@SP  // SP--
M=M-1"""
        # RAM[SP]=D
        sp_eq_d = """@SP  // RAM[SP]=D
A=M
M=D"""
        # D=RAM[SP]
        d_eq_sp = """A=M
D=M  // D=*SP"""
        # -1 means true
        sp_eq_true = """@SP
A=M
M=-1"""
        # 0 means false
        sp_eq_false = """@SP
A=M
M=0"""
        if command == "add":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
@SP
A=M
D=M+D  // D=RAM[SP-2]+RAM[SP-1]
{sp_eq_d}
{sp_inc}
"""
        elif command == "sub":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
@SP
A=M
D=M-D  // D=RAM[SP-2]-RAM[SP-1]
{sp_eq_d}
{sp_inc}
"""
        elif command == "neg":
            assembler_language = f"""{sp_dec}
{sp_eq_d}
@SP
A=M
M=-D  // M=-D is better than M=-M
{sp_inc}
"""
        elif command == "and":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
@SP
A=M
D=D&M  // D=RAM[SP-1]&RAM[SP-2]
{sp_eq_d}
{sp_inc}
"""
        elif command == "or":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
@SP
A=M
D=D|M  // D=RAM[sp-1]|RAM[sp-2]
{sp_eq_d}
{sp_inc}
"""
        elif command == "not":
            assembler_language = f"""{sp_dec}
{sp_eq_d}
@SP
A=M
M=!D  // same as the neg
{sp_inc}
"""
        # these three conditional command is difficult
        # by running Vm emulator we can know that True=-1 False=0
        # besides we need to create jump condition(use line number to avoid jump the same condition)
        # whether true or false,you must make SP++,this is important
        elif command == "eq":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
A=M
D=M-D  // D=RAM[SP-2]-RAM[SP-1]
@EQ{self.number}  // true
D;JEQ
{sp_eq_false}
{sp_inc}
@END{self.number}  // false
0;JMP
(EQ{self.number})  
{sp_eq_true}
{sp_inc}
(END{self.number})
"""
        elif command == "gt":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
A=M
D=M-D  // D=RAM[SP-2]-RAM[SP-1]
@GT{self.number}  // true
D;JGT
{sp_eq_false}
{sp_inc}
@END{self.number}  // false
0;JMP
(GT{self.number})  
{sp_eq_true}
{sp_inc}
(END{self.number})
"""
        elif command == "lt":
            assembler_language = f"""{sp_dec}
{d_eq_sp}
{sp_dec}
A=M
D=M-D  // D=RAM[SP-2]-RAM[SP-1]
@LT{self.number}  // true
D;JLT
{sp_eq_false}
{sp_inc}
@END{self.number}  // false
0;JMP
(LT{self.number})
{sp_eq_true}
{sp_inc}
(END{self.number})
"""
        return assembler_language

    def write_push_pop(self, command, segment, index):
        assembler_language = ""
        # SP++
        sp_inc = """@SP  // SP++
M=M+1"""
        # SP--
        sp_dec = """@SP  // SP--
M=M-1"""
        # RAM[SP]=D
        sp_eq_d = """@SP  // RAM[SP]=D
A=M
M=D"""
        # D=RAM[SP]
        d_eq_sp = """@SP
A=M
D=M  // D=RAM[SP]"""
        RAM_addr__eq_RAM_SP = """@SP  // RAM[SP]
A=M
D=M
@addr  // RAM[addr]=RAM[SP]
A=M
M=D"""
        if command == CommandType.C_POP:
            # we need to find a place to store addr
            # use addr(a variable)(maybe there has some better ways?)
            if segment == "local":
                assembler_language = f"""@{index}
D=A
@LCL
D=D+M  // addr = LCL + i
@addr  
M=D
{sp_dec}  
{RAM_addr__eq_RAM_SP}
"""
            elif segment == "argument":
                assembler_language = f"""@{index}
D=A
@ARG
D=D+M  // addr = ARG + i
@addr  
M=D
{sp_dec}  
{RAM_addr__eq_RAM_SP}
"""
            elif segment == "this":
                assembler_language = f"""@{index}
D=A
@THIS
D=D+M  // addr = THIS + i
@addr  
M=D
{sp_dec}  
{RAM_addr__eq_RAM_SP}
"""
            elif segment == "that":
                assembler_language = f"""@{index}
D=A
@THAT
D=D+M  // addr = THAT + i
@addr  
M=D
{sp_dec}  
{RAM_addr__eq_RAM_SP}
"""
            elif segment == "static":
                assembler_language = f"""{sp_dec}
{d_eq_sp}
@{self.file}.{index}
M=D
"""
            # because temp from 5 to 12,so D=D+A instead of D=D+M
            # same as the push operation
            elif segment == "temp":
                assembler_language = f"""@{index}
D=A
@5
D=D+A  // addr = 5 + i
@addr
M=D
{sp_dec}
{RAM_addr__eq_RAM_SP}
"""
            elif segment == "pointer":
                if index == 0:
                    assembler_language = f"""{sp_dec}
{d_eq_sp}
@THIS
M=D
"""
                else:
                    assembler_language = f"""{sp_dec}
{d_eq_sp}
@THAT
M=D
"""
        elif command == CommandType.C_PUSH:
            if segment == "local":
                assembler_language = f"""@{index}
D=A
@LCL
D=D+M  // addr = LCL + i
A=D  
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "argument":
                assembler_language = f"""@{index}
D=A
@ARG
D=D+M  // addr = ARG + i
A=D  
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "this":
                assembler_language = f"""@{index}
D=A
@THIS
D=D+M  // addr = THIS + i
A=D  
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "that":
                assembler_language = f"""@{index}
D=A
@THAT
D=D+M  // addr = THAT + i
A=D  
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "constant":
                assembler_language = f"""@{index}
D=A
{sp_eq_d}
{sp_inc}
"""
            elif segment == "static":
                assembler_language = f"""@{self.file}.{index}
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "temp":
                assembler_language = f"""@{index}
D=A
@5
D=D+A  // addr = 5 + i
A=D  
D=M
{sp_eq_d}
{sp_inc}
"""
            elif segment == "pointer":
                if index == 0:
                    assembler_language = f"""@THIS
D=M
{sp_eq_d}
{sp_inc}
"""
                else:
                    assembler_language = f"""@THAT
D=M
{sp_eq_d}
{sp_inc}
"""
        return assembler_language


class Main:  # drives the process (VMTranslator)
    def __init__(self, file):
        self.file = file

    def compile(self):
        # Create an asm file and write it
        index = self.file.find(".")
        file_name = self.file[:index]
        translator = CodeWriter(file_name)
        try:
            with open(self.file, "r") as f, open(file_name + ".asm", "a") as fw:
                line = f.readline()
                while line:
                    line = line.strip()
                    command = Parser(line)
                    command.advance()
                    command.commandType()
                    if command.command != "":
                        fw.write("// " + command.command + "\n")  # generate comments to help debug the project
                        translator.number += 1
                    if command.command_type == CommandType.C_ARITHMETIC:
                        assembler_language = translator.write_arithmetic(command.arg1())
                        fw.write(assembler_language)
                    elif command.command_type == CommandType.C_PUSH:
                        assembler_language = translator.write_push_pop(command.command_type, command.arg1(),
                                                                       command.arg2())
                        fw.write(assembler_language)
                    elif command.command_type == CommandType.C_POP:
                        assembler_language = translator.write_push_pop(command.command_type, command.arg1(),
                                                                       command.arg2())
                        fw.write(assembler_language)
                    line = f.readline()
        except FileNotFoundError as e:
            print(f"Error: {e}")


a = Main("StaticTest.vm")
a.compile()
