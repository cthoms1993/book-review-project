# Read & Review - the simple book review site


## Web application overview:
This web application project is the combined learning of the python fundamentals, practical python and data centric development modules of the full stack developer course.
The object of this project is to create a fully responsive CRUD web application. this application will allow users to create,update, delete and view book reviews that they have left and that other have left as well. 


## Website functionality:
My book review application contains the main crud functionality. I used a document database called MongoDB to handle the data used for this application.
The user functionality was made using HTML, Python, CSS and flask. I used bootstrap in conjunction with a Bootswatch theme to provide the overall look,feel, and functionality of the site..
This site is made to look and feel like an old style bookshelf,using the books on the shelf as the navigation bar. 

Within this web application there is a log in/logout and a registration system. I have used this to separate the users reviews from the main pool of reviews left by everyone and allows each review to be tagged with the user who left he review,and separate the user in sessions reviews into a dedicated "your reviews" page so they can easily view,edit and delete there own reviews. 
This log in function utilises the MongoDB database to store log in details , using password hashing to securely protect the users credentials.

This project uses version control via Git and Github and it has been deployed via Heroku. 

all environmental variables are held in a .py file that has been GIT ignored for security. 



## User design experience
**To view my user design experience please visit the User design experience folder link below where I have documents for strategy, scope, structure, and writeframes** - 
[user design experience](https://github.com/cthoms1993/book-review-project/tree/master/User%20design%20experience)

## Technologies used:
* HTML, CSS & Python : core languages used to create this multi-page CRUD application.
* Bootstrap Framework : Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* Bootswatch themes: utilising a predefined theme using bootstrap functionality. 
* PyCharm IDE : PyCharm was used as the preferred IDE for this project.
* PyCharm built-in Terminal : Used to commit to local repository and further push to Github Repo ensuring adequate version controlling throughout the life-cycle of the project build.
* Github : Used to host the repository of all previous versions of the build and linked to Heroku to push the latest changes to the deployed build version held there.
* Heroku : A cloud platform as a service enabling deployment for this CRUD application.
* MongoDB Atlas : Non-relational database hosting service used.
* Font awesome icons : for icons used in main display cards and social icons. 

## Deployment
The website was coded on Pycharm IDE,  I used a local GIT repository for version control committing every so often once I made changes or additions to my code using Git commit and then git push to push the changed to my online Git repository . once I had committed it locally, I then pushed it to my online repository in GITHUB.I completed this action throughout the project to maintain a high standard of version control. Once pushed to the online GITHUB repository it was made live by launching the site Through Heroku, the live site can be found here - https://thomson-book-review.herokuapp.com/

## Testing
The site was tested locally and on heroku  using Chrome development tools.
It was tested on landscape and portrait mode on Google pixel 2, Google pixel 3, Galaxy S5, Nexus 5S, Nexus 6P, iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, iPhone X, iPad, iPad Pro and responsive desktop.

## Future features
* for future releases once the site has build a dedicated user base, the ability to comment on reviews and the ability to like and dislike would be good from a social interaction and community perspective. 
* the ability to upload the book cover of the review to the database and be displayed would provide that extra bit of clarity for the reader. 


## Credits
* I have to give credit to the code institute course material.
* [Bootswatch](https://bootswatch.com/sketchy/) - custom template and styling from
* [Hashing passwords using bcypt](https://www.youtube.com/watch?v=CSHx6eCkmv0) -  Corey Schafer tutorial on Youtube.
* responsive [bookshelf tutorial](https://www.youtube.com/watch?v=toaFKVL39CQ) - from testamur on youtube. 

 
