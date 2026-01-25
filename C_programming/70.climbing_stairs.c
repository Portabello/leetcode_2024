/*
70. Climbing Stairs
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step



Constraints:

    1 <= n <= 45

*/
int memo[46];

int f(int n) {
    if (n <= 2) return n;
    if (memo[n] != 0) return memo[n];
    memo[n] = f(n-1) + f(n-2);
    return memo[n];
}

int climbStairs(int n) {
    for (int i = 0; i < 46; i++) memo[i] = 0;
    return f(n);
}
