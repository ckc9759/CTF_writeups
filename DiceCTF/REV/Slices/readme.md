### Chall Desc : 
Have a slice

### File attached : [slices.py](slices.py)

### Soln : 

We try understanding the python code

```py
flag = input('Enter flag: ')

def fail():
    print('Wrong!')
    exit(-1)

if len(flag) != 32: fail()

if flag[:5] != 'hope{': fail()
if flag[-1] != '}': fail()
if flag[5::3] != 'i0_tnl3a0': fail()
if flag[4::4] != '{0p0lsl': fail()
if flag[3::5] != 'e0y_3l': fail()
if flag[6::3] != '_vph_is_t': fail()
if flag[7::3] != 'ley0sc_l}': fail()

print('Congrats!')
print('flag is: ', flag)
```

It is basically a flag checker which checks the array of flag with different slicing.
In python when we write array [5::3], it means starting with index 5 and an increment of 3 till the end of the array index.
I use this principle and brute force the flag filling all the spaces.

Since, size was only 32 i could do it manually.

#### THE FLAG : hope{i_l0ve_pyth0n_sli3es_a_l0t}

Thank you
