# Scheduler Documentation
A quick and dirty Raspberry Pi project that displays someone's initial (informing them it's their day to do the dishes). When a button is pressed, it loops to the next person in the array, sends them a text message to remind them to do the dishes, and updates the display.

## Hardware Dependencies
This project was built to be deployed on a [Raspberry Pi](https://www.raspberrypi.org), using the [Sense HAT](https://www.raspberrypi.org/products/sense-hat/). You could probably modify it to use a different display/button.

## Software Dependencies
* [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python) — `pip install twilio` and update the credentials in [`scheduler.py`](./scheduler.py).

## Configuration
Look through the comments for the following placeholders you'll need to update:
* Array of names, initials, phone numbers (and colours, if you want)
* Twilio `account_sid` and `auth_token`, and Twilio phone number

----
_Updated on July 7, 2017 by Karan Varindani._