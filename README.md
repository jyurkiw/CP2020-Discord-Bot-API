# CP2020-Discord-Bot-API

A python API for the CP2020 discord bot.

Python code to run a basic test of family background generation:

```
from api.util import CPDataHandler
from api.lifepath.siblings import SiblingsModule
dh = CPDataHandler('data/family_background.json')
dh.registerSupportModule('Siblings', SiblingsModule)
for r in dh.runProcess():
    print(r)
```

Run code from the repo's root directory.

Need to replace the above with some basic unit-tests. Want to get something stood up for friday's game, though.
