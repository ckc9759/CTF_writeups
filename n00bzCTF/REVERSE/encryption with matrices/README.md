### Chall Desc:
My friend made this encryption scheme using matrices but he didn't make the decryption scheme, Please help me decrypt this message!

### File attached:
[chall.py](chall.py)

#### Soln (Author Troubleshooter16o4)

We have been given in chall.py how the flag string is encoded, we then have to write the decoding program to decode the input `ct` list.

`Encoding:`  

The `flag` and `rand` are two strings with 6 and 82 char respectively.  
We define a func ‘str_to_matrix’ which takes a single character as input and outputs a 2 repeated element list of corresponding Unicode character code (note this func runs only once and stops when the first time return is executed)  

Now `final_flag_matrix` and `leet_matrix` are the corresponding lists which has the matrices as elements corresponding to each character in flag and rand using str_to_matrix func

Enc_flag_matrix and Enc_leet_matrix is the list which as the numbers corresponding to strings in flag and rand and the number= (Unicode char code)^2  
Now each corresponding entry/number in enc_flag_matrix and enc_leet_matrix is multipled and appended to from the list ‘final_ct’ which is then printed as ct=[456547,546454,676754645] (Note: these are just random numbers for example purpose)  

`Decoding:`  
Now the given encoded `ct` is given as comment.  

We first divide each entry with n, where `n=(code of Թ)^2` and then take squareroot of each entry  

Now using chr() get the character corresponding to each entry in modified ct list and append them to make a string named `flag`  

Now you print the flag and retrieve it from output window of code.

Python Script
```py
import math
ct=[21629584900, 4118558976, 4118558976, 17167812676, 26606176996, 27044131401, 5407396225, 19334346304, 4291953169, 23640600025, 16132810225, 23640600025, 17519963769, 19334346304, 4649466969, 21238107289, 4649466969, 16132810225, 24053528464, 4118558976, 4118558976, 20465877481, 16132810225, 21238107289, 4649466969, 16132810225, 21238107289, 4118558976, 23231246724, 4649466969, 16132810225, 24053528464, 19334346304, 4833586576, 21629584900, 16132810225, 18597867876, 4291953169, 24890110756, 4649466969, 16132810225, 19334346304, 4118558976, 24470032041, 23231246724, 23640600025, 16132810225, 24053528464, 4118558976, 16132810225, 21238107289, 4833586576, 20465877481, 4649466969, 16132810225, 4833586576, 21629584900, 17875690000, 16132810225, 5021281321, 16132810225, 21238107289, 4291953169, 21629584900, 24470032041, 24053528464, 4649466969, 23640600025, 16132810225, 24053528464, 4118558976, 16132810225, 23640600025, 4118558976, 20850204816, 24890110756, 4649466969, 16132810225, 25740993600, 8265719056, 8265719056, 27930765625]
n = ord('Թ')**2
flag=''
for i in range(len(ct)):
    ct[i] /= n
    ct[i] = math.sqrt(ct[i])
    flag = flag + chr(int(ct[i]))
print(flag)
```

### THE FLAG: n00bz{7h1s_sch3m3_t00k_m3_m0r3_th4n_f1v3_h0urs_t0_m4k3_4nd_5_m1nut3s_t0_s0lv3_xDD}

Thanks for reading this writeup, it has been written by Priyansh Patel (Team: Hack3rs_0P)
