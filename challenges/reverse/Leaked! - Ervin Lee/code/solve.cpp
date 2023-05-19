#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <sstream>

using namespace std;

int main()
{
    // read all lines in file scraps.bin and store it in flag array
    ifstream file("scraps.bin");
    string flag;
    if (file)
    {
        ostringstream ss;
        ss << file.rdbuf();
        flag = ss.str();
        file.close();
    }

    char* flag_array = new char[flag.length() + 1];
    strcpy(flag_array, flag.c_str());
    
    // array of number to caesar shift each character in the flag array. array is 44 elements long. 
    int shifts[] = {0x1f, 0x2a, 0x3d, 0x4c, 0x5e, 0x6b, 0x7f, 0x8a, 0x9d, 0xa8, 0xb1, 0xc2, 0xd5, 0xe0, 0xf3, 0x0c, 0x1f, 0x2a, 0x3d, 0x4c, 0x5e, 0x6b, 0x7f, 0x8a, 0x9d, 0xa8, 0xb1, 0xc2, 0xd5, 0xe0, 0xf3, 0x0c, 0x1f, 0x2a, 0x3d, 0x4c, 0x5e, 0x6b, 0x7f, 0x8a, 0x9d, 0xa8, 0xb1, 0xc2};

    // caesar shift each character in the flag array
    for (int i = 0; i < sizeof(shifts); i++) {
        flag[i] -= shifts[i];
    }

    // print flag
    cout << flag << endl;
    return 0;
}