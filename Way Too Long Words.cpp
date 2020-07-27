#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,l;
    string s;
    cin>>n;
    fflush(stdin);
    for (int i = 0 ; i < n; i++ )
    {
        getline(cin,s);
        l = s.size();
        if(l > 10)
        {
            cout << s[0] << l-2 << s[l-1] << "\n";
        }
        else
            cout << s << "\n";
    }

    return 0;
}
