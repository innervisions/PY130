def print_message(*, message, level="INFO"):
    print(f"[{level}] {message}")
    
print_message(message="All about dolphins")
print_message(level="TASK", message="Clean the office")
