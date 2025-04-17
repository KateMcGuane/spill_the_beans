# :coffee: *Spill The Beans* :coffee:

Spill The Beans is a ficticious coffee blog. It is the ultimate online destination for coffee enthusiasts, connoisseurs, and casual sippers alike. Whether you're a seasoned barista, a home-brewing hobbyist, or someone just starting their coffee journey, our blog offers something for everyone who loves the rich, aromatic world of coffee.

![Spill The Beans](https://spill-the-beans-coffee-blog-8f04f8c6207f.herokuapp.com/)

## User Experience

### Target Audience
The target audience for this coffee blog is for those who is passionate about coffee and eager to deepen their knowledge. It appeals to a variety of people who have different levels of interest, knowledge or skills. The blog aims to enrich readers' understanding of coffee and foster a community of like-minded individuals who share this interest.


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


---


## UX Design

### Colour Scheme

### Typography

### Imagery
- ![Default](https://unsplash.com/s/photos/coffee-beans?license=free)

### Favicon

### Wireframes

#### Page1
#### Page2
#### Page3

### Database Design: Entity-Relationship Diagram (ERD)


---


## Features


---


## Technologies Used

  ### Languages

  - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - To add content & structure.
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - To add the styles and layout of the site.
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [Python](https://www.python.org/)


  ### Database

  - [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) was used as the PostgreSQL database for this project.
  - [Heroku App](https://www.heroku.com/)


  ### Frameworks
  - [Django](https://www.djangoproject.com/) - Version 4.2.18 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - [Bootstrap](https://getbootstrap.com/) - Version 5.0.1 - A framework for building responsive, mobile-first sites.


  ### Libraries & Packages

  - [Font Awesome](https://fontawesome.com/) - For icon creation.
  - [Google Fonts](https://fonts.google.com/) - To extract fonts for the website.
  - [gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server
  - [psycopg2](https://pypi.org/project/psycopg2/) - a postgres database adapter which allow us to connect with a postgres database


  ### Programs

  - [Am I Responsive?](http://ami.responsivedesign.is/) - To demonstrate the website on a range of devices.
  - [Balsamiq](https://balsamiq.com/) - To create wireframes.
  - [Canva](https://www.canva.com/) - To create favicon image.
  - [Chat GPT](https://chat.openai.com/) - To create written content & general consultation when troubleshooting.
  - [Coolors](https://coolors.co/) - To create colour palettes.
  - [Diffchecker](https://www.diffchecker.com/text-compare/) - Used for debugging & troubleshooting.
  - [DrawSQL.app](https://drawsql.app/) - Used to create the database schema.
  - [Favicon.io](https://favicon.io/favicon-converter/) - To convert favicon image into suitable sizes.
  - [Git](https://git-scm.com/) - For version control.
  - [GitHub](https://github.com/) - To store associated files & developments of the website.
  - [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - For troubleshooting and testing features, styling and responsiveness.
  - [Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.
  - [VS Code](https://code.visualstudio.com/) - IDE used for this project via Github.


  ### Stripe

  [Stripe](https://stripe.com/ie) has been used in the project to implement the payment system.

  Stripe for the website is currently in developer mode, which allows us to be able to process test payments to check the function of the site.

  | Type | Card No | Expiry | CVC | ZIP |
  | :--- | :--- |:--- | :--- | :--- |
  | Success| Visa | 4242 4242 4242 4242 | A date in the future | Any 3 digits | Any 5 digits |
  | Require authorisation | 4000 0027 6000 3184 | A date in the future | Any 3 digits | Any 5 digits |
  | Declined | 4000 0000 0000 0002 | A date in the future | Any 3 digits | Any 5 digits |


 ### Web-Based Services
  - [Lucid Chart](https://www.lucidchart.com/pages/) - To create Entity-Relationship Diagram.
  - [Raw Pixel](https://www.rawpixel.com/) - For images.
  - [Unsplash](https://unsplash.com/) - For images.


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
  2. The email confirmation sent will hold the URL for the Code Institute Postgres Database server.
  3. The email will contain a link for managing your databases.

  ##### Heroku App Setup
  1. Set up the Heroku app from the inital setup.
  2. Open the settings tab and create a new config var of DATABASE_URL and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

  ##### Preparation for Deployment with VS Code
  [Consult](https://github.com/kera-cudmore/seaside-sewing/blob/main/README.md)

  ##### Generate a SECRET KEY & Updating Debug
  [Consult](https://github.com/kera-cudmore/seaside-sewing/blob/main/README.md)


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
  | Blog | [Amber Everywhere](https://ambereverywhere.com/best-coffee-shops-in-cork-city-ireland/) | "11 Best Coffee Shops In Cork, Ireland (2024)" |
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
  | Recipe | [BBC Good Food](https://www.bbcgoodfood.com/recipes/coffee-cake) | "Coffee Cake" |
  | | [BBC Good Food](https://www.bbcgoodfood.com/recipes/coffee-cocktails) | "The Ultimate Coffee Cocktail" |
  | | [ChatGPT](https://chat.openai.com/) | "The Dalgona Coffee Craze: How to Make This Frothy Delight at Home" |
  | | | "The Ultimate Coffee Cocktail" (Introduction) |
  | | [SuperValu](https://supervalu.ie/recipes/classic-irish-coffee) | "Classic Irish Coffee" |

  All external references used in this project are for educational purposes only. Any ownership of referenced materials belongs solely to the parties accredited above, or where otherwise stated by said parties. 


  #### Template & README

  - The terminal function & template for the deployable application was created by Code Instutute for their [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template).
  - The introduction for the README file was generated by [Chat GPT](https://chatgpt.com).
  - Some instructions for deployment were taken from the Code Institute course material.


### Markup

  The markup outline for this project was taken from the following README files:
  - [Kate McGuane / nine-lives](https://github.com/KateMcGuane/nine-lives).
  - [Kera Cudmore / BookWorm](https://github.com/kera-cudmore/BookWorm?tab=readme-ov-file).
  - [Kera Cudmore / seaside-sewing](https://github.com/kera-cudmore/seaside-sewing) - for README.md & TESTING.md.
  - [rockroman / CI_PP4-Knowledge-Flow](https://github.com/rockroman/CI_PP4-Knowledge-Flow/blob/main/README.md) - for README.md & TESTING.md.


###  Acknowledgments

  - Thank you to my mentor, cohort leader, CI tutoring & extended team for your support and understanding during this project.
  - To Mikhail, and my family, thank you for your continued support.


---


Developed by Kate McGuane for Code Institute Portfolio Project 4: Full-Stack Toolkit, 2025