import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64


e = 0xe42a12145eaa816e2846200608080305c99468042450925789504307cbc54a20ed7071b68b067b703a1679d861795542f8cbd2d1cb4d3847d0940cac018cdb0fa729571afbe10c1b8be2dd8acd99ee48b77d53c435b9c2fed59e12e02ad8cfc2bcc46ad85534c266dcc1f3a1a03d87118eaf3f5b3eeeb3be84ad023a4bf34939
n = 0x1fb18fb44f4449f45ea938306c47b91f64b6c176bd24dbb35aa876f73859c90f0e1677d07430a1188176bc0b901ca7b01f6a99a7df3aec3dd41c3d80f0d17292e43940295b2aa0e8e5823ffcf9f5f448a289f2d3cb27366f907ee62d1aaeba490e892dc69dacbafa941ab7be809e1f882054e26add5892b1fcf4e9f1c443d93bf
p = 158822251136794944865323124199145317148993195697175575250620030834076269158370217730447422132291840359498307037951292219724248353952878182870794591411565869012281621591404559808567040937104513168558997436378361254840857304689282003972439950411832326518827485842928202470808822700781566552547057732045518407241
q = 158822251136794944865323124199145317148993195697175575250620030834076269158370217730447422132291840359498307037951292219724248353952878182870794591411565869012281621591404559808567040937104513168558997436378361254840857304689282003972439950411832326518827485842928202470808822700781566552547057732045518407103
phi = (p -1)*(q-1)
def egcd(a, b):
     if a == 0:
         return (b, 0, 1)
     else:
         g, y, x = egcd(b % a, a)
         return (g, x - (b // a) * y, y)

def modinv(a, m):
     gcd, x, y = egcd(a, m)
     if gcd != 1:
         return None  # modular inverse does not exist
     else:
         return x % m

d = modinv(e,phi)
print(d)
print(hex(d))
dp = modinv(e,(p-1))
dq = modinv(e,(q-1))
qi = modinv(q,p)

def pempriv(n, e, d, p, q, dP, dQ, qInv):
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for i,x in enumerate((0, n, e, d, p, q, dP, dQ, qInv)):
        seq.setComponentByPosition(i, pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodebytes(der).decode('ascii'))

key = pempriv(n,e,d,p,q,dp,dq,qi)
print(key)
f = open("recovered.key","w")
f.write(key)
f.close()