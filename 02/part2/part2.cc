#include <iostream>
#include <string>

int main() {
  int horizontal_position = 0;
  int depth = 0;
  int aim = 0;
  std::string inst;
  int unit;

  while (std::cin >> inst >> unit) {
    if (inst == "down") {
      aim += unit;
    } else if (inst == "up") {
      aim -= unit;
    } else if (inst == "forward") {
      horizontal_position += unit;
      depth += unit * aim;
    } else {
      std::cerr << "Unknown instruction: " << inst << std::endl;
      return 1;
    }
  }
  std::cout << horizontal_position * depth << std::endl;
}