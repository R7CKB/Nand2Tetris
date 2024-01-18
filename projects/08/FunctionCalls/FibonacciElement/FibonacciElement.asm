    @256
    D=A
    @SP  // SP=256
    M=D
    @Sys.init$ret0
    D=A  // This A mean (return_address)'s address 
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
// function Main.fibonacci 0
(Main.fibonacci)  
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
// lt
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]<RAM[SP-1]
    @LT4  // if true,jump to the EQ condition.
    D;JLT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END4  // if false,jump to the END,false operations have already been done.
    0;JMP
(LT4)
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END4)
// if-goto N_LT_2
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @N_LT_2
    D;JNE
// goto N_GE_2
    @N_GE_2
    0;JMP
// label N_LT_2
(N_LT_2)
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
// return
    @LCL
    D=M
    @end_frame  // end_Frame=LCL
    M=D
    @5  // retAddr=RAM[end_Frame-5]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @return_address  // return_address=R15
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
    @1  // THAT=RAM[end_frame-1]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @THAT
    M=D
    @2  // THIS=RAM[end_frame-2]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @THIS
    M=D
    @3  // ARG=RAM[end_frame-3]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @ARG
    M=D
    @4  // LCL=RAM[end_frame-4]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @LCL
    M=D
    @return_address
    A=M  // use pointer's format
    0;JMP
// label N_GE_2
(N_GE_2)
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
// call Main.fibonacci 1
    @Main.fibonacci$ret14
    D=A  // This A mean (return_address)'s address 
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
    @Main.fibonacci  // goto function_name
    0;JMP
(Main.fibonacci$ret14)
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
// call Main.fibonacci 1
    @Main.fibonacci$ret18
    D=A  // This A mean (return_address)'s address 
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
    @Main.fibonacci  // goto function_name
    0;JMP
(Main.fibonacci$ret18)
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
    @end_frame  // end_Frame=LCL
    M=D
    @5  // retAddr=RAM[end_Frame-5]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @return_address  // return_address=R15
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
    @1  // THAT=RAM[end_frame-1]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @THAT
    M=D
    @2  // THIS=RAM[end_frame-2]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @THIS
    M=D
    @3  // ARG=RAM[end_frame-3]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @ARG
    M=D
    @4  // LCL=RAM[end_frame-4]
    D=A
    @end_frame
    D=M-D
    A=D
    D=M
    @LCL
    M=D
    @return_address
    A=M  // use pointer's format
    0;JMP
// finish the program
(END)
    @END
    0;JMP// function Sys.init 0
(Sys.init)  
// push constant 4
    @4
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// call Main.fibonacci 1
    @Main.fibonacci$ret23
    D=A  // This A mean (return_address)'s address 
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
    @Main.fibonacci  // goto function_name
    0;JMP
(Main.fibonacci$ret23)
// label END
(END)
// goto END
    @END
    0;JMP
// finish the program
(END)
    @END
    0;JMP