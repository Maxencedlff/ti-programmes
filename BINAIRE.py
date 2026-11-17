def versbin(n):
  if n<0:
    return "-"+versbin(-n)
  if n==0:
    return "0"
  s=""
  while n>0:
    s=str(n%2)+s
    n=n//2
  return s

def versdec(s):
  if s[:1]=="-":
    r=versdec(s[1:])
    return None if r is None else -r
  if s=="":
    return None
  n=0
  for c in s:
    if c not in "01":
      return None
    n=n*2+int(c)
  return n

def c2(n):
  b=8
  while not(-2**(b-1)<=n<2**(b-1)):
    b=b+8
  s=versbin(n+2**b if n<0 else n)
  while len(s)<b:
    s="0"+s
  return s

while True:
  print("1:Decimal -> Binaire")
  print("2:Binaire -> Decimal")
  print("3:Complement a 2 -> Dec")
  print("4:Quitter")
  ch=input("Choix ? ")
  if ch=="1":
    n=int(input("Nombre ? "))
    print("=",versbin(n))
    print("C2 :",c2(n))
  elif ch=="2":
    r=versdec(input("Binaire ? "))
    if r is None:
      print("Que des 0 et des 1 !")
    else:
      print("=",r)
  elif ch=="3":
    s=input("Binaire C2 ? ")
    r=versdec(s)
    if r is None or s[:1]=="-":
      print("Que des 0 et des 1 !")
    else:
      if s[0]=="1":
        r=r-2**len(s)
      print("=",r)
  elif ch=="4":
    break
