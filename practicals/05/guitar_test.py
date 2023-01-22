"""
Now write a program with at least enough code to test that the last two methods work as expected.
So to test that the get_age() method works, you could test that the above example guitar does indeed output 98 as expected. Here is some sample output for testing two guitars where the second is called Another Guitar and has year=2013:

Gibson L-5 CES get_age() - Expected 98. Got 98
Another Guitar get_age() - Expected 7. Got 7
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
Do you see how this works?

We print our own literal for what we expect if the function works (e.g., 98), then we print what the method actually returns and we look at the output to see if they match.
This form of testing is quite 'manual' since we need to read the output and compare it ourselves, but it is a good start.

Let's say we wrote the is_vintage() method incorrectly, then we want to see something like:

50-year old guitar is_vintage() - Expected True. Got False
We can see that the actual does not match the expected, so we know we need to fix something.
"""
