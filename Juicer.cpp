#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);

    int n,m,d,x,s=0,c=0;
    cin >> n >> m >>d;
    for (int i = 0; i < n ; ++i)
    {
        cin >> x;
        if (x <= m)
            s += x;
        if (s>d){
            c++;
            s = 0;
        }
    }
    cout << c << "\n";
    return 0;
}
