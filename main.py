from date import Date

if __name__ == "__main__":
    # example of running:
    date = Date.from_string(text="21.05.2022")
    date.add_days(number_of_days=4)
    print(date)
