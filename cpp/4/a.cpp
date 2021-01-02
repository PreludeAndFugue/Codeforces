#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    string x;
    getline(cin, x);

    if (n > 2 && n % 2 == 0) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
