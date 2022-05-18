# User Guide

Sidekick takes voice commands and converts them to actions on the computer. It uses the default system mic. It operates differently when in different states or modes.

- `command` - this mode allows the user to issue a variety of commands
- `mouse` - this mode allows the user to control the mouse
- `text` - this mode transcribes spoken speech to text
- `alpha` - this mode provides the ability to write individual letters, numbers, and punctuation
- `pause` - in this mode no commands are processed (convenient if afk). 
- `volume` - this mode allows the user to control the mouse with the volume of their voice

In each mode certain keywords are linked to certain actions. To switch between modes, simply say `command`, `mouse`, `text`, or `alpha`. Say `pause` once to pause. Say `time to work` to restart back in the `command` state. 

**NOTE**: Make sure to either pause or stop Sidekick when not in use.

My recommended method for controlling the mouse is to use the `grid` command to navigate to the general area of the screen and then the `mouse` mode or cardinal directions commands to get the mouse to the precise location. 

If you seem to be having trouble try speaking a little slower, especially when switching modes.

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
- `ack` - alt + click
- `triple` - triple click
- `north [1-7]`, `south [1-7]`, `east [1-7]`, `west [1-7]` - move mouse in cardinal directions 
- `grid [a-k] [1-11]` - snap mouse to a point on a grid (like in chess or battleship - move to a1 would be near bottom left, k11 top right)
- `up [1-20,30,40,50,100]`, `left...`, `down...`, `right...` - arrow keys
- `copy` / `paste`
- `save`
- `escape` - hit escape key
- `scroll [up,down,left,right] [1-7]` 
- `lock` and `release` - say `lock` to save mouse destination location, then move mouse over item you want to drag to that location and say `release` - item will be dragged to that location
- `pup` / `pod` - page up / page down
- `in` / `out` - zoom in / zoom out
- `close` / `nab` - close tab or window / new tab 
- `nab` / `rab` / `lab` / `cab` - new tab in browser, right one tab, left one tab, reopen closed tab
- `lap` / `nip` - last page / next page in browser
- `find` / `replace` - open find or replace dialogue
- `undo` / `redo`
- `terminate` - ctrl + c 
- `switch` - hits `alt` + `tab` so you can switch apps - say `next` to move to next application. Say `enter` to pick that application. Say `escape` to go cancel the operation. 
- `key` + lower case letter - hold letter - can be useful for game if want to just hold button down (ex: `key a w stop`) will hold down `a` until you say `w`, hold down `w` until you say `stop`and then exit that command
- `hold` - holds down left mouse button until you say another word - useful for drag and drop or on Mac when need to hold and release to switch windows
- `hot` - hot key press (ex: `hot control alt delete go` presses `ctrl alt delete`) - using the word `apple` for the command key (ex: `hot apple f go` presses `command f`)

#### New Stateful commands
- `screenshot` opens a window that shows a real time screenshot with a red grid overlay. This overlay corresponds to the grid-based mouse control. To turn of screenshot, say the `screenshot` keyword again
- `overlay` overlays a red grid over the entire screen. To turn off the overlay, close the window manually


#### Examples

- `scroll up 1 2 1` - will scroll up 1, then 2, then 1 again - number can be repeated without repeating entire command
- `north 3 1` - moves mouse north 3, then 1
- `back 1 back 2` - backspace by 1, then 2 - can backspace up to 20 spaces
- `switch next next enter` - hit `alt` + `tab` and select 4th application option

## Mouse

Once you say `mouse` and provide a direction, such as `north`, the mouse will begin to move that direction at the `snail` speed. You then use the commands to change direction, change speed, or stop the mouse. When stopped, the state/mode is automatically switched back to the `command` mode. If you switch states before stopping, the mouse will automatically be stopped. 

- `north`, `south`, `east`, `west`, `northeast` or `one`, `northwest` or `two`, `southeast` or `three`, `southwest` or `four`
- `stop` - stop the mouse
- `snail`, `slow`, `medium`, `fast` - speed at which mouse moves - starts out at snail speed
- `counter` or `up` - rotate direction 15 degrees counterclockwise
- `clock` or `down` - rotate direction 15 degrees clockwise

#### Examples

- `mouse north medium clock stop` - mouse moves north, speed changed to medium, rotated clockwise 15 degreeds, then stopped

## Text

In text mode, speech will be transcribed to text. A space is automatically added before each word. This behavior can be toggled using the commands `underscore` and `pack`. 

- `underscore` - underscore before the following word
- `pack` - no space before the following word - good for coding variables
- `cap` - word spoken after this keyword will be capitalized

## Example

- `foo pack cap bar` = fooBar
- `foo underscore cap bar` = foo_Bar

## Alpha

The alpha mode enables punctuation as well as single alphanumeric characters.

- `period`
- `comma` 
- `colon`
- `equals` - =
- `question` for question mark
- `semicolon` 
- `exclamation` for exclamation point
- `hash`
- `dash`
- `dot`
- `cap` - character spoken afterwards capitalized
- `ren` / `len` - right/left parentheses
- `rack` / `lack` - right/left brackets 
- `quote` / `single` - " and '

#### Examples

- `alpha a dash three` produces 'a-3'

#### Examples

- `cap hello alpha comma text how are you alpha question` - will produce the text 'Hello, how are you?'

## Volume
Volume mode allows the mouse to be controlled using the volume of your voice
- `up` switch to vertical movement (default)
- `left` switch to horizontal movement
- `slow` mouse moves at a slow speed
- `medium` mouse moves at a medium speed (default)
- `fast` mouse moves at a fast speed
- `stop` exits to command mode



