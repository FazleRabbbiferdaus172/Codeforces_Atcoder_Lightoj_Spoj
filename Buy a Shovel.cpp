#include<bits/stdc++.h>

using namespace std;

int main()
{
    int s,c,i=1;
    cin >> s >> c;
    while(1)
    {
        if((i*s)%10==0 || (i*s-c)%10==0 )
            break;
        i++;
    }
    cout << i << "\n";
    return 0;
}
