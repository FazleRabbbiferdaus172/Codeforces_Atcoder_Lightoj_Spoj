#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    vector<int>h,a;
    int hj,aj,n,m=0;
    cin >> n;
    for (int i = 0 ; i < n ; ++i)
    {
        cin >> hj >> aj;
        h.push_back(hj);
        a.push_back(aj);
    }

    for (int i = 0; i < h.size(); ++i)
    {
        for ( int j = 0; j < a.size(); ++j)
            if(h[i]==a[j])
                m++;
    }

    cout << m << "\n";
    return 0;

}
