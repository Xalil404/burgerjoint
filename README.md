# Burger Joint 
The Burger Joint corporate website allows clients of the Burger Joint restaurant to book tables and meals in advance as well as as edit, delete or update their scheduled dine-in bookings should their plans change.  A prerequisite to making a table booking at the Burger Joint restaurant, the client must create or have a registered user account with the Burger Joint restaurant, otherwise, they will not be able to complete a table booking at the restaurant.   
<p align="center">
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698498511/Project%204/Screenshot_2023-10-28_at_2.07.02_PM_suhxrn.png" width="auto" height="auto" alt="image of the Burger Joint website home page on all devices"></p>

## Business Requirements
Prior to initiating the project's development, user stories were created to give a high level understanding of what the platform's functional requirements will be. The user stories were then placed into a kanban board in order to track the progress of the platform's development.  The Agile development kanban board can be found [here](https://github.com/users/Xalil404/projects/3/views/1).

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1698498639/Project%204/Screenshot_2023-10-28_at_2.10.19_PM_r5wtpl.png" width="auto" height="auto" alt="image of the burger joint project agile kanban board">

## Wireframes
Once the user stories were completed, the next phase of the project was to complete the UX of all the expected pages and different CRUD functionalites in the platform.  The wireframes were done with a focus on mobile and web; tablets were expected to be an enlarged version of the mobile experience. 

* Landing Page & menu

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634337/Project%201/Screenshot_2023-10-18_at_2.04.01_PM_coxmva.png" width="auto" height="auto" alt="landing page wireframes"> 

* Account Registration Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634429/Project%201/Screenshot_2023-10-18_at_2.04.16_PM_mxsm6v.png" width="auto" height="auto" alt="account registration page wireframes"> 

* Account Log-in Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634486/Project%201/Screenshot_2023-10-18_at_2.04.27_PM_sqrl8t.png" width="auto" height="auto" alt="account login page wireframes"> 

* Table Booking Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634559/Project%201/Screenshot_2023-10-18_at_2.04.37_PM_rldw23.png" width="auto" height="auto" alt="table booking page wireframes"> 

* View Bookings Page with options to edit or delete bookings

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634628/Project%201/Screenshot_2023-10-18_at_2.04.52_PM_hudysn.png" width="auto" height="auto" alt="view bookings page wireframes"> 

* Edit or Update Bookings Page

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1697634686/Project%201/Screenshot_2023-10-18_at_2.05.04_PM_lj8dll.png" width="auto" height="auto" alt="Edit bookings page wireframes"> 

## Features 
The Burger website consists of ...

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

* [The Habit Burger Grill](https://www.habitburger.com/) for menu items. 

* [Cloudinary](https://cloudinary.com/) for image hosting. 

* [Picusm](https://picsum.photos/) for for placeholder images during development. 
