#include<bits/stdc++.h>

using namespace std;

vector<int>w_n;

int main()
{
    //freopen("input.txt","r",stdin);
    int n,m,wn,x,y;
    cin >> n;
    for (int i = 0; i < n ; ++i)
    {
        cin >> wn;
        w_n.push_back(wn);
    }

    cin >> m;

    for(int i = 0; i < m; ++i)
    {
        cin >> x >> y;
        if(x == 1){
            if(x == n)
            {
                w_n[x-1] = 0;
                continue;
            }
            w_n[x] += w_n[x-1] - y;
            w_n[x-1] = 0;
        }
        else if(x==n){
            w_n[x-2] += y-1;
            w_n[x-1] = 0;
        }
        else{
            w_n[x-2] += y-1;
            w_n[x] += w_n[x-1] - y;
            w_n[x-1] = 0;
        }

    }

    for (int i = 0; i < n; ++i){
        cout << w_n[i] << "\n";
    }

    return 0;
}
