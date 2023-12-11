// push constant 3030
    @3030
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop pointer 0
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @THIS
    M=D
// push constant 3040
    @3040
    D=A
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
// push constant 32
    @32
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop this 2
    @2
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
// push constant 46
    @46
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop that 6
    @6
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
// push pointer 0
    @THIS
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push pointer 1
    @THAT
    D=M
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
// push this 2
    @2
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
// push that 6
    @6
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
