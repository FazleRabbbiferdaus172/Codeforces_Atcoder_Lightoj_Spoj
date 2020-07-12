#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    string c,s;
    cin >> c >> s;
    int j=1,r=0,x=2;
    if (s[0]!=c[0])
    {
        j = 0;
        x = 1;
    }

    for (int i = 0; i < s.size();++i)
    {
        if (s[i] == c[j])
        {
            r+=1;
            j+=1;
        }
    }
    int ll= c.size();
    cout << min(r+x,ll)<<"\n";
    return 0;
}
