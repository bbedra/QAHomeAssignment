# Strategy and Recommendations

## Why you selected these 2 tests for automation over other candidates?

First, UI test. It verifies the core functionality of the tested app.
It covers most of the available paths that a typical user will follow.
Automating this test increases our confidence in the tested product.
It is also a good candidate for automation because it is likely 
to be executed frequently during regression testing.

Second, API test. It verifies the correctness of the functionality that directly affects the betting process. 
It helps ensure that users cannot place bets outside the permitted range.
This test is fast, deterministic and covers multiple scenarios thanks to parametrization.

## What you intentionally left as manual only and why?
I intentionally left lower priority scenarios as manual tests.
The task was to automate two scenarios, so given that I had limited time, I picked those two 
that bring the biggest business value and risk coverage.
For example TEST-03 - checking the Upcoming Football Matches list can be done manually with relatively low effort.
Same goes with TEST-05 that checks if odds can be changed in a single event.

## Your top 2–3 recommendations if this project were to scale
- First, I would configure a jenkins pipeline for running automated tests daily. Thanks to that, We would be able to execute regression testing.
- Second, the whole test framework can be configured to run in a docker container so it would increase portability of the testing framework and ensured that the test environment is consistent across different machines.
- Finally, I would create a separate pipeline for the smoke tests. These tests could be run before merging code changes to provide fast feedback.
