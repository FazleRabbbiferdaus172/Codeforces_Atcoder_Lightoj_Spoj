#include<bits/stdc++.h>

using namespace std;

int main()
{
    map<char,int>d;
    int a = 1;
    for (char i = 'a' ; i <= 'z' ; ++i)
    {
        d.insert({i,a});
        a++;
    }

    string s;
    cin >> s;
    int x = d['a'],y,r=0;
    for(int i = 0; i < s.size() ; ++i)
    {
        y = d[s[i]];
        r += min(abs(y - x),26-abs(y-x));
        x = y;
    }
    cout << r << "\n";
    return 0;
}
