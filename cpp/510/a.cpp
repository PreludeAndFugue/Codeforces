#include <iostream>

using namespace std;

int main() {
    int n;
    int m;
    cin >> n;
    cin >> m;
    for (int r = 0; r < n; r++) {
        if (r % 2) {
            string row(m, '.');
            if ((r + 1) % 4) {
                row[m - 1] = '#';
            } else {
                row[0] = '#';
            }
            cout << row << endl;
        } else {
            cout << string(m, '#') << endl;
        }
    }
}
