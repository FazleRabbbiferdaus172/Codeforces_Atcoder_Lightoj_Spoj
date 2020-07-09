#include<bits/stdc++.h>

using namespace std;

int main()

{
    //freopen("input.txt","r",stdin);
    int n,a,b,c=1;
    cin >> n;
    cin >> a;
    for (int i = 1; i < n ; ++i)
    {
        cin >> b;
        if (a != b)
            c++;
        a = b;
    }

    cout << c << "\n";
    return 0;
}
