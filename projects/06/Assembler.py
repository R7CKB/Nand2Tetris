# author:R7CKB@qq.com
# divide this Project into three segments: Paser,Code,Symbol_Table
# do it all by yourself then you will learn it worthwhile

"""
to be honest,you need to have your own thoughts,
besides you can't rely solely on the guideline either.
if you rely too much on it,
you will find it hard for you to implement these all steps one by one.
In my opinion,first,I do it all by guideline,
but then I find it is so hard for me to do these steps.
so I don't do all depend on the guideline,
this version is my views about this project.
I will keep most of the primary steps sand delete some unnecessary steps.
"""


class Parser:  # The parser only need to parse each instruction
    def __init__(self, sentence):
        self.instruction = sentence  # current instruction
        self.instruction_type = ""  # instruction type

    """I delete the method hasMoreLine,I don't think it is useful to implement this project"""

    def advance(self):  # Get next instruction and make it current_instruction
        line = self.instruction
        if "//" in line and not line.startswith("//"):  # for those comments not start withs //
            index = line.find("//")
            self.instruction = line[0:index]  # Handle the case of comments after instructions
        if line.startswith("//") or not line or line.startswith("("):  # Handle single-line comment and spaces and labels
            self.instruction = ""
        else:
            self.instruction = line.strip()  # Remove unnecessary symbols

    def instructionType(self):  # classify these instructions
        line = self.instruction  # only to shorten the length
        if line.startswith("@"):
            self.instruction_type = "A_INSTRUCTION"
        elif line.startswith("//") or not line or line.startswith("("):  # if line is single-line comment or spaces or labels
            self.instruction_type = ""
        else:
            self.instruction_type = "C_INSTRUCTION"
        # In the all project, you will find it is no need to classify L_INSTRUCTION
        # because L_INSTRUCTION is label,and we will deal with labels in the scan method

    def symbol(self):
        return self.instruction[1:]

    def dest(self):
        if ";" not in self.instruction:  # handle case such as D=M
            return self.instruction.split("=")[0]
        else:
            dest_comp = self.instruction.split(";")[0]
            if "=" not in dest_comp:  # handle case such as D;JMP ATTENTION: This D means comp not dest
                return None
            else:
                return dest_comp.split("=")[0]

    def comp(self):
        if ";" not in self.instruction:  # handle case such as D=M
            return self.instruction.split("=")[1]
        else:
            dest_comp = self.instruction.split(";")[0]
            if "=" not in dest_comp:  # handle case such as D;JMP
                return dest_comp
            else:
                return dest_comp.spli("=")[1]

    def jump(self):
        if ";" not in self.instruction:
            return None
        else:
            return self.instruction.split(";")[1]


def comp(code):
    if code in Code.comp_dict:
        return Code.comp_dict.get(code)


def binary(code):  # translate A_INSTRUCTION into machine code
    if int(code) < 0 or int(code) > 32767:  # to make sure the range is correct
        raise ValueError("Invalid Value : %s" % code)
    code = bin(int(code))[2:].zfill(16)  # find in the StackOverFlow,Cool!!!
    return code


def dest(code):
    if code in Code.dest_dict:
        return Code.dest_dict.get(code)


def jump(code):
    if code in Code.jump_dict:
        return Code.jump_dict.get(code)


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


class SymbolTable:
    def __init__(self):
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
            "SCREEN": 16384,
            "KBD": 24576,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
        }

    def addEntry(self, symbol, address):
        self.symbol_table[symbol] = address

    def contains(self, symbol):
        if self.symbol_table.get(symbol) is not None:
            return True
        else:
            return False

    def getAddress(self, symbol):
        return self.symbol_table.get(symbol)


class Assembler:  # This class is responsible for the assembly

    def __init__(self, file_name):
        self.file = file_name
        self.st = SymbolTable()

    def compile(self):
        machine_code = ""
        with open(self.file, "r") as f:
            line = f.readline()
            while line:
                line = line.strip()
                sentence = Parser(line)
                sentence.instructionType()
                sentence_type = sentence.instruction_type
                sentence.advance()  # read instruction
                if sentence_type == "A_INSTRUCTION":
                    instruction = sentence.symbol()
                    if instruction in self.st.symbol_table:  # handle case like instruction in symbol_table
                        instruction = self.st.symbol_table.get(instruction)
                    machine_code = binary(instruction)
                elif sentence_type == "C_INSTRUCTION":
                    instruction_dest = sentence.dest()
                    instruction_comp = sentence.comp()
                    instruction_jump = sentence.jump()
                    machine_code = "111" + comp(instruction_comp) + dest(instruction_dest) + jump(instruction_jump)
                # you don't need to worry about L_INSTRUCTION ,because we will handle it in the scan method
                else:  # single-line and spaces
                    machine_code = ""
                # Create a hack file and write it
                index = self.file.find(".")
                file_name = self.file[:index]
                with open(file_name + ".hack", "a") as fw:  # a means in the mode of appending
                    if machine_code != "":
                        fw.write(machine_code)
                        fw.write("\n")
                line = f.readline()

    def first_scan(self):  # For the first scan, add loops to the symbol_table
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
                    self.st.symbol_table[line[1:-1]] = number + 1  # add labels to the symbol_tables
                line = f.readline()

    def second_scan(self):  # For the second scan, add variables to the symbol_table
        with open(self.file) as f:
            addr = 16  # base address begin from 16
            line = f.readline()
            while line:
                line = line.strip()
                # the following is how to deal with variables
                if line.startswith("@") and line[1:] not in self.st.symbol_table:
                    if line[1:].isdigit():  # deal with case like @32
                        pass
                    else:
                        self.st.symbol_table[line[1:]] = addr
                        addr += 1
                line = f.readline()
            print(self.st.symbol_table)


file_asm = Assembler("Max.asm")
file_asm.first_scan()
file_asm.second_scan()
file_asm.compile()
