for x in range(201455, 201471):
  D = []
  for d in range(1, x // 2 + 1):
    if x % d == 0:
      D.append(d)
  if x % 2 != 0:
    D.append(x)
  if len(D) == 6:
    print(D)

