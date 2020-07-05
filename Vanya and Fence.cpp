#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,h,c=0,x;
    vector<int>l;
    cin>>n>>h;
    for(int i = 0 ; i < n; ++i){
        cin >> x;
        l.push_back(x);
    }
    sort(l.begin(),l.end());

    for (int i = 0; i < n;i++)
    {
        if (l[i] > h)
            break;
        c++;
    }
    cout << c+(l.size()-c)*2 << "\n";

    return 0;
}
