#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e6 + 1)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
using namespace std;


int mark[N];
int phi[N];
vector < int > prime;

void sieve(int n)
{
    for(int i = 3 ; i*i<=n ; i += 2){
        if(!mark[i]){
            for(int j = i*i ; j<=n ; j += (i<<1)){
                mark[j] = 1; /// 0000000...1
            }
        }
    }
    prime.push_back(2);
    //cout << prime[0];
    for(int i = 3 ; i<=n ; i += 2){
        if(!mark[i]) prime.push_back(i);
    }
}
int main()
{
    sieve(N);
    for(int i = 1 ; i<=N ; i++) phi[i] = i;
    for(int p:prime){
        for(int j = p ; j<=N ; j += p){
            phi[j] = phi[j]/p;
            phi[j] = phi[j]*(p-1);
        }
    }
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        cout << phi[n] << endl;
    }



    return 0;
}


