#include <string>
#include <vector>

class MyClass {
  std::vector<std::string> _students;
public:
  MyClass();
  void addStudent(std::string name);
  std::string displayString();
  void removeStudent(std::string name);
};