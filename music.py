
import winsound
from pathlib import Path
import time
import sys
import wave

from functions import get_path

file = str(sys.argv[1])
repeat = bool(int(sys.argv[2]))

while True:
    path = get_path() / file

    with wave.open(str(path), "rb") as f:
        frames = f.getnframes()
        rate = f.getframerate()

    sec = frames / rate

    print("File:", file, "|", "Repeat:", repeat, "|", "Duration:", round(sec))

    winsound.PlaySound(str(path),winsound.SND_FILENAME | winsound.SND_ASYNC)

    time.sleep(sec)
    #time.sleep(10)



    if not repeat:
        break
