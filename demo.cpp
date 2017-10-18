#include <iostream>

#include <mathutils/add.hpp>
#include <mathutils/add5.hpp>
#include <mathutils/sub.hpp>

int main() {
  std::cout << "add(1, 2) = " << add(1, 2) << std::endl;
  std::cout << "sub(4, 3) = " << sub(4, 3) << std::endl;
  std::cout << "add5(40) = " << add5(40) << std::endl;
  return 0;
}
