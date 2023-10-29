# Burger Joint 
The Burger Joint corporate website allows clients of the Burger Joint restaurant to book tables and meals in advance as well as as edit, delete or update their scheduled dine-in bookings should their plans change.  A prerequisite to making a table booking at the Burger Joint restaurant, the client must create or have a registered user account with the Burger Joint restaurant, otherwise, they will not be able to complete a table booking at the restaurant.   
Link to live site [here](https://burger-joint-286ef76e4359.herokuapp.com/).
<p align="center">
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698498511/Project%204/Screenshot_2023-10-28_at_2.07.02_PM_suhxrn.png" width="auto" height="auto" alt="image of the Burger Joint website home page on all devices"></p>

## Business Requirements
Prior to initiating the project's development, user stories were created to give a high level understanding of what the platform's functional requirements will be. 

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698577639/Project%204/Screenshot_2023-10-29_at_11.02.11_AM_yo6fj2.png" width="auto" height="auto" alt="image of the burger joint userstories">

The user stories were then placed into a kanban board in order to track the progress of the platform's development.  The Agile development kanban board can be found [here](https://github.com/users/Xalil404/projects/3/views/1).

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698498639/Project%204/Screenshot_2023-10-28_at_2.10.19_PM_r5wtpl.png" width="auto" height="auto" alt="image of the burger joint project agile kanban board">

## Wireframes
Once the user stories were completed, the next phase of the project was to complete the UX of all the expected pages and different CRUD functionalites in the platform.  The wireframes were done with a focus on mobile and web; tablets were expected to be an enlarged version of the mobile experience. 

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698500773/Project%204/Screenshot_2023-10-28_at_2.45.41_PM_smntxv.png" width="auto" height="auto" alt="Burger joint project wireframes"> 

## Database Schema
After the wire-frames completion, a database schema was created to understand what information should be stored on the back-end database.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698509403/Project%204/Screenshot_2023-10-28_at_5.09.28_PM_zxwb9c.png" width="auto" height="auto" alt="Project DB schema"> 

## Features 
The Burger website consists of the following pages and features:

* Landing Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698502222/Project%204/Screenshot_2023-10-28_at_3.09.48_PM_ggu4lo.png" width="auto" height="auto" alt="landing page"> 

* Menu with filtration options - web

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698502324/Project%204/Screenshot_2023-10-28_at_3.11.45_PM_gd6kkp.png" width="auto" height="auto" alt="menu"> 

* Menu with filtration options - mobile

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494676/Project%204/Screenshot_2023-10-28_at_1.04.15_PM_ciaoig.png" width="auto" height="auto" alt="mobile menu"> 

* Create Table Booking Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495264/Project%204/Screenshot_2023-10-28_at_1.14.01_PM_faby1v.png" width="auto" height="auto" alt="table booking page"> 

* View Bookings Page with options to edit or delete bookings

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495450/Project%204/Screenshot_2023-10-28_at_1.17.11_PM_coc7bh.png" width="auto" height="auto" alt="view bookings page"> 

* Edit or Update Bookings Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495521/Project%204/Screenshot_2023-10-28_at_1.18.22_PM_fdrent.png" width="auto" height="auto" alt="Edit bookings page"> 

* Create Food delivery page 

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698496841/Project%204/Screenshot_2023-10-28_at_1.40.22_PM_w763aj.png" width="auto" height="auto" alt="create food delivery page"> 

* View Food Deliveries Page with options to edit or delete delivery

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698496972/Project%204/Screenshot_2023-10-28_at_1.42.33_PM_zknun1.png" width="auto" height="auto" alt="view deliveries page"> 

* Edit or Update food delivery Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698497025/Project%204/Screenshot_2023-10-28_at_1.43.26_PM_ehx2kh.png" width="auto" height="auto" alt="Edit delivery page"> 

* Pop-up to confirm deletion of table booking or food delivery

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698497117/Project%204/Screenshot_2023-10-28_at_1.44.58_PM_b725no.png" width="auto" height="auto" alt="pop-up to delete booking or delivery"> 

* Account Registration Page via username or google account

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698577815/Project%204/Screenshot_2023-10-29_at_11.09.33_AM_jwufbd.png" width="auto" height="auto" alt="account registration page"> 

* Account Log-in Page via username or google account

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698577855/Project%204/Screenshot_2023-10-29_at_11.10.36_AM_k5yv8v.png" width="auto" height="auto" alt="account login page"> 

* Account Log-out Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495701/Project%204/Screenshot_2023-10-28_at_1.21.22_PM_hptvnc.png" width="auto" height="auto" alt="account logout page"> 

## Testing
All fucntional testing, user story testing, device compatibility testing and browswer compatibility testing can be found in the [TestingMD](https://github.com/Xalil404/burgerjoint/blob/main/TESTING.md) file.

## Deployment

Deployment of the Burger Joint application was done from the very start of the project and continous deployment was performed after every feature implementation in order to avoid any unforeseen hurdles or blockers during the final deployment of the application. Upon implementing the django framework and PostgreSQL databse in the my local environment, in order to deploy the project, the following steps were taken:

* I created a new application in Heroku by giving it an app name and selecting its region.

* Then in Elephant SQL I created a new instance in order to host the database. 

* I copied the Elephant SQL Postgres URL which I then pasted into my env.py file and then added a few lines of code in my settings.py file to make my django project aware of it.

* I completed migration of the database structure to the newly connected ElephantSQL database.

* Once the database had been migrated to ElephantSQL and a Profile for Heroku was created, in the application's Heroku interface I added a few config vars in the project's settings.

* Finally in the app's Heroku interface in the deploy section, I connected the project's Github repository and initiated manual deployment.

## Credits
* All images provided by [Unsplash](https://unsplash.com/) & [Pixels](https://www.pexels.com/).

* The fav icon was generated by [Favicon.io](https://favicon.io/).

* [Online Converter](https://www.online-convert.com/) was used to convert jpeg or png images into webp files.

* [Github](https://github.com/) for version control.

* [GoogleFonts](https://fonts.google.com/) for fonts selection.

* [FontAwesome](https://fontawesome.com/) for icons selection.

* [Django Framework](https://www.djangoproject.com/) for adminpanel, account authentication and other apps.

* [Heroku](https://www.heroku.com/) for front-end deployment.

* [ElephantSQL](https://www.elephantsql.com/) for database hosting. 

* [Bootstrap](https://getbootstrap.com/) for HTML and CSS code snippets.

* [Task Manager](https://zadachamanager-d3722b3cb1b7.herokuapp.com/), [To Do App](https://todoprilozheniya-b8e10f9f2dc1.herokuapp.com/), [Code Star Blog](https://helloblog-eb1bdbb756c3.herokuapp.com/) walk-through projects for guidance during development. 

* Google API for account sign up and registration  with a google account.

* This [tutorial](https://www.youtube.com/watch?v=56w8p0goIfs) on how to set up Google Authentication.

* This [StackOverflow](https://stackoverflow.com/questions/70873098/login-with-google-redairecting-on-conformation-page-to-continue-django) post on how to exclude the sign up/sign in with google intermeidiary [step/template](https://gyazo.com/afbbdbf822579d00e0b7ad4cbb5fa121). 

* [The Habit Burger Grill](https://www.habitburger.com/) for menu items. 

* [Cloudinary](https://cloudinary.com/) for image hosting. 

* [Picusm](https://picsum.photos/) for for placeholder images during development. 

* [DrawSQL](https://drawsql.app/) to create database schema.

* [Miro](https://miro.com/) to create design wireframes.
