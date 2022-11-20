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
    string s;
    cin>>s;
    int m=0;
    for(int i=0;i<s.size();i++){
        if(s[i]!='1'){
            m++;
        }
        else{
            cout<<'D';
            cout<<char(m/6);
            m=0;
        }
    }
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
