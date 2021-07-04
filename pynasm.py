

import os, sys
import subprocess
from dasm6.dasm6 import dasm6
import argparse

SOURCE_DIR='./nesrc'
# Compiler name
ASM = 'asm6'
# ASM compiler
ASMC = f'./{ASM}/{ASM}.out'
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The file to compile (*.asm) or the file to disassemble (*.nes)."
    +" The main ASM file or NES game must be in a directory with the same name in './nesrc/'.")
    parser.add_argument("-o", "--out", required=False, help='Result name, no extension required')
    args = parser.parse_args()
    
    if args.file == 'setup':
        print(f'All sources must be located in "{SOURCE_DIR}".')
        if os.path.isdir(SOURCE_DIR):
            print(f'The source directory "{SOURCE_DIR}" already exists.')
        else:
            os.mkdir(SOURCE_DIR)
            print(f'The source directory "{SOURCE_DIR}" was created.')
        if os.path.isfile(ASMC):
            '''
            Verifica si existe el compilador de asm6
            '''
            print(f'The "{ASM}" compiler already exists.')
        else :
            print(f"Compiling '{ASM}.c'")
            try:
            #Ejecuta make sobre el directorio especificado
                s=subprocess.check_output(f"gcc ./{ASM}/{ASM}.c -o {ASMC}",
                    shell=True,stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                #Si se genera un error se imprime la información
                raise RuntimeError(
                "command '{}' return with error (code {}): {}".format(
                      e.cmd, e.returncode, e.output.decode('utf8')
                    )
                )
        sys.exit(0)
    baseInputName, extension = os.path.splitext(args.file)
    extension = extension.lower()
    # Verifica la extensión del archivo de entrada
    if extension not in ('.nes','.asm'):
        raise Exception(f'The file "{args.file}" is not valid, one of type *.nes or *.asm is required')
    
    inputFilename = os.path.join('./nesrc',baseInputName,args.file)
    
    if not os.path.isfile(inputFilename):
        raise Exception(f'Not found the file "{inputFilename}".')
    
    
    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Ejecuta las funciones
    if extension == '.nes':
        dasm6(inputFilename, args.out)
        outName = '{baseInputName}.asm'
        if args.out != None:
            outName = '{args.out}.asm'
    elif extension == '.asm':
        outName = '{baseInputName}.nes'
        if args.out != None:
            outName = args.out
        
        try:
        #Ejecuta make sobre el directorio especificado
            working_dir = f"./{SOURCE_DIR}/{baseInputName}"
            cmd = f"../.{ASMC} {args.file} {outName}"
            s=subprocess.check_output(cmd , 
                shell = True, stderr = subprocess.STDOUT,cwd=working_dir)
            print(s.decode('utf8'))
        except subprocess.CalledProcessError as e:
            #Si se genera un error se imprime la información
            raise RuntimeError(
            "command '{}' return with error (code {}): {}".format(
                  e.cmd, e.returncode, e.output.decode('utf8')
                )
            )
    print(f"base: {baseInputName}  ext:{extension}")
    print(f"file: {args.file}  out:{outName}")
    
