#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define MOD ((int)1e9 + 7)
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;

ll binpow (ll a, ll n)
{
    ll ans = 1;
    while (n > 0)
    {
        //if (n&1) ans *= a;
        if (n&1) ans = ans * a %MOD;
        //a *= a;
        a = a * a % MOD;
        n >>= 1;
    }
    return ans;
}


int arr[N];
int main()
{
    fastio;
    ll n,m,k;
    cin >> n >> m >> k;
    if (n%2 != m%2 && k == -1 ) cout << 0 << endl;
    else cout << binpow(binpow(2ll, (n-1)), (m-1)) << endl;

    return 0;
}


