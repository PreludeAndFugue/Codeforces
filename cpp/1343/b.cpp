#include <iostream>
#include <vector>

using namespace std;

void make_result(int);

int main() {
    int t;
    cin >> t;
    int n;
    for (int i = 0; i < t; i++) {
        cin >> n;
        if (n % 4) {
            cout << "NO" << endl;
        } else {
            make_result(n);
        }
    }
}


void make_result(int n) {
    int vs[n];
    for (int i = 0; i < n/2; i++) {
        vs[i] = 2 * (i + 1);
    }
    for (int i = n/2; i < n; i++) {
        vs[i] = 2 * (i - n/2) + 1;
    }
    vs[n - 1] = vs[n - 1] + n/2;
    cout << "YES" << endl;
    for (int i = 0; i < n; i++) {
        cout << vs[i] << " ";
    }
    cout << endl;
}
