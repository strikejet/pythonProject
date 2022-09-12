
def test_min():
    assert min(10, 20, 30) == 20, "it should be 20"   # this is error message if there is error


def test_sum_list():
    assert sum([10, 20, 30]) == 60, "IT should be 60"

if __name__ == "__main__":
    test_min()
    test_sum_list()
    print("everything right")
