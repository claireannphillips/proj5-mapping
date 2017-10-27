# Project 4:  Brevet time calculator with Ajax
#Claire Phillips, cphillip@uoregon.edu
#Reimplement the RUSA ACP controle time calculator with flask and ajax

## Project Description

Create a replacement for the brevet controle time calculator at 
http://www.rusa.org/octime_acp.html in accordance with ACP rules described 
at http://www.rusa.org/octime_alg.html.
Controles are points where a rider must obtain proof of passage, and control[e] 
times are the minimum and maximum times by which the rider must arrive at the 
location. This code deals with different oddities like when the control is greater
than the brevet, when the control distance is 20% greater than the brevet, and 
edge cases.
 
##
## How to use
##


Clone the repository and then CD into the proj4-brevets. 
Then in your terminal you type "make start" to install the enviornment
and then to see what port the computer is listening on.Then when you have the 
port type in your web browser, localhost:portnumber, which the port number 
will be 8000. Once there you can type in the brevets and see the calculations.

 
 

## Testing

I have a nose test module that in the terminal can type "make test" and will run
the nose tests with different test cases to see if code is working properly.

Talked with Dr. Young and we fixed one tiny thing on project the mornig after due date.











