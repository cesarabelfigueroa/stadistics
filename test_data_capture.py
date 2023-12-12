from solution import DataCapture

class TestDataCapture:
    def test_less(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        assert stats.less(4) == 2

    def test_greater(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        assert stats.greater(4) == 2

    def test_between(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        assert stats.between(3, 6) == 4

    def test_empty_data(self):
        capture = DataCapture()
        stats = capture.build_stats()
        assert stats.less(4) == 0
        assert stats.greater(6) == 0
        assert stats.between(2, 8) == 0

    def test_single_value(self):
        capture = DataCapture()
        capture.add(7)
        stats = capture.build_stats()
        assert stats.less(7) == 0
        assert stats.greater(7) == 0
        assert stats.between(5, 10) == 1

    def test_all_same_values(self):
        capture = DataCapture()
        for i in range(1000):
            capture.add(5)
        stats = capture.build_stats()
        assert stats.less(5) == 0
        assert stats.greater(5) == 0
        assert stats.between(0, 10) == 1000

    def test_full_range(self):
        capture = DataCapture()
        for i in range(1000):
            capture.add(i)
        stats = capture.build_stats()
        assert stats.less(500) == 500
        assert stats.greater(500) == 499
        assert stats.between(200, 800) == 601

    def test_large_values(self):
        capture = DataCapture()
        capture.add(999)
        capture.add(998)
        stats = capture.build_stats()
        assert stats.less(999) == 1
        assert stats.greater(998) == 1
