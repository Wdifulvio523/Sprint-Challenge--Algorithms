# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0

    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
```

```
c)  def bunnieEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the
runtime complexity of your solution.

ANSWER: I would use a binary search here, as the floors are already sorted. I would find the middle floor, drop an egg. If breaks, I would find the middle floor again, this time using the floor I'm on (the previous middle floor) as the top floor. I would do this to I get to the correct floor. This minimizes the total number of dropped eggs.

// Binary search, because floors are already "sorted"
// Find middle floor between first flor and top floor, and dorp egg
// If egg breaks, middle floor is now top floor. If egg does not break, middle floor is now bottomr floor
// Find middle floor again, using the previous middle floor as top/bottom
// Keep doing this until I find `_f_`