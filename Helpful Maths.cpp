#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    char s[1001],sa[1001];
    int j=0;
    gets(s);

    for (int i=0; i < strlen(s) ; ++i)
    {
        if (isdigit(s[i]))
        {
            sa[j] = s[i];
            j++;
        }
    }
    sa[j] = '\0';
    sort(sa,sa+strlen(sa));
    for (int i=0; i < strlen(sa) ; ++i)
    {
        cout << sa[i];
        if(i == strlen(sa)-1)
            continue;
        cout << "+";
    }
    cout << "\n";


    return 0;
}
