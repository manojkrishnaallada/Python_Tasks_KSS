"""A school system calculates student results differently depending on available data. 
Create a Result class where a method can calculate the result using either two 
subjects or three subjects. """

class Result:
    def calculate(self, m1, m2, m3=None):
        if m3 is None:
            return (m1 + m2) / 2
        return (m1 + m2 + m3) / 3

r = Result()
print("Average of 2 subjects:", r.calculate(80, 90))
print("Average of 3 subjects:", r.calculate(80, 90, 70))
