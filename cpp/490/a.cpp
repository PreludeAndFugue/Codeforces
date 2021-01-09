#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> ones;
    vector<int> twos;
    vector<int> threes;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        if (t == 1) {
            ones.push_back(i + 1);
        } else if (t == 2) {
            twos.push_back(i + 1);
        } else {
            threes.push_back(i + 1);
        }
    }
    int team_count = min(ones.size(), min(twos.size(), threes.size()));
    cout << team_count << endl;
    for (int i = 0; i < team_count; i++) {
        cout << ones.at(i) << " " << twos.at(i) << " " << threes.at(i) << endl;
    }
    return 0;
}
