import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    i=0
    while i < 1:
        city = input("You are interested in some bike data? Which city would you like? chicago, new york city or washington: ").lower()
        i=0
        if city in ["chicago", 'new york city', "washington"]:
            i=1
            print('-'*40)
            print("You have choosen:", city)
        else:
            print("sorry. That was not a correct City. Try again!")
            print('-'*40)
            i=0
    
    # get user input for month (all, january, february, ... , june)
    i=0
    j=0
    while j < 1:
        by_month = input("Do you want to filter by month? yes / no: ").lower()
        if by_month in ["yes"]:
            while i<1:
                month = input("Which month do you want to analyze? january, february, march, april, may, june: ").lower()
                if month in ["january", "february", "march", "april", "may", "june"]:
                    i=1
                    j=1
                    print('-'*40)
                    print("You have choosen:", month)
                else:
                    print("Sorry. That was not a correct month. Try again!")
                    print('-'*40)
                    i=0
        elif by_month in ["no"]:
            month="all"
            print('-'*40)
            print("You have choosen:", month)
            j=1
        else:
            print("Sorry. That was not a correct option. Try again!")
            print('-'*40)
            j=0
    # get user input for day of week (all, monday, tuesday, ... sunday)
    i=0
    j=0
    while j < 1:
        by_day = input("Do you want to filter by day? yes / no: ")
        if by_day in ["yes"]:
            while i<1:
                day = input("Which month do you want to analyze? monday, tuesday, wednesday, thursday, friday, saturday, sunday: ").lower()
                if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                    i=1
                    j=1
                    print('-'*40)
                    print("You have choosen:", day)
                else:
                    print("Sorry. That was not a correct day. Try again!")
                    print('-'*40)
                    i=0
        elif by_day in ["no"]:
            day="all"
            print('-'*40)
            print("You have choosen:", day)
            j=1
        else:
            print("Sorry. That was not a correct option. Try again!")
            print('-'*40)
            j=0


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df["month"].value_counts().idxmax()
    month_list=["January", "February", "March", "April", "May", "June", "July", "August"]
    print("The most common month is:         ", month_list[most_month])
    
    # display the most common day of week
    most_day = df["day_of_week"].value_counts().idxmax()
    print("The most common day is:           ", most_day)
   

    # display the most common start hour
    df["hour_of_timestamp"] = df["Start Time"].dt.hour
    most_hour = df["hour_of_timestamp"].value_counts().idxmax()
    print("The most common starting hour is:  ", most_hour, "'o clock")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_st = df["Start Station"].value_counts().idxmax()
    print("The most common start station is: ", most_start_st)

    # display most commonly used end station
    most_end_st = df["End Station"].value_counts().idxmax()
    print("The most common end station is:   ", most_end_st)

    # display most frequent combination of start station and end station trip
    df['Start - End Station'] = df[['Start Station', 'End Station']].agg(' - '.join, axis=1)
    most_start_end=df["Start - End Station"].value_counts().idxmax()
    print("\nThe most frequent combination of start station and end station trip is:\n", most_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time= df["Trip Duration"].sum()
    print("The total travel time was:", total_time, "sec's")

    # display mean travel time
    mean_time= df["Trip Duration"].mean()
    print("The mean travel time was: ", mean_time, "sec's")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_typ = df["User Type"].value_counts()
    print("\nThe counts of the User Types are: ")
    print(count_user_typ)

    # Display counts of gender
    count_gender = df["Gender"].value_counts()
    print("\nThe counts of the Genders are: ")
    print(count_gender)


    # Display earliest, most recent, and most common year of birth
    earliest=df["Birth Year"].min()
    print("\nThe earliest year of birth is:    ", earliest)
    
    most_recent=df["Birth Year"].max()
    print("The most recent year of birth is: ", most_recent)
    
    most_common=df["Birth Year"].value_counts().idxmax()
    print("The most common year of birth is: ", most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def show_raw_data(df):
    """Displays 5 rows of the Raw Data (DataFrame) as long the User wants to"""
    
    # Ask the user if he wants to see raw data
    j=0
    n=0
    m=5    
    while j<1:
        raw_ans=input("Do you want to see 5 lines of the raw data? Yes/No: ").lower()
        i=0
        if raw_ans in ["yes"]:
            while i<1:
                print(df[n:m])
                n=n+5
                m=m+5
                more_raw=input("Do you want to see 5 more lines?: Yes/No: ").lower()
                if more_raw in ["yes"]:
                    i=0
                elif more_raw in ["no"]:
                    i=1
                    j=1
                else:
                    i=1
                    raw_ans="wrong"
                    print("Sorry. That was not a correct answer. Try again!")
        elif raw_ans in ["no"]:
            j=1
        else:
            print("Sorry. That was not a correct answer. Try again!")
    print("Fine. Let's start with data analysis\n")
    print("-"*40)    
        
                

    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
