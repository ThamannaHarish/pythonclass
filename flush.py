import time

print("Typing without flush: ", end="")
for X in "Hello":
    print(X, end="",)  # No flush
    time.sleep(0.5)


print("\nTyping with flush: ", end="")
for y in "Hello":
    print(y, end="", flush=True)  # Force flush
    time.sleep(0.5)