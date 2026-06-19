## Why I built it this way

Started with a flat script, then restructured into 5 files (DataManager, 
FlightSearch, FlightData, NotificationManager, main.py) once I understood 
why OOP made sense here — each class owns one responsibility and main.py 
just coordinates them, instead of one file doing everything.

Used requests_cache during development to avoid burning through SerpAPI's 
free tier while testing repeatedly, but explicitly excluded the Sheety 
endpoint from caching — sheet data needs to be fresh on every real run, 
or price comparisons would be wrong.

Spent two days on a Sheety auth bug that looked like a token problem but 
was actually a Google account mismatch — the form collecting responses 
was linked to a different Google account than the one Sheety was 
authenticated with. Taught me to check account-level config before 
re-debugging code that was already correct.

Added a direct-flight-first, indirect-flight-fallback search instead of 
one blanket search, since some routes only have connecting flights — 
this meant tracking number of stops in the FlightData object too.

What i made:

I made a flight dealer project that can find the cheapest flight from any destination airport(for which i used DEL) to paris, frankfurt and tokyo in upcoming 6 months, once a flight is cheapest
it sends me a twilio message on my phone number which tells me the specific flight data with historic low, furthermore once the twilio message is done it also updates the spreadsheet in sheety 
and replaces the lowestprice to the current cheapest price.

What i learned:
This was a capstone project so i roughly used all the previous python and APIs concepts and also used OOPs for first time in APIs pproject, Cmbining all of them into single file.


#WORK IN PROGRESS FOR THE FLIGHT CLUB PROJECT, THE FLIGH DEALER IS FINISHED BUT FOR THE FLIGHT CLUB THE WORK IN PROGRESS - SHEETY AUTH ISSUE UNDER INVESTIGATION, THERE WAS A TACHINACAL BUG.


