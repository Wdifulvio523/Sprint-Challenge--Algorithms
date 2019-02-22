Add your answers to the Algorithms exercises here.

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
Runtime: `O(n)` because as `n` increases, the amount of steps increases

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
Runtime: `O(n^4)` because we at the first loop we're automatically at `O(n)` and we have 3 additional nested loops

```
c)  def bunnieEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Runtime: `O(n)` because as bunnies increases, more steps are added

## Exercise II

-- Binary search, because floors are already "sorted"
-- Find middle floor between first flor and top floor, and dorp egg
-- If egg breaks, middle floor is now top floor. If egg does not break, middle floor is now bottomr floor
-- Find middle floor again, using the previous middle floor as top/bottom
-- Keep doing this until I find `_f_`