Calculating rating : 

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define vi vector<ll>
#define mod 1000000007
#define f0 for(int i=0;i<n;i++)
#define mi map<ll,ll>
#define srt(a) sort(a.begin(),a.end())
#define rev(a) revese(a.begin(),a.end();

void baj(){
    double pc = 1299/5315.0;
    double pc2 = 1/50.0;
    double e;
    if(pc>0){
        e=((pc+pc2)*23.58)*(1+(50/240));
    }
    cout<<e+29.797<<endl;
}

int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
	  baj();
	}
	return 0;
}
```
