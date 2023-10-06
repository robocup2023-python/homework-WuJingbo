/*
题⽬：给⼀个任意位数的正整数，要求：⼀、求它是⼏位数，⼆、逆序打印出各位数字。程序分析：⼀、针对整数，分解出每⼀位数。⼆、整数转换为字符串，利⽤字符串的⽅法
*/

#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    string s = to_string(n);
    cout << s.length() << endl;
    reverse(s.begin(), s.end());
    cout << s;
    return 0;
}
