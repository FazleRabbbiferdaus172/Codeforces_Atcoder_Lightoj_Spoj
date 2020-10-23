#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;


int arr[N];
int main()
{
    //fastio;
    int t;
    cin >> t;
    for (int x = 0; x < t ; ++x)
    {
        int a, b;
        cin >> a >> b;
        int j = __gcd(a,b);
        int c = 0;
        for (int i = 1; i*i <= j; ++i)
        {
            if(j%i == 0)
            {
                if(i != j/i)
                {
                    c += 2;
                }
                else
                {
                    c += 1;
                }
            }
        }
        cout << c << endl;

    }
    return 0;
}


