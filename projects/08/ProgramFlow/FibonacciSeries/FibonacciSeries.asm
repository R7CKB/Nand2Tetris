// push argument 1
    @1
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
// pop pointer 1
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @THAT
    M=D
// push constant 0
    @0
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop that 0
    @0
    D=A
    @THAT
    D=D+M  
    @addr  // addr = THAT + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// push constant 1
    @1
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop that 1
    @1
    D=A
    @THAT
    D=D+M  
    @addr  // addr = THAT + i
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
// push constant 2
    @2
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
// if-goto COMPUTE_ELEMENT
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @COMPUTE_ELEMENT
    D;JNE
// goto END
    @END
    0;JMP
// label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// push that 0
    @0
    D=A
    @THAT
    D=D+M  
    @addr // addr = THAT + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push that 1
    @1
    D=A
    @THAT
    D=D+M  
    @addr // addr = THAT + i
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
// pop that 2
    @2
    D=A
    @THAT
    D=D+M  
    @addr  // addr = THAT + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// push pointer 1
    @THAT
    D=M
    @SP  // RAM[SP]=D
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
// pop pointer 1
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @THAT
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
// goto LOOP
    @LOOP
    0;JMP
// label END
(END)
// finish the program
(END)
    @END
    0;JMP