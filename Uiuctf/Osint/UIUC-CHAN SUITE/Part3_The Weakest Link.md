### UIUC CHAN SUITE

---
<br />

> ## Description:
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/64738a84-b9c7-4489-80f1-87dec9530309)

This was the third part of UIUC CHAN SUITE from **UIUCTF 2024**.
<br />

> ## Approach:
It talks about a public spotify account where the flag could be hidden and also mention of another business partner or maybe UIUC Chan again as in last part.

Continuing again from where we left, we reach again to the linkedin account of [UIUC CHAN](https://www.linkedin.com/in/uiuc-chan/).

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/df790a53-ecfd-4878-842b-ec5c32768f60)

The about section mentions about spotify as well so looks like we're on the right track.

Looking at the profile, again nothing else was useful. I checked the banner and profile picture again, no posts, nothing on skills. I check the `Contact info` to find a spotify link embedded there.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/758b69df-b5d4-49f1-835d-4e9d24149fc1)

[LINK](https://open.spotify.com/user/31d2lcivqdieyl4qzx25vfmp6jt4?si=b769b2466f7e4101&nd=1&dlsi=b7e9f3a586c64e89)

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/3c1b27f5-7225-4962-bae1-cc5431d44ace)

The same profile pic is there so we know we're doing fine.

There is a single playlist on UIUC Chan spotify profile which has three songs.

Searched everything in there but nothing helped, the songs were irrelevant. Nothing on lyrics as they were actual songs.
<br />

> ## Final Solve:
After spending some time on this challenge, I tried the desktop version of spotify, followed `uiuc chan` and saw their activity.

Finally, there was some lead to this challenge. A playlist was mentioned named `songs for train lovers` and there was our flag. It took a lot of time to figure this out
as it wasn't a direct approach.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/43d59d5c-2d03-4ae0-9c9c-47669897f48f)

The fact that it is only accessible to desktop version made it a bit harder and time taking.

#### Flag : uiuctf{7rU1Y_50N65_0F_7H3_5UMM3r_432013}

Special mention to `@cha0s` who helped in solving this challenge

---

Thank you  
***ckc9759***


