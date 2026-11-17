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

def lire(t):
  # "5,75" ou "-5.75" -> (signe, entier, chiffres apres la virgule)
  t=t.replace(" ","").replace(",",".")
  sg=1
  if t[:1]=="-":
    sg=-1
    t=t[1:]
  if "." in t:
    a,f=t.split(".")
  else:
    a,f=t,""
  if a=="":
    a="0"
  return sg,int(a),f

def decbin(t):
  sg,a,f=lire(t)
  s=versbin(a)
  if f!="" and int(f)>0:
    num=int(f)
    den=10**len(f)
    s=s+"."
    k=0
    while num>0 and k<16:
      num=num*2
      s=s+str(num//den)
      num=num%den
      k=k+1
    if num>0:
      s=s+"..."
  return ("-" if sg<0 else "")+s

def bindec(t):
  t=t.replace(" ","").replace(",",".")
  sg=""
  if t[:1]=="-":
    sg="-"
    t=t[1:]
  if "." in t:
    a,f=t.split(".")
  else:
    a,f=t,""
  if a=="":
    a="0"
  e=versdec(a)
  if e is None or (f!="" and versdec(f) is None):
    return None
  if f=="":
    return sg+str(e)
  m=len(f)
  d=str(versdec(f)*5**m)
  while len(d)<m:
    d="0"+d
  d=d.rstrip("0")
  return sg+str(e)+("."+d if d else "")

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
    t=input("Nombre ? ")
    print("=",decbin(t))
    sg,a,f=lire(t)
    if f.strip("0")!="":
      continue
    n=sg*a
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
    r=bindec(input("Binaire ? "))
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
