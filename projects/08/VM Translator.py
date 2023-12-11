# author:R7CKB@qq.com
#  I divide it into three segments: Parser, CodeWriter, Main
# This is for project8,because of the label and the function,
# we need to use indent to let our codes look more readable
"""
Before you do this project, I recommend you to review the project4;
you can have a better understanding of the assembly language.
I'm not an English native speaker, so my sentences maybe wrong sometimes, hope you can understand.
I'm a rookie in the Python, if you can point out my faults, I'll appreciate you very much.
In my opinion, this is as same as the Assembler, just a little different.
Besides, I also need to change the Assembler Construction to make it more coherent.
However, When I begin to implement this project, it isn't as easy as seen.
Unlike Assembler, it's more challenging.
If you have any questions, please ask me at any time.
I'll answer you patiently.

"""

from enum import Enum
import glob  # this for match different .vm files


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
        elif line.startswith("label"):
            self.command_type = CommandType.C_LABEL
        elif line.startswith("if-goto"):
            self.command_type = CommandType.C_IF
        elif line.startswith("goto"):
            self.command_type = CommandType.C_GOTO
        elif line.startswith("function"):
            self.command_type = CommandType.C_FUNCTION
        elif line.startswith("call"):
            self.command_type = CommandType.C_CALL
        elif line.startswith("return"):
            self.command_type = CommandType.C_RETURN
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

    RAM_addr_eq_RAM_SP = """@SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D"""

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
        # In the StaticTest the jump condition must be the file name, not the directory name,
        # so you must adapt to use the file name.
        self.file_name = ""

    # This isn't a good solution for this class,but I'll implement it in my way.
    # instead of using \n for indicating next line,
    # I use a more readable way to implement it(use """ to indicate multiple lines).

    # You must make SP++ after each arithmetic command.
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
        # by running Vm emulator we can know that True=-1 False=0,
        # besides we need to create jump condition (use line number to avoid jumping the same condition);
        # whether true or false,you must make SP++,this is important,
        # In additional,condition judgement must be the jump instruction
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
    @{self.file_name}.{index}
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
                assembler_language = f"""    @{self.file_name}.{index}
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

    @staticmethod
    def write_label(label):
        assembler_language = f"""({label})
"""
        return assembler_language

    @staticmethod
    def write_go_to(label):
        assembler_language = f"""    @{label}
    0;JMP
"""
        return assembler_language

    # let cond equal pop
    # if cond jump to execute the command just after the label
    # else executes the next command.

    # test the FibonacciSeries and BasicLoop, you should use the JGT instead of JLT
    @staticmethod
    def write_if(label):
        assembler_language = f"""    {CodeWriter.sp_dec}
    {CodeWriter.d_eq_sp}
    @{label}
    D;JLT
"""
        return assembler_language

    @staticmethod
    def write_function(function_name, nVars):
        function_label = f"""({function_name})  
"""
        assembler_language = ""
        for i in range(nVars):
            assembler_language += f"""    @0  // push constant 0
    D=A
    {CodeWriter.sp_eq_d}
    {CodeWriter.sp_inc}
"""
        return function_label + assembler_language

    def write_call(self, function_name, nArgs):
        # First, we need to store the return address and caller's segment pointers
        # use sp pointer to store each value
        # second. We need to reposition LCL and ARG
        assembler_language = f"""    @{function_name}$ret{self.number}
    D=A  // This A mean address (But Why?)
    {CodeWriter.sp_eq_d}  // push return_address
    {CodeWriter.sp_inc}
    @LCL  // push LCL
    D=M
    {CodeWriter.sp_eq_d}  
    {CodeWriter.sp_inc}
    @ARG  // push ARG
    D=M
    {CodeWriter.sp_eq_d}  
    {CodeWriter.sp_inc}
    @THIS  // push THIS
    D=M
    {CodeWriter.sp_eq_d}  
    {CodeWriter.sp_inc}
    @THAT  // push THAT
    D=M
    {CodeWriter.sp_eq_d}  
    {CodeWriter.sp_inc}
    @5  // reposition ARG (This should be OK)
    D=A
    @{nArgs}
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @{function_name}  // goto function_name
    0;JMP
({function_name}$ret{self.number})
"""
        return assembler_language

    # This is challenging;
    # after seeing many of the answers, it seems they all see end_frame as R13 or R14,
    # which is mentioned in the book.
    @staticmethod
    def write_return():
        assembler_language = f"""    @LCL
    D=M
    @R14  // R14=end_Frame=LCL
    M=D
    @5  // retAddr=RAM[end_Frame-5]
    D=A
    @R14
    D=M-D
    A=D
    D=M
    @R15  // return_address=R15
    M=D
    {CodeWriter.sp_dec}  
    {CodeWriter.d_eq_sp}
    @ARG  // RAM[ARG]=pop()
    A=M
    M=D
    @1  // SP=ARG+1
    D=A
    @ARG  
    D=M+D
    @SP
    M=D
    @1  // THAT=RAM[R14-1]
    D=A
    @R14
    D=M-D
    A=D
    D=M
    @THAT
    M=D
    @2  // THIS=RAM[R14-2]
    D=A
    @R14
    D=M-D
    A=D
    D=M
    @THIS
    M=D
    @3  // ARG=RAM[R14-3]
    D=A
    @R14
    D=M-D
    A=D
    D=M
    @ARG
    M=D
    @4  // LCL=RAM[R14-4]
    D=A
    @R14
    D=M-D
    A=D
    D=M
    @LCL
    M=D
    @R15
    A=M  // Why is there this sentence?
    0;JMP
"""
        return assembler_language


class Main:  # drives the process (VMTranslator)
    def __init__(self, file):
        self.file = file
        self.file_name = ""

    def compile(self):
        files = glob.glob(f"{self.file}/*.vm")  # traverse all the .vm files,just for directory
        sys_file = glob.glob(f"{self.file}/Sys.vm")
        # Create an asm file and write it
        # index = self.file.find(".")
        # file_name = self.file[:index]
        translator = CodeWriter(self.file)
        try:
            with open(self.file + ".asm", "a") as fw:
                if sys_file:
                    # You can find this in the book,
                    # before doing this project, you should read the book
                    boot_strap_code = f"""    @256
    D=A
    @SP  // SP=256
    M=D
{translator.write_call("Sys.init", 0)}"""
                    fw.write(boot_strap_code)
            for file in files:
                self.file_name = file.split('\\')[1]
                translator.file_name = self.file_name
                with open(file, "r") as f, open(self.file + ".asm", "a") as fw:
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
                        elif command.command_type == CommandType.C_LABEL:
                            assembler_language = translator.write_label(command.arg1())
                            fw.write(assembler_language)
                        elif command.command_type == CommandType.C_IF:
                            assembler_language = translator.write_if(command.arg1())
                            fw.write(assembler_language)
                        elif command.command_type == CommandType.C_GOTO:
                            assembler_language = translator.write_go_to(command.arg1())
                            fw.write(assembler_language)
                        elif command.command_type == CommandType.C_CALL:
                            assembler_language = translator.write_call(command.arg1(), command.arg2())
                            fw.write(assembler_language)
                        elif command.command_type == CommandType.C_FUNCTION:
                            assembler_language = translator.write_function(command.arg1(), command.arg2())
                            fw.write(assembler_language)
                        elif command.command_type == CommandType.C_RETURN:
                            assembler_language = translator.write_return()
                            fw.write(assembler_language)
                        line = f.readline()
        except FileNotFoundError as e:
            print(f"Error: {e}")


a = Main("StaticsTest")
a.compile()
