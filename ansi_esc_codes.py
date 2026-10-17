# -------------------- DEFINING ESCAPE CODE FOR TEXT FORMATTING --------------------

b = "\033[1m"               # BOLD
bff = "\033[22m"            # BOLD OFF
i = "\033[3m"               # ITALIC
iff = "\033[23m"            # ITALIC OFF
bl = "\033[5m"              # BLINKING
u = "\033[4m"               # UNDERLINING
uff = "\033[24m"            # UNDERLINING OFF
d = "\033[2m"               # DIM/FAINT
dff = "\033[22m"            # DIM/FAINT OFF
r = "\033[0m"               # RESET FORMAT (COLOR)
c0 = "\033[30m"             # BLACK
c1 = "\033[31m"             # RED
c2 = "\033[32m"             # GREEN
c3 = "\033[33m"             # YELLOW
c4 = "\033[34m"             # BLUE
c5 = "\033[35m"             # MAGENTA
c6 = "\033[36m"             # CYAN
c7 = "\033[37m"             # WHITE
# c8 = "\033[38m"
c9 = "\033[39m"             # DEFAULT
c = c9                      # CONSOLE COLOR
cursor = "\033[#G"