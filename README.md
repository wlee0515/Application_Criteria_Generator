# Application Criteria Generator

This project is for the course CEBD1260: Big Data Analytics.

## Objective

In this project, we will study the application usage database provided by China Mobile. The database provides a list of events listing the applications installed and in used in the client’s device. The database also provides information about the client device model and their associated user information (age, gender and location).

The expected outcome of this exercise is to be able to generate a set of topics targeted towards a set of audience to maximize user engagement.

## Data Source
https://www.kaggle.com/chinapage/china-mobile-user-gemographics/home

## Data Description
The data is generated  by an application developed by a company named TalkingData. Talking Data is a Chinese analytics company.

The provided data is the application usage of a device of TalkingData users starting from April 30th 2016 to May 7th 2016. The span of the data is 1 week.

This data was provided on Kaggle for the development of a user classification model that will predict the Age and Gender of the user.

The application will periodically return an event back to China Mobile with the following information:
  - Device id
  - A list of applications installed on the device
  - A list of applications that are active on the device
  - The location of the device
  - The time of event

In addition to the returned event China mobile has a list of user information associated on the device and the categories of each application.

The list of user information provided is as follow for the training set:
  - Device Brand
  - Device Model
  - User Age
  - User Gender

The list of user information provided is as follow for the test set:
  - Device Brand
  - Device Model

## Project Assumption
it is possible to maximise the engagement of an application if the application carries the same attributes of the interest of the user at a given time frame.

## Project Methodology
In order to generate a list of topics for the development of a new application, this project will use the provided data to monitor the interest level of a user base on the applications they are using. This is made possible because the database provides a list of applications that are installed and active on the user’s device in a periodic matter.

## Project Steps
  1) Take the application categories and generate a word vector that will describe the interest attribute of an application. This vector will be referred to as the “interest Vector”
  2) Aggregate the interest vector of each active application noted in each event to get an interest vector representing the interest of the user at the time and location of the event.
  3) Find a correlation between the user profile and the interest vector
  4) Model the correlation between the user profile and the interest vector to predict the interest vector of an artificial user profile.
  5) Find the list of application categories that correlates to the generated interested vector
  6) Rank the application categories base on the interest vector
  7) Recommend the ranked list of applications categories to the developer.

## Analysis of the Provided Data
### Event Time Distribution
En general users are subjected to time constraints when using the applications on their devices. Base on the time of day or day of the week the user will be using different applications on their devices or simply use less of their devices.

Below are some charts to demonstrate the fluctuation of user usage data for the given time frame.

#### Event Count Grouped in 24 Hour
![Event Count Grouped in 24 Hours](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/EventDistribution_hour_of_day.png)

As demonstrated above there is a dip in events from 2:00 am to 5:00 am in the morning. This is most probably due to the human sleep cycle. A rise in the events from 10:00 am to 1:00 pm and from 7:00 pm to 8:00 would most likely do to breaks and end of the workday.

We could further extend this chart to fit the entire week.
#### Event Count Grouped per hour for 7 days
![Event Count Grouped per hour for 7 days](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/EventDistribution_hour_of_week.png)

As visible above the events generated in this dataset is cyclic.

### Event Interest Time Distribution
Applying the same logical thinking in time constraints  on device usage, it is possible to assume that the interest of the user will shift base on time constraints as well. Below are the interest vector of each hour plotted for the entire duration of the dataset.

#### Event Interest Grouped in hours for 7 days for Male users
![Event Interest Grouped per hour for 7 days for Male Users](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/Interest_vector_per_time_male.png)

#### Event Interest Grouped in hours for 7 days for Female users
![Event Interest Grouped per hour for 7 days for Female Users](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/Interest_vector_per_time_female.png)

In the above plots each line represents a dimension of the interest vector. Whenever the lines intersects  it represents a shift in the interest level of the users.

### Interest Vector
As a point of interest to demonstrate the effectiveness of the interest vector: in analyzing the sharts above, it is visible to see that there are several lines that are greater than the other features of the interest vector. We could retrieve them by plotting a histogram of all the interest values.

#### Top 20 Interest of Male Users
![Top 20 Interest of Male Users](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/Top_interests_male.png)

#### Top 20 Interest of Female Users
![Top 20 Interest of Female Users](/Application_Criteria_Generator/Docs/Project/Images/ReadMe/Top_interests_female.png)

The top 3 dimensions of the interest vector are "tag", "industry", and "property". Performing a lookup of categories containing this dimension of the interest vector, the following categories are found:
  - Property Industry 1.0
  - Property Industry 2.0
  - Property Industry new	
  - Real Estate Property	
  - Device Properties
  - Property Trust	
  - Intellectual Property Trust	
  - Industry tag
  - Games deep tags

Base on the categories above, the users top interest in database are Real Estate Property, Industry tag, and Games with Tag systems.

### Extra Remarks
Given the level of description provided by the categories, further exploration may be required to have a comprehensive topic ranking system.
