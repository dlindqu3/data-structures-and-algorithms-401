from cmath import exp
import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# setting a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
# @pytest.mark.skip("TODO")
def test_get_nonexistent():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("banana")
    print('actual: ', actual)
    expected = None
    assert actual == expected

# Successfully returns a list of all unique keys that exist in the hashtable
# @pytest.mark.skip("TODO")
def test_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('banana', "used for sundaes")
    hashtable.set("strawberry", "taste good")
    actual = hashtable.keys()
    expected = {'apple', 'banana', 'strawberry'}
    assert actual == expected

# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
# @pytest.mark.skip("TODO")
def test_with_collisions():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("pplea", 'not used for apple sauce')
    hashtable.set('banana', "used for sundaes")
    actual = hashtable.keys()
    expected = {'apple', 'pplea', 'banana'}
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_in_range():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    index1 = hashtable.hash('apple')
    hashtable.set("pplea", 'not used for apple sauce')
    index2 = hashtable.hash('pplea')
    hashtable.set('banana', "used for sundaes")
    index3 = hashtable.hash('banana')
    assert 0 <= index1 <= hashtable.size
    assert 0 <= index2 <= hashtable.size
    assert 0 <= index3 <= hashtable.size

@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable.buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
