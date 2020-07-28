#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    long long n,x,b,d=0;
    char a;
    cin >> n >> x;
    for (int i = 0 ; i < n ; ++i)
    {
        cin >> a >> b;
        if (a == '+')
            x += b;
        else
            if (b <= x)
                x -= b;
            else
                d++;
    }
    cout << x << " " << d;
    return 0;
}
