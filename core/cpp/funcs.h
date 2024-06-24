#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT __attribute__((visibility("default")))
#endif

#ifdef _WIN32
#define CALL_CONV __stdcall
#else
#define CALL_CONV
#endif

DLL_EXPORT int CALL_CONV Func_001(int val1, int val2);
DLL_EXPORT void CALL_CONV Func_002(const char* msg);
