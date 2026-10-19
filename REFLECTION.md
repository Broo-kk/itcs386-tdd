# Part B: Reflection

1. Part A has 9 tests and 46 lines of production code in `kitchen.py`, a test-to-production ratio of 9:46 (about 1 test per 5.1 production lines).

2. I did not record how long each red bar lasted. The clearest early failure was A1, when pytest reported that `kitchen` did not exist yet. Later, the mixed-unit test first reported that `Converter.add_rate` was missing, which pointed directly to the next behavior to implement.

3. I used Fake It in A1 by returning the expected constant, 600, and again for the first simple-addition green step. A2 triangulated multiplication with a second input, which forced the implementation away from the constant. For Obvious Implementation, the conversion rule multiplies an amount by the matching rate; the directional conversion test verifies that choice.

4. All required behaviors, including optional A8 sum multiplication, have passing tests. Hashability remains an unchecked note because no current use case requires quantities as set members or dictionary keys. I would only implement it if that need arises.

5. Probably not. `Quantity.reduce` emerged because the converter needed to reduce both a quantity and a sum through the same interface. A quantity needs a conversion rate only when its unit differs from the requested unit; the tests helped reveal that design incrementally.

6. In Part 0, the production examples were supplied and the tests checked their behavior. In Part A, tests came first and drove the design: multiplication became non-mutating, equality included the unit, and addition became an expression that could be reduced after a target unit was chosen. Watching each new test fail before its implementation made the next change clearer.
