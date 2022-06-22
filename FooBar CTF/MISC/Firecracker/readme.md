### Chal Desc:
Zip me up and crack me down

### File attached:
[Enc.zip](ENC.zip)
[CRACKME.jpg](CRACKME.jpg)

#### Soln:

We are given two files, there is a protected zip file containing the flag and a jpg. The jpg inside the zip file is given to us.
We can use a `plaintext attack` to decode the flag.

`./pkcrack -C ENC.zip -c CRACKME.jpg -P REF.zip -p CRACKME.jpg -d decrypted -a`

#### THE FLAG: GLUG{CRAckERs_5hInE_BrI6h7_1n_THE_ni6ht_5Ky}

Thank you
