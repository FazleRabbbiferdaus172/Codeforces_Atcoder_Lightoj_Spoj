#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
#define MOD ((int)1e9 + 7)

using namespace std;

//ll found[200005];
int arr[N];
int main()
{
    fastio;
    ll t;
    cin >> t;
    for (ll x = 0; x <t ; ++x)
    {
        ll n;
        cin >> n;
        ll l[1000006];
        ll found[1000006];
        ll tt = 10000005;
        ll ind = -1;
        for (ll i = 0 ; i < 100005+1 ; ++i)
        {
            found[l[i]] = 0;
        }
        for (ll i = 0 ; i < n ; ++i)
        {
            cin >> l[i];
            found[l[i]]++;
        }

        for (ll i = 0 ; i < n ; ++i)
        {
            if (found[l[i]]==1 && l[i] < tt)
            {
                tt = l[i];
                ind = i+1;
            }
        }
        cout << ind << endl;
    }
    return 0;
}


