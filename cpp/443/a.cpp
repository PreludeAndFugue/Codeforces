#include <iostream>
#include <unordered_set>


using namespace std;

int main() {
    string l;
    getline(cin, l);

    unordered_set<int> s{};
    for (char c : l) {
        if (c >= 'a' && c <= 'z') {
            s.insert(c);
        }
    }
    cout << s.size() << endl;
}
