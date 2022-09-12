def multi(a, b):
    return a * b

# will give error if tester wants answer of the function to be 400 no matter the logic
def test_multi():
    assert multi(10, 20) == 400, "it should be 400"


if __name__ == "__main__":
    test_multi()
    print("alright")
