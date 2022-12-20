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
    string name;
    getline(cin,name);
    int n=name.size();
    cout<<name[n-5];
    cout<<name[n-4];
    cout<<name[n-3];
    cout<<name[n-2];
    cout<<name[n-1]<<endl;;
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
