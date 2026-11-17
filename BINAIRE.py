BITS=0

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
  s=s.replace(" ","")
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

def tient(n,b):
  return -2**(b-1)<=n<2**(b-1)

def c2(n,b):
  s=versbin(n+2**b if n<0 else n)
  while len(s)<b:
    s="0"+s
  return s

def affiche(s):
  g=""
  for i in range(len(s)):
    if i>0 and i%16==0:
      print(g)
      g=""
    elif i>0 and i%4==0:
      g=g+" "
    g=g+s[i]
  print(g)

while True:
  print("1:Decimal -> Binaire")
  print("2:Binaire -> Decimal")
  print("3:Complement a 2 -> Dec")
  print("4:Nb de bits :",BITS if BITS else "auto")
  print("5:Quitter")
  ch=input("Choix ? ")
  if ch=="1":
    n=int(input("Nombre ? "))
    print("=",versbin(n))
    b=BITS
    if b==0:
      b=8
      while not tient(n,b):
        b=b+8
    if tient(n,b):
      print("C2 sur",b,"bits :")
      affiche(c2(n,b))
    else:
      print("Trop grand pour",b,"bits")
  elif ch=="2":
    r=versdec(input("Binaire ? "))
    if r is None:
      print("Que des 0 et des 1 !")
    else:
      print("=",r)
  elif ch=="3":
    s=input("Binaire C2 ? ").replace(" ","")
    r=versdec(s)
    if r is None or s[:1]=="-":
      print("Que des 0 et des 1 !")
    else:
      if BITS and len(s)<BITS:
        s="0"*(BITS-len(s))+s
      if s[0]=="1":
        r=r-2**len(s)
      print("=",r,"(sur",len(s),"bits)")
  elif ch=="4":
    print("0=auto, 8, 16, 32, 64")
    b=int(input("Bits ? "))
    if b in (0,8,16,32,64):
      BITS=b
    else:
      print("Choisis 0, 8, 16, 32 ou 64")
  elif ch=="5":
    break
