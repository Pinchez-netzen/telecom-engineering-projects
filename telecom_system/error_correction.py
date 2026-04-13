def hamming_encode(data_bits):
    """
    Encode binary string using Hamming (7,4)
    """
    encoded = ''

    for i in range(0, len(data_bits), 4):
        block = data_bits[i:i+4]

        # pad if needed
        if len(block) < 4:
            block = block.ljust(4, '0')

        d1, d2, d3, d4 = map(int, block)

        # parity bits
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4

        # construct 7-bit code
        code = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
        encoded += code

    return encoded       


def hamming_decode(encoded_bits):
    """
    Decode Hamming (7,4) and correct single-bit errors
    """
    decoded = ''

    for i in range(0, len(encoded_bits), 7):
        block = encoded_bits[i:i+7]

        if len(block) < 7:
            continue

        bits = list(map(int, block))

        p1, p2, d1, p3, d2, d3, d4 = bits

        # syndrome calculation
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4

        error_position = s1 * 1 + s2 * 2 + s3 * 4

        # correct error if exists
        if error_position != 0:
            bits[error_position - 1] ^= 1

        # extract original data
        decoded += f"{bits[2]}{bits[4]}{bits[5]}{bits[6]}"

    return decoded