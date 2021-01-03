#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int n;
    cin >> n;
    // https://www.learncpp.com/cpp-tutorial/an-introduction-to-stdstring/
    cin.ignore(32767, '\n');

    string word;
    getline(cin, word);

    unordered_set<char> letters;
    for (int i = 0; i < word.size(); i++) {
        auto c = word.at(i);
        auto c_lower = tolower(c);
        letters.insert(c_lower);
    }
    string answer;
    if (letters.size() == 26) {
        answer = string("YES");
    } else {
        answer = string("NO");
    }

    cout << answer << endl;
}
