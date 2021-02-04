# User Guide

Sidekick takes voice commands and converts them to actions on the computer. It uses the default system mic. It operates differently when in different states or modes. There are currently three modes, described below, but more can be added.

- `command` - this mode allows the user to issue a variety of commands
- `mouse` - this mode allows the user to control the mouse
- `text` - this mode transcribes spoken speech to text
- `alpha` - this mode provides the ability to write individual letters, numbers, and punctuation
- `pause` - in this mode no commands are processed (convenient if afk or switching between devices)

In each mode certain keywords are linked to certain actions. To switch between modes, simply say `command`, `mouse`, `text`, or `alpha`. Say `pause` once to pause. Say `pause` again to restart. When you restart the mode/state will be the same as when you first paused. These keywords are reserved to switch between modes. 

My recommended method for controlling the mouse is to use the `grid` command to navigate to the general area of the screen and then the `mouse` mode or cardinal directions commands to get the mouse to the precise location. 

## Command

Some commands are stateless, in that they function no matter what state/mode you are in. Others only function when in the command state. The mouse can be moved using both cardinal directions and the `grid` command, but this is different from the `mouse` mode which tries to replicate normal mouse movement. 

- note: `[1-7]` is not literally 1-7 pixels or spaces. For any given command, 1-3 is usally a small movement or number of spaces, with 4-7 being larger relative to the nature of the command.

#### Stateless

- `click` or `go` - double click left mouse button
- `double` - double click left mouse button
- `enter` 
- `space`
- `back [1-20,30,40,50,100]` - hit backspace n times - `hundred` = 100

#### Stateful

- `rick` - right click 
- `triple` - triple click
- `north [1-7]`, `south [1-7]`, `east [1-7]`, `west [1-7]` - move mouse in cardinal directions 
- `grid [a-k] [1-11]` - snap mouse to a point on a grid (like in chess or battleship - move to a1 would be near bottom left, k11 top right)
- `up [1-20,30,40,50,100]`, `left...`, `down...`, `right...` - arrow keys
- `copy`
- `paste`
- `save`
- `scroll [up,down,left,right] [1-7]` 

#### Examples

- `scroll up 1 2 1` - will scroll up 1, then 2, then 1 again - number can be repeated without repeating entire command
- `north 3 1` - moves mouse north 3, then 1
- `back 1 back 2` - backspace by 1, then 2 - can backspace up to 20 spaces

## Mouse

Once you say `mouse` and provide a direction, such as `north`, the mouse will begin to move that direction at the `snail` speed. You then use the commands to change direction, change speed, or stop the mouse. When stopped, the state/mode is automatically switched back to the `command` mode. 

- `north`, `south`, `east`, `west`, `northeast` or `one`, `northwest` or `two`, `southeast` or `three`, `southwest` or `four`
- `stop` - stop the mouse
- `snail`, `slow`, `medium`, `fast` - speed at which mouse moves - starts out at snail speed
- `counter` or `up` - rotate direction 15 degrees counterclockwise
- `clock` or `down` - rotate direction 15 degrees clockwise

#### Examples

- `mouse north medium clock stop` - mouse moves north, speed changed to medium, rotated clockwise 15 degreeds, then stopped

## Text

In text mode, speech will be transcribed to text. A space is automatically added before each word, except for capital words. Capital words have the space after instead of before in order to avoid extra space at beginning of sentences. 

- `cap` - word spoken after this keyword will be capitalized

## Alpha

The alpha mode enables punctuation as well as single alphanumeric characters.

- `period`
- `comma` 
- `colon`
- `question` for question mark
- `semicolon` 
- `exclamation` for exclamation point
- `hash`
- `dash`
- `dot`
- `cap` - character spoken afterwards capitalized

#### Examples

- `alpha a dash three` produces 'a-3'

#### Examples

- `cap hello alpha comma text how are you alpha question` - will produce the text 'Hello, how are you?'