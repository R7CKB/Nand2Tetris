// push constant 0
    @0
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop local 0
    @0
    D=A
    @LCL
    D=D+M  
    @addr  // addr = LCL + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// label LOOP
(LOOP)
// push argument 0
    @0
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push local 0
    @0
    D=A
    @LCL
    D=D+M
    @addr  // addr = LCL + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// add
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M+D  // D=RAM[SP-2]+RAM[SP-1]
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop local 0
    @0
    D=A
    @LCL
    D=D+M  
    @addr  // addr = LCL + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// push argument 0
    @0
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 1
    @1
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// sub
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop argument 0
    @0
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// push argument 0
    @0
    D=A
    @ARG
    D=D+M  
    @addr  // addr = ARG + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// if-goto LOOP
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @LOOP
    D;JNE
// push local 0
    @0
    D=A
    @LCL
    D=D+M
    @addr  // addr = LCL + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// finish the program
(END)
    @END
    0;JMP