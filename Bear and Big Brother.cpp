#include<bits/stdc++.h>
using namespace std;

int main(){
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
int a,b,y=0;

cin >> a >> b;

while(a <= b){
    a *= 3;
    b *= 2;
    y++;
}

cout << y << "\n";

return 0;
}
