1. When several fields differ, which step comes first, and why?
2. How do you tell an operation that’s still running from one that was lost?
3. For “is an operation in flight?”, which is the truth: your store or the
   provider?
4. What do you write before a provider call, and what after? What if you crash
   between the two?
5. What happens if a lease expires while its worker is still working?
6. When exactly does an operation become `STALLED`, and what evidence do you
   record?
