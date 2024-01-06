// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// This question is concerned about keyboard and screen 
// problem is how to draw the all screen
// need pointers to solve this problem 

//pseudocode
// (INFINITELOOP)
//      if (KBD !=0 goto BLACK)
//      else goto WHITE
// (BLACK)
//      if i == KBD goto LOP
//      RAM[SCREEN+i]=-1
// (WHITE)     
//      if i == KBD goto LOP
//      RAM[SCREEN+i]=0
// i means registers

// In My opinion this problem should not be complicaed 
// but it spend me a lot of time
// its target to mainpulate address of keyboard
// and put these value to -1 or 0

(LOOP)
    // read keyboard input
    @KBD
    D=M

    // if KBD==0 goto WHITE
    @WHITE
    D;JEQ

    // if KBD!=0 goto BLACK
    @BLACK
    D;JNE

    // INFINTELOOP
    @LOOP
    0;JMP

// how to make th entire screen black??
// because screen address is 16384 
// use pointer to move pointer to make pixel black or white
(BLACK)
    @SCREEN
    D=A
    @i
    M=D // set i to be SCREEN address 16384
    // after this step we only need to manipulate i instead of SCREEN
    (BLACKLOOP)
        // if (i == KBD) goto LOOP
        // which means the pixels is full of the entire SCREEN
        @i
        D=M
        @KBD
        D=D-A
        // SCREEN is full
        @LOOP
        D;JEQ

        // This is the hard part to understand
        // to make pixels black
        @i
        A=M  // This step is to put address into A register
        M=-1 // make the pixel black (use pointers)
             // if you can't figure out what happens here you need 
             // to watch the video and learn more about pointers
        @i
        M=M+1 // let address plus 1

        //or use following method 
        // the prinpicle is the same
//        // RAM[SCREEN+i]=-1
//        @SCREEN
//        D=M
//        @i
//        A=D+M
//        M=-1 // put the address register into -1
//
//        //i++
//        @i
//        M=M+1
//
//        In addition modify the above JEQ to JGT

        // goto BLACKLOOP
        @BLACKLOOP
        0;JMP

(WHITE)
    @SCREEN
    D=A
    @i
    M=D // same as the above
    (WHITELOOP)
        // if (i == KBD) goto LOOP
        @i
        D=M
        @KBD
        D=D-A
        // SCREEN is empty
        @LOOP
        D;JEQ

        // to make pixels white
        @i
        A=M  // This step is to put address into A register
        M=0  // make the pixel white

        @i
        M=M+1 // let address plus 1

        //goto WHITELOOP
        @WHITELOOP
        0;JMP

