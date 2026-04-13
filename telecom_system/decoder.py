def binary_to_text(binary):
    """
    Convert binary string back to text
    """
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))

    return ''.join(chars)