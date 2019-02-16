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


