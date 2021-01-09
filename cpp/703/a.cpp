#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int m_total { 0 };
    int c_total { 0 };
    for (int i = 0; i < n; i++) {
        int m, c;
        cin >> m >> c;
        if (m > c) {
            m_total += 1;
        } else if (m < c) {
            c_total += 1;
        }
    }
    if (m_total > c_total) {
        cout << "Mishka" << endl;
    } else if (m_total < c_total) {
        cout << "Chris" << endl;
    } else {
        cout << "Friendship is magic!^^" << endl;
    }
}
