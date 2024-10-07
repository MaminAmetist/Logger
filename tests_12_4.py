# Логирование
# Задача "Логирование бегунов":

import rt_with_exceptions as runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(funcName)s: %(lineno)d | %(message)s')


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.obj_walk = runner.Runner('Ann', 5)
        self.obj_run = runner.Runner('Maks', 5)

        def test_walk(self):
        """Test for walk"""
        try:
            for _ in range(10):
                self.obj_walk.walk()
            self.assertEqual(self.obj_walk.distance, 50)
            logging.warning('"test_walk" выполнен успешно.')
        except TypeError and ValueError as err:
            logging.error(err,'Неверная скорость для Runner', exc_info=True)  # логируйте его на уровне WARNING

    def test_run(self):
        """Test for run"""
        try:
            for _ in range(10):
                self.obj_run.run()
            self.assertEqual(self.obj_run.distance, 100)
            logging.warning('"test_run" выполнен успешно.')
        except TypeError and ValueError as err:
            logging.error(err, 'Неверный тип данных для объекта Runner', exc_info=True)  # логируйте его на уровне WARNING

    def test_challenge(self):
        """Test walk == run"""
        for _ in range(10):
            self.obj_run.walk()
            self.obj_walk.run()
        self.assertNotEqual(self.obj_run.distance, self.obj_walk.distance)
