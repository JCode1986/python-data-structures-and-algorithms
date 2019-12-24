# Fizz Buzz Tree

## Challenge Description
* Write a function called `FizzBuzzTree` which takes a tree as an argument.
* Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
    * If the value is divisible by 3, replace the value with “Fizz”
    * If the value is divisible by 5, replace the value with “Buzz”
    * If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    * If the value is not divisible by 3 or 5, simply turn the number into a String.
* Return the new tree.

## Approach & Efficiency
* Instantiate new tree
* Helper function to traverse tree recursively and implementing Fizz Buzz approach
* Make a copy of the results of Fizz Buzz to new tree
* Return new tree
* Big O - Space & Time O(n)

## Solution
![Fizz Buzz Tree](./image/fizz-buzz.jpg)