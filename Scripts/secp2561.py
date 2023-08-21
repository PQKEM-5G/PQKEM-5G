from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.asymmetric import ec


import time


outputFile = open('secp256_MiniPC.csv', 'w')
outputFile.write("Public Key gen UE(us)" + ',')
outputFile.write("Shared Key gen UE(us)" + ',')
outputFile.write("Shared Key gen CN(us)" + ',' + '\n')

numSamples = 100000
i = 0
t_start = time.perf_counter()

private_key_cn = ec.generate_private_key(ec.SECP256R1())
public_key_cn = private_key_cn.public_key()


for i in range(numSamples):
    
    t1 = time.perf_counter()

    private_key_ue = ec.generate_private_key(ec.SECP256R1())
    public_key_ue = private_key_ue.public_key()

    t2 = time.perf_counter()
    duration = (t2 - t1) * 1000000
    outputFile.write(str(duration)+ ',')

    t3 = time.perf_counter()

    shared_key = private_key_ue.exchange(ec.ECDH(),public_key_cn)

    t4 = time.perf_counter()
    duration = (t4 - t3) * 1000000
    outputFile.write(str(duration)+ ',' +'\n')

'''
    t5 = time.perf_counter()

    shared_key = private_key_cn.exchange(ec.ECDH(),public_key_ue)

    t6 = time.perf_counter()
    duration = (t6 - t5) * 1000000
    outputFile.write(str(duration)+ ',' +'\n')
    print("success")
'''
print(len(str(public_key_ue)))

'''
derived_key = HKDF(

    algorithm=hashes.SHA256(),

    length=32,

    salt=None,

    info=b'handshake data',

).derive(shared_key)

shared_key_2 = private_key_2.exchange(public_key)
print(shared_key_2)
derived_key_2 = HKDF(

    algorithm=hashes.SHA256(),

    length=32,

    salt=None,

    info=b'handshake data',

).derive(shared_key_2)


derived_key_3 = HKDF(

    algorithm=hashes.SHA256(),

    length=32,

    salt=None,

    info=b'handshake data',

).derive(shared_key_2)

print(derived_key)
print(derived_key_2)

'''
sharedinfo = b"ANSI X9.63 Example"
derived_key_4 = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo
)

derived_key_5 = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo
)
key_x = derived_key_4.derive(shared_key)
print(key_x)




