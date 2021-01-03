#include <iostream>

using namespace std;

int main() {
    int a;
    int b;
    cin >> a;
    cin >> b;
    int m = min(a, b);
    int n = max(a, b);
    int o = (n - m) / 2;
    cout << m << " " << o << endl;
}
