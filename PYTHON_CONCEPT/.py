# Big Green "A" and Red "M" — old-school hacker terminal style

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

A = r"""
        █████
       ██   ██
      ██     ██
     ███████████
    ██         ██
   ██           ██
  ██             ██
"""

M = r"""
███         ███
████       ████
██ ██     ██ ██
██  ██   ██  ██
██   ██ ██   ██
██    ███    ██
██     █     ██
"""

print(GREEN + A + RESET)
print(RED + M + RESET)
