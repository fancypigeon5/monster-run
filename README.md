# Monster Run

[Live website on Heroku](https://monster-run-deaac2a71438.herokuapp.com)

![mockup](static\images\mockup.png)

## Strategy
Monster Run is designed to motivate individuals to start or maintain their running routines. Players can create and battle monsters, earning points by entering their running data to unlock new equipment or recover health points lost during battles. The game features a leaderboard to compare monsters and track points.

The project aims to demonstrate proficiency in the Django framework by showcasing an understanding of database models and delivering a fully functional web application that highlights both front-end and back-end capabilities.


### Leading User Stories
#### As a user...

- I can Sign up so that I can use the site
- I can Create a monster so that I can start to develop my monster stats
- I can Create a new monster so that I have multiple monsters
- I can Choose an item so that I can start unlocking that item
- I can Enter running data so that I make progress and unlock items
- I can unlock equipment if i have met the required goal so that I can equip it to my monster if I want
- I can Choose more than one equipment so that I can make progress on multiple equipments
- I can Equip an item to my monster so that My monster gains the items benefits
- I can delete a run so that the progress it made for unlocking or recovery is undone
- I can Go to the arena so that I can battle my monster
- I can go to the scoreboard so that I can see the monster with the highest score
- I can view the site on different types of devices so that everything looks good

#### As an admin...

- I want to add monster types so users have more options for creation.
- I want to add equipment types for users to unlock and equip.

### Primary strategic aims for the application
- Provide an engaging platform for users to track their running and develop monsters.
- Ensure a responsive design that adapts seamlessly to different devices.
- Encourage competition through leaderboards and battles to foster user engagement.

## Scope
An agile approach will be adopted, keeping features simple and aligned with the user stories.

### In Scope Features
- User registration and login.
- Monster creation interface.
- Equipment management system.
- Run data entry and management.
- Arena for monster battles.
- Leaderboard to display top monsters.

### Out of Scope Features (for future releases)
- Integration with the Strava API for automatic running data collection.
- Development of a PvP arena for player-versus-player battles.

## Structure
The website is designed with a user-centric approach, ensuring that all features align with the identified user stories. The following elements illustrate the structure of the application:

### Navigation Bar:
- Located at the top of the page, the navbar allows users to access key sections of the application easily.
- Features a logout button for quick session termination, promoting user security.

### User Registration and Login:
- A simple and intuitive sign-up form allows users to create accounts, facilitating access to the game’s features.
- Once logged in, users are directed to their personalized dashboard.

### Monster Creation Interface:
- Users can create their first monster upon logging in or navigate to the "Create Monster" page if they have no existing monsters.
- The form for monster creation is straightforward, prompting users to input basic stats and select a type, allowing for the development of unique monsters.

### Multiple Monster Management:
- Once users have created a monster, they can easily access their "Monsters Page," displaying all owned monsters and their stats.
- Users can create additional monsters from this page, promoting diversity in gameplay.

### Equipment Management System:
- On the "Equipment Page," users can view available items, track their unlocking progress, and choose items to unlock.
- The ability to equip or unequip items to specific monsters is clearly presented, enhancing customization and strategy.

### Run Data Entry and Management:
- Users can navigate to the "Run Data Page" to enter their running data, essential for unlocking new equipment and recovering health points.
- Each run entry includes a form where users specify whether the data is for equipment unlocking or monster recovery.
- Users can also delete run entries if incorrect information was entered, automatically reverting any associated progress.

### Arena for Monster Battles:
- Users can go to the "Arena Page" to battle their monsters against randomly generated enemy monsters.
- The page provides a clear interface for selecting a monster and initiating battles, ensuring users know how to proceed.

### Leaderboard Display:
- The "Leaderboard Page" showcases the top monsters based on points, allowing users to compare their progress against others.
- This competitive aspect encourages engagement and motivates users to continue playing.

### Responsive Design:
- The site is fully responsive, ensuring that all elements are accessible and visually appealing on various devices, including smartphones and tablets.
- The layout adapts seamlessly, maintaining usability across different screen sizes.

By focusing on these structural elements, the application not only fulfills the user stories but also creates an enjoyable and engaging experience for players, fostering a community centered around fitness and gaming.

## Skeleton
The application prioritizes ease of use, featuring a clean interface that guides users through the process of creating monsters, entering run data, and battling in the arena.

Users can navigate quickly, and the aesthetic maintains a fun yet straightforward theme, enhancing the overall gaming experience.

## Surface
I am aiming for a clean, readable interface that enhances user experience.

### Colour
The color palette is chosen to convey an energetic and fun theme that aligns with the game's purpose of motivating users to run and play.


### Font
A legible font has been selected to ensure clarity across the interface, contributing to an enjoyable user experience.

## Features

### Existing features

- #### __Navbar__

- At the top of the page we find a nav section that lets players navigate the application and has a log out button.

![Navbar big screenshot](static/images/navbar-big.png)

- The navbar is responsive and changes into a burger icon on smaller screens.

![Navbar small collapsed screenshot](static/images/navbar-small-collapsed.png)
![Navbar small extended screenshot](static/images/navbar-small-extended.png)

- #### __Monster page__

- This page is the homepage for users that are logged in.
- This page displays all the users monsters with their stats and equipped equipments.

![Monsters page](static/images/monsters-page.png)

- #### __Create monster page__

- Users without any monsters are directed to this page when trying to enter the home page.
- Users are presented with a simple form where they can create their own monsters.

![Monsters page](static/images/create-monster-page.png)

- #### __Equipment page__

- On this page users can manage their equipments.
- Users are able to start unlocking new equipments by clicking on one of the available equipments.
- Users can track the progress on the equipments they are unlocking.
- Once enough progress is made users can unlock the equipment.
- Users can choose to equip/unequip their unlocked equipments to their monsters.

![Monsters page](static/images/equipment-page.png)

- #### __Run data page__

- On this page users can see their previously entered runs.
- Users can delete runs if they entered wrong information.
- Users can also enter new runs.
- When entering a new run, users will have to choose if they want to enter the run to recover a damaged monster or to unlock equipment.
- When a run is deleted its effect is also deleted (equipments can become locked again).

![Monsters page](static/images/run-data-page.png)

- #### __Arena page__

![Monsters page](static/images/arena-page.png)

- ##### __Leaderboard__
- On this page users can see a leaderboard of the monsters with the most points.

![Monsters page](static/images/leaderboard-page.png)

- ##### __Battleground__
- When a user enters the battleground they have to choose one of their monsters to use in the fight.
- An enemy monster is randomly generated and has 0, 1 or 2 randomly assigned equipments.
- the user and enemy take turns atacking, each time it is the users turn, when they click the box in the center it starts rapidly generating random numbers between 0 and their monsters damage points. When they stop by clicking again, that number is the damage of their attack. The enemy (computer) does the same thing on their turn.
- Once one of the monsters reaches 0 or less health the battle is over. if the user won, they gain points equal to the health points they have left.

![Monsters page](static/images/battleground-page.png)

### Features left to implement on future releases

- Connecting to the strava api to automaticly collect running data.

- Create a PvP arena where players can battle each other.

## User Stories

- ### As a user:
- I can Sign up so that I can use the site
- I can Create a monster so that I can start to develop my monster stats
- I can Create a new monster so that I have multiple monsters
- I can Choose an item so that I can start unlocking that item
- I can Enter running data so that I make progress and unlock items
- I can unlock equipment if i have met the required goal so that I can equip it to my monster if I want
- I can Choose more than one equipment so that I can make progress on multiple equipments
- I can Equip an item to my monster so that My monster gains the items benefits
- I can delete a run so that the progress it made for unlocking or recovery is undone
- I can Go to the arena so that I can battle my monster
- I can go to the scoreboard so that I can see the monster with the highest score
- I can view the site on different types of devices so that everything looks good

- ### As a site owner/admin:
- I can add monster types from the admin panel so that users can use it when creating their monster
- I can Add equipment types so that Users can select equipment to unlock

## Database structure

In order to help navigating the database I created this database model. It shows the different tables in the database and their relation to eachother.

![Database structure](static/images/database-structure.png)

## styling

### Colors


### typography


## Testing

### Tests

- __All the tests can be found in [this file](readme-assets/testing/testing.md).__

### Validators

- I used the W3 validator for both HTML and CSS

- HTML: As shown in the screenshot below it passed all tests
![html test](readme-assets/readme-images/HTML-validator.png)

- CSS: As shown in the screenshot below it passed all tests
![css test](readme-assets/readme-images/CSS-validator.png)

- JS: As shown in the screenshot below it passed all tests
![js test](readme-assets/readme-images/JS-validator.png)


### Performance

- To check the performance of the page we used PageSpeed which tests for both mobile and desktop. We got an acceptable score both on mobile and on desktop.
![mobile performance](readme-assets/readme-images/performance-mobile.png)
![desktop performance](readme-assets/readme-images/performance-desktop.png)

### Compatibility

- I tested the site on several different browsers (Chrome, Firefox, Opera and Safari) and did not notice any problems on Different browsers.

### Responsiveness

- I tested the site on a number of different screen sizes ranging from very small screens e.g. iPhone 5 (320px wide) to very large screens e.g. 5K iMac Pro (5120 x 2880 px).

## Deployment

### How the page is deployed

- In the GitHub repository, navigate to the Settings tab, then choose Pages from the left hand menu 
- From the source section drop-down menu, select the Master Branch
- Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment
- Any changes pushed to the master branch will take effect on the live project

### How to clone the repository

- Go to the repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

## Credits

### Content

- [W3 Schools](https://www.w3schools.com): They prodided a lot of documentation on basic JS concepts whitch helped a lot. [This example](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp) I used to style the arrows on the number type inputs. 

- [Stackoverflow](https://stackoverflow.com): A few times while experiencing a problem, this site was very useful to find others experiencing simular issues.

- [MDN wbe docs](https://developer.mozilla.org/en-US/): Just like w3 this site helped to understand some core concepts by providing well written documentation.

- [ChatGPT](https://chat.openai.com): Helped me in coming up with the name Homesquare.

- [Font Awesome](https://fontawesome.com): The burger icon for the navigation on mobile.

- [Google Fonts](https://fonts.google.com): The fonts used in the site are taken from Google fonts.


### Media

- The favicon was created by myself on inkscape.

- The chess pieces were taken from [wikimedia](https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces) and are free to use.

- The logo is custom generated by ChatGPT.