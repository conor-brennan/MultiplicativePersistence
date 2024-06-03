# MultiplicativePersistence
Calculates the multiplicative persistence of a lot of numbers very quickly

Multiplicative persistence of a number x, denoted as mp(x), is the number of times you can recursively multiply the digits of x together before you get to single digit number.

Examples:
* Starting with 2314, we do 2x3x1x4=12, then 1x2=2. This means mp(2314)=2, because we achieved a single digit number after 2 steps.
* Starting with 8167, we do 8x1x6x7=336, then 3x3x6=54, then 5x4=20, then 2x0=0. So mp(8167)=4

Currently, the largest known multiplicative persistence of any number is 11. The first number to achieve this is 277777788888899.
