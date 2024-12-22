class StringManipulator:
    def __init__(self, string):
        self.string = string

    def concatenate(self, other_string):
        return self.string + other_string

    def length(self):
        return len(self.string)

    def slice(self, start, end):
        return self.string[start:end]

    def repeat(self, times):
        return self.string * times

    def uppercase(self):
        return self.string.upper()

    def lowercase(self):
        return self.string.lower()

    def strip(self):
        return self.string.strip()

    def split(self, separator):
        return self.string.split(separator)

    def format(self, *args):
        return self.string.format(*args)

    def interpolate(self, **kwargs):
        return self.string.format(**kwargs)
