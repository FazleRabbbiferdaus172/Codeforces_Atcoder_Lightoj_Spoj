#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int x,y,input;
    for(int i = 1; i <= 5 ; ++i)
        for(int j = 1; j <= 5; ++j)
    {
        cin >> input;
        if (input==1)
        {
            x = i;
            y = j;
        }
    }

    cout << abs(x-3)+abs(y-3) << "\n";
    return 0;

}
