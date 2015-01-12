#include "MyClass.h"

#include <iostream>  // std::cout
#include <sstream>   // std::ostringstream
#include <algorithm> // std::find

MyClass::MyClass() {}

void MyClass::addStudent(std::string name) {
  _students.push_back(name);
}

std::string MyClass::displayString() {
  std::ostringstream outStream;
  outStream << "[ ";
  for (int i=0; i < _students.size(); i++) {
    outStream << _students[i];
    if (i < _students.size() - 1)
      outStream << ", ";
  }
  outStream << " ]";
  return outStream.str();
}

void MyClass::removeStudent(std::string name) {
  std::vector<std::string>::iterator studentFound = std::find(_students.begin(), _students.end(), name);
  if (studentFound != _students.end()) {
    _students.erase(studentFound);
  } else {
    std::cout << "Warning: student " << name << " not found.\n";
  }
}