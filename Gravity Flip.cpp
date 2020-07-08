#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int n,b[101];
    cin >> n;
    for(int i = 0; i < n ; ++i)
        cin >> b[i];

    sort(b,b+n);

    for(int i = 0; i < n ; ++i)
        cout << b[i]<<" ";
    cout<<"\n";
    return 0;
}
