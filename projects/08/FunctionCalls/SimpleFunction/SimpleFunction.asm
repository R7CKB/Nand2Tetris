// function SimpleFunction.test 2
(SimpleFunction.test)  
    @0  // push constant 0
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
    @0  // push constant 0
    D=A
    @SP  // RAM[SP]=D
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
// push local 1
    @1
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
// not
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP
    A=M
    M=!D  // same logic as the neg
    @SP  // SP++
    M=M+1
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
// return
    @LCL
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
    @SP  // SP--
    M=M-1  
    @SP
    A=M
    D=M  // D=RAM[SP]
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
