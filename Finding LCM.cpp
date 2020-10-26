#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
using namespace std;


//int arr[N];
int main()
{
    //fastio;
    int t;
    cin >> t;
    for ( int c = 1 ; c <= t ; c++)
    {
        ll a,b,L;
        cin >>a>>b>>L;
        cout<< "Case " << c << ": ";
        ll x = a*(b/__gcd(a,b));
        if(L%x != 0 ){
            cout << "impossible" << endl;
            continue;
        }
        ll ans = L/__gcd(x,L);
        while(1){
            ll g = __gcd(ans, x);
            if(g == 1) break;
            x/=g;
            ans*=g;
        }
        cout << ans << endl;
    }

    return 0;
}

