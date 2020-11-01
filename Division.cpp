#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((long long)1e9 )
#define MAX ((long long)1e9 )
#define endl "\n"
#define ll long long
using namespace std;


//ll arr[N];
vector <ll> vec[N];
vector <ll> f;
void fm()
{
    for(int i = 1; i <= MAX; i++)
    {
        for (int j = 1 ; i <= MAX; j+=i)
        {
            vec[j].push_back(i);
        }
    }
}

int main()
{
    fastio;
    fm();
    int t;
    cin >> t;
    while(t--){
    ll p,q;
    cin >>p,q;

    for (auto& it : vec[p]){
        if (it % q != 0)
        {
            f.push_back(it);
        }
    }
    cout << *max_element(f.begin(),f.end())<<endl;
    }

    return 0;
}
