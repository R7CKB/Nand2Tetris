# Author:R7CKB@qq.com
# Divide it into three segments: Parser, CodeWriter and Main.

"""
I'm not an English native speaker, so my sentences maybe wrong sometimes, hope you can understand.
I'm a rookie in the Python, if you can point out my faults, I'll appreciate you very much.
If you have any questions, please ask me at any time.
I'll answer you patiently.
"""

from enum import Enum


class CommandType(Enum):  # use enumerating to make types instead of string
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
    Parser class is as same as the Assembler, this class isn't difficult.
    """

    def __init__(self, sentence):
        self.command = sentence
        self.command_type = ""

    def advance(self):  # Get the next instruction and make it current_instruction
        line = self.command
        if "//" in line and not line.startswith("//"):  # For those comments that follow the commands
            index = line.find("//")
            self.command = line[:index].strip()
        elif not line.startswith("//") and line:  # not space line and comment line
            self.command = line.strip()
        else:  # For those comments that stand alone
            self.command = ""  # Remove unnecessary things (ignore space and comments)

    """ 
    maybe what I think is wrong,
    but I don't think the has_more_line method is useful (maybe because the Python language? ヾ(•ω•`)o)
    or maybe the structure is different?
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

    # RAM[addr]=RAM[SP]
    RAM_addr_eq_RAM_SP = """@SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D"""

    # RAM[SP]=RAM[addr]
    RAM_sp_eq_RAM_addr = """@addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D"""

    # -1 means true
    sp_eq_true = """@SP
    A=M
    M=-1"""

    # 0 means false
    sp_eq_false = """@SP
    A=M
    M=0"""

    def __init__(self, file):
        self.file = file
        self.number = 0  # file line number

    # This isn't a good solution for this class,but I'll implement it with my way.
    # instead of using \n for indicating next line,
    # I use a more readable way to realize it(use """ indicate multiple lines).
    # You must make SP++ after each command.

    def write_arithmetic(self, command):
        assembler_language = ""

        if command == "add":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    @SP
    A=M
    D=M+D  // D=RAM[SP-2]+RAM[SP-1]
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        elif command == "sub":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    @SP
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        elif command == "neg":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @SP
    A=M
    M=-D  // M=-D is better than M=-M (I think)
    {CodeWriter.sp_inc}
"""
        elif command == "and":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    @SP
    A=M
    D=D&M  // D=RAM[SP-1]&RAM[SP-2] (This is depend on the C-instruction)
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        elif command == "or":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    @SP
    A=M
    D=D|M  // D=RAM[sp-1]|RAM[sp-2]
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        elif command == "not":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @SP
    A=M
    M=!D  // same logic as the neg
    {CodeWriter.sp_inc}
"""
        # these three conditional commands are challenging;
        # besides, we need to create jump condition (use line number to avoid jumping the same condition);
        # whether true or false,you must make SP++,this is important,
        # In additional,condition judgement must be the jump instruction.
        elif command == "eq":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    @EQ{self.number}  // if true,jump to the EQ condition.
    D;JEQ
    {CodeWriter.sp_eq_false}
    {CodeWriter.sp_inc}
    @END{self.number}  // if false,jump to the END,false operations have already been done.
    0;JMP
(EQ{self.number})  
    {CodeWriter.sp_eq_true}
    {CodeWriter.sp_inc}
(END{self.number})
"""
        elif command == "gt":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]>RAM[SP-1]
    @GT{self.number}  // if true,jump to the EQ condition.
    D;JGT
    {CodeWriter.sp_eq_false}
    {CodeWriter.sp_inc}
    @END{self.number}  // if false,jump to the END,false operations have already been done.
    0;JMP
(GT{self.number})  
    {CodeWriter.sp_eq_true}
    {CodeWriter.sp_inc}
(END{self.number})
"""
        elif command == "lt":
            assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    {CodeWriter.sp_dec}
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]<RAM[SP-1]
    @LT{self.number}  // if true,jump to the EQ condition.
    D;JLT
    {CodeWriter.sp_eq_false}
    {CodeWriter.sp_inc}
    @END{self.number}  // if false,jump to the END,false operations have already been done.
    0;JMP
(LT{self.number})
    {CodeWriter.sp_eq_true}
    {CodeWriter.sp_inc}
(END{self.number})
"""
        return assembler_language

    def write_push_pop(self, command, segment, index):
        assembler_language = ""
        if command == CommandType.C_POP:
            # we need to find a place to store addr
            # use addr(a variable)(maybe there has some better ways?) to store address
            # // pop local i
            # addr ← LCL+i
            # SP--
            # RAM[addr] ← RAM[SP]
            if segment == "local":
                assembler_language = f"""    @{index}
    D=A
    @LCL
    D=D+M  
    @addr  // addr = LCL + i
    M=D
    {CodeWriter.sp_dec}  
    {CodeWriter.RAM_addr_eq_RAM_SP}
