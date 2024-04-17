def string_to_binary(string):
    binary_string = ""
    for char in string:
        ascii_value = ord(char)
        binary_char = bin(ascii_value)[2:]
        binary_char = binary_char.zfill(8)
        binary_char = binary_char[-4:]
        binary_string += binary_char
    return binary_string

# Example usage
text = "hello"
binary_text = string_to_binary(text)
print(binary_text)
