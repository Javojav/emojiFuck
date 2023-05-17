from symbols import emojiFuck as symbols
import sys

debug = False

def interpret(code):
    codeLength = len(code)
    instruction = 0
    tape = list([0])
    pointer = 0
    stack = []

    # loop through the code
    while instruction < codeLength:
        char = code[instruction]

        if debug:
            print("\n", "Instruction: " + str(instruction), "codeLength: ", str(codeLength), "char: " + char, "pointer: " + str(pointer), "tape: " + str(tape), "stack: " + str(stack))
        
        if char == symbols["inc"]:
            tape[pointer] += 1
        elif char == symbols["dec"]:
            tape[pointer] -= 1
        elif char == symbols["print"]:
            print(chr(tape[pointer]), end='')
        elif char == symbols["input"]:
            tape[pointer] = ord(input()[0])
        elif char == symbols["forward"]:
            pointer += 1
            if pointer >= len(tape):
                tape.append(0)
        elif char == symbols["back"]:
            pointer -= 1

            # if pointer is less than 0 go to the end of the tape
            if pointer < 0:
                pointer = len(tape) - 1
        elif char == symbols["loop"]:
            # Skip to the end of the loop if the current cell is 0
            if tape[pointer] == 0:
                if debug:
                    print("Skipping loop")

                skipLoopStack = [code[instruction]]
                while len(skipLoopStack) > 0:
                    if debug:
                        print("Skipping instruction: " + str(code[instruction]))
                    instruction += 1

                    # balancing loop symbols 
                    if code[instruction] == symbols["loop"]:
                        skipLoopStack.append(code[instruction])
                    
                    if code[instruction] == symbols["endloop"]:
                        skipLoopStack.pop()

            else:
                stack.append(instruction)
        elif char == symbols["endloop"]:
            goto = stack.pop() - 1

            # check exit condition
            if tape[pointer] != 0:
                instruction = goto

        instruction += 1




# main function
if __name__ == '__main__':
    # check if there is a file to interpret
    if len(sys.argv) > 1:
        # open the file
        file = open(sys.argv[1], 'r')
        # read the file
        code = file.read()
        # close the file
        file.close()
        # interpret the code
        interpret(code)
    else:
        # print the usage
        print("Usage: python3 interpreter.py <file>")