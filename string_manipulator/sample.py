from string_manipulator import StringManipulator

my_string = "Hello, World!"
manipulator = StringManipulator(my_string)

print("Concatenated string:", manipulator.concatenate(" Goodbye"))
print("Length of the string:", manipulator.length())
print("Sliced string:", manipulator.slice(7, None))
print("Repeated string:", manipulator.repeat(3))
print("Uppercase:", manipulator.uppercase())
print("Lowercase:", manipulator.lowercase())
print("Stripped string:", manipulator.strip())
print("Split string:", manipulator.split(","))
print("Formatted string:", manipulator.format("Alice", 30))
print("Interpolated string:", manipulator.interpolate(name="Bob", age=25))
