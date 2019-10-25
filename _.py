"""
# SOME TEST
"""
print(__doc__)

class Test():
    def handy(self):
        a = input('How many hands? ')

        d = {}
        for i in range(int(a)):
            h = f"hand_{str(i+ 1)}"
            vars()[h] = self.do_something(i)
            print(h, '=', self.do_something(i))


    def do_something(self, i):
        return "something " + str(i)

#
# a = Test()
# a.handy()


info = {
    'Mike' : 29,
    'Jane' : 16,
    'William' : 45
}


keys = list(info.keys())

for i, key in enumerate(keys):
    globals()[key] = info[key]


print(f"Mike = {Mike}")
print(f"Jane = {Jane}")
print(f"Willam = {William}")
