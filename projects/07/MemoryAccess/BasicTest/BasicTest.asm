// push constant 10
    @10
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
// push constant 21
    @21
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 22
    @22
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop argument 2
    @2
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
// pop argument 1
    @1
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
// push constant 36
    @36
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop this 6
    @6
    D=A
    @THIS
    D=D+M  
    @addr  // addr = THIS + i
    M=D
    @SP  // SP--
    M=M-1  
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
// push constant 42
    @42
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 45
    @45
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop that 5
    @5
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
// push constant 510
    @510
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop temp 6
    @6
    D=A
    @5
    D=D+A  
    @addr  // addr = 5 + i
    M=D
    @SP  // SP--
    M=M-1
    @SP  // RAM[SP]
    A=M
    D=M
    @addr  // RAM[addr]=RAM[SP]
    A=M
    M=D
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
// push that 5
    @5
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
// push this 6
    @6
    D=A
    @THIS
    D=D+M  
    @addr  // addr = THIS + i
    M=D
    @addr  //RAM[addr]
    A=M
    D=M
    @SP  // RAM[SP]=RAM[addr]
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push this 6
    @6
    D=A
    @THIS
    D=D+M  
    @addr  // addr = THIS + i
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
// push temp 6
    @6
    D=A
    @5
    D=D+A  
    @addr  // addr = 5 + i
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
// finish the program
(END)
    @END
    0;JMP