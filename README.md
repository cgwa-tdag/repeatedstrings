# Repeated Strings

Lilah has a string, **s**, of lowercase English letters that she repeated infinitely many times.

Given an integer, **n**, find and print the number of letter _a_'s in the first **n** letters of Lilah's infinite string.

For example, if the string **s='abcac'** and **n=10**, the substring we consider is **abcacabcac**, the first 10 characters of her infinite string. There are 4 occurrences of **a** in the substring.

## Function Description

Complete the repeatedString function in `repeated.py` on this repo. It should return an integer representing the number of occurrences of **a** in the prefix of length **n** in the infinitely repeating string.

`repeatedString` has the following parameters:

* s: a string to repeat
* n: the number of characters to consider

## Input Format

The first argument is a single string, **s**. 

The second argument is an integer, **n**.

## Constraints

* 1 <= |s| <= 100
* 1 <= n <= 1E12

## Output Format

Return a single integer denoting the number of letter _a_'s in the first **n** letters of the infinite string created by repeating **s** infinitely many times.

### Sample Input 0

    aba
    10

### Sample Output 0

    7
    
### Explanation 0

The first **n=10** letters of the infinite string are abaabaabaa. Because there are 7 _a_'s, we return 7.

### Sample Input 1

    a
    1000000000000

### Sample Output 1

    1000000000000

### Explanation 1

Because all of the first **n = 1000000000000** letters of the infinite string are _a_, we return 1000000000000.

***

Originally from https://www.hackerrank.com/challenges/repeated-string/problem
