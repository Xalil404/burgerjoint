# Burger Joint Testing
This document is a summary of the manual testing which was done for the Burger Joint web application. 

## Browser Compatibility
The platform was tested on the following browsers: Chrome, Safari & Firefox.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493384/Project%204/Screenshot_2023-10-28_at_12.41.33_PM_slrcj7.png) | Works as expected |
| Firefox | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493424/Project%204/Screenshot_2023-10-28_at_12.41.54_PM_lzpx2q.png) | Works as expected |
| Safari | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493456/Project%204/Screenshot_2023-10-28_at_12.42.23_PM_mlbrav.png) | Works as expected |

## Responsiveness
The platform was tested for responsiveness on the following devices through Chrome's developer tools: 

| Device | Screenshot | Notes |
| --- | --- | --- |
| iPhone SE | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493548/Project%204/Screenshot_2023-10-28_at_12.45.32_PM_qdf1bb.png) | Works as expected |
| iPhone XR | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493598/Project%204/Screenshot_2023-10-28_at_12.46.21_PM_sd54x7.png) | Works as expected |
| iPhone 12 PRO | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493670/Project%204/Screenshot_2023-10-28_at_12.47.33_PM_kkqxc7.png) | Works as expected |
| Galaxy Fold | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493724/Project%204/Screenshot_2023-10-28_at_12.48.26_PM_cgkie2.png) | Works as expected |
| Galaxy S8+ | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493793/Project%204/Screenshot_2023-10-28_at_12.49.36_PM_ee0aqc.png) | Works as expected |
| Nest Hub Max | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493842/Project%204/Screenshot_2023-10-28_at_12.50.21_PM_wonxv9.png) | Works as expected |
| iPad Air | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493899/Project%204/Screenshot_2023-10-28_at_12.51.22_PM_r0rykb.png) | Works as expected |
| iPad Mini | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698493950/Project%204/Screenshot_2023-10-28_at_12.52.08_PM_bgiusy.png) | Works as expected |

## Functional Testing
Testing results of functionalities not considered to be feature or user story.

| Function(s) | Screenshot | Expected Result | Notes |
| --- | --- | --- | --- |
| Web Navigation | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494305/Project%204/Screenshot_2023-10-28_at_12.58.06_PM_feqj6p.png) | Should be visible in the middle of the header | Works as expected |
| Mobile Navigation | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494361/Project%204/Screenshot_2023-10-28_at_12.59.03_PM_yquqqd.png) | Should be visible in a hamburger dropdown menu in the header | Works as expected |
| Landing Page Carousel | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494418/Project%204/Screenshot_2023-10-28_at_12.59.51_PM_otezyz.png) | The carousel should have clickable indicators and buttons to go through the slides. | Works as expected |
| Landing Page Jumbotron - under the carousel | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494472/Project%204/Screenshot_2023-10-28_at_1.00.51_PM_zwpnvf.png) | Clicking on the Jumbotron CTA buton should take the user to the booking page if they are logged in or the sign-in page if they are logged out. | Works as expected |
| Landing Page Jumbotron above the footer | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494529/Project%204/Screenshot_2023-10-28_at_1.01.46_PM_wwrsa1.png) | Clicking on the Jumbotron CTA buton should take the user to the booking page if they are logged in or the sign-in page if they are logged out. | Works as expected |
| Landing Page Menu filter | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494616/Project%204/Screenshot_2023-10-28_at_1.03.13_PM_l741zq.png) | Clicking on the different meal categories should show the relevant meals. | Works as expected |
| Landing Page Menu filter - Mobile | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494676/Project%204/Screenshot_2023-10-28_at_1.04.15_PM_ciaoig.png) | The different meal categories filter should be a drop down menu. | Works as expected |
| Footer Social Media links | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494725/Project%204/Screenshot_2023-10-28_at_1.05.06_PM_pgj5bo.png) | Clicking on the four social media links should open up those platforms in a new tab. | Works as expected |
| Logged-in Status | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494790/Project%204/Screenshot_2023-10-28_at_1.06.12_PM_i3scdg.png) | When a user is logged in they should no longer see the log-in and register buttons in the navigation. | Works as expected |
| Logged-in Notification | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698584530/Project%204/Screenshot_2023-10-29_at_12.57.29_PM_lofkt0.png) | When a user is logged in they should see a notification indicating they are logged in. | Works as expected |
| Logged-out Status | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494305/Project%204/Screenshot_2023-10-28_at_12.58.06_PM_feqj6p.png) | When a user is logged out they should see the log-in and register buttons in the navigation and no longer see the log-out button. | Works as expected |
| Logged-out Notification | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698584508/Project%204/Screenshot_2023-10-29_at_12.57.06_PM_yqlfna.png) | When a user is logged out they should see a notification indicating they are logged out. | Works as expected |
| Website Logo & Home Page Button | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494873/Project%204/Screenshot_2023-10-28_at_1.07.36_PM_pdtizy.png) | Clicking on the website logo and home page button in the header should take the user to the home page. | Works as expected |

