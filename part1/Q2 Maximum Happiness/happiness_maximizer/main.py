from src.happiness_maximizer import HappinessMaximizer, HappinessException

def main():
    num_tasks = int(input("Enter the number of tasks(int): "))
    num_people = int(input("Enter the number of people(int): "))

    print("Enter the happiness of each task(int):")
    happ_of_task = [int(input(f"Task {i+1}: ")) for i in range(num_tasks)]

    print("Enter the difficulty of each task(int):")
    diff_of_task = [int(input(f"Task {i+1}: ")) for i in range(num_tasks)]

    print("Enter the skill level of each person(int):")
    skill_of_ppl = [int(input(f"Person {i+1}: ")) for i in range(num_people)]

    try:
        task_assignment = HappinessMaximizer(num_tasks, num_people, happ_of_task, diff_of_task, skill_of_ppl)
        total_happiness = task_assignment.hmax()
        print(f"Total happiness: {total_happiness}")
    except HappinessException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
