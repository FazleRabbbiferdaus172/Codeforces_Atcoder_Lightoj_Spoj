#include<bits/stdc++.h>
using namespace std;
void lower(string &n)
{
    for (int i = 0; i < n.length(); ++i)
    {
        if (n[i] >= 'A' && n[i] <= 'Z')
            n[i] += 32;

    }
}
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    string a,b;
    cin >> a >>b;
    lower(a);
    lower(b);
    if (a < b)
        cout << -1 << "\n";
    else if (b < a)
        cout << 1 << "\n";
    else
        cout << 0 << "\n";
    return 0;
}
