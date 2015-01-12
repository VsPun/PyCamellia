%module MyClass
%{
#include "MyClass.h"
%}

%include "std_string.i"

class MyClass {
public:
  MyClass();
  void addStudent(std::string name);
  std::string displayString();
};