#Required package:
import pip

#Function:
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
     
#Example:
install('numpy')
