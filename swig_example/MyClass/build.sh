#!/bin/sh
swig -Wall -c++ -python MyClass.i
g++ -c -Wall -Werror -fpic MyClass.cpp MyClass_wrap.cxx -I/System/Library/Frameworks/Python.framework/Versions/Current/include/python2.7
g++ -framework python -dynamiclib MyClass.o MyClass_wrap.o -o _MyClass.so
#g++ -lpython -dynamiclib MyClass.o MyClass_wrap.o -o _MyClass.so
#ld -dylib MyClass.o MyClass_wrap.o -o _MyClass.so
