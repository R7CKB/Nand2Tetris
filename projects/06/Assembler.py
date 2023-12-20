# author:R7CKB@qq.com
# divide this Project into three segments: Paser, Code, Symbol_Table
# do it all by yourself then you'll learn it worthwhile

"""
I'm not an English native speaker, so my sentences maybe wrong sometimes, hope you can understand.
I'm a rookie in the Python, I want you to point out my faults, and I'll correct them as soon as possible.
To be honest, you need to have your own thoughts,
besides you can't rely solely on the guidelines either.
If you rely too much on it,
you will find it hard for you to implement these all steps one by one.
In my opinion, first,I do it all by guideline,
but then I find it's so hard for me to do these steps.
So I don't do all depend on the guidelines,
this version is my views about this project.
I'll keep most of the primary steps and delete some unnecessary steps.
"""
from enum import Enum


class InstructionType(Enum):  # use enumerating to make a type not be the string
    A_INSTRUCTION = 1
    C_INSTRUCTION = 2


class Parser:  # The parser only needs to parse each instruction
    def __init__(self, sentence):
        self.instruction = sentence  # current instruction
        self.instruction_type = ""  # instruction type

    """I delete the method hasMoreLine, I don't think it's useful to implement this project"""

    def advance(self):  # Get the next instruction and make it current_instruction
        line = self.instruction
        if "//" in line and not line.startswith("//"):  # for those comments not start withs //
            index = line.find("//")
            self.instruction = line[0:index]  # Handle the case of comments after instructions
        if line.startswith("//") or not line or line.startswith(
                "("):  # Handle single-line comment and spaces and labels
            self.instruction = ""
        else:
            self.instruction = line.strip()  # Remove unnecessary symbols

    def instructionType(self):  # classify these instructions
        line = self.instruction  # only to shorten the length
        if line.startswith("@"):
            self.instruction_type = InstructionType.A_INSTRUCTION
        elif line.startswith("//") or not line or line.startswith(
                "("):  # if line is single-line comment or spaces or labels
            self.instruction_type = ""
        else:
            self.instruction_type = InstructionType.C_INSTRUCTION
            # In the all projects, you'll find it's no need to classify L_INSTRUCTION
            # because L_INSTRUCTION is label,and we'll deal with labels in the scan method

    def symbol(self):
        return self.instruction[1:]

    def dest(self):
        if ";" not in self.instruction:  # handle a case such as D=M
            return self.instruction.split("=")[0]
        else:
            dest_comp = self.instruction.split(";")[0]
            if "=" not in dest_comp:  # handle a case such as D;JMP ATTENTION: This D means comp not dest
                return None
            else:
                return dest_comp.split("=")[0]

    def comp(self):
        if ";" not in self.instruction:  # handle a case such as D=M
            return self.instruction.split("=")[1]
        else:
            dest_comp = self.instruction.split(";")[0]
            if "=" not in dest_comp:  # handle a case such as D;JMP
                return dest_comp
            else:
                return dest_comp.spli("=")[1]

    def jump(self):
        if ";" not in self.instruction:
            return None
        else:
            return self.instruction.split(";")[1]


class Code:
    comp_dict = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        '!D': '0001101',
        '!A': '0110001',
        '-D': '0001111',
        '-A': '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M': '1110000',
        '!M': '1110001',
        '-M': '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101',
    }
    dest_dict = {
        None: '000',
        'M': '001',
        'D': '010',
        'DM': '011',  # my version point that the DM equals MD
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'ADM': '111',  # and ADM also equals AMD
        'AMD': '111',
    }
    jump_dict = {
        None: '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111',
    }

    @staticmethod
    def jump(code):
        if code in Code.jump_dict:
            return Code.jump_dict.get(code)

    @staticmethod
    def dest(code):
        if code in Code.dest_dict:
            return Code.dest_dict.get(code)

    @staticmethod
    def binary(code):  # translate A_INSTRUCTION into machine code
        MAX_VALUE = 32767
        try:
            if not 0 <= int(code) <= MAX_VALUE:  # to make sure the range is correct
                raise ValueError("Invalid Value : %s" % code)
            code = bin(int(code))[2:].zfill(16)  # find in the StackOverFlow, Cool!!!
            return code
        except ValueError as e:
            print(f"Error:{e}")
            return None

    @staticmethod
    def comp(code):
        if code in Code.comp_dict:
            return Code.comp_dict.get(code)


class SymbolTable:
    def __init__(self):
        SCREEN_ADDRESS = 16384
        KBD_ADDRESS = 24576
        self.symbol_table = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": SCREEN_ADDRESS,
            "KBD": KBD_ADDRESS,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
        }

    def add_entry(self, symbol, address):
        self.symbol_table[symbol] = address

    def contains(self, symbol):
        return symbol in self.symbol_table

    def get_address(self, symbol):
        return self.symbol_table.get(symbol)


class Assembler:  # This class is responsible for the assembly

    def __init__(self, file_name):
        self.file = file_name
        self.st = SymbolTable()

    def compile(self):
        # Create a hack file and write it
        index = self.file.find(".")
        file_name = self.file[:index]
        try:
            with open(self.file, "r") as f, open(file_name + ".hack", "a") as fw:  # a means in the mode of appending
                line = f.readline()
                while line:
                    line = line.strip()
                    sentence = Parser(line)
                    sentence.instructionType()
                    sentence_type = sentence.instruction_type
                    sentence.advance()  # read instruction
                    if sentence_type == InstructionType.A_INSTRUCTION:
                        instruction = sentence.symbol()
                        if instruction in self.st.symbol_table:  # handle a case like instruction in symbol_table
                            instruction = self.st.get_address(instruction)
                        machine_code = Code.binary(instruction)
                    elif sentence_type == InstructionType.C_INSTRUCTION:
                        instruction_dest = sentence.dest()
                        instruction_comp = sentence.comp()
                        instruction_jump = sentence.jump()
                        machine_code = "111" + Code.comp(instruction_comp) + Code.dest(instruction_dest) + Code.jump(
                            instruction_jump)
                    # you don't need to worry about L_INSTRUCTION, because we'll handle it in the scan method
                    else:  # single-line and spaces
                        machine_code = ""
                    if machine_code != "":
                        fw.write(machine_code)
                        fw.write("\n")
                    line = f.readline()
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def first_scan(self):  # For the first scan, add loops to the symbol_table
        try:
            with open(self.file) as f:
                number = -1  # Start with the zero row, not the first row, so set it to -1
                line = f.readline()
                while line:
                    line = line.strip()
                    # the following is how to deal with labels
                    if not line.startswith("(") and not line.startswith("//") and line != "":
                        # only instructions can be calculated into numbers
                        number += 1
                    if line.startswith("("):
                        self.st.add_entry(line[1:-1], number + 1)  # add labels to the symbol_tables
                    line = f.readline()
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def second_scan(self):  # For the second scan, add variables to the symbol_table
        try:
            with open(self.file) as f:
                BASE_ADDRESS = 16  # base address begins from 16
                line = f.readline()
                while line:
                    line = line.strip()
                    # the following is how to deal with variables
                    if line.startswith("@") and not self.st.contains(line[1:]):
                        if line[1:].isdigit():  # deal with case like @32
                            pass
                        else:
                            self.st.add_entry(line[1:], BASE_ADDRESS)
                            BASE_ADDRESS += 1
                    line = f.readline()
                print(self.st.symbol_table)
        except FileNotFoundError as e:
            print(f"Error: {e}")


file_asm = Assembler("Max.asm")
file_asm.first_scan()
file_asm.second_scan()
file_asm.compile()
