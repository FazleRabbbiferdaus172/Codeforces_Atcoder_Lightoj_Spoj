#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        long long n;
        cin >> n;
        if (n%2==1)
        {
            cout << "Case " << i <<": Impossible"<< endl;
        }
        else
        {
            long long d = n;
            while (d % 2 == 0)
            {
                d /= 2;
            }
            cout << "Case " << i <<": "<< d << " "<< n/d << endl;
        }
    }
    return 0;
}


