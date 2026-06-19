Why I built it this way:

Originally I called the API every time I tested, which burned through the free tier limit fast. I switched to caching responses locally so I could keep developing without hitting rate limits, 
then excluded the Sheety endpoint from caching specifically because I needed fresh sheet data on every real run. Took two days to figure out a separate auth bug was actually a Google account mismatch 
between Sheety and the linked sheet, not a code issue.


What i made:

I made a flight dealer project that can find the cheapest flight from any destination airport(for which i used DEL) to paris, frankfurt and tokyo in upcoming 6 months, once a flight is cheapest
it sends me a twilio message on my phone number which tells me the specific flight data with historic low, furthermore once the twilio message is done it also updates the spreadsheet in sheety 
and replaces the lowestprice to the current cheapest price.

What i learned:
This was a capstone project so i roughly used all the previous python and APIs concepts and also used OOPs for first time in APIs pproject, Cmbining all of them into single file.


#WORK IN PROGRESS FOR THE FLIGHT CLUB PROJECT, THE FLIGH DEALER IS FINISHED BUT FOR THE FLIGHT CLUB THE WORK IN PROGRESS - SHEETY AUTH ISSUE UNDER INVESTIGATION, THERE WAS A TACHINACAL BUG.


