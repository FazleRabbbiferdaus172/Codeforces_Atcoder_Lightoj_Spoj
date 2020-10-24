#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;

int main()
{
    //fastio;
    int t;
    cin >> t;
    for (int x = 1 ; x <= t ; ++x)
    {
        long long n,m;
        cin >>n>>m;
        long long ans = (n*m)/2;
        cout << "Case " << x<< ": " << ans << endl;
    }
    return 0;
}


