import os
import time
import random

loadingSymbols = ["|", "/", "-", "\\"]
loadingSymbolsIndex = 0

# I dont write this shit
os.system("clear")

while True:
    loadingSymbolsIndex = (loadingSymbolsIndex + 1) % len(loadingSymbols) 
    print(f"\r[{loadingSymbols[loadingSymbolsIndex]}]" + "Loading tests" + loadingSymbolsIndex * "." + " " * (len(loadingSymbols) - loadingSymbolsIndex - 1), end='', flush=True)
    time.sleep(random.uniform(0,.25))