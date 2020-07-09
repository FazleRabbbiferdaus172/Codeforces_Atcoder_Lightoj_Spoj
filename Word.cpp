#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    string s;
    int ss=0,sc=0;
    cin >> s;
    for(int i = 0; i<s.length(); ++i)
    {
        if (s[i] >= 'A' && s[i] <= 'Z')
            sc++;
        else
            ss++;
    }

    if (sc > ss){
        for_each(s.begin(),s.end(), [](char & c){
            c = toupper(c);});
        cout << s << "\n";
    }
    else{
        for_each(s.begin(),s.end(), [](char & c){
            c = tolower(c);});
        cout << s<<"\n";
    }

    return 0;
}
