#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    int n,a,nuc=0,p=0;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> a;
        if (a > 0)
            p += a;
        else
        {
            if ( p > 0 )
                p += a;
            else
                nuc -= a;
        }
    }
    cout << nuc << "\n";
    return 0;
}
