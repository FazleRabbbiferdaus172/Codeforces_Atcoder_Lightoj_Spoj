#include<bits/stdc++.h>

using namespace std;

int main(){

int n,a,b,c,l=0;
cin >> n;

for (int i =0 ; i < n ; i++)
{
    cin >> a >> b >> c;
    if(a+b+c>=2)
    {
        l++;
    }
}

cout << l << "\n";

return 0;


}
