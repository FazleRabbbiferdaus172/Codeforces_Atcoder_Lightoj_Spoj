#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;

int main()
{
    fastio;
    int t;
    cin >> t;
    for (int z = 1; z <= t; z++){


    double v1,v2,v3,a1,a2,t,t1,t2,s1,s2,ss,bs;
    cin >> v1 >> v2 >> v3 >> a1 >> a2;
    t1 = v1/a1;
    t2 = v2/a2;
    t = max(t1,t2);
    s1 = v1*t1 - .5 * a1 * t1 * t1;
    s2 = v2*t2 - .5 * a2 * t2 * t2;
    ss = s1+s2;
    bs = v3*t;
    printf("Case %d: %.8lf %.8lf\n",z,ss,bs);

    }
    return 0;
}

