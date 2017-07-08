# Simple script to determine whose turn it is to do dishes, and texts them
# See README for more
# Written by Karan Varindani

## Import software dependencies
from sense_hat import SenseHat
from twilio.rest import Client

## Orient the display, change if necessary
sense = SenseHat()
sense.set_rotation(270)

## Change the values below
L = ["Paul", "David", "Anthony", "Eric", "Michael", "Wayne"] ## List of first names
I = ["P", "D", "A", "E", "M", "W"] ## Corresponding initials
C = [[102,0,102], [0,102,102], [51,25,0], [0,0,102], [0,102,51], [102,0,0]] ## Background color
N = ['1234567890', '1234567890', '1234567890', '1234567890', '1234567890', '1234567890'] ## Phone number 

## Where the magic happens
def main(i):
    i = i % len(L) ## Uses modulo to make sure i !< len(L)
    sense.show_message(L[i], back_colour=C[i]) ## First scrolls and shows first name
    sense.show_letter(I[i], back_colour=C[i]) ## Then sticks at initial
    message(i) ## Sends a text message
    #debug(i) ## Used when fixing things
    event = sense.stick.wait_for_event() ## Waits for button press
    if event.action == 'pressed': ## Does something on every button press
        action(i)
    if event.action == 'held' or event.action == 'released': ## This is probably redundant, I'll test later
        action(i)

## Increases the counter
def action(i):
    i += 1 ## Jump to the next person in the list
    sense.stick.wait_for_event() ## 'press' and 'release' are two actions, this strips one out
    main(i)

## Sends the message    
def message(i):
	ACCOUNT_SID = '' ## Enter your account_sid here
	AUTH_TOKEN = '' ## Enter your auth_token here
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	## Change from and body to your Twilio number and message
	client.messages.create (
		to = '+1' + N[i], ## Texts the ith person in the array
		from_ = '+19876543210',
		body = 'It\'s your turn to do the dishes.', 
	) 
	return

## Testing method/routine
def debug(i):
    print ("Test for %s" % L[i])
    return

main(0)
