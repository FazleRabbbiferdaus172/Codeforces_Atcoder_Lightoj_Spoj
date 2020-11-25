#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
#define ll long long
#define MOD ((int)1e9 + 7)

using namespace std;
int l[1000005+1]; //cause of this
int found[1000005+1]; //cause of this
int ind = -1;
int maxx = 1e5+1;
int n,t;
int main()
{
    //fastio;
    cin >> t;
    for (int x = 0; x <t ; x++)
    {
        cin >> n;
        int ind = -1;
        int maxx = 1e9;
        for (int i = 1 ; i <= n ; i++)found[i] = 0;

        for (int i = 1 ; i <=n ; i++)cin >> l[i],found[l[i]]++;

        for (int i = 1 ; i <= n ; i++)
            if (found[l[i]]==1 && l[i] < maxx)
                ind = i,maxx = l[i];


        cout << ind << endl;
    }
}


