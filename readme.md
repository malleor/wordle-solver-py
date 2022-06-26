### How to play the game in a terminal?

Run `python3` and run the challenge like so:

```
from wordle import *
from getpass import getpass
run_challenge(MockChallenge(getpass('set the challenge word: ')), InteractiveSolver())
```

After the prompt, ask someone to type in the challenge word and start solving the puzzle.
It may look like this:

```
>>> run_challenge(MockChallenge(getpass('set the challenge word: ')), InteractiveSolver())
set the challenge word:
guess the word: FINER
FINER ➡️ ⬜️⬜️⬜️⬜️🟨
guess the word: TRUTH
TRUTH ➡️ ⬜️🟨⬜️⬜️⬜️
guess the word: WORRY
WORRY ➡️ ⬜️⬜️🟩🟨⬜️
guess the word: CARDS
CARDS ➡️ 🟨🟨🟩⬜️🟨
guess the word: SCRAP
SCRAP ➡️ 🟩🟩🟩🟩🟩
5
```

If you'd rather play alone, you can use a randomly selected challenge word.
After running `python3`, type:

```
from wordle import *
from getpass import getpass
run_challenge(RandomChallenge(), InteractiveSolver())
```

### Dictionary

The package uses a 5-letter words dictionary from Bill Cruise, available on
[Kaggle](https://www.kaggle.com/datasets/bcruise/wordle-valid-words).
