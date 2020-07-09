#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    int n,a,m;
    vector<int>l,s,d;
    cin >> n;
    for (int i = 0; i < n ; ++i)
    {
        cin >> a;
        l.push_back(a);
    }

    while(l.size()){
        if(l.size() == 1)
        {
            m = max(l[0],l[l.size()-1]);
            s.push_back(m);
            l.erase(find(l.begin(),l.end(),m));
            break;
        }
        m = max(l[0],l[l.size()-1]);
        s.push_back(m);
        l.erase(find(l.begin(),l.end(),m));
        m = max(l[0],l[l.size()-1]);
        d.push_back(m);
        l.erase(find(l.begin(),l.end(),m));
    }

    int sums = accumulate(s.begin(),s.end(),0);
    int sumd = accumulate(d.begin(),d.end(),0);
    cout << sums << " " << sumd << "\n";
    return 0;
}
