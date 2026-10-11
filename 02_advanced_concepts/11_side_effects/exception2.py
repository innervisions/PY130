def divide_by(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Divide by zero!")
            # exception is caught below; no immediate side effect

        return numerator / denominator
    except ZeroDivisionError as error:
        print(error)  # side effect: output to console
        return None
