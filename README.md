pynasm
=====

1. This tool allows you to disassemble * .nes files and compile * .asm files. 
The disassembler is an adaptation of the one proposed by 
[Dougeff](https://github.com/nesdoug/NES-DISASSEMBLER), and the compiler is 
made in C language, which is thanks to the work of loopy published in
 [NesDev](https://wiki.nesdev.com/w/index.php/Tools).

2. Works with Python 3 on Linux


How to use
----------
Before starting to work, the compiler and the working folder 'nesrc' must 
be generated. To simplify this task run pynasm in a command prompt or terminal emulator, and type
~~~~
    $ python3 pynasm.py setup
~~~~

All files must be located in './nesrc' within a folder or directory with the same name as the main file, either * .nes, or * .asm.

To disassemble a * .nes file run pynasm in a command prompt or terminal emulator, and type
~~~~
    $ python3 pynasm.py <nes_file>
~~~~

If the file is a good .NES file, and the filesize matches the header, it should ask you...
Default Program Bank size OK? Y/N
-if type anything other than 'Y' or 'y'
"1 = 8192, 2 = 16384, 4 = 32768:"

It really doesn't make much difference, except that you will generate more .asm files with a smaller Bank size, but they should all assemble the same.

It should generate a .bin file (=the PRG ROM minus the header, not needed for reassembly), a .chr file (if present), and 1 or more .asm file

Assemble with asm6 like this 

~~~~
    $ python3 pynasm.py <asm_file>
~~~~

Examples
---------------
Disassemble the game './nesrc/test/test.nes'
~~~~
    $ python3 pynasm.py test.nes
~~~~

Compile the game './nesrc/test/test.asm'
~~~~
    $ python3 pynasm.py test.asm
~~~~



Compile the game './nesrc/test/test.asm' and specify the name under 
which it is saved
~~~~
    $ python3 pynasm.py test.asm myGame.nes
~~~~

Disassembler Troubleshooting
---------------

The very first .nes file I tested...Failed the filesize check. Whoever dumped the ROM, put about 64 bytes at the end of the file, a signature. You would have to open the ROM in a hex editor and delete that part to get it to function...or maybe edit the source code.

Also, if there is a signature in the header (DISKDUDE, etc), my program will not copy it, but remove it. The ROM will run the same, but its hash value will be different (for comparison / security). I also didn't implement any iNES 2.0 stuff...those bytes will be zero.

You may have to edit the .base directives in the main .asm file. Especially if you are editing the source in the file. Do NOT assume that my program has any idea about what address each bank should start with. 

You may have to remove spaces from the .nes filename, before disassembling. The file would probably disassemble correctly, but, asm6 will give error messages for filenames with spaces in them.

I didn't use any illegal opcodes. Feel free to edit the source, if you want them in.



Feel free to use this, change the source code, etc. I'd appreciate if you credit me somewhere in the new version. Thanks. Dougeff.

