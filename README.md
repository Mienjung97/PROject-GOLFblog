![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Sebastian Kefer,

31.07.2024:
Problems with git commit because of user story template commit directly in github. fix Provided by tutor support (Oisin):

"Sometimes there are conflicts between your github repository and your local one. This can happen because you made a change directly on github, or because you are working from two computers or IDEs. Here is how to do a git pull and fix and merge conflicts:
- In the terminal type git config pull.rebase false # merge
- Run the command git pull
- Type git status to see which files have a conflict that needs fixing.
- Then check those files and look for places marked with #### or <<<<. These are the areas that differ between your local files and the Github ones. Correct these areas until the code is how you need it to be.
- Save all the files you changed.
- Then in the terminal type git add .  (don't forget the . that will add all the files changed since the last time they were committed.)
- Then git commit -m "fixed merge conflict"  You will know the merge is complete because (main | MERGING)  will return to just (main)  in the terminal
- Finally git push origin main so all your files are synced up."

-> The reason the first apps were installed without corresponding git commits.

Followed the "I think therfore I blog" project -> styling thats needs to be changed:
- base.html
- index.html
- post_detail.html
- templates -> login.html/logout.html/signup.html
    -> Add log in via google?

03.08.2024:
Ran into problems with wrong migrations -> restarted the project, left issues in old repository

05.08.2024:
Blog is up to date with "I think therfore I blog" -> started custom CSS -> About page is styled for anything over 968px. Fix coming soon.

Profile picture for Assessor: Photo by <a href="https://unsplash.com/@markusspiske?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Markus Spiske</a> on <a href="https://unsplash.com/photos/colorful-software-or-web-code-on-a-computer-monitor-Skf7HxARcoc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

My Profile (Sebastian) Picture: 
Photo by <a href="https://unsplash.com/@alexacea?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Alexandru Acea</a> on <a href="https://unsplash.com/photos/turned-on-flat-screen-tv--WBYxmW4yuw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  

Imported Readme from distinction project and will be modified:

# **PROject GOLFblog**
PROject GOLFblog is a blog project which in the future is intended to be to be an extension for the webpage of [PROject GOLFacademy](https://projectgolfacademy.com/). The goal for this blog is to serve as a central hub for everyone who associated with PROject GOLFacademy, including staff members and students, as well as anyone who is interested in golf. Staff members are can post updates and information (e.g. available spaces in courses, holidays and more) that can be pinned to the top, while site users can ask questions related to the sport or the company, write about their personal experiences, give feedback to the staff or just ask for play partners. 

[Access live website here](https://project-golfblog-96e6107b0f52.herokuapp.com/)

This site was created for Portfolio Project #4 (Full-Stack Toolkit) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).


![PROject GOLFblog responsive design](readme/assets/images/responsive.PNG)

# Table of Content

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Project Management](<#project-management>)
    * [Repository Issues](<#repository-issues>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)

* [**Existing Features**](<#existing-features>)
    * [Navigation](<#navigation>)
    * [About](<#about>)
    * [All](<#all>)
    * [Albums](<#albums>)
    * [Concerts](<#concerts>)
    * [Review Detail View](<#review-detail-view>)
    * [Update / Delete Comment](<#update-and-delete-comment>)
    * [Member Reviews](<#member-reviews>)
    * [Create Review](<#create-review>)
    * [Update Review](<#update-review>)
    * [Profile Page](<#profile-page>)
    * [Admin Area](<#admin-area>)
    * [Sign Up](<#sign-up>)
    * [Sign In](<#sign-in>)
    * [Sign Out](<#sign-out>)
    * [Footer](<#footer>)
    * [Flash Messages](<#flash-messages-and-confirmation-pages-to-the-user>)

* [**Future Features**](<#future-features>)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
    * [Libraries](<#libraries>)

* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# **Project**

## Objective
I knew I was going to create a blog project for my PP4 and after talking to my brother about it, he suggested that I could create a blog that can work as an extension of his [webpage](https://projectgolfacademy.com/). This would allow both the staff to keep the members up to date with news as well as members being able to communicate about anything related to golf or the company. Since I used to golf myself, I am not completely unfamiliar with the topic and highly enjoyed the idea. For my project to fully function as the blog it is intended to be, there are quite a few more features that still need to be implemented (more about this in the "Future features" section). This would have stretched way beyond the requirements and will be addressed as soon as I have finished the course. Nevertheless I am happy about the current state of the project.

## Site Users Goal
Site users can inform themselves about PROject GOLFacademy, learn about the experiences others have had with the company, leave reviews or suggestions, and get information about updates on courses, clubs, trips, and more. They can also try to find people to play with, as every user can include their local golf course and handicap, making it easy to connect with others in their area who have similar skill levels.

## Site Owners Goal
All staff members can post updates that can be pinned and unpinned at the top. These updates include, but are not limited to, letting people know that courses and tournaments from one of their locations, or holidays from [PROject GOLFtravel](https://projectgolfworld.com/project-golftravel/) have available slots, explaining changes in the system or new rules in the golf world, or asking for feedback themselves. Also, seeing the students interact with each other would be a huge plus, as this would improve customer satisfaction, provide valuable information for the company, and could additionally lead to more new customers.

## Project Management

### Github Board
For organizing and planning my project, I have used the [Github board](https://github.com/users/Mienjung97/projects/8/views/1), which has helped me a lot with planning out and fulfilling the acceptance criterias. 

<details><summary><b>Github Board</b></summary>

![User Stories](readme/assets/images/User_stories.PNG)

</details><br/>

### Repository Issues

Due to migration issues early in production, I had to restart the project in a new repository. The old repository is [PROject GOLDacademy blog](https://github.com/Mienjung97/PROject-GOLFacademy-blog) and the board has been moved to the new project. 

Since I had already created most user stories before, I assigned the user stories to the new project. The entire documentation can be traced in the individual user stories, including the labels that I added later. I started to use sprint labels, but have not followed through with them since this was my first django project, and I was unable to properly estimate the time needed for each user story. An example of the documentation can be seen here:

<details><summary><b>User Story documentation</b></summary>

![user story example](readme/assets/images/user_story.PNG)

</details><br/>


[Back to top](<#table-of-content>)

### Database Schema

* **Post** - Handles all the posts
* **Comment** - Handles all the comments
* **UserProfile** - Handles the user profile information (first name, last name, bio and profile image for the specific user). There is a one-to-one relation to the user model to connect it to the standard user model.

<details><summary><b>Database Schema</b></summary>

![Database Schema]()
</details><br/>

# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

<details><summary><b>Wireframes</b></summary>

![Wireframes]()
</details><br/>

## User Stories
Below the user stories for the project are listed to clarify why particular feature matters. These will then be tested and confirmed in the [Testing](<#testing>) section. In the Github board are two more user stories included, which are not part of the project yet and will be explained in the [Future Features](<#future-features>) section.

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can view a list of posts so that I can select which post I want to view | &check; |
| As a Site User | I can click on a post so that I can view the whole post | &check; |
| As a Site User | I can register an account so that I can use all features on the webpage | &check; |
| As a Site User | I can create comments on posts so that I can express my opinion or share information related to a post | &check; |
| As a Site User | I can modify or delete my comments so that I can correct my comment or delete it, if it is not valid anymore. | &check; |
| As a Site User | I can create draft posts so that I can finish writing the content later | &check; |
| As a Site User | I can view comments on an individual post so that I can read the conversation | &check; |
| As a Site User | I can delete my account so that if I want to leave the website, I no longer have an active account | &check; |
| As a Site User | I will as a logged in user start the home page on the blog site so that I dont have to sign up or see the about page | &check; |
| As a Site User | While logged out or being a new user I will start on the about page so that I get information about what the website is about | &check; |
| As a Site User | As a logged out / new user I can press a button to sign in / sign up on the about page so that I don't have manually search for the link | &check; |
| As a Site User | I can access the about page so that they can get more information about the website | &check; |
| As a Site User | I can access my profile page so that I can modify and delete information about me | &check; |
| As a Site User | I can create posts so that I can share my thoughts on the blog | &check; |
| As a Site User | I can modify and delete my posts so that I can correct mistakes or delete irelevant posts | &check; |
| As a Site User | I can access the profile page of other users so that I can see who is posting/commenting | &check; |
| As a Site User | I can use the search function so that I can find posts, comments or users | &check; |
| As a Site User | I can access a page that results in an error so that I get a custom error html page | &check; |
| As a Site User | I can like posts so that other users see how well the post is perceived | &check; |

### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can create, read, update and delete posts so that manage my blog content | &check; |
| As a Site Admin | I can create draft posts so that I can finish writing the content later | &check; |
| As a Site Admin | I can delete accounts so that users who break the GTCs no longer have access to the blog | &check; |
| As a Site Admin | I can create an about page so that I can present information of the company | &check; |
| As a Site Admin | I can access the admin panel so that the url does not have to be typed manually | &check; |
| As a Site Admin | I can pin a post to the top so that other users can be informed about important infos | &check; |

[Back to top](<#table-of-content>)

## Site Structure

The PROject GOLFblog site is split up in two parts: **when the user is logged out** and **when the user is logged in**. Depending on login status, the user will either start on the **About** page with visible buttons for **login** and **Register**, while a logged in user will start on the **Home** page.


When the user is logged out, the pages **About**, **Home**, as well as the **Search** bar are avaliable. A logged out user is able to access any post or comment to read - commenting, visiting profile pages, writing comments or posts and liking them is reserved for logged in users. Trying to access a profile page will redirect a user to the **Login** page, in the comment section, the user is informed that a login is necessary to leave a **comment** or **like** a post.

If a user is logged in, they have the additional **Add Post** Nav-link which lets them create a new post and a **Profile** drop down menu, where they have access to their profile page (labled withe their **username**), the **Show Posts** section, in which they can see their published and drafted posts, as well as the **Logout** button. While visiting a posts site, they additionally have a **like** button and a field to leave a **comment**.

If a staff user is logged in, they have an additional **Amin Panel** button, which directs them to the django admin panel.

Read more about all functionalities in the [Features](<#features>) section.

[Back to top](<#table-of-content>)

## Design Choices

* ### Color Scheme

[Coolors](https://coolors.co/)

![Color Palette image]()

* ### Typography
The fonts used for the site are 'Roboto' and 'Tinos'. Fallback font for both of them is sans-serif.

* 'Roboto' is used on all headlines including the brand logo. It's a very clean font that works really well for headlines and logos. It's easy to read and matches the minimalistic style that I wanted the site to 'breath'.

* 'Tinos' was chosen for the review excerpt and the review full text. It has a nice serif design and works really well for longer paragraphs of text.

![Google Fonts Impact](readme/assets/images/google_fonts_roboto.png)

![Google Fonts Tinos](readme/assets/images/google_fonts_tinos.png)

[Back to top](<#table-of-content>)

# **Features**
This section is devided in **Existing Features** and **Future Features** since there are more features needed for the production ready page.

## **Existing Features**

### **Navigation**
The styling of the navigation bar was heavily influenced by the [PROject GOLFacademy](https://projectgolfacademy.com/) website, while I tried to keep it as clean as possible. Depending if you are logged in or not, different menus are visible for the site user. **Login** and **Register** will transform to the **Profile** dropdown, a staff member will get the extra menu item **Admin Panel**.


*Links that are visible to logged out users*

* About - Includes information about the PROject GOLFblog and the PROject GOLFacademy.
* Home - Lists all posts on the site.
* Search - a search bar that filters for profiles, posts and comments.
* Login / Register - Gives the user the option to log in or register to the PROject GOLFblog.

<details><summary><b>Navigation Large - User Not Logged In</b></summary>

![Navigation Large - User Not Logged In]()
</details><br/>

<details><summary><b>Navigation Small - User Not Logged In</b></summary>

![Navigation Small - User Not Logged In]()
</details><br/>

*Links that are visible to logged in users*

All of the links that are visible to a not logged in user plus the ones below.

* Add Post - Lets the user create a new review.
* Profile - Acts as a drop down menu where the user can access the following:
- "Username" - Shows logged in users profile page.
- Show posts - Allows the user to access all their posts, including the ones they saved as a draft.
- Log Out - Logs out the user.

<details><summary><b>Navigation Large - User Logged In</b></summary>

![Navigation Large - User Logged In](readme/assets/images/navbar_large_logged_in.png)
</details><br/>

<details><summary><b>Navigation Small - User Logged In</b></summary>

![Navigation Small - User Logged In](readme/assets/images/navbar_small_logged_in.png)
</details><br/>

*Link that is visible if user is administrator*

All of the links above plus the one below.
* Admin Panel - Directs the superuser to the django admin panel where they have full access to all users, posts, comments and more (see more in the features section).

<details><summary><b>Navigation Large - Admin Logged In</b></summary>

![Navigation Large - Admin Logged In](readme/assets/images/navbar_large_admin_logged_in.png)
</details><br/>

<details><summary><b>Navigation Small - Admin Logged In</b></summary>

![Navigation Small - Admin Logged In](readme/assets/images/navbar_small_admin_logged_in.png)
</details><br/>

### **About**
In the about section the user can read about ...

<details><summary><b>About Section</b></summary>

![About](readme/assets/images/about.png)
</details><br/>

### **All**
This page lists all the reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. The page shows 6 cards on bigger screens before a pagination mechanism kicks in. On smaller screens the cards are stacked vertically.

<details><summary><b>All Reviews - User Logged Out</b></summary>

![All Reviews - User Logged Out](readme/assets/images/all_reviews_logged_out.png)
</details><br/>

<details><summary><b>All Reviews - User Logged In</b></summary>

![All Reviews - User Logged In](readme/assets/images/all_reviews_logged_in.png)
</details><br/>

### **Albums**
This page lists all the album reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. No screenshots for this view due to the fact it's the same concept as in the all reviews section except that the review cards are filtered on the category 'album'.

### **Concerts**
This page lists all the concert reviews that has been made at Review | Alliance. If the user is not logged in there is only a "read more" option visible for the user on each review card. If the user is logged in an *update* and *delete* option gets visible on the reviews that the user has written. No screenshots for this view due to the fact it's the same concept as in the all reviews section except that the review cards are filtered on the category 'concert'.

### **Review Detail View**
The review detail shows the details about the review that the user has chosen in the all, albums or concert view. Depending on if the user is logged in the view looks a little bit different. If the user is logged in they get the possibility to like the review and also update and delete it if they have written it. A logged in user can also leave a comment (and update / delete their own comment as well).

<details><summary><b>Review Detail View - User Logged Out</b></summary>

![Review Detail View - User Logged Out](readme/assets/images/review_detail_logged_out.png)
![Review Detail View Comment - User Logged Out](readme/assets/images/review_detail_comment_logged_out.png)
</details><br/>

<details><summary><b>Review Detail View - User Logged In</b></summary>

![Review Detail View - User Logged In](readme/assets/images/review_detail_logged_in.png)
![Review Detail View Comment - User Logged In](readme/assets/images/review_detail_comment_logged_in.png)
</details><br/>

### **Update And Delete Comment**
If the user is logged in and has written a comment there is a possibility to edit and delete the comment. When the comment has been updated it needs to be re-approved by Review | Alliance.

<details><summary><b>Update Comment</b></summary>

![Update Comment](readme/assets/images/update_comment.png)
</details><br/>

### **Member Reviews**
The Member Review Page lists the reviews that the logged in user has written. The user can update and delete their review on this page and also gets information about the status of the review. There are 4 different statuses:

* *Your review is awaiting approval* - Review has been submitted with the status 'published' and awaits approval
* *Your review is in draft status but is approved* - The review is in draft status but has been approved
* *Your review is published and approved* - The review is published and approved
* *Your review is in draft status* - The review has been submitted with the status 'draft'

<details><summary><b>Member Reviews</b></summary>

![Member Reviews](readme/assets/images/member_reviews.png)
</details><br/>

### **Create Review**
On this page the registered and logged in user can create their own review. When they have sent it in Review | Alliance needs to approve it, until it's approved it will not be visible for the public.

<details><summary><b>Create Review</b></summary>

![Create Review](readme/assets/images/create_review.png)
</details><br/>

### **Update Review**
On this page the registered and logged in user can update their own review. When they have updated it in Review | Alliance needs to re-approve it, until it's re-approved it will not be visible for the public.

<details><summary><b>Update Review</b></summary>

![Update Review](readme/assets/images/update_review.png)
</details><br/>

### **Profile Page**
On this page the user can view and update their own profile page. The profile is visible in the about section.

<details><summary><b>Profile Page</b></summary>

![Profile Page](readme/assets/images/update_profile.png)
</details><br/>

### **Admin Area**
On this page the administrator (or other superuser decided by Review | Alliance) can *approve* / *unapprove* / *publish* / *unpublish* and *delete* reviews and comments. General information about *number of users*, *number of comments*, *number of reviews*, *unapproved comments / reviews* is also being showed on the page.

<details><summary><b>Admin Area</b></summary>

![Admin Area](readme/assets/images/admin_area.png)
</details><br/>

### **Sign Up**
If the site visitor has no registered user at Review | Alliance they can sign up. They can also add a presentation and upload a featured image that will be used on the users profile page.

<details><summary><b>Sign Up</b></summary>

![Sign Up](readme/assets/images/sign_up.png)
</details><br/>

### **Sign In**
On this page the user can sign in to Review | Alliance

<details><summary><b>Sign In</b></summary>

![Sign In](readme/assets/images/sign_in.png)
</details><br/>

### **Sign Out**
When the user clicks sign out in the menu bar a confirmation page is being showed so that the user don't accidently sign out.

<details><summary><b>Sign Out</b></summary>

![Member Reviews](readme/assets/images/sign_out.png)
</details><br/>

### **Footer**
The footer area includes short information about Review | Alliance, contact information and links to relevant social media.

<details><summary><b>Footer</b></summary>

![Footer](readme/assets/images/footer.png)
</details><br/>

### **Flash Messages and confirmation pages to the user**
The sites incorporates flash messages and confirmation pages when an action has been performed (i.e. delete/update actions). Examples of this in the screenshots below.

<details><summary><b>Confirmation Messages</b></summary>

![Review Created Success](readme/assets/images/review_created_success.png)
![Review Deleted Success](readme/assets/images/review_deleted_success.png)
</details><br/>

### Future Features

* Add more automated testing
* Add 'current page is active' in navbar
* Search reviews functionality from the navbar
* Information in the about section how many reviews each reviewer has made
* Add / remove genre and category in admin section
* Add image resize functionality
* Remove admin approval of comments

[Back to top](<#table-of-content>)

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks & Software
* [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
* [Django](https://www.djangoproject.com/) - A model-view-template framework used to create the Review | Alliance site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe.
* [Microsoft Excel](https://www.microsoft.com/sv-se/microsoft-365/excel) - Used to create testing scenarios.
* [Github](https://github.com/) - Used to host and edit the website.
* [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
* [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used for responsiveness check.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Used to validate the sites accessibility.
* [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - Used to test color contrast on the site
* [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) - Used to create a *.dot file of all models in the project.
* [dreampuf](https://dreampuf.github.io/GraphvizOnline/) - Creates visually appealing database diagrams of *.dot files.
* [Favicon](https://favicon.io/) - Used to create the favicon.
* [VSCode](https://code.visualstudio.com/) - Used to create and edit the site.
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.
* [Trello](https://trello.com/en-GB) - A project management tool to organize the project.
* [Cloudinary](https://cloudinary.com/) - A service that hosts all static files in the project.
* [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
* [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
* [PEP8 Validation](http://pep8online.com/) - At the time for deploying this project the PEP8 Online Validaton service was offline, therefore not used.
* [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code

## Libraries

[Back to top](<#table-of-content>)

The libraries used in this project are located in the requirements.txt file and have been documented below

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
* [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload and manage your cloud's assets.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
* [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Used to integrate Django DRY forms in the project.
* [django-extensions](https://pypi.org/project/django-extensions/) - Django Extensions is a collection of custom extensions for the Django Framework.
* [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
* [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
* [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
* [pylint-django-2.5.3](https://pypi.org/project/pylint-django/) - A Pylint plugin for improving code analysis when analysing code using Django.
* [pylint-plugin-utils-0.7](https://pypi.org/project/pylint-plugin-utils/) - This is not a direct Pylint plugin, but rather a set of tools and functions used by other plugins such as pylint-django.
* [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
* [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - P    rovides first-class OAuth library support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
* [cryptography-3.3.23](https://pypi.org/project/cryptography/3.3/) - Cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Testing

## Testing User Stories

* As a Site User | I can view a list of the music reviews so that I can select one to read
    * At the top of the site there is a navigation bar with a link that lists all reviews when the user clicks on it.

* As a Site User | I can view a list of the concert reviews so that I can select one to read
   * At the top of the site there is a navigation bar with a link that lists all concert reviews when the user clicks on it.

* As a Site User | I can click on a specific review so that I can read it in detail
   * At the top of the site there is a navigation bar with a link that lists all album reviews when the user clicks on it.

* As a Site User | I can like and unlike a review so that it is possible for me to interact with the review
    * When the user is logged it is possible to click on a heart on the review detail page to like / unlike a review.

* As a Site User | I can view the number of likes on each review so that I can see how popular a specific review is
    * On the review detail page the user can see how many likes the specific review has.

* As a Site User | I can contact Review Alliance in an easy way so that I can interact with them if I have a need for it
    * In the footer there is clear information about how to contact Review | Alliance.

* As a Site User | I can navigate easy on the site through paginated list of posts so that I feel comfortable using the site
    * On the review pages the pagination is activated when there are more than 6 reviews on a page.

* As a Site User | I can view comments on a specific review so that I can read the conversations between different users on the site
    * When the user clicks on a specific review the comment section can, in an easily way, be viewed.

* As a Site User | I can sign up an account so that I can like and comment on reviews, create a profile page, create own reviews and edit / remove my reviews
    * In the navigation bar the user can click the Login / Sign up link to either login or sign up for a new account. When this is done the user can interact on the page as stated in the user story).

* As a Site User | I can create a profile page so that other reviewers can read about who I am
    * If a user is registered and logged in there is a 'Show Profile'-page in the navigation menu where the user can fill in profile details. The profile is shown for the site users in the about section.

* As a Site User | I can comment on a review so that I can be involved in the conversation
    * When the user is logged in they can write a comment on a specific review on the review detail page.

* As a Site User | I can edit my comment so that I can change the content if needed
    * When the user is logged in an edit button appears on the all comments that the specific user has written. When the user clicks the edit button they can change the content in the comment.

* As a Site User | I can remove my review so that I have full control of my reviews
    * When the user is logged in a delete button appears on the all comments that the specific user has written. When the user clicks the delete button they get the option to delete the comment.

* As a Site User | I can choose to see my own reviews so that I can find them easily
    * When a user is logged in they can choose to view their own reviews through the link 'My Reviews'.

* As a Site User | I can create a new review so that I can contribute to with new content to Review Alliance
    * When a user is logged in they can create a new review through the 'Create New Review'-link in the navigation bar.

* As a Site User | I can log out from the site so that I can feel safe that nobody can access my information
    * When the user is logged in it is possible to choose the 'Log Out'-option in the navigation menu.

* As a Site User | I can create draft reviews so that I can finish writing the content later
    * When a logged in user creates a review they have the possibility to set the status on the review either on published or draft.

* As a Site User | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page
    * When the user sign in, sign out, create / update / deletes reviews and comments they always get a confirmation message to secure visual feedback.

* As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information
   * When the admin is logged in it is possible to choose the 'Log Out'-option in the navigation menu.

* As a Site Admin | I can create, read, update and delete reviews so that I can manage my review content
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can read, update and delete reviews. Creation of reviews can be made the same way as any logged in user. Updating reviews can only be made if the administrator has written the original review.

* As a Site Admin | I can approve reviews so that I can secure high quality of the content
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can approve / unapprove / publish / unpublish reviews.

* As a Site Admin | I can approve and disapprove comments so that I can secure a safe environment for the Site Users
    * When the user is logged in as an administrator / superuser a new item show up in the navigation menu called 'Admin Area'. In this area the user can approve / unapprove comments.

* As a Site Admin | I can create draft reviews so that I can finish writing the content later
    * When a user is logged in as an administrator they have the possibility to create a review they and set the status to published or draft.

* As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts
    * In the admin area there is an summary area in the top with general information about the site (i.e. number of users, number of reviews / comments that need approval)

* As a Site Admin | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page
    * When the admin signs in, signs out, create / update / deletes reviews and comments they always get a confirmation message to secure visual feedback.

## Code Validation
The code on the 'Review | Alliance' site has been tested through W3C Markup Validation Service, W3C CSS Validation Service and JSHint. Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed (see bugs section). One error appeared as well in the W3C CSS Validation but that was connected to Font Awesome and not to the site code itself (see bugs section).

### Markup Validation
After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned.

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
At the time of this project the website [pep8online](http://pep8online.com/) is currently offline. Usually I'm using that site to validate my Python code. Due to the site being offline I have followed Code Institutes workaround to add the PEP8 validator 'pycodestyle' to the Gitpod Workspace. I have tested the following Python files:

* admin.py - No errors or warnings reported
* forms.py - No errors or warnings reported
* models.py - No errors or warnings reported
* test_forms.py - No errors or warnings reported
* urls.py - No errors or warnings reported
* views.py - No errors or warnings reported

[Back to top](<#table-of-content>)

### JavaScript Validation
The JSHint validator results can be seen below:

No errors were returned when passing through JSHint (script.js) but the test reported one undefined variable connected to Bootstrap which is no problem.

<details><summary><b>JSHint Validation Result</b></summary>

![JSHint Validation](readme/assets/images/js_hint_validation.png)
</details><br/>

[Back to top](<#table-of-content>)

## Additional Testing

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | Clicking the Log In / Sign Up loads the sign up page
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the details view the user cannot create a comment
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the detail view the logged in user can comment a review
| &check; | When user submits a comment a message with approval information is being showed on the page
| &check; | In the detail view the logged in user can update/delete the comments written by themselves
| &check; | Clicking the update button loads the update comment page
| &check; | Clicking the delete button loads the delete comment page
| &check; | In the detail view the logged in user can like/unlike reviews
| &check; | In the detail view the logged in user can update/delete the reviews written by themselves
| &check; | Clicking the update button in the detail view loads the update review page
| &check; | Clicking the delete button in the detail view loads the delete review page
| &check; | Clicking the My Reviews button in the logged in user menu lists the logged in users reviews
| &check; | Clicking the update button in the My Reviews view loads the update review page
| &check; | Clicking the delete button in the My Reviews view loads the delete review page
| &check; | In the My Reviews view the information about the review status is correct
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the Show Profile Page button in the logged in user menu loads the My Profile page
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | Clicking the Admin Area button in the logged in user menu loads the Admin Area Page
| &check; | In the review section. Clicking the approve / unapprove / publish / unpublish toggles the approve and status signs
| &check; | The view button is only visible if a review is published
| &check; | In the comment section. Clicking the approve / unapprove toggles the approve and status signs
| &cross; | When clicking delete / add genre the appropiate page loads and shows success page after submit
| &check; | Total Users shows correct number of total users
| &check; | Total Reviews shows the correct number of total reviews
| &check; | Total Comments shows the correct number of total comments
| &check; | Reviews that need approval shows the correct numer of reviews that need approval
| &check; | Comments that need approval shows the correct numer of comments that need approval

 Status | **Create A Review - User Logged In**
|:-------:|:--------|
| &check; | Title field is required
| &check; | Title field does not accept empty field
| &check; | Title field does not accept just spaces
| &check; | Artist field is required
| &check; | Artist field does not accept empty field
| &check; | Artist field does not accept just spaces
| &check; | Featured Image is not required
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Body field is required
| &check; | Body field does not accept empty field
| &check; | Category field defaults to Uncategorized
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Record Label is not required
| &check; | Venue is not required
| &check; | Genre field defaults to Uncategorized
| &check; | Rating field defaults to 3
| &check; | Status field defaults to Draft
| &check; | Posting as shows name of logged in user
| &check; | Review Success Page is displayed when the user submits the review and the form validation is ok.

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field does not accept empty field
| &check; | Success flash message is displayed when the user submits the create a new user form
| &check; | Default biography is visible in about page (with i.e default featured image)

Status | **Create A Profile Page - User Logged In**
|:-------:|:--------|
| &check; | Default featured image is visible the first time a user opens the 'my profile' page
| &check; | First Name field is required
| &check; | First Name field does not accept empty field
| &check; | First Name field does not accept just spaces
| &check; | Last Name field is required
| &check; | Last Name field does not accept empty field
| &check; | Last Name field does not accept just spaces
| &check; | Update profile success Page is displayed when the user submits the profile form

### Automated Testing
Some automated testing has been done during this project. Due to prioritization of other tasks I only could provide 34% coverage. See screenshot below. Automated tests can be run by typing the command - *python3 manage.py test*

<details><summary><b>Automated Testing</b></summary>

![Automated Testing](readme/assets/images/test_coverage_report.png)
</details><br/>

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-content>)

### Browser Compatibility
* Google Chrome Version (106.0.5249.119)
* Mozilla Firefox (version 105.0.3)
* Min (version 1.26.0)
* Apple Safari (version 16.0)
* Microsoft Edge (version 106.0.1370.47)

[Back to top](<#table-of-content>)

### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the *index page*, *review details page*, *the admin area* and *the about page*. The testing showed the following:

* Index Page - Performance: 75, Accessibility: 100, Best Practises: 100, SEO: 92
* Review Details Page - Performance: 81, Accessibility: 98, Best Practises: 100, SEO: 92
* Admin Area - Performance: 85, Accessibility: 97, Best Practises: 100, SEO: 100
* About page - Performance: 73, Accessibility: 98, Best Practises: 100, SEO: 100

In general this is OK results. The performance is affected in a negative way by external scripts (connected to i.e. Bootstrap) and the lower result on SEO on the Index page and Admin Area Page is i.e. connected to the 'read more' links that is not a 100% optimal description from a SEO point of view. The lower accessibility result on the review details page is connected to the heading elements not being in sequentially-descending order, but this is an active design choice and not a big issue (but I thought it would be proper to highlight it here so that it's clear I'm aware of it).

<details><summary><b>Lighthouse Index Result</b></summary>

![Lighthouse Index Result](readme/assets/images/lighthouse_index.png)
</details><br/>

<details><summary><b>Lighthouse Review Details Page Result</b></summary>

![Lighthouse Review Details Page](readme/assets/images/lighthouse_review_details_page.png)
</details><br/>

<details><summary><b>Lighthouse Admin Area Result</b></summary>


![Lighthouse Admin Area Result](readme/assets/images/lighthouse_admin_area.png)
</details><br/>

<details><summary><b>Lighthouse About Page Result</b></summary>

![Lighthouse About Page Result](readme/assets/images/lighthouse_about.png)
</details><br/>


### WAVE
[WAVE](https://wave.webaim.org/) was used to check accessibility. 0 errors were found.

<details><summary><b>WAVE Result</b></summary>

![WAVE Result](readme/assets/images/wave_result.png)
</details><br/>

### a11y Color Contrast Accessibility Validator
[a11y](https://color.a11y.com/Contrast/) was used to check the color contrast accessibility. 0 errors were found.

<details><summary><b>a11y Result</b></summary>

![a11y Result](readme/assets/images/a11y_contrast_test.png)
</details><br/>

[Back to top](<#table-of-content>)

### Peer Review
Additional testing of the application was conducted by people outside of the software development field. Some smaller spelling and grammar errors were found and corrected. No issues connected to design or handling of the site.

## Known bugs
No known bugs besides those in the fixed / unfixed bugs section.

### Fixed Bugs
**2022-10-10**
* Bug: When updating a review or comment the approved variable did not get updated to 'False'. This is is now handled and fixed.

**2022-10-11**
* Bug: When updating a review the slug did not change. I chose to fix this bug so that the slug updates when a review is updated but one 'school' within this area says that a slug never should be changed (due to problems with urls / linking in the future). This functionality is an easy fix to remove if necessary but I chose to keep it for now.

**2022-10-14**
* Bug: When the Markup Validation was done there was initially quite a lot of errors. The debugging process was very straight forward and the errors could easily be fixed.

<details><summary><b>HTML Validation</b></summary>

![HTML Validation](readme/assets/images/html_validation_error.png)
</details><br />

**2022-10-17**
* Bug: The CSS Validation reported an error that is connected to Font Awesome. When I validate my own CSS code there are no errors at all. So this might be a Font Awesome bug that is out of my control. But I thought it would be proper to highlight the error here in the bugs section.

<details><summary><b>CSS Validation</b></summary>

![CSS Validation](readme/assets/images/css_validaton_error.png)
</details><br />

### Unfixed Bugs

**2022-10-14**
* Bug: Summernote is not working 100% properly. I have debugged and sweeped the Internet for solutions. The issue is that when a user creates a review it's not possible to overide the choices the user makes when writing the review (i.e. font-size and font). I tried to handle this by setting rules of what tools to show in the Summernote editor without success. One workaround could of course be to remove the Summernote functionality but I did not want to do that in this project at least. This bug is still unfixed and I haven't found a solution to it yet.

**2022-10-15**
* Bug: 2 warning / issues reported in the Google Chrome DevTools console. The first one is connected to a navigator.userAgent issue and the second to usage of a deprecated feature. I have done some digging and it seems that these issues have been reported within different forums on the web. I have checked other browsers (i.e. Firefox, Min and Edge) and the issue does not show up there.

<details><summary><b>Warnings from Google Chrome DevTools</b></summary>

![HTML Validation](readme/assets/images/google_chrome_warning.png)
</details><br />

[Back to top](<#table-of-content>)

# Deployment

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). To deploy a project, these are the steps:

1. Begin by creating a GitHub repository using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template). Navigate to the template and select 'Use this template'.

<details><summary><b>Heroku Deployment - Step 1</b></summary>

![Heroku Deployment Step 1]()
</details><br />

2. Complete the necessary details as shown in the provided image, then click 'Create Repository From Template'.

<details><summary><b>Heroku Deployment - Step 2</b></summary>

![Heroku Deployment Step 2]()
</details><br />

3. After the repository is created, click on 'Gitpod' as indicated in the picture.

<details><summary><b>Heroku Deployment - Step 3</b></summary>

![Heroku Deployment Step 3]()
</details><br />

4. Install Django by entering this command:

* ```pip3 install Django~=4.2.1```

<details><summary><b>Heroku Deployment - Step 4</b></summary>

![Heroku Deployment Step 4]()
</details><br />

5. Generate a requirements file using the following command:

* ```pip3 freeze --local > requirements.txt``` - This will create the requirements.txt file and adds required libraries to it. This command needs to exectuted every time a new libary gets added to the project.

<details><summary><b>Heroku Deployment - Step 5</b></summary>

![Heroku Deployment Step 5](readme/assets/images/heroku_05.png)
</details><br />

6. Create your project:

* ```django-admin startproject YOUR_PROJECT_NAME .``` - "YOUR_PROJECT_NAME" is the name you choose for your project.

<details><summary><b>Heroku Deployment - Step 6</b></summary>

![Heroku Deployment Step 6](readme/assets/images/heroku_06.png)
</details><br />

7. Create your application using:

* ```python3 manage.py startapp APP_NAME``` - This will create your application with the name "APP-NAME"

<details><summary><b>Heroku Deployment - Step 7</b></summary>

![Heroku Deployment Step 7](readme/assets/images/heroku_07.png)
</details><br />

8. Add your local server to "ALLOWED_HOSTS" in the settings.py file. For this you need to run the command

* ```python3 manage.py runserver``` - This runs the server. This will give you an error message "DisallowedHost at /", following the link of your local server. Copy this link and add it in your settings.py file.
* While in the settings.py file, also add your newly created app in the "INSTALLED_APPS" section at the bottom of the list. In the picture, the first app is called "APP".

<details><summary><b>Heroku Deployment - Step 8</b></summary>

![Heroku Deployment Step 8](readme/assets/images/heroku_08.png)
</details><br />

9. To get the code ready for deployment, gunicorn needs to be installed and added to the requirements with the following commands:

* ```pip3 install gunicorn~=20.1``` - This installs gunicorn
* ```pip3 freeze --local > requirements.txt``` - This will add gunicorn to the requirements.txt file

<details><summary><b>Heroku Deployment - Step 9</b></summary>

![Heroku Deployment Step 9]()
</details><br />

10. Create a file in the root directory named "Procfile" and add the nessesary lines to the settings.py file:

- Procfile:
* ```web: gunicorn "proejec_name".wsgi``` - "project_name" stands for the name of your project
- settings.py:
* ```DEBUG = False``` - This is the debug line in the settings.py file. It is very important that debug is never set to "True" on a deployed webpage for security reasons. While in development, DEBUG should be set to "True"
* ```,'.herokuapp.com'``` needs to be added to the "ALLOWED_HOSTS" section in the settings.py file, so that heroku has the permission to access the project.

<details><summary><b>Heroku Deployment - Step 10 - Procfile</b></summary>

![Heroku Deployment Step 10 - Procfile]()
</details><br />

<details><summary><b>Heroku Deployment - Step 10 - settings.py</b></summary>

![Heroku Deployment Step 10 - settings.py]()
</details><br />

11. Now it is time to create the application on Heroku:

* Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

* In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

<details><summary><b>Heroku Step 11</b></summary>

![Heroku Step 11]()
</details><br />

12. On Heroku, enter a unique application name, choose your region, and click 'Create app':

<details><summary><b>Heroku Step 12</b></summary>

![Heroku Step 12]()
</details><br />

13. Add a Postgres database, which is created with the Code Institute link for [PostgresSQL](https://dbs.ci-dbs.net/) from the LMS and add it to your app via the Settings tab on Heroku:

* Press "Reveal Config Vars" and add "DATABASE_URL" as key and enter the postgres URL, which has been sent by email, as the value.
* Addistionally, add the "DISABLE_COLLECTSTATIC" key with a value of "1" as a second config var. This is nessesary for the later implementation of the Cloudinary API.

<details><summary><b>Heroku Step 13</b></summary>

![Heroku Step 13]()
</details><br />

14. In GitPod, create an env.py file in the top-level directory with the following content:

* ```import os``` - This imports the os library
* ```os.environ("DATABASE_URL", "postgres://*********************")``` - This sets database variable to your PostgresSQL database.
* ```os.environ("SECRET_KEY", "actual_secret_key")``` - You can create your own key with a webpage like [RandomKeyGen](https://randomkeygen.com/).
* if using the Code Institute template, the env.py file should already be in the "gitignore" file, if not, it has to be added manually.

<details><summary><b>Heroku Step 14</b></summary>

![Heroku Step 14]()
</details><br />

15. Add your secret key to Heroku's Config Vars:

<details><summary><b>Heroku Step 15</b></summary>

![Heroku Step 15]()
</details><br />

16. In settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

<details><summary><b>Heroku Step 16</b></summary>

![Heroku Step 15]()
</details><br />

17. Replace the insecure secret key in settings.py with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

<details><summary><b>Heroku Step 17</b></summary>

![Heroku Step 17]()
</details><br />

18. Comment out the old database settings and add the link to DATABASE_URL since the project does not use the standart sqlite3 database. 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

<details><summary><b>Heroku Step 18</b></summary>

![Heroku Step 18]()
</details><br />


18. Save all your fields and migrate the changes with the following commands:

```python3 manage.py migrate```

19. Set up Cloudinary for static file storage: After creating a Cloudinary account, you can copy the API Environment Variable from the Cloudinary dashboard.

20. In the env.py file, add the Cloudinary url (it's very important that the url is unaltered):

```os.environ.setdefault("CLOUDINARY_URL", "cloudinary://*********************************")```

21. In the Config Vars of heroku, add the Cloudinary url (CLOUDINARY_URL as the key, the actual url as the value). 

<details><summary><b>Heroku Step 21</b></summary>

![Heroku Step 21]()
</details><br />

22. In the settings.py file, the Cloudinary Libraries have to be added to the installed apps. The correct order is very important.

<details><summary><b>Heroku Step 22</b></summary>

![Heroku Step 22]()
</details><br />

23. In the bottom of settings.py, add additional settings for static file management:

<details><summary><b>Heroku Step 23</b></summary>

![Heroku Step 23]()
</details><br />

24. The next step is to link the file to the Heroku templates directory:

<details><summary><b>Heroku Step 24</b></summary>

![Heroku Step 24]()
</details><br />

25. Now edit the templates directory to "TEMPLATES_DIR" in the teamplates array.

<details><summary><b>Heroku Step 25</b></summary>

![Heroku Step 25]()
</details><br />

26. Some more files are needed before deploying:

* Create 2 folders in the top level directory: **static** and **templates**
* The **static** folder will include all CSS and JS files as well as images.
* The **templates** folder will include the "base.html" file, as well as all django related templates.

27. Make sure that all the files are saved, then enter the following lines in the console for the first commit and push to Github:

* ```git add .```
* ```git commit -m "Deployment commit"```
* ```git push```

30. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

31. Scroll down to the manual deployment section and click 'Deploy Branch'.

<details><summary><b>Heroku Step 31</b></summary>

![Heroku Step 31](readme/assets/images/heroku_31.png)
</details><br />

The live link to the 'PROject GOLFblog' site on Heroku an be found [here](https://project-golfblog-96e6107b0f52.herokuapp.com/). And the Github repository can be found [here](https://github.com/Mienjung97/PROject-GOLFblog).

[Back to top](<#table-of-content>)

## How To Fork The Repository On GitHub

It is possible to do a independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

<details><summary><b>Github Fork</b></summary>

![Fork](readme/assets/images/github_fork.png)
</details><br />

[Back to top](<#table-of-content>)

## Cloning And Setting Up This Project

To clone and set up this project you need to follow the steps below.

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

<details><summary><b>Github Create Local Clone</b></summary>

![Clone](readme/assets/images/github_clone_01.png)
</details><br />

5. To be able to get the project to work you need to install the requirements. This can be done by using the command below:

* ```pip3 install -r requirements.txt``` - This command downloads and install all required dependencies that is stated in the requirements file.

6. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.

<details><summary><b>Setup env.py</b></summary>

![Clone](readme/assets/images/github_clone_02.png)
</details><br />

[Back to top](<#table-of-content>)

# Credits

## Content

* All text content written by Marcus Eriksson.

* Test concert images on review cards taken from [Shutterstock](https://www.shutterstock.com/sv)

* Test album images on review cards taken from [Kollektiv Fem](https://www.kollektivfem.se) which is owned by Marcus Eriksson.

* Featured default review image taken from [FAVPNG](https://favpng.com/png_view/download-clip-art-png/hHNmGh4R)

* Template for read.me provided by Code Institute (*with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/))* suggested.

## Technical

* Inspiration regarding UpdateView taken from [Learn Django Class Based Views](https://www.youtube.com/watch?v=EUUjJdw3EBM)

* Formatting date format [Formatting Date, Time, and Numbers in Django Templating](https://collinshillary1.medium.com/formatting-date-time-and-numbers-in-django-templating-f53fea027a06)

* Inspiration regarding CSS code to add circle around text [How to Add a Circle Around a Number in CSS](https://www.w3docs.com/snippets/css/how-to-add-a-circle-around-a-number-in-css.html)

* Inspiration regarding adding extra forms in Django Allauth form [How to add more custom fields on signup form?](https://stackoverflow.com/questions/68591755/django-allauth-how-to-add-more-custom-fields-on-signup-form)

# Acknowledgements
This fictional site was created for Portfolio Project #4 (Full-Stack Tolkin) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net). I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for relevant feedback during the project.

*Marcus Eriksson, 2022-10-18*

[Back to top](<#table-of-content>)