
lerp = lambda a, b, t=.5: a + (b - a) * t

def trange(count, start=0.0, stop=1.0):
  span = float(count)
  for i in range(count+1):
    yield lerp(start, stop, i / span)
  raise StopIterator('trange({:d}, {:f}, {:f}) exhausted'.format(count, start, stop))