"""
            # // pop argument i
            # as same as the local
            elif segment == "argument":
                assembler_language = f"""    @{index}
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    {CodeWriter.sp_dec}  
    {CodeWriter.RAM_addr_eq_RAM_SP}
"""
            # // pop this i
            # as same as the local
            elif segment == "this":
                assembler_language = f"""    @{index}
    D=A
    @THIS
    D=D+M  
    @addr  // addr = THIS + i
    M=D
    {CodeWriter.sp_dec}  
    {CodeWriter.RAM_addr_eq_RAM_SP}
"""
            # // pop that i
            # as same as the local
            elif segment == "that":
                assembler_language = f"""    @{index}
    D=A
    @THAT
    D=D+M  
    @addr  // addr = THAT + i
    M=D
    {CodeWriter.sp_dec}  
    {CodeWriter.RAM_addr_eq_RAM_SP}
"""
            # Constant can't be pop.
            # // Pop static i
            # This is different from the four instructions above,
            # when we push/pop static values,
            # like push/pop filename.i
            elif segment == "static":
                assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @{self.file}.{index}
    M=D
"""
            # because temp is from 5 to 12,so use D=D+A instead of D=D+M
            # push/pop temp i as same as the push/pop RAM[5+i]
            # addr = 5+i
            # SP--
            # RAM[addr] ← RAM[SP]
            elif segment == "temp":
                assembler_language = f"""    @{index}
    D=A
    @5
    D=D+A  
    @addr  // addr = 5 + i
    M=D
    {CodeWriter.sp_dec}
    {CodeWriter.RAM_addr_eq_RAM_SP}
"""
            # push/pop pointer 0 as same as the push/pop THIS
            # push/pop pointer 1 as same as the push/pop THAT
            elif segment == "pointer":
                if index == 0:
                    assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @THIS
    M=D
"""
                else:
                    assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @THAT
    M=D
"""
        # like the pop operations,
        # we use addr to complete all operations.
        elif command == CommandType.C_PUSH:
            # // push local i
            # addr ← LCL + i
            # RAM[SP] ← RAM[addr]
            # SP++
            if segment == "local":
                assembler_language = f"""    @{index}
    D=A
    @LCL
    D=D+M
    @addr  // addr = LCL + i
    M=D
    {CodeWriter.RAM_sp_eq_RAM_addr}
    {CodeWriter.sp_inc}
"""
            # // push argument i
            # as same as the local
            elif segment == "argument":
                assembler_language = f"""    @{index}
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    {CodeWriter.RAM_sp_eq_RAM_addr}
    {CodeWriter.sp_inc}
"""
            # // push this i
            # as same as the local
            elif segment == "this":
                assembler_language = f"""    @{index}
    D=A
    @THIS
    D=D+M  
    @addr  // addr = THIS + i
    M=D
    {CodeWriter.RAM_sp_eq_RAM_addr}
    {CodeWriter.sp_inc}
"""
            # // push that i
            # as same as the local
            elif segment == "that":
                assembler_language = f"""    @{index}
    D=A
    @THAT
    D=D+M  
    @addr // addr = THAT + i
    M=D
    {CodeWriter.RAM_sp_eq_RAM_addr}
    {CodeWriter.sp_inc}
"""
            # // push constant i
            # D=i
            # RAM[SP]=D
            # SP++
            elif segment == "constant":
                assembler_language = f"""    @{index}
    D=A
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
            # // push static i
            # as same as the push operation
            elif segment == "static":
                assembler_language = f"""    @{self.file}.{index}
    D=M
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
            # // push temp i
            # addr ← 5+i
            # RAM[SP] ← RAM[addr]
            # SP++
            elif segment == "temp":
                assembler_language = f"""    @{index}
    D=A
    @5
    D=D+A  
    @addr  // addr = 5 + i
    M=D
    {CodeWriter.RAM_sp_eq_RAM_addr}
    {CodeWriter.sp_inc}
"""
            # // push pointer i
            # as same as the pop operation
            elif segment == "pointer":
                if index == 0:
                    assembler_language = f"""    @THIS
    D=M
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
                else:
                    assembler_language = f"""    @THAT
    D=M
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        return assembler_language


class Main:  # drives the process (VMTranslator)
    def __init__(self, file):
        self.file = file

    def finish_program(self, file):
        index = self.file.find(".")
        file_name = self.file[:index]
        try:
            with open(file, "a") as fw:
                finish_sentence = """// finish the program
(END)
    @END
    0;JMP"""
                fw.write(finish_sentence)
        except Exception as e:
            print(f"Error: {e}")

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
            self.finish_program(f"{file_name}.asm")
        except Exception as e:
            print(f"Error: {e}")


a = Main("StaticTest.vm")
a.compile()
