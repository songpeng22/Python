from hook import reset_tracing,stop_tracing
# or
#import the_imported

def function_01():
    print( "this is function_01()" )

def function_02():
    print( "this is function_02()" )

def function_03():
    print( "this is function_03()" )

def function_04():
    print( "this is function_04()" )

def function_05():
    print( "this is function_05()" )

if __name__ == '__main__':
    print(f"main()")
    
    reset_tracing(1)
    function_01()

    stop_tracing()
    function_02()

    #reset_tracing(2)
    function_03()

    function_04()

    function_05()