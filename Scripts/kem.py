# key encapsulation Python example
import base64
import datetime
import os
import sys
import time
import oqs
from pprint import pprint
from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF
from cryptography.hazmat.primitives import hashes

#######################################################################
# KEM example
#######################################################################

print("liboqs version:", oqs.oqs_version())
print("liboqs-python version:", oqs.oqs_python_version())
print("Enabled KEM mechanisms:")
kems = oqs.get_enabled_kem_mechanisms()
#pprint(kems, compact=True)

# create client and server with sample KEM mechanisms
kemalg = "Kyber512"


outputFile = open('key_generation_Kyber.csv', 'w')
outputFile.write("Public Key gen UE(us)" + ',')
outputFile.write("Shared Key gen UE(us)" + ',')
outputFile.write("Shared Key gen CN(us)" + ',' + '\n')

numSamples = 1
i = 0
t_start = time.perf_counter()

cn = oqs.KeyEncapsulation(kemalg)
cn_public_key = cn.generate_keypair()
secret_key = cn.export_secret_key()
#print("CN public key size: "+str(len(cn_public_key)))
for i in range(numSamples):

    t1 = time.perf_counter()
    ue = oqs.KeyEncapsulation(kemalg)
    t2 = time.perf_counter()
    duration = (t2 - t1) * 1000000
    outputFile.write(str(duration)+ ',')

    t3 = time.perf_counter()
    ciphertext, shared_secret_ue = ue.encap_secret(cn_public_key)
    #print("Cipher Text Size: "+str(len(ciphertext)))
    #print("Shared secret size: "+str(len(shared_secret_ue)))
    t4 = time.perf_counter()
    duration = (t4 - t3) * 1000000
    outputFile.write(str(duration)+ ',')
    

    t5 = time.perf_counter()
    shared_secret_cn = cn.decap_secret(ciphertext)
    t6 = time.perf_counter()
    duration = (t6 - t5) * 1000000
    outputFile.write(str(duration)+ ','+'\n')
    print("Success")


#print(ciphertext)
#print("************\n")
#print(shared_secret_ue)
print(len(shared_secret_ue))
print(len(cn_public_key))
print(len(ciphertext))
'''

sharedinfo = b"ANSI X9.63 Example"
derived_key_4 = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo
)
print("################")
key_x = derived_key_4.derive(shared_secret_ue)
print(key_x)


shared_secret_cn = cn.decap_secret(ciphertext)

sharedinfo = b"ANSI X9.63 Example"
derived_key_5 = X963KDF(
    algorithm=hashes.SHA256(),
    length=32,
    sharedinfo=sharedinfo
)
print("++++++++++++++++++++")
key_x = derived_key_5.derive(shared_secret_cn)
print(key_x)



with oqs.KeyEncapsulation(kemalg) as client:
    with oqs.KeyEncapsulation(kemalg) as server:
        print("\nKey encapsulation details:")
        #pprint(client.details)

        # client generates its keypair
        public_key = client.generate_keypair()
        #print(public_key)
        # optionally, the secret key can be obtained by calling export_secret_key()
        # and the client can later be re-instantiated with the key pair:
        # secret_key = client.export_secret_key()
        # store key pair, wait... (session resumption):
        # client = oqs.KeyEncapsulation(kemalg, secret_key)

        # the server encapsulates its secret using the client's public key
        ciphertext, shared_secret_server = server.encap_secret(public_key)
        print(ciphertext)
        print("***************")
        print(shared_secret_server)

        # the client decapsulates the server's ciphertext to obtain the shared secret
        shared_secret_client = client.decap_secret(ciphertext)

        print("\nShared secretes coincide:", shared_secret_client == shared_secret_server)

for i in range(numSamples):
    t1 = time.perf_counter()
    public_key = oqs.KeyEncapsulation(kemalg).generate_keypair()
    t2 = time.perf_counter()
    duration = (t2 - t1) * 1000000
    print("Verification time"+str(duration))
    outputFile.write(str(duration)+'\n')	
	#time.sleep(0.5)
	
t_end = time.perf_counter()
time = (t_end - t_start) * 1000000
print("Total Key generation Time"+","+str(time))
outputFile.write("Total Key generation Time"+","+str(time))
'''