## Features & User Story Testing

| User Story | Screenshot | Notes |
| --- | --- | --- |
| As an administrator and owner of the restaurant, I need to access an interface where I can see the list of total bookings/deliveries and the bookings' and deliveries' details. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495005/Project%204/Screenshot_2023-10-28_at_1.09.47_PM_i63s4z.png) | Works as expected |
| As a user, I want to view the landing page of a restaurant which contains its menu offerings.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698494616/Project%204/Screenshot_2023-10-28_at_1.03.13_PM_l741zq.png) | Works as expected |
| As a user, I want to register an account with the restaurant either through a username or google account in order to book a table or order delivery.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1702980493/Project%204/Screenshot_2023-12-19_at_10.07.59_AM_qkk4ex.png) | Works as expected |
| As a user, I want to log-into my account with the restaurant either through username and password or via Google account authentication in order to CRUD bookings and deliveries.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698577855/Project%204/Screenshot_2023-10-29_at_11.10.36_AM_k5yv8v.png) | Works as expected |
| As a user, I want to be able to book a table at the restaurant which includes my details such as: name, phone number, email, number of guests, date and desired meal.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1702979933/Project%204/Screenshot_2023-12-19_at_9.58.23_AM_ggqvum.png) | Works as expected |
| As a user, I want to view the list of bookings and details of my booking with the restaurant. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495450/Project%204/Screenshot_2023-10-28_at_1.17.11_PM_coc7bh.png) | Works as expected |
| As a user, I want to be able to edit and update my previous booking details.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1702980064/Project%204/Screenshot_2023-12-19_at_10.00.52_AM_h7hl0t.png) | Works as expected |
| As a user, I want to be able to delete my scheduled restaurant booking. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495586/Project%204/Screenshot_2023-10-28_at_1.19.28_PM_clmlvk.png) | Works as expected |
| As a user, I want to be able to see a pop-up asking me to confirm my booking deletion prior to it being deleted. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495641/Project%204/Screenshot_2023-10-28_at_1.20.20_PM_stcn16.png) | Works as expected |
| As a user, I need to be able to log out of my account if I happen to be on a device that isn't mine and I would like to protect my account.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698495701/Project%204/Screenshot_2023-10-28_at_1.21.22_PM_hptvnc.png) | Works as expected |
| As a user, I want to be able to book a food delivery which includes my details such as: name, phone number, address, city, delivery date, desired meals and add a note with any additional information.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1702980201/Project%204/Screenshot_2023-12-19_at_10.03.09_AM_eahamc.png) | Works as expected |
| As a user, I want to view the list of deliveries and details of my delivery with the restaurant. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698496972/Project%204/Screenshot_2023-10-28_at_1.42.33_PM_zknun1.png) | Works as expected |
| As a user, I want to be able to edit and update my food delivery details.  | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1702980350/Project%204/Screenshot_2023-12-19_at_10.05.38_AM_png8ae.png) | Works as expected |
| As a user, I want to be able to delete my food delivery order. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698497072/Project%204/Screenshot_2023-10-28_at_1.44.13_PM_sgzr5m.png) | Works as expected |
| As a user, I want to be able to see a pop-up asking me to confirm my food order deletion prior to it being deleted. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698497117/Project%204/Screenshot_2023-10-28_at_1.44.58_PM_b725no.png) | Works as expected |

## Code Validators 
| Instrument | URL | Screenshot | Notes |
| --- | --- | --- | --- |
| W3C HTML | [W3C](https://validator.w3.org/nu/?doc=) | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698658750/Project%204/Screenshot_2023-10-30_at_9.36.09_AM_gv66j7.png) | Pass: No Errors; errors related to Django templating were ignored |
| W3C CSS | [W3C CSS](https://jigsaw.w3.org/css-validator/) | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698584889/Project%204/Screenshot_2023-10-29_at_1.07.48_PM_norebb.png) | Pass: No Errors |
| JSHint | [JSHint](https://jshint.com/) | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698585177/Project%204/Screenshot_2023-10-29_at_1.12.39_PM_onx9pt.png) | Pass: No Errors |
| Pep8 | [Pep8](https://pep8ci.herokuapp.com/) | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698587284/Project%204/Screenshot_2023-10-29_at_1.47.39_PM_scvwco.png) | Pass: No Errors; E501 line too long errors were ignored |

## Lighthouse Report
| Instrument | Screenshot | Notes |
| --- | --- | --- |
| Dev Tools | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1698743380/Project%204/Screenshot_2023-10-31_at_8.58.30_AM_pwiqck.png) | N/A |