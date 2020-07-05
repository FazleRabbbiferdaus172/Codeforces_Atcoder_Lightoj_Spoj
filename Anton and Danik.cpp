#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int n;
    string l;
    cin >> n >> l;

    if (count(l.begin(),l.end(),'A') == count(l.begin(),l.end(),'D'))
        cout << "Friendship"<< "\n";
    else if((count(l.begin(),l.end(),'A') > count(l.begin(),l.end(),'D')))
        cout << "Anton" << "\n";
    else
        cout << "Danik" << "\n";
    return 0;
}
