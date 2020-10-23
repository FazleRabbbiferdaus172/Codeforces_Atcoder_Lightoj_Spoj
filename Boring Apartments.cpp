#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;

int main()
{
    fastio;
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int x;
        cin >> x;
        //cout << x << endl;
        int k = x%10;
        int ans = 0;
        for (int j = 1; j < k; j++)
        {
            ans += 10;
        }
        //cout << ans<< endl;
        int l = 1;
        while (x>0)
        {
            ans += l;
            l++;
            x /= 10;

        }
        cout << ans << endl;
    }
    return 0;
}

