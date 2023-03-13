Packages in Python are a way to organize related modules into a single namespace. They help to organize code and avoid naming conflicts. Packages are used extensively in Python's standard library and are an essential tool for developers working on large-scale projects.

In Python, a package is simply a directory containing Python modules. That's it!

The directory must contain a special file called __init__.py for Python to recognize it as a package. This file can be empty, or it can contain initialization code for the package, which is automatically executed when the package is imported. 

Whatever we want to be imported when someone imports the package must be defined inside the `__init__.py` file, or in another file (module or subpackage) imported into it.

Folder Structure 
===

```
package/
├── __init__.py
├── module1.py
├── module2.py
├── README.md
├── subpackage1
│   ├── __init__.py
│   ├── submodule1.py
│   └── submodule2.py
└── subpackage2
    ├── __init__.py
    ├── submodule3.py
    └── submodule4.py
```

```python
# `__init__.py`

from .module1 import some_function as f1 # We will see what this means in a few minutes
from .module2 import some_function as f2
```

In this example, `package` is the root package. It contains two subpackages, `subpackage1` and `subpackage2`, and two modules, `module1` and `module2`.

To be able to import a package, python needs to know where to look for it. To do this, python has a list of `search path` (we can call it python path) which are directories that contain packages and modules. 

Python will always first look for any package you try to import in your current directory. 

For example, if we want to import our package named `package`, we must create a python file next to our package, and start it with: 

```python
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
from package.subpackage1.submodule2 import *

from package.subpackage2.submodule3 import * as m3

```

We can also import from one subpackage to another using the same principle.

```python
# We can import all objects from subpackage2 into subpackage1
from package.subpackage2 import *
```

Relative imports are important, because they allow us to import code from any subpackage, using the same parent module.
    
```python
# You can import using relative notation from within a submodule

from . import submodule1 # you can do this in submodule2

