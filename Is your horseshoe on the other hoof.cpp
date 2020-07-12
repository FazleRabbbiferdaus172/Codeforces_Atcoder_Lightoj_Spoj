#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n[4],c=0,a=0;
    for(int i = 0 ; i < 4 ; ++i)
        cin >> n[i];
    sort(n,n+4);
    for (int i = 0 ; i < 4 ; ++i){
        if(a == n[i])
            continue;
        for(int j = i+1 ; j < 4;++j)
        {
            if (n[i] == n[j])
            {
                c++;
            }
        }
        a = n[i];
    }

    cout << c;
    return 0;
}
