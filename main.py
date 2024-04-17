
def string_to_binary(string):
    binary_string = ""
    for char in string:
        ascii_value = ord(char)
        binary_char = bin(ascii_value)[2:]
        binary_char = binary_char.zfill(8)
        binary_char = binary_char[-3:]
        binary_string += binary_char
    return binary_string

class Assembler:
    def __init__(self):
        self.symbol_table = {}

    def assemble(self, input_file, output_file):
        with open(input_file, 'r') as f:
            asm_code = f.readlines()

        obj_code = self.generate_code(asm_code)

        with open(output_file, 'w') as f:
            for line in obj_code:
                f.write(line + '\n')
    def generate_code(self, asm_code):
        obj_code = []
        for line in asm_code:
            tokens = line.strip().split()
            if tokens[0] == 'SET':
                obj_code.append('0001')
                obj_code.append(tokens[1]) 
                obj_code.append(tokens[2]) 
            elif tokens[0] == 'ADD':
                obj_code.append('0010')
                obj_code.append(tokens[1])
                obj_code.append(tokens[2])
            elif tokens[0] == 'SUB':
                obj_code.append('0011')
                obj_code.append(tokens[1])
                obj_code.append(tokens[2])
            else:
                # Handle unsupported instructions or comments
                pass
        return obj_code

# Example usage
assembler = Assembler()
assembler.assemble('test.asm', 'output.obj')
