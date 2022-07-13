### Chall Desc:
I made the most secure login page ever, obviously it's uncrackable if I used Wasm!


### Link : https://challs.viewsource.me/basic-wasm-m9c6xdb7


### Soln: 

The web app uses a wasm `(web assembly)` file to handle the login. You can download the file and use wabt (https://github.com/WebAssembly/wabt) to decompile it.

Searching for "password" in the decompiled code, you can find various strings relating to the login (e.g. Login failed, Login successful, here's your flag:). Amongst these is the string "admin" which is clearly the username.

There is also a weird string "exclusive_disjunction_is_amazing_also_this_entire_string_might_be_relevant". Exclusive disjunction is a fancy name for XOR, and the rest of the string suggests this is a key to recover the password. Lo and behold, slightly before this string is a hex string "1311061b2a000603173c0136001f0      50b112b1a0a0d2d0c070000090c130731173e121f04002d1037031a2f0e0d1c184b01251b1e010c1e52275f1c5e5e40390d533c0a00190d1c575b".

Convert the "exclusive_disjunction..." string to hex and use CyberChef to do the XOR on the previous hex string, and you get: "view_source_super_secret_admin_password_jipkchq9dzhjsep5x2u964fo6cxeuhj65"

 Use that whole string as the password with the admin username to log in and get the flag.
 
 #### THE FLAG : vsctf{w45m_i5_4w350m3_A8GiQVbn9f
 
 Thank you
