def divide_by(numerator, denominator):
    if denominator == 0:
        raise ValueError("Divide by zero!")
        # side effect: uncaught exception

    return numerator / denominator
