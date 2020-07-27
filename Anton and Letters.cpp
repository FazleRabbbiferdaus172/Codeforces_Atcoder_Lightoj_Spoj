#include<bits/stdc++.h>

using namespace std;
map<char,int>temp;
int main()
{
    string s;
    set<char> st;
    getline(cin, s);
    //cout << s;
    //cout << s.length();
    for (int i = 0; i < s.size(); ++i)
    {
        //cout << s[i];
        if (s[i] != ' ' && s[i] != '{' &&  s[i] != '}' && s[i] != ',')
            st.insert(s[i]);

    }

    cout << st.size()<<"\n";

    return 0;
}
