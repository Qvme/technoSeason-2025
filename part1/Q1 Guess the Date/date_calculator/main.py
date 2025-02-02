from src.date_calculator import DateCalculator

def main():
    date_calculator = DateCalculator()
    try:
        input_date = input("Enter a date (DD-MM-YYYY): ")
        result = date_calculator.predict_day(input_date)
        print(f"The day for {input_date} is: {result}")
    except DateException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 