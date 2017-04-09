from unittest import TestCase, main

def number_needed(a, b):
    total = 0
    dic_a = {}
    dic_b = {}
    for x in a:
        if x not in dic_a.keys():
            dic_a[x] = 1
        else:
            dic_a[x] += 1

    for x in b:
        if x not in dic_b.keys():
            dic_b[x] = 1
        else:
            dic_b[x] += 1

    d = set.symmetric_difference(set(dic_a.keys()), set(dic_b.keys()))
    i = set.intersection(set(dic_a.keys()), set(dic_b.keys()))

    for x in list(i):
        total += abs(dic_a[x] - dic_b[x])

    for x in list(d):
        if x in a:
            total += dic_a[x]

        if x in b:
            total += dic_b[x]

    return total


class NumberNeededTest(TestCase):

    def test_number_needed_test_case0(self):
        n = number_needed("cde", "abc")
        self.assertEqual(4, n)

    def test_number_needed_test_case1(self):
        n = number_needed("cdee", "abc")
        self.assertEqual(5, n)

    def test_number_needed_test_case2(self):
        n = number_needed("cde", "ecdjduebckfot")
        self.assertEqual(10, n)

    def test_number_needed_test_case3(self):
        a = "fsqoiaidfaukvngpsugszsnseskicpejjvytviya"
        b = "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"
        n = number_needed(a, b)
        self.assertEqual(42, n)

if __name__ == '__main__':
    main()
