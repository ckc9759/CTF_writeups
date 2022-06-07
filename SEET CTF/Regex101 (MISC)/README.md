### Chal Desc:

Our team stored a flag on our machine, however, we were hacked by someone, and he generated 2999 flags and hid our original flag in the .txt file. The flag consists of 5 uppercase letters, followed by 5 digits and another 6 uppercase letters. Can you find it for us?

`MD5: 20651445a358372970c74c270d5995d3`

### File attached:  [zip_file](https://github.com/ckc1404/CTF_writeups/blob/main/SEET%20CTF/Regex101%20(MISC)/misc_regex101.zip)

### Soln: 

I made a script in C++ to check that the middle 5 characters are digits or not and it gave me the answer.

```c
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<ll>
#define mod 1000000007
#define f0 for(int i=0;i<n;i++)
#define mi map<ll,ll>

int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
	    string s;
	    cin>>s;
	    if(isdigit(s[9])&&isdigit(s[10])&&isdigit(s[11])&&isdigit(s[12])&&isdigit(s[13])){
	        cout<<s<<endl;
	    }
	}
	return 0;
}
```

The output which i got was:

```c
SEE{JBVHB86919B2BWU6}
SEE{7PQ2K94621S5PRKM}
SEE{RGSXG13841KLWIUO}
SEE{H4TJC914992UVHCC}
```

The right answer is the third option which is `SEE{RGSXG13841KLWIUO}`.

Thank you
