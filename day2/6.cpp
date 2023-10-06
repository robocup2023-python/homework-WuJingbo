#include<bits/stdc++.h>
using namespace std;
bool isFirst = true;
bool isPrime(int n){
    for(int i=2;i<=sqrt(n);i++){
        if(n%i == 0) return false;
    }
    return true;
}
void dec(int n){
    if(isPrime(n)){
        if(isFirst){
            cout << n << "=" << n;
            isFirst = false;
        }
        else
            cout << "*" << n;
        return ;
    }
    int m;
    for(int i=2;i<=100;i++){
        if(isPrime(i) && n%i==0){
            if(isFirst){
                isFirst = false;
                cout << n << "=" << i;
            }
            else cout << "*" << i;
            m = i;
            break;
        }
    }
    dec(n/m);
}

int main(){
    int n;
    cin >> n;
    dec(n);
    return 0;
}
