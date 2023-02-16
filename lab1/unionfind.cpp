
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <istream>
#include <set>
#include <algorithm>

using namespace std;

void query(set<int>* sets, int a, int b) {
    if(sets[a].count(b) > 0) {
        std::cout << "yes" << endl;
    } else {
        std::cout << "no" << endl;
    }
}

set<int>* joined(set<int>* sets, int a, int b) {
    set<int> merged;
    set<int>::iterator it, st;
    set<int> first = *(sets+a);
    set<int> second = *(sets+b);

    set_union(first.begin(), first.end(), second.begin(), second.end(), inserter(merged, merged.begin()));
    for (it = merged.begin(); it != merged.end(); it++) {
        *(sets + *it) = merged;
    }
    return sets;
}

int main () {
    string lineone;
    int N{0};
    int Q{0};
    std::cin >> N;
    std::cin >> Q;
    set<int>* sets 
    while (std::cin >> lineone) {
        std::cout << lineone << endl;
        if (lineone == "?") {
            query()
        } else if ()
    }
    stringstream ss(lineone);
    ss >> N;
    ss >> Q;
    //cout << "N: " << N << endl;
    //cout << "Q: " << Q << endl;
}