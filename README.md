# :coffee: *Spill The Beans* :coffee:

Spill The Beans is a ficticious coffee blog. It is the ultimate online destination for coffee enthusiasts, connoisseurs, and casual sippers alike. Whether you're a seasoned barista, a home-brewing hobbyist, or someone just starting their coffee journey, our blog offers something for everyone who loves the rich, aromatic world of coffee.

The deployed site, [Spill The Beans](https://spill-the-beans-coffee-blog-8f04f8c6207f.herokuapp.com/).

## User Experience

### Target Audience
The target audience for this coffee blog is for those who are passionate about coffee and eager to deepen their knowledge. It appeals to a variety of people who have different levels of interest, knowledge or skills. The blog aims to enrich readers' understanding of coffee and foster a community of like-minded individuals who share this interest.


### User Stories

  #### First Time Visitor
  As a first time visitor I want to:
  - easily understand what the blog is about, so that I can quickly decide if the content is relevant to me.
  - navigate the site with ease.
  - register an account.
  - learn more about coffee.

  #### Return Visitor
  As a return visitor I want to:
  - quickly find new content since my last visit, so that I can stay up-to-date with the blog.
  - easily filter blog posts to find articles I've not yet read.
  - comment on existing blog entries.
  - intuitive submission process, so that I can easily contribute to the website with a blog entry of my own.
  - connect with other users of the blog site via social media.

  #### Admin
  As site admin I want to:
  - enhance user experience.
  - grow and engage the audience.
  - screen all blog entries and comments before publication.
  - ensure community guidelines are being upheld.


### Agile

As the project progressed through various stages of development, the Agile methodology became increasingly valuable. The iterative nature of Agile allowed me to adapt quickly to changes, refine features based on ongoing feedback, and better manage time across development sprints. Each iteration served not just as a milestone, but as an opportunity to reflect, reassess, and re-prioritise tasks according to evolving project needs.

Throughout the process, I relied extensively on structured notes and task tracking to maintain continuity between sessions. These notes acted as a critical anchor, helping me resume work efficiently and stay focused on immediate priorities without losing sight of the broader project scope.

By the project's completion, my understanding of Agile had grown considerably. I now feel much more confident in applying Agile to future projects, particularly in terms of managing scope, setting realistic goals, and maintaining momentum over time.


For a detailed look at how I implemented Agile practices during development, please see my [Github Projects](https://github.com/users/KateMcGuane/projects/3/views/1).

---


## Design

  ### Colour Scheme

  The following are the majority of colours that were used for this website design. The first colour palette ofrmes the lighter, more subtle colours for optimal contrast against the darker. The second colour palette showcases a selection of rich earthy tones. Both palettes reflect the theme of the page are in keeping with the colours found in the imagery.
  
  <br>

  ![Coffee Colour Palette 1](documentation/readme/design/coffee-palette-light.PNG)
  ![Coffee Colour Palette 2](documentation/readme/design/coffee-palette-rich.PNG)

  Both colour palettes were created using the [Coolors](https://coolors.co/) website.

  ### Typography

  ![Poppins](documentation/readme/design/poppins.PNG)

  This is a legible, sans serif font with many varieties of weight to choose from. It is versatile and accomodates all structural styling needs. It is a very accessible font, and easy to read. This is used for more word heavy content sections of the website.

  ![Półtawski Nowy](documentation/readme/design/półtawski-nowy.PNG)

  - This is a more stylised font that was used for features such as the title in the navbar. A different font was chosen so the name of the website stood out from the rest of the text.

  - Both fonts were sourced from [Google Fonts](https://fonts.google.com/).


  ### Imagery
  Images for this project were sourced from [Unsplash](https://unsplash.com/s/photos/coffee-beans?license=free).


### Wireframes

#### About
![About Desktop](documentation/readme/wireframes/about-desktop.png)
![About Tablet](documentation/readme/wireframes/about-tablet.png)
![About Mobile](documentation/readme/wireframes/about-mobile.png)

#### Blog Home
![Blog Desktop](documentation/readme/wireframes/blog-desktop.png)
![Blog Tablet](documentation/readme/wireframes/blog-tablet.png)
![Blog Mobile](documentation/readme/wireframes/blog-mobile.png)

#### Blog Detail
![Blog Detail Desktop](documentation/readme/wireframes/blog-detail-desktop.png)
![Blog Detail Tablet](documentation/readme/wireframes/blog-detail-tablet.png)
![Blog Detail Mobile](documentation/readme/wireframes/blog-detail-mobile.png)

#### Contact Form
![contact Form Desktop](documentation/readme/wireframes/contact-form-desktop.png)
![contact Form Tablet](documentation/readme/wireframes/contact-form-tablet.png)
![contact Form Mobile](documentation/readme/wireframes/contact-form-mobile.png)

#### Terms of Use
![Terms of Use Desktop](documentation/readme/wireframes/terms-desktop.png)
![Terms of Use Tabletp](documentation/readme/wireframes/terms-tablet.png)
![Terms of Use Mobile](documentation/readme/wireframes/terms-mobile.png)


#### Login
![Login Desktop](documentation/readme/wireframes/login-desktop.png)
![Login Tablet](documentation/readme/wireframes/login-tablet.png)
![Login Mobile](documentation/readme/wireframes/login-mobile.png)

#### Register
![Register Desktop](documentation/readme/wireframes/register-desktop.png)
![Register Tablet](documentation/readme/wireframes/register-tablet.png)
![Register Mobile](documentation/readme/wireframes/register-mobile.png)


### Database Design: Entity-Relationship Diagram (ERD)

![Spill the Beans ERD](documentation/readme/design/erd-spill-the-beans.png)

  - For this Django project I used the PostgreSQL relational database management system.
  - This outlines where the different databases have relationships to one another through foreign and primary keys. It also highlights isolated databases.
  - On reflection, this could be enhanced further with User as a foreign key for most models displayed here.


---


## Features

| Feature | Detail | Screenshots |
| --- | --- | --- |
**General Features**
| Favicon | This feature was generated from the [Font Awesome 6](https://fontawesome.com/) library and is displayed in the navigation bar. The favicon was converted using [Favicon.io](https://favicon.io/favicon-converter/) to help illustrate the browser tab. |  |
| Navbar | The navbar is a simple design that remains consistent across all pages. On smaller screens a burger icon replaces all navbar items for a clear display that's easy to navigate. |  |
| Footer | The footer is once again simple with social icons. Each icon can be clicked an will open the relative social media platform in another tab. |  |
||||
**Isolated Features**
| Home Page | - Acts as the main blog post page and the general landing page of the site. All blog posts are organised in pagination for clear visibilty. <br> On smaller screens, the pagination is adjusted to render the posts stacked vertically. <br> - There is a "Next" and "Previous" button featured at the end of the page whereby a user can easily navigate to and from the various paginated posts. <br> - When a registered user is logged in, they can comment, edit or delete posts. |  |
| About Page | Gives a description of what the page is about. |  |
| Registration Page | - Simple in design, so as not to confuse the user. <br> -There are a clear set of instructions on how to register. <br> - The user is remined that all fields need to be completed for succesful registration. <br> Once registered the user can engage in all general user CRUD functionality. |  |
| Login Page | - A purely functional and clear page for user to sign in. <br> - There is an active link for those who are not registerd, that will redirect them to the correct page. |  |



  ### Potential Future Developments

  Due to time constraints, I have some remaining features that were not essential to the MVP, however would have been a nice addition to the overall website. The following will be executed in future iterations.

  | Feature | Description |
  | --- | --- |
  | Database | Create stronger relationships through the various models. |
  | Photo Gallery | Featured on the About page in carousel format. |
  | 404 Page | Add custom 404 page. |
  | Recipes | Isolate the blog types into at least two different sections of the blog within the navigation bar. |
  | E-commerce | Integrating e-commerce to the website, selling products that are coffee adjacent. Hopefully this would afford the blog to run ad-free, thereby making it a more enjoyable user experience. |
  | Navigation Bar | With the addition of more offerings to the website, the 'Home' navbar would be replaced with 'Blogs', and separate out the different types of blogs by category. |


  ### Accessibility

  The entire website was designed with a responsive-first ethos in mind. Some best practices implemented were:

   - Using semantic HTML.
   - Good used of colour contrast throughout the website.
   - Use of aria labels where.
   - All pages are responsive for various media screen sizes.


---


## Technologies Used

  ### Languages

  - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - To add content & structure.
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - To add the styles and layout of the site.
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - To give functionality to the features.
  - [Python](https://www.python.org/) - Version 3.12.10


  ### Database

  - [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) was used as the PostgreSQL database for this project.
  - [Heroku App](https://www.heroku.com/) was used to host the site.


  ### Frameworks
  - [Django](https://www.djangoproject.com/) - Version 4.2.18 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - [Bootstrap](https://getbootstrap.com/) - Version 5.0.1 - A framework for building responsive, mobile-first sites.


  ### Libraries & Packages

  - [Cloudinary](https://cloudinary.com/) - Used the cloud-based media management platform to store and handle media files that may be subject to change.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - An extension pack for Crispy Forms, allowing it to render Django forms using Bootstrap 5 styles.
  - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/2.0/) - To build easily customisable forms.
  - [Django Summernote](https://pypi.org/project/django-summernote/) - The rich text editor built for the web, was used to allow users to write and format text in a way that looks similar to how it will appear on the final page.
  - [Font Awesome 6](https://fontawesome.com/) - For up-to-date icon creation (socials & favicon tab).
  - [Google Fonts](https://fonts.google.com/) - To extract fonts for the website.
  - [gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server, was used to help deploy the Django project.
  - [psycopg2](https://pypi.org/project/psycopg2/) - A postgres database adapter which allowed to connect with the postgres database.
  - [White Noise](https://pypi.org/project/whitenoise/) - A solution for serving CSS, JavaScript & static images.

  To view any additional dependencies not mentioned, view requirements.txt


  ### Programs

  - [Balsamiq](https://balsamiq.com/) - To create wireframes.
  - [Canva](https://www.canva.com/) - To create favicon image.
  - [Chat GPT](https://chat.openai.com/) - To create written content & general consultation when troubleshooting.
  - [Coolors](https://coolors.co/) - To create colour palettes.
  - [Diffchecker](https://www.diffchecker.com/text-compare/) - Used for debugging & troubleshooting.
  - [Favicon.io](https://favicon.io/favicon-converter/) - To convert favicon image into suitable sizes.
  - [Git](https://git-scm.com/) - For version control.
  - [GitHub](https://github.com/) - To store associated files & developments of the website.
  - [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - For troubleshooting and testing features, styling and responsiveness.
  - [Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.
  - [VS Code](https://code.visualstudio.com/) - IDE used for this project via Github.


 ### Web-Based Services & Tools

  - [DrawSQL.app](https://drawsql.app/) - Used to create the database schema.
  - [Ezgif.com](https://ezgif.com/maker) - Used to create gif of accumulative images.
  - [ImageResizer.com](https://imageresizer.com/) - To resize & compress images.
  - [Raw Pixel](https://www.rawpixel.com/) - For sourced images.
  - [Stack Overflow](https://stackoverflow.com/) - For troubleshooting.
  - [Unsplash](https://unsplash.com/) - For sourced images.
  - [WAVE](https://chromewebstore.google.com/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) - A Chrome extension used to evaluate web accessibility within the browser.

---

## Deployment & Local Development

  ### Deployment

<details><summary>Initial Heroku Deployment</summary>

  This is how to set up the live site for Heroku using VS Code:

  | Step | Instruction |
  | --- | --- |
  | **Heroku** |
  | 1 | Log in (or sign up) to Heroku. |
  | 2 | Go to the user dashboard & click "Create new app". Keep in mind that each app name on Heroku has to be unique. |
  | 3 | Select the region & click "Create app". |
  | 4 | Go to the settings tab & scroll to the "Config vars" section. |
  | 5 | Click "Reveal Config Vars". |
  | 6 | Create a Config Var, input the required hidden variables (DISABLE_COLLECTSTATIC = 1). |
  | **VS Code** |
  | 7 | Use pip3 to install gunicorn~=20.1 and freeze it to the requirements.txt file. |
  | 8 | In the Procfile, add a command using gunicorn and codestar wsgi file to start the webserver. |
  | 9 | In the project settings.py, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list. |
  | 10 | Git add, commit and push the code to your GitHub repo. |
  | **Heroku** |
  | 11 | Scroll to the “Deployment Method” section.
  | 12 | Click on “Connect to Github”. Search for the repository name & click "Connect".
  | 13 | Scroll to the "Manual Deploys" section.
  | 14 | Click "Deploy Branch". A message will show up to say "Your app was usccessfully deployed. The "View" button will take you to your deployed link.
</details>

  #### Deployment for Developed Site

  ##### Create the Database

  This database was created using [Code Institue's Database Maker](https://dbs.ci-dbs.net/).
  1. Input email to create a database.
  2. The email confirmation sent will hold the URL for the Code Institute PostgresSQL Database server.
  3. The email will contain a link for managing your databases.

  ##### Heroku App Setup
  1. Set up the Heroku app from the inital setup.
  2. Open the settings tab and create a new config var of DATABASE_URL and paste the database URL you copied from PostgresSQL into the value (the value should not have quotation marks around it).

  ##### Preparation for Deployment with VS Code

  - It is on the developers' discretion to ignore steps where they may already have been established.

1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update your requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from PostgreSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-postgres-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. You should now be able to go to the browser tab on the left of the page in PostgreSQL, click the table queries button and see the user you've just created by selecting the auth_user table.

9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
    ```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn coffee.wsgi
    ```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
    ```

14. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

    ```bash
    heroku git:remote -a {app name here}
    git push heroku master
    ```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

  ##### Generate a SECRET KEY & Updating Debug

  1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.

2. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) is an example of a site we could use to create our secret key. Create a new key and copy the value.

3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.

4. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save, add, commit and push these changes.


  ### Local Development

  #### How to Fork

To fork the Spill the Beans repository, to either propose changes or to use as an idea for another website, follow these steps:

  1. Log in (or sign up) to Github.
  2. Go to the repository for this project, [Kate McGuane / spill_the_beans](https://github.com/KateMcGuane/spill_the_beans).
  3. Click the Fork button in the top right of the page.


  #### How to Clone

  To clone the Spill the Beans repository:

  1. Log in (or sign up) to GitHub.
  2. Go to the repository for this project, [Kate McGuane / spill_the_beans](https://github.com/KateMcGuane/spill_the_beans).
  3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
  4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned respository.
  5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
  6. Set up a virtual environment (not applicable for fully managed cloud development environments).
  7. Install the dependencies (packages) from the requirements.txt file by running the following command in the terminal:

  ```bash
pip3 install -r requirements.txt
```


---


## Testing

Please see [TESTING.md](TESTING.md) for a comprehensive list of tests performed.


---


## Credits

### Content

  #### External Resources

  | Entry Type | Sourced From | Entry Title |
  | --- | --- | --- |
  | About Page | [ChatGPT](https://chat.openai.com/) & own content writing | "Welcome to <em>Spill the Beans</em>" |
  | Blog General | [Amber Everywhere](https://ambereverywhere.com/best-coffee-shops-in-cork-city-ireland/) | "11 Best Coffee Shops In Cork, Ireland (2024)" |
  | | [Artemis Blog](https://artemis.coffee/blog/history-of-coffee-top-5-most-influential-people/) | "Inventing Coffee Paper Filter" |
  | | [ChatGPT](https://chat.openai.com/) | "A Brew of Her Own: The Story of Ava Brewster in the World of Coffee" |
  | | | "Coffee Trends 2024" |
  | | | "Essential Coffee Gear and Gadgets: Elevate Your Home Brewing Game" |
  | | | "How Coffee Influences Productivity & Creativity" |
  | | | "La Dolce Vita: My Journey as an Italian Coffee Connoisseur" |
  | | | "The Health Benefits of Coffee: More Than Just a Morning Boost" |
  | | | "The Impact of Climate Change on Coffee Production" |
  | | | "The Industrialization of Coffee" |
  | | | "The Origins of Coffee: From Mystical Beginnings to Global Obsession" |
  | | | "The Story of Coffee: How I Discovered the Magic Beans" |
  | | | "The Ultimate Guide to Coffee Brewing Methods: Finding Your Perfect Cup" |
  | | [National Coffee Association USA Website](https://www.ncausa.org/About-Coffee/What-is-Coffee) | "What is Coffee?" | 
  | Blog Recipe | [BBC Good Food](https://www.bbcgoodfood.com/recipes/coffee-cake) | "Coffee Cake" |
  | | [BBC Good Food](https://www.bbcgoodfood.com/recipes/coffee-cocktails) | "The Ultimate Coffee Cocktail" |
  | | [ChatGPT](https://chat.openai.com/) | "The Dalgona Coffee Craze: How to Make This Frothy Delight at Home" |
  | | | "The Ultimate Coffee Cocktail" (Introduction) |
  | | [SuperValu](https://supervalu.ie/recipes/classic-irish-coffee) | "Classic Irish Coffee" |
  | Terms of Use | [ChatGPT](https://chat.openai.com/) | "Terms of Use" |

  All external references used in this project are for educational purposes only. Any ownership of referenced materials belongs solely to the parties accredited above, or where otherwise stated by said parties.
  Smaller snippets of content such as comments were written by myself.


  ### Documentation

  The following documentation proved useful for troubleshooting attempts and handling specific alterations imposed on the Bootstrap Styling.
  - [How to unstyle anchor when using bootstrap](https://stackoverflow.com/questions/22429881/how-to-unstyle-anchor-when-using-bootstrap)
  - [Bootstrap - Text](https://getbootstrap.com/docs/5.0/utilities/text/#text-decoration)

  #### Template & README

  - The terminal function & template for the deployable application was created by Code Instutute for their [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template).
  - The introduction for the README file was generated by [Chat GPT](https://chatgpt.com).
  - Some instructions for deployment were taken from the Code Institute course material.


### Markup

  The markup outline for this project was taken from the following README and TESTING files:
  - [Kate McGuane / nine-lives](https://github.com/KateMcGuane/nine-lives)
  - [Kera Cudmore / seaside-sewing](https://github.com/kera-cudmore/seaside-sewing)
  - [rockroman / CI_PP4-Knowledge-Flow](https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md)


###  Acknowledgments

  - Thank you to my mentor, cohort leader, CI tutoring & extended team for your support and understanding during this project.
  - To Mikhail, and my family, thank you for your continued support.


---


Developed by Kate McGuane for Code Institute Portfolio Project 4: Full-Stack Toolkit, 2025
