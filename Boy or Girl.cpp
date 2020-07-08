#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    string n;
    int c=1;
    getline(cin,n);
    sort(n.begin(),n.end());
    for (int i = 1; i < n.length(); i++)
    {
        if(n[i]==n[i-1])
            continue;
        c++;
    }
    if (c % 2 == 0 )
        cout << "CHAT WITH HER!" << "\n";
    else
        cout << "IGNORE HIM!" << "\n";
    return 0;
}
