#include <iostream>
#include "python/include/Python.h"

using namespace std;

static wchar_t* charToWChar(const char* text)
{
    size_t size = strlen(text) + 1;
    wchar_t* wa = new wchar_t[size];
    mbstowcs(wa,text,size);
    return wa;
}

int
main(int argc, char *argv[])
{
    wchar_t* pySearchPath = charToWChar("python");
   Py_SetPythonHome(pySearchPath);
    Py_SetProgramName(charToWChar(argv[0]));
  Py_Initialize();

    PyRun_SimpleString("import os, sys\npath = os.path.abspath('src')\nsys.path.append(path)");
    PyRun_SimpleString("f=open('src/main.py')\ncode = compile(f.read(), 'src/main.py', 'exec')\nexec(code, None, None)");

  Py_Finalize();
  return 0;
}


