// push constant 17
    @17
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 17
    @17
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// eq
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    @EQ3  // if true,jump to the EQ condition.
    D;JEQ
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END3  // if false,jump to the END,false operations have already been done.
    0;JMP
(EQ3)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END3)
// push constant 17
    @17
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 16
    @16
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// eq
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    @EQ6  // if true,jump to the EQ condition.
    D;JEQ
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END6  // if false,jump to the END,false operations have already been done.
    0;JMP
(EQ6)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END6)
// push constant 16
    @16
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 17
    @17
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// eq
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1]
    @EQ9  // if true,jump to the EQ condition.
    D;JEQ
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END9  // if false,jump to the END,false operations have already been done.
    0;JMP
(EQ9)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END9)
// push constant 892
    @892
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 891
    @891
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
    @LT12  // if true,jump to the EQ condition.
    D;JLT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END12  // if false,jump to the END,false operations have already been done.
    0;JMP
(LT12)
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END12)
// push constant 891
    @891
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 892
    @892
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
    @LT15  // if true,jump to the EQ condition.
    D;JLT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END15  // if false,jump to the END,false operations have already been done.
    0;JMP
(LT15)
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END15)
// push constant 891
    @891
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 891
    @891
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
    @LT18  // if true,jump to the EQ condition.
    D;JLT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END18  // if false,jump to the END,false operations have already been done.
    0;JMP
(LT18)
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END18)
// push constant 32767
    @32767
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 32766
    @32766
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// gt
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]>RAM[SP-1]
    @GT21  // if true,jump to the EQ condition.
    D;JGT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END21  // if false,jump to the END,false operations have already been done.
    0;JMP
(GT21)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END21)
// push constant 32766
    @32766
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 32767
    @32767
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// gt
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]>RAM[SP-1]
    @GT24  // if true,jump to the EQ condition.
    D;JGT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END24  // if false,jump to the END,false operations have already been done.
    0;JMP
(GT24)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END24)
// push constant 32766
    @32766
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 32766
    @32766
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// gt
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    A=M
    D=M-D  // D=RAM[SP-2]-RAM[SP-1],test if RAM[SP-2]>RAM[SP-1]
    @GT27  // if true,jump to the EQ condition.
    D;JGT
    @SP
    A=M
    M=0
    @SP  // SP++
    M=M+1
    @END27  // if false,jump to the END,false operations have already been done.
    0;JMP
(GT27)  
    @SP
    A=M
    M=-1
    @SP  // SP++
    M=M+1
(END27)
// push constant 57
    @57
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 31
    @31
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 53
    @53
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
// push constant 112
    @112
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
// neg
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP
    A=M
    M=-D  // M=-D is better than M=-M (I think)
    @SP  // SP++
    M=M+1
// and
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=D&M  // D=RAM[SP-1]&RAM[SP-2] (This is depend on the C-instruction)
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// push constant 82
    @82
    D=A
    @SP  // RAM[SP]=D
    A=M
    M=D
    @SP  // SP++
    M=M+1
// or
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=M  // D=RAM[SP]
    @SP  // SP--
    M=M-1
    @SP
    A=M
    D=D|M  // D=RAM[sp-1]|RAM[sp-2]
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
