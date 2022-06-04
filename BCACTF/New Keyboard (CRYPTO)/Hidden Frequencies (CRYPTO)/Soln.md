### Chall Desc: 
I downloaded one of my friend's files and he got really defensive... it looks like gibberish but I think there might be more to it.

### File attached: [msg.txt](msg.txt)

### Soln:

The frequency of each character in the ciphertext was different.   
Therefore i created a frequency array of all the character's occurence and converted them to characters with their ascii value using a C script.

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
	string s;
	cin>>s;
	int l=s.size();
	for(int i=0;i<l;i++){
	    if(s[i]==s[i+1]){
	        int cnt=1;
	        while(s[i]==s[i+1]){
	            i++;
	            cnt++;
	        }
	        cout<<char(cnt);
	    }
	}
	return 0;
}

```

I got the flag as output: bcactf{ch4r4ct3r_fr3qu3ncy_15_50_c00l_55aFejnb}

Thank you
