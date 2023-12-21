from pydash import py_

# Method calling which is equivalent to pydash.flatten(...)
py_.flatten([1, 2, [3, [4, 5, [6, 7]]]])
[1, 2, 3, [4, 5, [6, 7]]]

# Method chaining which is equivalent to pydash.chain(...)
py_([1, 2, 3, 4]).without(2, 3).reject(lambda x: x > 1).value()
[1]

# Late method chaining
py_().without(2, 3).reject(lambda x: x > 1)([1, 2, 3, 4])
[1]