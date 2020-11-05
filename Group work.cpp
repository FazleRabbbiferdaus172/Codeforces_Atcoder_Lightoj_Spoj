#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
using namespace std;
int dp[31][31];
int ncr(int n, int r)
{
    if (n == r) return 1;
    if (r == 1) return n;
    if (r == 0) return 0;
    if (dp[n][r] != 0) return dp[n][r];
    int ans = ncr(n-1,r) + ncr(n-1,r-1);
    dp[n][r] = ans;

    return ans;
}

//int arr[N];
int main()
{
    fastio;
    int n;
    cin >> n;
    int ans=0;
    for (int i = 2; i <= n; ++i)
    {
        ans += ncr(n,i);
    }
    cout << ans;
    return 0;
}


