def text_to_binary(message):
    """
    Convert text message to binary string (8-bit per character)
    """
    binary = ''.join(format(ord(char), '08b') for char in message)
    return binary