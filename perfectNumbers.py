class PerfectNumbers:
  def __init__(self, maxN):
    self.maxN = maxN
    self.sieve = [1] * (self.maxN + 1)

  def getPerfectNumbers (self):
    for n in range(2, self.maxN):
      if self.sieve[n] == n:
        print(n)
      kn = 2 * n
      while kn <= self.maxN:
        self.sieve[kn] += n
        kn += n
perfect = PerfectNumbers(100000)
perfect.getPerfectNumbers()