# Part B: Reflection

1. Part A has 9 tests, a test-to-production ratio of 9:46.

2. I did not record how long each red bar lasted. The clearest early failure was A1, when pytest reported that `kitchen` did not exist yet. Later, the mixed-unit test first reported that `Converter.add_rate` was missing, which pointed directly to the next behavior to implement.

3. I used Fake It in A1 by returning the expected result 600. A2 triangulated multiplication with a second input, which forced the implementation away from the constant. Obvious Implementation, the conversion rule multiplies an amount by the matching rate; 

4. nothing, A8 sum multiplication are implemented and tested. I would delete hashability from the test list because there is no current need.

5. Probably not. `Quantity.reduce` emerged because the converter needed to reduce both a quantity and a sum through the same interface. A quantity needs a conversion rate only when its unit differs from the requested unit; the tests helped reveal that design incrementally.

6. In Part 0 wrote the tests after the code. In Part A, tests came first and drove the design, it feel different cause part 0 you like thinking for solution, but part a you building a test.
