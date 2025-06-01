#include <iostream>
using namespace std;

int main() {
    int number_people;
    std::cin >> number_people;
    
    int approves = 0, denies = 0;
    for (int i = 0; i < number_people; i++) {
      int vote;
      std::cin >> vote;
      if (vote == 0) {
        approves++;
      } else {
        denies++;
      }
    }
    
    if(approves > denies) {
      std::cout << "Y" << std::endl;
    } else {
      std::cout << "N" << std::endl;
    }
    return 0;
}
