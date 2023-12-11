    @256
    D=A
    @SP  // SP=256
    M=D
    @Sys.init$ret0
    D=A  // This A mean address (But Why?)
    @SP  // RAM[SP]=D
    A=M
    M=D  // push return_address
    @SP  // SP++
    M=M+1
    @LCL  // push LCL
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @ARG  // push ARG
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THIS  // push THIS
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THAT  // push THAT
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @5  // reposition ARG (This should be OK)
    D=A
    @0
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @Sys.init  // goto function_name
    0;JMP
(Sys.init$ret0)
// function Sys.init 0
(Sys.init)  
// push constant 4000
    @4000
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
// push constant 5000
    @5000
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
// call Sys.main 0
    @Sys.main$ret6
    D=A  // This A mean address (But Why?)
    @SP  // RAM[SP]=D
    A=M
    M=D  // push return_address
    @SP  // SP++
    M=M+1
    @LCL  // push LCL
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @ARG  // push ARG
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THIS  // push THIS
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THAT  // push THAT
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @5  // reposition ARG (This should be OK)
    D=A
    @0
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @Sys.main  // goto function_name
    0;JMP
(Sys.main$ret6)
// pop temp 1
    @1
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
// label LOOP
(LOOP)
// goto LOOP
    @LOOP
    0;JMP
// function Sys.main 5
(Sys.main)  
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
    @0  // push constant 0
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 4001
    @4001
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
// push constant 5001
    @5001
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
// push constant 200
    @200
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop local 1
    @1
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
// push constant 40
    @40
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop local 2
    @2
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
// push constant 6
    @6
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// pop local 3
    @3
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
// push constant 123
    @123
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// call Sys.add12 1
    @Sys.add12$ret22
    D=A  // This A mean address (But Why?)
    @SP  // RAM[SP]=D
    A=M
    M=D  // push return_address
    @SP  // SP++
    M=M+1
    @LCL  // push LCL
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @ARG  // push ARG
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THIS  // push THIS
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @THAT  // push THAT
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D  
    @SP  // SP++
    M=M+1
    @5  // reposition ARG (This should be OK)
    D=A
    @1
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @Sys.add12  // goto function_name
    0;JMP
(Sys.add12$ret22)
// pop temp 0
    @0
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
// push local 2
    @2
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
// push local 3
    @3
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
// push local 4
    @4
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
// function Sys.add12 0
(Sys.add12)  
// push constant 4002
    @4002
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
// push constant 5002
    @5002
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
// push constant 12
    @12
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
