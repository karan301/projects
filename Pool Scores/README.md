# Shortcut for keeping 8-Ball Scores

I'd wager that [GamePigeon][1]'s 8-Ball is the most used iMessage app out there. It feels like everyone (myself included) plays it. But how does go about keeping score?[^1] I used to type the score after every game but after forgetting / losing track a couple of times, I decided to build a [shortcut][2] to semi-automate the process.

## Getting started
Other than the [GamePigeon][3] and [Shortcuts][4] apps (both free on the App Store), you'll need both of the following shortcuts: [Manage Pool Opponents][5]and [Pool Scores][6].

The first thing you do is run `Manage Pool Opponents`, which is a Normal shortcut (it only shows up in the Shortcuts app, not the widget). It'll ask for your name the first time you run it, and to set a file name[^2]. The shortcut will then ask if you would like to 'Add an opponent' or 'Remove an opponent'. Choose the former, enter the name of your opponent, and choose if you want to initialize scores. If you say yes, you can set the score to what your current scores are. If not, it'll set the score to 0-0. Repeat this for each of your opponents. It'll save your scores as `'Pool Scores'` in Shortcuts' iCloud Drive directory.

Next, run `Pool Scores` and enter your name **exactly as you did above**. It'll grab the `'Pool Scores'` dictionary file and ask you to select a name from your list of opponents, and then ask if you won, lost, or just want to get the score. If you choose won or lost, it'll update the score accordingly and then get the score (it both displays the score and copies it to clipboard in case you want to send it to your opponent). 

The `Pool Scores` shortcut is a Today Widget (and Apple Watch) shortcut so after every game, you can just swipe down to bring up Notification Center and update scores from there.  

Read on below for a more detailed documentation of how the shortcuts work.

---- 

## How does it work? (Documentation)
Each shortcut has two Import Questions:
1. Enter your name here. Expected input is text `myname` with no white-space (e.g. Karan), but anything works (so long as you enter it exactly the same in both shortcuts).
2. What would you like the file to be saved as in iCloud Drive? Both shortcuts rely on a dictionary file in Shortcut's iCloud Drive directory. By default, this is read and written as `Pool Scores.json` but you can change it to whatever you like here - just make sure that you change it in both shortcuts.

### Manage Pool Opponents
This is where you initially create the dictionary, and where you can add or remove opponents. It either adds or updates key-value pairs in an existing dictionary, or it creates a new dictionary with the given key-value pair. It works as follows.

_Add an opponent:_
1. The shortcut asks for your opponent's name. Expected input is text `opponentname` with no white-space (e.g. James), but anything works.
2. The shortcut asks if you want to initialize scores. If yes, expected input is number. Enter your score and your opponent's score where prompted. If no, scores are assigned as 0-0. 
3. The shortcut gets the `Pool Scores` dictionary file from Shortcuts' iCloud Drive directory, and gets the dictionary from the file. If the file doesn't exist (for example, if you're running the shortcut for the first time) it'll be created later. 
4. The shortcut sets the dictionary value for you and for your opponent. It does this with keys `mynameopponentname` and `opponentname`  with values `myscore` and `opponentscore` respectively _(e.g. {"KaranJames":100, "James":0})_. If these names already exist in the dictionary, they will be overwritten.
5. The shortcut saves the dictionary to the `Pool Scores` file in Shortcuts' iCloud Drive directory. If the file exists (for example, if you're adding a new opponent or re-initializing scores) it'll overwrite the file.

_Remove an opponent:_
1. The shortcut gets the `Pool Scores` dictionary file from Shortcuts' iCloud Drive directory. **This file must already exist**, execution will end here otherwise. 
2. The shortcut gets all keys from the dictionary file. Some of these will be in the form `opponentname` while others will be in the form `mynameopponentname`. We need to get rid of the latter to present a list of opponent names. 
3. The shortcut splits these keys into new lines. It then finds all the keys that begin with `myname` and replaces them with a blank. It then goes through and deletes all blank lines. 
4. The shortcut presents this updated list of keys (opponent names) and asks you to pick one or more.
5. For each selected opponent, the shortcut will set both your scores to 0.
6. The shortcut will then remove your scores from the dictionary, and then clean itself up (for example: any leading or trailing commas in the dictionary will be removed).
7. The shortcut will finally ask you to confirm your changes. If you say yes, it will save the updated dictionary to iCloud Drive. If you cancel, execution will stop here.

## Pool Scores
This shortcut grabs an existing dictionary (make sure you run the `Manage Pool Opponents` shortcut at least once first to create one), asks you to choose from a list of your opponents, updates the score (if necessary), and copies/displays it. This shortcut is best used from the Today Widget (after first run). It works as follows.

1. The shortcut gets the `Pool Scores` dictionary file from Shortcuts' iCloud Drive directory. **This file must already exist**, execution will end here otherwise. 
2. The shortcut gets all keys from the dictionary file. Some of these will be in the form `opponentname` while others will be in the form `mynameopponentname`. We need to get rid of the latter to present a list of opponent names. 
3. The shortcut splits these keys into new lines. It then finds all the keys that begin with `myname` and replaces them with a blank. It then goes through and deletes all blank lines. 
4. The shortcut presents this updated list of keys (opponent names) and asks you to pick one.
5. The shortcut fetches the dictionary file again, getting just the key-value pairs for you and the opponent you selected this time, and stores the values in `My Score` and `Opponent Score` variables as appropriate (with the keys again being of the form `mynameopponentname` and `opponentname`).
6. The shortcut asks you to choose from a menu: "I won", "I lost", or "Get score". "I won" and "I lost" simply increment either the `My Score` or `Opponent Score` variable as appropriate, and then jumps to "Get score".
7. The shortcut fetches the dictionary file again. It sets (updates) the dictionary value for keys `mynameopponentname` and `opponentname` with the updated score variables. 
8. The shortcut saves the updated dictionary file, overwriting `Pool Scores.json`.
9. The shortcut copies `My Score - Opponent Score` to clipboard, so you can share it with your opponent if you want.
10. The shortcut displays the text `MyName MyScore-OpponentScore OpponentName`.

---- 

[^1]:	The app keeps track of how many games you've won, but it doesn't sync across devices (so iPhone and iPad keep different scores) and it doesn't let you know your opponent's score. I've also found the number to be inconsistent.

[^2]:	I expect most people to leave this as the default. Truthfully, it only exists so that I can more easily test and debug when I add new features without messing with my canonical dictionary.

[1]:	https://itunes.apple.com/us/app/gamepigeon/id1124197642?mt=8&uo=4&at=10l6nh
[2]:	https://itunes.apple.com/us/app/shortcuts/id915249334?mt=8&uo=4&at=10l6nh
[3]:	https://itunes.apple.com/us/app/gamepigeon/id1124197642?mt=8&uo=4&at=10l6nh
[4]:	https://itunes.apple.com/us/app/shortcuts/id915249334?mt=8&uo=4&at=10l6nh
[5]:	./Manage%20Pool%20Opponents.shortcut
[6]:	./Pool%20Scores.shortcut