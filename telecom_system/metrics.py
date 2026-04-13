def calculate_ber(original, received):
    errors = 0

    for o, r in zip(original, received):
        if o != r:
            errors += 1

    ber = errors / len(original)
    return ber, errors