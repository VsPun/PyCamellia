#!/bin/sh
swig -Wall -c++ -python Factorial.i
g++ -c -Wall -Werror -fpic Factorial.cpp Factorial_wrap.cxx -I/System/Library/Frameworks/Python.framework/Versions/Current/include/python2.7
g++ -lpython -dynamiclib Factorial.o Factorial_wrap.o -o _Factorial.so
