# Test Plan

## TEST-01 Check that user can place a bet
**Priority:** Critical

**Risk Rationale:**
Placing bets is a core functionality.

### Steps
1. Open app: https://qae-assignment-tau.vercel.app/?user-id=<actual-user-id>.
1. Check user initial balance.
1. Find an UPCOMING event and click "1" button.
1. Enter stake value "10.00".
1. Check computed potential payout.
1. Click "PLACE BET" button.

### Expected result
- Success receipt modal appeared.
- Modal contains following data:
   - Bet ID
   - Match details - same as selected event
   - Selection - home
   - Stake - 10 EUR
   - Odds at placement
   - Potential payout - same as in step 4
   - Placement timestamp


- User balance is updated correctly - initial balance from step 2 minus 10.00.

---

## TEST-02 Verify that the user cannot place a bet with insufficient funds
**Priority:** Critical

**Risk Rationale:**
User is not allowed to place bets without money. Such a defect could result in financial losses for the company.

### Steps
1. Open app: https://qae-assignment-tau.vercel.app/?user-id=<actual-user-id>.
1. Place bets so the user has 80 EUR in his account.
1. Find an UPCOMING event and click "2" button.
1. Enter stake value "80.01".

### Expected result
- "Insufficient balance" message appeared.
- "PLACE BET" button is inactive.

---

## TEST-03 Check that Match List displays only upcoming football matches
**Priority:** Medium

**Risk Rationale:**
Users can be confused when seeing past events in Upcoming Football Matches list. It can lead to incorrect betting decisions and reduced trust in the platform.

### Steps
1. Open app: https://qae-assignment-tau.vercel.app/?user-id=<actual-user-id>.

### Expected result
- Only UPCOMING events are visible.
- No PAST events are present

---

## TEST-04 Check min/max stake values
**Priority:** High

**Risk Rationale:**
Incorrect minimum or maximum stake limits may allow users to place bets outside the permitted range, resulting in regulatory issues or an inconsistent user experience. 

### Steps
1. Open app: https://qae-assignment-tau.vercel.app/?user-id=<actual-user-id>.
1. Find an UPCOMING event and click "1" button.
1. Provide multiple values to the stake field: 0.99, 1.00, 1.01, 99.99, 100.00, 100.01.

### Expected result
- On value 0.99:
   - Message shows: "Minimum stake is €1.00".
   - "PLACE BET" button is inactive.
- On value 100.01:
   - Message shows: "Maximum stake is €100.00".
   - "PLACE BET" button is inactive.
- On values 1.00, 1.01, 99.99, 100.00:
   - "PLACE BET" button is active.

---

## TEST-05 Check odds can be changed for single event
**Priority:** Medium

**Risk Rationale:**
UI allows user to change his decision. Check if UI is intuitive and easy to use.

### Steps
1. Open app: https://qae-assignment-tau.vercel.app/?user-id=<actual-user-id>.
1. Find an UPCOMING event and click following buttons: 1, X, 2.

### Expected result
- Check if Match Winner and Odds change accordingly to user selection.
