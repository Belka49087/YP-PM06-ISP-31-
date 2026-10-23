import unittest
import os
import json
import functionalnie

class TestProgressionModules(unittest.TestCase):
    """Класс модульного верификационного тестирования с поддержкой логирования"""

    def setUp(self):
        """Действия перед запуском каждого теста"""
        functionalnie.write_log("TEST_START", f"Инициализация автоматизированного теста: {self._testMethodName}")

    def tearDown(self):
        """Действия после завершения каждого теста"""
        functionalnie.write_log("TEST_END", f"Завершение автоматизированного теста: {self._testMethodName}")

    def test_arithmetic_calculation(self):
        """Тестирование точности ядра арифметических вычислений"""
        try:
            # an = 5 + 2 * (10 - 1) = 23
            self.assertEqual(functionalnie.calculate_arithmetic_member(5, 2, 10), 23)
            # Тестирование с отрицательным шагом
            self.assertEqual(functionalnie.calculate_arithmetic_member(100, -10, 5), 60)
            functionalnie.write_log("TEST_PASSED", "Тест арифметических вычислений успешно пройден.")
        except AssertionError as e:
            functionalnie.write_log("TEST_FAILED", f"Ошибка в тесте арифметики: {str(e)}")
            raise e

    def test_geometric_calculation(self):
        """Тестирование точности ядра геометрических вычислений"""
        try:
            # bn = 2 * (3 ** (4 - 1)) = 54
            self.assertEqual(functionalnie.calculate_geometric_member(2, 3, 4), 54)
            # Тестирование со знаменателем равным нулю
            self.assertEqual(functionalnie.calculate_geometric_member(10, 0, 3), 0)
            functionalnie.write_log("TEST_PASSED", "Тест геометрических вычислений успешно пройден.")
        except AssertionError as e:
            functionalnie.write_log("TEST_FAILED", f"Ошибка в тесте геометрии: {str(e)}")
            raise e

    def test_automated_backup_subsystem(self):
        """Верификация подсистемы создания локальных бэкапов конфигурации"""
        try:
            # Гарантируем наличие тестового профиля для успешного прохождения
            if not os.path.exists(functionalnie.PROFILE_FILE):
                with open(functionalnie.PROFILE_FILE, "w", encoding="utf-8") as f:
                    json.dump({"test_profile": {"type": "arithmetic", "first_member": 1, "step": 1}}, f)
            
            success, _ = functionalnie.create_backup()
            self.assertTrue(success)
            functionalnie.write_log("TEST_PASSED", "Тест подсистемы резервного копирования успешно пройден.")
        except AssertionError as e:
            functionalnie.write_log("TEST_FAILED", f"Ошибка в тесте резервного копирования: {str(e)}")
            raise e

if __name__ == '__main__':
    unittest.main()
