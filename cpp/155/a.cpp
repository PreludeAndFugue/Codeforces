#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int min_score = 0;
    int max_score = 0;
    int count = 0;
    int s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        if (i == 0) {
            min_score = s;
            max_score = s;
        } else {
            if (s > max_score) {
                count += 1;
                max_score = s;
            } else if (s < min_score) {
                count += 1;
                min_score = s;
            }
        }
    }
    cout << count << endl;
}
