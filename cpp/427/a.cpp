#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int m;
    int police { 0 };
    int crimes { 0 };
    for (int i = 0; i < n; i++) {
        cin >> m;
        if (m == - 1) {
            if (police > 0) {
                police -= 1;
            } else {
                crimes += 1;
            }
        } else {
            police += m;
        }
    }
    cout << crimes << endl;
}
