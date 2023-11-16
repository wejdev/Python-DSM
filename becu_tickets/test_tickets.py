import pytest
from tickets import matching

users = [
	["John A.", "john.a@mail.com", "Top", "3"],
	["James S.", "j.s@mail.com", "Economy", "2"],
	["Stacy C.", "stacy.c@test.com", "Economy", "2"],
	["Bobby B.", "bob@mail.com", "Medium", "10"],
	["Michelle X.", "mix@test.com", "Medium", "10"],
	["Linda F.", "l.f@mail.com", "Top", "10"],
	["Betty T.", "b.t@mail.com", "ThreeEco", "1"],
	["Nancy L.", "n.l@test.com", "TwoEco", "1"],
	["Daniel O.", "d.o@mail.com", "OneEco", "1"],
	["Mike E.", "m.e@mail.com", "FourEco", "1"],
	["Matthew R.", "mr@test.com", "OneEco", "5"],
	["Albert K.", "albert@test.com", "OneEco", "5"]
]

payments = [
	["1", "john2@mail.com", "33"],
	["2", "michelle@mail.com", "60"],
	["4", "james@mail.com", "8"],
	["3", "stacy.c@test.com", "8"],
	["5", "bob@mail.com", "60"],
	["6", "email not found", "110"],
	["7", "email not found", "1"],
	["8", "email not found", "2"],
	["9", "email not found", "3"],
	["99", "email not found", "4"],
	["10", "mr@test.com", "5"],
	["11", "a@mail.com", "5"]
]

prices = [
	["Economy", "4"],
	["Top", "11"],
	["Medium", "6"],
	["OneEco", "1"],
	["TwoEco", "2"],
	["ThreeEco", "3"],
	["FourEco", "4"]
]

expected = {
    1: "John A.",
    2: "Michelle X.",
    3: "Stacy C.",
    4: "James S.",
    5: "Bobby B.",
    6: "Linda F.",
    7: "Daniel O.",
    8: "Nancy L.",
    9: "Betty T.",
    10: "Matthew R.",
    11: "Albert K.",
    99: "Mike E."
}
def test_matching():
    matched = matching(users, payments, prices)
    print(expected)
    print(matched)
    assert matched == expected

def test_the_test():
    assert True == True
