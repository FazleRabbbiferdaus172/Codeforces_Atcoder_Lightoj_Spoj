#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    map<char,int>m;
    int input,c=0;
    for (char i = '1' ; i <= '4'; ++i)
    {
        cin >> input;
        m[i] = input;
    }

    string s;
    cin >> s;
    for(int j = 0; j < s.size(); ++j)
    {
        c += m[s[j]];
     }
     cout << c << "\n";
    return 0;
}
