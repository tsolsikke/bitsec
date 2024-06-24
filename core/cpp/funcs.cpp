extern "C" {
#include <stdio.h>
}
#ifdef _WIN32
#define DLL_EXPORT extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT extern "C" __attribute__((visibility("default")))
#endif

#ifdef _WIN32
#define CALL_CONV __stdcall
#else
#define CALL_CONV
#endif

DLL_EXPORT int CALL_CONV Func_001(int val1, int val2)
{
    int sum = val1 + val2;
    return sum;
}

DLL_EXPORT void CALL_CONV Func_002(char* msg)
{
    printf("%s\r\n", msg);
}