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
// function Class1.set 0
(Class1.set)  
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
// pop static 0
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @Class1.vm.0
    M=D
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
// pop static 1
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @Class1.vm.1
    M=D
// push constant 0
    @0
    D=A
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
// function Class1.get 0
(Class1.get)  
// push static 0
    @Class1.vm.0
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push static 1
    @Class1.vm.1
    D=M
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
// function Class2.set 0
(Class2.set)  
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
// pop static 0
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @Class2.vm.0
    M=D
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
// pop static 1
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @Class2.vm.1
    M=D
// push constant 0
    @0
    D=A
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
// function Class2.get 0
(Class2.get)  
// push static 0
    @Class2.vm.0
    D=M
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push static 1
    @Class2.vm.1
    D=M
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
// function Sys.init 0
(Sys.init)  
// push constant 6
    @6
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 8
    @8
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// call Class1.set 2
    @Class1.set$ret28
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
    @2
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @Class1.set  // goto function_name
    0;JMP
(Class1.set$ret28)
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
// push constant 23
    @23
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 15
    @15
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// call Class2.set 2
    @Class2.set$ret32
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
    @2
    D=D+A
    @SP
    D=M-D
    @ARG
    M=D
    @SP // this step seems important LCL=SP
    D=M
    @LCL  
    M=D
    @Class2.set  // goto function_name
    0;JMP
(Class2.set$ret32)
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
// call Class1.get 0
    @Class1.get$ret34
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
    @Class1.get  // goto function_name
    0;JMP
(Class1.get$ret34)
// call Class2.get 0
    @Class2.get$ret35
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
    @Class2.get  // goto function_name
    0;JMP
(Class2.get$ret35)
// label END
(END)
// goto END
    @END
    0;JMP
