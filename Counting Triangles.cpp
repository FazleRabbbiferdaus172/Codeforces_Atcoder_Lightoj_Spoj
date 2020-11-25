#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
using namespace std;


int arr[N];
int main()
{
    //fastio;
    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x)
    {
        ll n;
        cin >>n;
        ll l[N];
        ll ans = 0;
        for (int i = 1; i <= n; ++i ) cin >> l[i];
        sort(l+1, l+n+1);
        l[n+1] = 2e9;
        for (int i = 1; i < n ; ++i)
            for (int j = i+1; j<n ; ++j)
            {
                int sum = l[i] + l[j];
                int lef = j+1, rig = n+1;
                while (lef<rig)
                {
                    int mid = (lef+rig)/2;
                    if (l[mid] >= sum) rig = mid;
                    else lef = mid + 1;
                }
                ans += (rig-1) - (j+1) + 1 ;
            }
        cout <<"Case " << x << ": " << ans << endl;
    }
    return 0;
}


