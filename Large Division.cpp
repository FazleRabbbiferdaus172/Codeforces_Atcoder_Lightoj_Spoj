#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;


//int arr[N];
int main()
{
    //fastio;
    int t;
    cin >> t;
    for (int x = 1; x <= t;x++)
    {
        string a;
        long long b;
        cin >> a >> b;
        long long l = a.length();
        long long r = 0;
        for (long long i = 0; i<l; ++i)
        {
            if (a[i] == '-')
            {
                continue;
            }
            long long q = a[i] - '0';
            long long p = r*10+ q;
            r = p % b;
        }
        if (r == 0)
        {
            cout << "Case "<< x << ": divisible" << endl;
        }
        else
        {
            cout << "Case "<< x << ": not divisible" << endl;
        }
    }
    return 0;
}


