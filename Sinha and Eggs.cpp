#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e5 + 5)
#define endl "\n"
using namespace std;

int main()
{
    fastio;
    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x )
    {
        double n;
        cin >> n;
        if (sqrt(n) == floor(sqrt(n)))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}


