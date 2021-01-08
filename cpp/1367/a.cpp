#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    string b;
    for (int i = 0; i < t; i++) {
        cin >> b;
        string a{ "" };
        a += b[0];
        for (int j = 1; j < b.size(); j += 2) {
            a += b[j];
        }
        cout << a << endl;
    }
    cout << endl;
}
