c=0x19d1669746c16dfb5cd5ca2d03d2e2b907f9b3f5f2fcd9b8c144845ff1a8d482dc278efd9981e95d6b97c3c19f0f2f88b689ca8eb89cc6e7c3ab3869c739920335e64fd7f844b341ef44b32b8d24f540b408da581c3730406db5ede63f0eb304b67610625b01651d08997ebdcf493822b6e37461fbc08ee407f7de44d853872bc
d=0xe42a12145eaa816e2846200608080305c99468042450925789504307cbc54a20ed7071b68b067b703a1679d861795542f8cbd2d1cb4d3847d0940cac018cdb0fa729571afbe10c1b8be2dd8acd99ee48b77d53c435b9c2fed59e12e02ad8cfc2bcc46ad85534c266dcc1f3a1a03d87118eaf3f5b3eeeb3be84ad023a4bf34939
n= 0x1fb18fb44f4449f45ea938306c47b91f64b6c176bd24dbb35aa876f73859c90f0e1677d07430a1188176bc0b901ca7b01f6a99a7df3aec3dd41c3d80f0d17292e43940295b2aa0e8e5823ffcf9f5f448a289f2d3cb27366f907ee62d1aaeba490e892dc69dacbafa941ab7be809e1f882054e26add5892b1fcf4e9f1c443d93bf
m=pow(c,d,n)
print 'sctf{'+hex(m)[2:len(hex(m))-1].decode('hex')+'}'