# We can now import our package 
import package

package.f1()

# If we want to import a specific module only, we can use dot notation like so:
import package.module1

package.module1.some_function()

# Same thing if we want to import a submodule
import package.subpackage1.submodule1

# We can also use the `from` keyword to import specific objects from a module
from package.module1 import some_function

# Or we can also rename them using the `as` keyword
from package.module2 import some_function as some_function_renamed

# Finally, we can use the `*` character to import everything in a module
from package.subpackage1 import *


from package.subpackage2 import submodule3 as m3

some_function_renamed()

m3.do_stuff()

