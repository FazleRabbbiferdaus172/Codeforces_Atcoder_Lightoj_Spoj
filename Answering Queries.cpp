#include<bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL)
#define N ((int)1e5 + 5)
#define MAX ((int)1e6 + 5)
#define endl "\n"
using namespace std;


int arr[N];
int con[N];
int main()
{
    //fastio;
    int t;

    cin >> t;

    for (int i = 1; i <= t ; ++i)
    {
        int n,q;
        long long sum = 0;
        cin >> n >>q;
        for(int j = 1 ; j <= n ; ++j)
        {
            cin >> arr[j];
            con[j] = -(j-1) + (n-j);
            sum += 1LL*con[j]*arr[j];
        }
        cout << "Case " << i<<":"<<endl;
        while(q--){
            int z;
            cin >> z;
            if(z==0){
                int e,w;
                cin >>e>>w;
                e++;
                sum -= 1LL*arr[e]*con[e];
                arr[e] = w;
                sum += 1LL*arr[e]*con[e];
            }
            else{
                cout<<sum<<endl;
            }
        }




    }


    return 0;
}
