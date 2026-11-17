# reconcile-db

Python 3.12, SQLite, with a fake provider. Written by hand.

A hand-written reconcilee loop for managed databases (desired vs. actual state, crashes, leases), rebuilding the core of the DBaaS I built at AZUL Cloud.

## The world

The actual state has several fields:

- The size in the spec
- The volume’s requested size
- The volume’s real capacity
- A “resizing” condition and a “filesystem pending” condition
- Whether the primary is ready

Done means:

- Capacity is greater than or equal to the desired size
- No resize condition is open
- The primary is ready

“Storage is 20 GB” is not a done-test.

The provider is a second controller. It makes progress on its own, can sit in
progress for a while, and has a “stuck forever” mode.

Provider errors come in three classes:

- **Transient:** Back off and retry
- **Credentials expired:** Renew, then retry
- **Permanent:** Stop

## The rules

- Validate the desired state when it’s submitted. A shrink is rejected there,
  before any mutation.
- Every observation is known or unknown. Never mutate on unknown.
- Keep two records: the database’s phase and the operation’s status. A failed
  operation is not a failed database.
- On each pass: observe, compare, perform at most one mutation, and record.
- An operation has a deadline. Past it, the operation ends in `STALLED` with
  evidence of what was observed and when.
- Only one worker acts on a database at a time.
- Be crash-safe: kill the worker at any line, and a fresh one converges with no
  double mutation.

## The tests

- Convergence from random states
- A crash at every step
- Running a pass twice changes nothing
- Two workers never act on the same database at once
- An unknown observation causes no mutation
- A stuck provider ends in `STALLED`
- Each error class leads to its own action

