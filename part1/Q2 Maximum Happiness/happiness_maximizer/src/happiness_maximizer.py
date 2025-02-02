class HappinessException(Exception):
    pass


class HappinessMaximizer:
    def __init__(self, num_tasks :int, num_people :int, happ_of_task :list[int], diff_of_task:list[int], skill_of_ppl:list[int]):
        self.num_tasks = num_tasks
        self.num_people = num_people
        self.happ_of_task = happ_of_task
        self.diff_of_task = diff_of_task
        self.skill_of_ppl = skill_of_ppl

    def hmax(self):
        if self.num_tasks < self.num_people:
            raise HappinessException("Number of people should be less than/equal to the number of tasks.")

        # zipped object (diff, happ) in descending order in accord with happ

        diff_happ = list(zip(self.happ_of_task, self.diff_of_task))
        sorted_diff_happ = sorted(diff_happ, key=lambda x: x[1], reverse=True)
        mod_sorted_diff_happ = [(j, i) for i, j in sorted_diff_happ]

        total_happiness = 0
        for skill in self.skill_of_ppl:
            max_happiness = 0
            best_difficulty_level = None
            for value in mod_sorted_diff_happ:
                if value:
                    difficulty_level, happiness = value
                    if skill >= difficulty_level and happiness > max_happiness:
                        max_happiness = happiness
                        best_difficulty_level = difficulty_level
                        mod_sorted_diff_happ.remove(value)
                        break
            if best_difficulty_level is not None:
                total_happiness += max_happiness

        return total_happiness

