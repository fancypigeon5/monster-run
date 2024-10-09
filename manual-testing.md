# Tests

## General Tests

### Header

| Test | Expected result | Pass |
|:---|:---|:---:|
| View the site on different types of devices | The layout should be responsive, adapting appropriately for mobile, tablet, and desktop views. | :heavy_check_mark: |
| Check site navigation | The main navigation should be accessible and functional across devices. | :heavy_check_mark: |

## User Tests

### User Registration

| Test | Expected result | Pass |
|:---|:---|:---:|
| Signing up with valid details | The user should receive a confirmation message and be redirected to the homepage. | :heavy_check_mark: |
| Entering the site without being logged in | The user should be redirected to the Login page. | :heavy_check_mark: |
| Signing out | The user should be signed out and redirected to the Login page. | :heavy_check_mark: |

### Monster Management

| Test | Expected result | Pass |
|:---|:---|:---:|
| Creating a monster | A new monster should be created and appear in the user’s monster list. | :heavy_check_mark: |
| Creating multiple monsters | Each created monster should be listed separately with its stats, correct color and equipped equipments. | :heavy_check_mark: |

### Item and Equipment Management

| Test | Expected result | Pass |
|:---|:---|:---:|
| Choosing an equipment to unlock | The selected equipment should appear in the unlocking field with its progress. | :heavy_check_mark: |
| Unlocking equipment upon goal achievement | The equipment should appear in the user’s equipment list and be available to equip to their monsters. | :heavy_check_mark: |
| Unlocking multiple equipment types | The user can have multiple equipments unlocking at once. | :heavy_check_mark: |
| Equipping an item to a monster | The monster’s stats should update to reflect the benefits of the equipped item. | :heavy_check_mark: |
### Run data

| Test | Expected result | Pass |
|:---|:---|:---:|
| choosing benefit of running data | The user should be able to choose to run for unlocking equipment or recovering monster health. | :heavy_check_mark: |
| Entering running data | The user should receive a confirmation that their data was saved successfully, and the data should be displayed in the list. | :heavy_check_mark: |
| Deleting a run | The progress should be undone, and the run should be removed from the list. | :heavy_check_mark: |

## Arena and Scoreboard

### Battleground

| Test | Expected result | Pass |
|:---|:---|:---:|
| Navigating to the Battleground | The user should be able to select their monster for battle and be taken to the batlleground. | :heavy_check_mark: |
| Battle | Both the players chosen monster and the enemy should be displayed. | :heavy_check_mark: |
| Players turn | A box with a number should be on screen when clicked it starts displaying random numbers between 0 and the monsters damage, when clicked again it should stop, this number is the damage that will be done | :heavy_check_mark: |
| Enemy turn | The same thing should happen as on players turn, but this time automated so the player should not do anything | :heavy_check_mark: |
| End of battle | When one monsters health is 0 or less, the battle should end, players are redirected back to the arena with a display telling them Win/Loss and in case of a win how many points the monster gained | :heavy_check_mark: |

### Scoreboard

| Test | Expected result | Pass |
|:---|:---|:---:|
| Navigating to the scoreboard | The user should be able to view a list of monsters with the highest scores. | :heavy_check_mark: |

## Admin Tests

### Admin Panel Management

| Test | Expected result | Pass |
|:---|:---|:---:|
| Adding monster types | The new monster type should be listed in the user interface for monster creation. | :heavy_check_mark: |
| Adding equipment types | The new equipment type should be available for users to select when unlocking items. | :heavy_check_mark: |
| Editing monster types | Changes to monster types should be reflected in the user interface immediately. | :heavy_check_mark: |
| Editing equipment types | Changes to equipment types should be reflected in the user interface immediately. | :heavy_check_mark: |


