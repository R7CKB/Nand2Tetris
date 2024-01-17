// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// Assumes that R0 >= 0, R1 >= 0, and R0 * R1 < 32768.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// pseudocode 
    // i=1
    // sum=0
// LOOP:
    // if (i==R0) goto STOP
    // sum=sum+R1
    // i=i+1
    // goto LOOP
// STOP
    // R2=sum
// END
    // finished program

// machine language

    // i
    @i
    M=1

    // sum
    @sum
    M=0

(LOOP)
    // if i==R0 goto STOP
    @R0
    D=M
    @i
    D=D-M
    @STOP
    D;JLT

    // sum=sum+R1
    @sum
    D=M
    @R1
    D=D+M
    @sum
    M=D

    // i=i+1
    @i
    M=M+1
    
    // goto LOOP
    @LOOP
    0;JMP

(STOP)
   // R2=sum
   @sum
   D=M
   @R2 
   M=D

(END)
    // finished program
    @END
    0;JMP
