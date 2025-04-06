import pytest
from prob import tsp, calculate_distance  # Импортируем функции

class TestTSP:
    # Тесты для calculate_distance
    def test_calculate_distance_same_point(self):
        assert calculate_distance((0, 0), (0, 0)) == 0.0

    def test_calculate_distance_horizontal(self):
        assert calculate_distance((0, 0), (3, 0)) == 3.0

    def test_calculate_distance_vertical(self):
        assert calculate_distance((0, 0), (0, 4)) == 4.0

    def test_calculate_distance_diagonal(self):
        assert calculate_distance((0, 0), (3, 4)) == 5.0  # 3-4-5 triangle

    # Тесты для tsp

    def test_tsp_two_cities(self):
        cities = [(0, 0), (3, 0)]
        route, distance = tsp(cities)
        assert set(route) == set(cities)  # Порядок может быть любым
        assert distance == pytest.approx(6.0)  # Туда и обратно

    def test_tsp_three_cities(self):
        cities = [(0, 0), (0, 3), (4, 0)]  # Прямоугольный треугольник
        route, distance = tsp(cities)
        assert len(route) == 3
        assert distance == pytest.approx(12.0)  # 3 + 4 + 5
