# py-morse-ping
Send Text using the ping command (proof of concept)

This is a simple "proof of concept" idea. The two scripts make use of the "ping" command to transfer
simple text messages using "morse-code".

In the early days of the last century many ships had used the morse code to transmit simple text informations
using light signals (light on / light off) the delay between the light on / light off transmissions was enought
to transmit some basic text messages.

The idea for this "proof of concept" idea is the same it is simple using the delay between two "ping" signals
from a host to a recipiant to do the same thing.

I have not tested it but it might work. 😉

I have no idea for what it could be used because it might be very slow - but how ever it should work IMHO 🙂

The Transmission requires two Scripts, the first is to send the text informations (converted to morse code
using the build in converter) to the receiver Scipt using ping to the target system (requires administrator
credentials to work).
