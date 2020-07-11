#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,a[5]={100,20,10,5,1},i=0,nb=0;
    cin >> n;
    while(n)
    {
        nb += n/a[i];
        n %= a[i];
        i++;
    }
    cout << nb;
    return 0;
}
