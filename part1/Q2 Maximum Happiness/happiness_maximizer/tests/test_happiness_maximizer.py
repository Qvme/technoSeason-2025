import unittest
from src.happiness_maximizer import HappinessMaximizer, HappinessException

class TestHappinessMaximizer(unittest.TestCase):

    def test_hmax_valid_case(self):
        num_tasks = 5
        num_people = 5
        happ_of_task = [10, 50, 20, 40, 30]
        diff_of_task = [3, 8 ,2 ,5 ,6]
        skill_of_ppl = [2, 6 ,8 ,3 ,7]

        maximizer = HappinessMaximizer(num_tasks, num_people, happ_of_task, diff_of_task, skill_of_ppl)
        result = maximizer.hmax()
        self.assertEqual(result, 150)  

    def test_hmax_more_people_than_tasks(self):
        num_tasks = 2
        num_people = 3
        happ_of_task = [10, 20]
        diff_of_task = [1, 2]
        skill_of_ppl = [1, 2, 3]

        maximizer = HappinessMaximizer(num_tasks, num_people, happ_of_task, diff_of_task, skill_of_ppl)
        with self.assertRaises(HappinessException) as context:
            maximizer.hmax()
        self.assertEqual(str(context.exception), "Number of people should be less than/equal to the number of tasks.")

    def test_hmax_no_skills(self):
        num_tasks = 3
        num_people = 3
        happ_of_task = [10, 20, 30]
        diff_of_task = [1, 2, 3]
        skill_of_ppl = [0, 0, 0]  # No skills

        maximizer = HappinessMaximizer(num_tasks, num_people, happ_of_task, diff_of_task, skill_of_ppl)
        result = maximizer.hmax()
        self.assertEqual(result, 0)  # No happiness can be gained

    def test_hmax_partial_skills(self):
        num_tasks = 3
        num_people = 3
        happ_of_task = [10, 20, 30]
        diff_of_task = [1, 2, 3]
        skill_of_ppl = [1, 2, 1]  # Only some skills

        maximizer = HappinessMaximizer(num_tasks, num_people, happ_of_task, diff_of_task, skill_of_ppl)
        result = maximizer.hmax()
        self.assertEqual(result, 30)  # Only task 3 can be completed by the last person

if __name__ == '__main__':
    unittest.main()
