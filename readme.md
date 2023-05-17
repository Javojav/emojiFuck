# EmojiFuck
This is a [Brainfuck](https://es.wikipedia.org/wiki/Brainfuck) interpreter with a different set of symbols.

## How to use
Run the [interpreter](interpreter.py) with your file as an argument
```
python3 interpreter.py <file>
```

## Defining new symbols
Go to [symbols.py](symbols.py) and define a dictionary with the following instructions and a symbol for each of them
``` python 
customFuck = dict({
    "inc": '1',
    "dec": '2',
    "print": '3',
    "input": '4',
    "forward": '5',
    "back": '6',
    "loop": '7',
    "endloop": '8',
})
```

Then replace the import at the top of the [interpreter](interpreter.py)
``` python 
from symbols import emojiFuck as symbols
```

to 
``` python 
from symbols import customFuck as symbols
```

## Implementation

* **Tape**: List of values (default: 0)

* **Pointer**: index to tape list

### Instructions:
 * **inc** : adds 1 to wherever the pointer is pointing to 
    * Symbol: 🥵 <- This is u when inc happens on temperature

 * **dec** : subtracts 1 from wherever the pointer is pointing to 
    * Symbol: 🥶 <- This is u when inc happens on temperature

 * **print** : prints the ascii symbol of whatever cell the pointer is pointing to
    * Symbol: 🤑 <- This is u when u print money
 * **input**: stores the first character of the users input on whatever cell the pointer is pointing to 
    * symbol: 🤓 

    ![🤓](./imgs/dehecho.jpeg) <- This is u when u give input 

 * **forward**: Moves the pointer one cell forward (if that cell doesnt exist it gets created)
    * symbol: 🤰 <- this is u if u are becoming a mom (forwarding life of some shit)

 * **back**: Moves the pointer one cell back (if the pointer is 0 go to the end of the tape)
    * symbol: ⚓ <- this is u if u were an anchor (u would be using this probably if u go back to ur life driving boats and shit)

 * **loop**: Stores current instructions address to a stack. If the pointer is pointing at 0 the interpreter skips the loop 
    * symbol: 🗿 <- this is not u, its just a cool emoji 

 * **endloop**: Pops the stacks top value and goes to the instruction its pointing to as long as the pointer is not pointing to a cell with value 0
    * symbol: 💀 <- this is u when u die (like the loop after this symbol)