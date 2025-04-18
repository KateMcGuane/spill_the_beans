# Spill The Beans - Testing

Visit the deployed site: [Spill The Beans](https://spill-the-beans-coffee-blog-8f04f8c6207f.herokuapp.com/)

---

All outlined testing was done upon completion of this project. Please see Bugs for any documented errors that occured while the build was in progress.

## Validation Testing

<details>
  <summary>Result Key</summary>
  <table>
    <thead>
      <tr>
        <th>Key</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>:heavy_check_mark:</td>
        <td>Pass</td>
      </tr>
      <tr>
        <td>:x:</td>
        <td>Fail</td>
      </tr>
      <tr>
        <td>:grey_exclamation:</td>
        <td>Minor Error</td>
      </tr>
    </tbody>
  </table>
  </details>


### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. I chose to directly input the html code for each related page into the validator.

| Page | Status | Evidence |
| :--- | :---: | :---: |
| Home |   | [Home Page Validation](ENTER_HTTP_HERE) |
| About |   | [About Page Validation](ENTER_HTTP_HERE) |
| Register |   | [Register Page Validation](ENTER_HTTP_HERE) |
| Login |   | [Login Page Validation](ENTER_HTTP_HERE) |
| 404 |   | [Home Page Validation](ENTER_HTTP_HERE) |
| *Custom* |   | [Custom Page Validation](ENTER_HTTP_HERE) |


### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

| Filepath | Status | Evidence |
| :--- | :---: | :---: |
| static/base.css | | [static/base.css validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |


### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result | Evidence |
| :--- | :---: | :---: |
| file/as/found/in/directory/filename.js | Pass | [filename.js](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| file/as/found/in/directory/filename.js | Pass | [filename.js](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| file/as/found/in/directory/filename.js | Pass | [filename.js](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |


### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

| File | Result | Evidence |
| :--- | :---: | :---: |
| custom_storages.py | Pass | [custom_storages.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **SEASIDE_SEWING** |
| seaside_sewing/settings.py | Pass | [settings.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| seaside_sewing/urls.py | Pass | [urls.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **HOME** |
| home/apps.py | Pass | [apps.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| home/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/home-urls-validation.png)|
| home/views.py | Pass | [views.py validation](documentation/testing/validation/python/home-views-validation.png) |
| home/test_views.py | Pass | [test_views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **PROFILES** |
| profiles/apps.py | Pass | [apps.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| profiles/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/profiles-forms-validation.png) |
| profiles/models.py | Pass | [models.py validation](documentation/testing/validation/python/profiles-models-validation.png) |
| profiles/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/profiles-urls-validation.png) |
| profiles/views.py | Pass | [views.py validation](documentation/testing/validation/python/profiles-views-validation.png) |
| profiles/test_views.py | Pass | [test_views.py validation](documentation/testing/validation/python/profiles-test-views.png) |
| profiles/test_models.py | Pass | [test_models.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **CONTACT** |
| contact/admin.py | Pass |[admin.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| contact/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/contact-apps-validation.png) |
| contact/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/contact-forms-validation.png) |
| contact/models.py | Pass | [models.py validation](documentation/testing/validation/python/contact-models-validation.png) |
| contact/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/contact-urls-validation.png) |
| contact/views.py | Pass | [views.py validation](documentation/testing/validation/python/contact-views-validation.png) |
| contact/test_forms.py | Pass | [test_forms.py validation](documentation/testing/validation/python/contact-test-forms-validation.png) |
| contact/test_models.py | Pass | [test_models.py validation](documentation/testing/validation/python/contact-test-models.png)|
| contact/test_views.py | Pass | [test_views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |


---


## Lighthouse Report

Google's Lightouse was used to test the performance, accessibility, best practices ad SEO of the site.


### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| Products Page | ![Products Desktop Lighthouse Testing](documentation/testing/lighthouse/products-desk-lh-val.png) |
| Product Details Page | ![Product Detail Desktop Lighthouse Testing](documentation/testing/lighthouse/product-detail-desk-lh-val.png) |
| Add Product Page | ![Add Product Desktop Lighthouse Testing](documentation/testing/lighthouse/add-product-desk-lh-val.png) |
| Edit Product Page | ![Edit Product Desktop Lighthouse Testing](documentation/testing/lighthouse/edit-product-desk-lh-val.png) |
| Bag Page | ![Bag Desktop Lighthouse Testing](documentation/testing/lighthouse/bag-desk-lh-val.png) |
| Checkout Page | ![Checkout Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-desk-lh-val.png) |
| Checkout Success Page | ![Checkout Success Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-success-desk-lh-val.png) |
| Profile Page | ![Profile Desktop Lighthouse Testing](documentation/testing/lighthouse/profile-desk-lh-val.png) |
| Contact Us Page | ![Contact Us Desktop Lighthouse Testing](documentation/testing/lighthouse/contact-desk-lh-val.png) |
| Privacy Policy Page| ![Privacy Desktop Lighthouse Testing](documentation/testing/lighthouse/privacy-desk-lh-val.png)  |
| Terms & Conditions Page | ![Terms Desktop Lighthouse Testing](documentation/testing/lighthouse/terms-desk-lh-val.png) |
| Delivery Policy Page | ![Delivery Desktop Lighthouse Testing](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |


### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| Products Page | ![Products Desktop Lighthouse Testing](documentation/testing/lighthouse/products-desk-lh-val.png) |
| Product Details Page | ![Product Detail Desktop Lighthouse Testing](documentation/testing/lighthouse/product-detail-desk-lh-val.png) |
| Add Product Page | ![Add Product Desktop Lighthouse Testing](documentation/testing/lighthouse/add-product-desk-lh-val.png) |
| Edit Product Page | ![Edit Product Desktop Lighthouse Testing](documentation/testing/lighthouse/edit-product-desk-lh-val.png) |
| Bag Page | ![Bag Desktop Lighthouse Testing](documentation/testing/lighthouse/bag-desk-lh-val.png) |
| Checkout Page | ![Checkout Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-desk-lh-val.png) |
| Checkout Success Page | ![Checkout Success Desktop Lighthouse Testing](documentation/testing/lighthouse/checkout-success-desk-lh-val.png) |
| Profile Page | ![Profile Desktop Lighthouse Testing](documentation/testing/lighthouse/profile-desk-lh-val.png) |
| Contact Us Page | ![Contact Us Desktop Lighthouse Testing](documentation/testing/lighthouse/contact-desk-lh-val.png) |
| Privacy Policy Page| ![Privacy Desktop Lighthouse Testing](documentation/testing/lighthouse/privacy-desk-lh-val.png)  |
| Terms & Conditions Page | ![Terms Desktop Lighthouse Testing](documentation/testing/lighthouse/terms-desk-lh-val.png) |
| Delivery Policy Page | ![Delivery Desktop Lighthouse Testing](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |


---


## Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

| Page | Errors |
| :--- | :--- |
| Home Page | No errors|
| Profile Page |No errors. It is showing 1 low contrast warning, however I am unable to find where it is as the badge for the contract warning is not actually displaying on the page |
| Contact Us Page | No errors |
| Privacy Policy Page| No errors |
| Terms & Conditions Page | No errors |
| Delivery Policy Page | No errors |
| 404 Error Page | No errors |


---


## Manual Testing

### User Stories Testing

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |
| 1 | Site User | view a paginated list of posts | select which post I want to view.  | Given more than one post in the database, these multiple posts are listed. These are organised into columns and rows so that the user can clearly see the blog posts available. [Lg Screen Pagination](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Sm Screen Pagination](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 2 | Site User | click on a post | read the full text. | When a user clicks on a blog post title, they are provided with a detailed view of the post.| [Blog Post Title](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 3 | Site User/Admin | view comments on an individual post | read the conversation thread. | Given one or more user comments they can view them, and click on the comment thread to read the conversation. | [View Comments](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 4 | Site User | register for an account | comment on a post.  | Given an email, a user can register an account, log in & comment on a blog post. | [Account Registration](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Login](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Comment as User](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 5 | Site User | leave comments on a post | be involved in the conversation. | A user can leave a comment for review by admin. Once this is approved by admin, then a user can reply. Given more than one comment, the conversation becomes a thread. | [Comment](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Comment Approved](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Conversation becomes Thread](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 6 | Site User | modify or delete my comment on a post | be involved in the conversation. | Given a logged in user, they can modify or delete their comment. | [Modify Comment](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Delete Comment](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 7 | Site Admin | Create, Read, Update and Delete posts | manage my blog content. | Given a loggined in user, they can create, read, update or delete a blog post. | [Create Post](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Read Post](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Update Post](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Delete Post](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 8 | Site Admin/User | create draft posts | finish writing the content later. | Given a logged in user, they can save a draft blog post & finish the content at a later time. | [Blog Post Draft](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 9 | Site Admin | approve or disapprove of comments | filter out an objectionable comments. | Given a logged in site admin, they can approve or disapprove a comment for publication. | [Approve Comment](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Disapprove Comment](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 10 | Site User | click on the About link | I can read more about the site. | Users are able to access the About page (visible from the navigation) when the link is clicked. | [About Page](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 11 | Site Admin | create or update the About page content | it is available on the site. | The About app is visible in the admin panel & edits can be made to the About section with ease. | [About Admin Panel](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Edit About Content](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 12 | Site Admin/User | see timestamps | I know all entries are current. | All updates to the About page are timestamped. | [About Timestamp](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 13 | Site User | easily understand what the blog is about | navigate the website with ease. | The website uses clear and descriptive titles; intuitive navigation; clean, readable font; consistent structure; unclutter imagery that reflects the topic; high contrast between backgrounds and text. | [Clear & Descriptive Titles](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Intuitive Navigation](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [clean & Readable Font](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Consistent Structure](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [Uncluttered Imagery](documentation/testing/user-stories/NAME_OF_IMG.png) <br> [high Contrast](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 14 | Potential collaborator | fill in a contact form | submit a request for collaboration. | The site owner can be contacted when someone wishes to collaborate. | [Contact Form](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 15 | Site Owner | store collaboration requests in the database | review them. | All collaboration requests submitted are stores in the database where they can be reviewed. | [Store & Review Collaboration Requests](documentation/testing/user-stories/NAME_OF_IMG.png) |
| 16 | Site Owner | mark collaboration requests as "read" | see how many I still need to process. | The site owner can see the progress made on collaboration requests at a glance, and can manage the processing of these requests. | [Collaboration Requests "Read"](documentation/testing/user-stories/NAME_OF_IMG.png) |


### Features Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **NAVBAR** |
| Search Bar | Search with no search term entered will display a toast error message letting the user know they haven't entered any search criteria and to try again | Clicked search button with no search term | Error toast displayed | Pass |
| | Search with search terms entered will display the results of that search on the products page. In the top left corner the user will be told how many products matched along with search term entered | Searched for soft | Products page loads up with results of search. Top left tells me there were 16 products found for "soft"| Pass |
| Account Icon | User not logged in - 2 options should be presented to a user if they are not logged in, one to register and one to login | Clicked account icon when not logged in | Dropdown menu with login and register presented | Pass |
| | User Logged in - When a user is logged in they should be shown a dropdown menu dependant on their privileges - standard users are shown the profile and logout links. Superusers are shown product management, profile and logout links. | Viewed links as a superuser and as a standard user | The correct links are displayed dependant on the users privileges | Pass |
| | Account icon links should take the user to the expected page - eg the profile link should take the user to their profile | Clicked on links | Each link takes the user to the correct page for the link | Pass |
| Bag icon | When items are added to the bag, the value underneath the bag should automatically update (this will include the delivery charge if the free delivery limit has not been reached) | Add items to cart to check the value is added | The value adds the correct amount for each product added, and includes the delivery fee if the free delivery limit has not been reached | Pass |
| | Clicking on the bag icon takes the user to their bag page which will display what they have in their bag (if any) or a message to let them know their bag is empty | Clicked on the bag icon with an empty bag and with items | Taken to the bag page, which displays items (if any in bag) or a message if no items | Pass |
| Categories Navbar | Home link - this loads the home page if clicked | Clicked home | Taken to home page | Pass |
| | All products - this allows the user to select how they would like to display all the products, either by rating, price, category or show all products. All links in the dropdown menu should take you to the correct page | Tested each of the links to ensure products display correctly, and that the sorting dropdown displays the choice selected | Links work as expected and the sort dropdown displays how results are being sorted | Pass |
| | Categories links when clicked display a dropdown menu of the products within that category. Each link should direct you to the correct page  | Clicked each of the links to ensure taken to the correct page | Taken to the correct page  | Pass |
| Navbar Responsiveness | Navbar should be displayed using a hamburger menu toggle on smaller screens | Checked the site on smaller screens | Navbar is displayed using a hamburger menu toggle | Pass |
||||||
| **FOOTER** |
| About Section | The links in the about section should open the correct page when clicked | Clicked each link | Taken to the correct page | Pass |
| Contact Section | Clicking on Contact Us Form should take the user to the contact form | Clicked link | Taken to the contact form | Pass |
|| Social Media Icons open the social page in a new browser tab | Clicked each icon | Social page opened in a new browser tab | Pass |
| Kera Cudmore Link | Takes the user to my Github Profile in a new browser tab | Clicked link | Github profile opened in a new tab | Pass |
| Footer Responsiveness | The footer sections should become stacked on smaller screens | Looked at site on smaller screens | Sections of footer became stacked | Pass |
||||||
| **HOME PAGE** |||||
| Category Cards | Clicking on a card should take the user to the products page for that category | Clicked cards and checked the right category loads | The correct categories are displayed for the right cards | Pass |
||||||
| **PRODUCTS PAGE** ||||||
| Sort By dropdown | Products are sorted correctly depending on which option is chosen | Chose the different options and check to see the products are displayed by that criteria | Products are displayed according to the chosen criteria | Pass |
| Product details | Clicking on a product image will load the products detail page | Clicked on a product image | The product detail page loads for that product | Pass |
| Back to top button | Clicking on the back to top button will return the user to the top of the page to enable them to easily use the sites navigation | Clicked the back to top button while partway down the all products page | Returned to the top of the page | Pass |
| Category Tag underneath product | Clicking on the category tag will load the products page for that category | Clicked a product tag on the all products page | The products page reloads showing only the category of the tag clicked | Pass |
||||||
| **PRODUCT DETAIL PAGE** |||||
| Hover over image | When hovering over an image, you should be able to see the magnify lens to see a more details view of the product. | hovered over the image | Magnify lens appears showing a more detailed view of the product | Pass |
| Click on image | When you click on an image, a new tab should open displaying the image| Clicked on the product image | A new browser tab opened with the image | Pass |
| Quantity Plus Button | When you click the plus button the quantity should increase by one until you reach the stock level for the product. Once you reach the stock level, the button becomes disabled. If you lower the quantity, the plus button will reenable. | Clicked on the plus button to the stock level | Clicking on the plus button increments the quantity by 1, and once you reach the stock level the button is disabled. Lowering the quantity reenabled the plus button. | Pass |
| Quantity Minus Button | The minus button will be disabled at 1, if the quantity is more than one, the minus button will be enabled. The minus button should decrement the quantity by one | Added product, then used the minus button to lower the quantity |The button is disabled when the product quantity is 1. The quantity is decreased by 1 each time you click. | Pass |
| Quantity input | If a user manually enters a value larger than the stock level and tries to add the product to their bag, they will be presented with a tooltip that lets them know the value must be equal to or less than the stock level | Add 200 to quantity input for a product with stock level of 44 and click add to bag. | A tooltip pops up with a message letting me know that the value must be equal or less than 44. | Pass |
| Add to bag button | When clicked the quantity of the item will be added to the bag. A success toast message will display letting the user know the quantity of the product added to the bag. | Incremented quantity to 4 and clicked add to bag button | A toast displays to let the user know that they have added 4 of the product to their bag and shows the image of the item with the title and quantity in the bag | Pass |
| Back button | When clicked the user will be taken back to the products page | Clicked the back button | Taken to the products page | Pass |
||||||
| **BAG** |||||
| Quantity Plus Button | When you click the plus button the quantity should increase by one until you reach the stock level for the product. Once you reach the stock level, the button becomes disabled. If you lower the quantity, the plus button will reenable. | Clicked on the plus button to the stock level | Clicking on the plus button increments the quantity by 1, and once you reach the stock level the button is disabled. Lowering the quantity reenabled the plus button. | Pass |
| Quantity Minus Button | The minus button will be disabled at 1, if the quantity is more than one, the minus button will be enabled. The minus button should decrement the quantity by one | Added product, then used the minus button to lower the quantity |The button is disabled when the product quantity is 1. The quantity is decreased by 1 each time you click. | Pass |
| Quantity input | If a user manually enters a value larger than the stock level and tries to update their bag, they will be presented with an error toast that lets them know the stock level for the product and asks them to adjust the quantity and try again. | Add 200 to quantity input for a product with stock level of 44 and click update. | An error toast displays with a message letting me know that the stock level of the product is 44 and to edit my quantity and try again. | Pass |
| Update Link | When a products quantity has been updated and the link clicked, a success toast displays to let the user know the update was successful along with the product and the quantity. If the user tries to update a product over the stock level they are shown an error toast. | Updated a products quantity within the stock level. Updated a products quantity over the stock level | Within the stock level, a success toast is shown with the product information and quantities. Over the stock level an error toast is displayed informing the user of the stock level and asking them to try again | Pass |
| Remove Link | When clicked the product will be removed from the basket and a success toast displayed to let the user know the action was successful, along with letting them know which product they have removed and the shopping bag page updates | Remove product from bag by clicking remove link | Clicked the remove link and a success toast is shown letting me know what product has been removed from the bag | Pass |
| Back to shop button | When clicked this will take the user to the products page | Clicked back to shop button in an empty bag and in a bag with products | Taken back to the products page each time. | Pass |
| Special Offers Button in empty bag | Clicking the button takes the user to the products page displaying all the products in the special offers categories | Clicked button | Taken to the special offers categories products page | Pass |
| Secure Checkout Button | When clicked the user is taken to the checkout page to fill in their details and make payment | Clicked button | Taken to checkout | Pass|
| Go to secure checkout button on success toast | A toast will be displayed each time a user adds an item to their bag which lets them know the product and quantity along with the total excluding delivery and if they haven't reached the free delivery threshold, they will be informed of how much more they need to spend to qualify. They are also shown a go to secure checkout button that allows them to navigate to the bag to confirm their items before checking out | Add product to bag, click the checkout button | The toast displays the item added to the bag, and any previous items added, together with the quantity, total excluding delivery and the spend to get free delivery message as I haven't reached the threshold. Clicking the button takes me to the bag to review my order | Pass |
||||||
| **CHECKOUT PAGE** |||||
| Form Validation | The user is informed if they have not filled in required information | Submitted the form with required fields left blank | A tooltip informs the user that they need to fill in the required fields. | Pass |
| Save delivery information checkbox | When clicked, the current delivery information in the form is saved to the profile | Filled out form and checked the profile after checkout | Profile information was populated with the correct information | Pass |
| Login link on checkout page | Users are given the option to log into their account during checkout, which will allow them to save their order to their profile. If clicked the user is taken to the log in page, once logged in they can navigate to their basket to continue checkout | Not logged in as a user. Clicked the log in link, logged in | Logged in successfully and received a success toast, redirected to the home page and products are still saved in basket | Pass |
| Register Link on checkout page | Users are given the option to register for an account to be able to save their order details before checking out | Click the link, create an account | Redirected to home page and bag available | Pass |
| Payment information section | If the user has entered incorrect information in the payment section, they are given feedback about the error| Entered an invalid card number in the payment section | Information is displayed in red text below the payment information section informing the user that the number they have entered is invalid | Pass |
| Complete order button | Once the user has clicked the complete order button they should be shown a loading status overlay to let the user know their payment is processing. Once checkout has been completed they are then redirected to the checkout success page which gives a breakdown of the order | Clicked button | A loading overlay displays and then the checkout success page is displayed | Pass |
||||||
| **CHECKOUT SUCCESS PAGE** |||||
| View our latest deals button | When clicked the user is taken to the product page showing the deals category | Clicked the button | Taken to the products page showing products in the deals category | Pass |
| Order Confirmation Email | Upon successful checkout the user should also receive an email confirming their order at the email address provided during checkout | Made a successful purchase through the site | An email confirmation was received (this can sometimes go to junk) | Pass |
||||||
| **PROFILE PAGE** |||||
| Update default delivery information | Once the user has filled in the default delivery information they wish to store and clicked the update button, the information should be saved and be available in their profile and at checkout | Add default delivery information, save and then check the information displays in their profile and at checkout | Page reloads with the updated information pre-populated and a success toast is displayed to let the user know their profile was updated successfully | Pass |
| View previous orders made from my account | Users should be able to click on the first part of their order number in the order history section and be taken to the checkout success page for that order. A toast will also inform the user that they are viewing a previous order summary for the order number | Clicked on an order number | The checkout success page is displayed with the order summary and an alert toast is displayed letting the user know this is a past confirmation for the order number | Pass |
||||||
| **CONTACT US FORM** |||||
| Form Validation | If the user doesn't fill in the required fields and tries to submit the form, they will be shown a tooltip letting them know they need to fill in the required fields | Submit the form without filling in the required fields | Tooltip lets me know which fields I need to fill in | Pass |
| Send contact form | Once sent the user should be shown the contact page with a message thanking them for their enquiry and giving them a button to view the latest deals. A toast should also be displayed letting them know their enquiry was sent successfully | Fill in the contact form and clicked send. | Contact us page displays with thank you message and toast displayed letting me know enquiry was sent successfully. | Pass |
| **SUPERUSER OPTIONS**|||||
| Account icon Product management dropdown link | This links should only be displayed to a superuser. When clicked, the superuser will be taken to the add product page. If a regular user tries to manually view this page by using the url, they are not able to view the page and an error toast displays to let them know only administrators can perform that task. | Signed in as superuser and clicked the link. Signed in as a regular user and added the url into the address bar. | Link only shown to superuser. Superusers are taken to the add product page. Regular users are shown an error toast that informs them only administrators can perform that action. | Pass |
| Add Product Form Validation | The form will only be submitted and the new product created if the required fields have been filled in | Tried to submit the form without filling in all required fields | Tooltips let me know which fields need to still be filled in | Pass |
| New product created saved in the products section of the admin page | When a product is created, a record of it should also be displayed in the products section of the admin page | Create a new product, navigate to the admin products section | We can see the record created for the new product | Pass |
| Edit Product Link | This link should only be shown when logged in as a superuser. When the edit link is clicked (either on the products page or from the product detail page) superusers are taken to the edit product page. If a regular user tries to manually access the edit page using the url, they are given an error toast letting them know only administrators can perform that action | Clicked the Edit link as a superuser.  Logged in as regular user and manually enter the url into the address bar. | The edit link is only shown when logged in as a superuser. Superusers are shown the edit product page and regular users are shown an error toast letting them know that only administrators have permission to perform that action. | Pass |
| Delete Product Link | This link should only be shown to superusers. when clicked a superuser should be shown a modal asking them to confirm they would like to delete the product, and reminds them that this action cannot be undone. If a regular user tries to manually access this page using the url, they should be shown an error toast telling them they cannot perform the action. | Clicked the link as a superuser. Manually accessed the url as a regular user. | This link is only shown to superusers. The superuser is shown a modal that asks if they are sure they want to delete the product as this action cannot be undone. Regular users are shown an error toast letting them know that only administrators can perform that action | Pass |
| Contact form sent | All contact forms submitted to the site are stored in the contact form section of the admin page. It will display the name, email address, phone number (if filled in) and message, and will also detail the date of the contact along with a replied checkbox to enable the admin to keep track of whether they have responded | Open the admin page and navigate to the contact form section, select a contact email and view the information. | Information is displayed about the users name, email address, phone number (if entered), message sent and the date it was sent along with a checkbox for replied. | Pass |


---


## Responsiveness

The website was tested manually throughout the project development using DevTools to check for responsiveness.

The responsiveness was confirmed with [Responsive Website Design Tester](https://responsivedesignchecker.com/). The following are samples of some of the responsiveness implemented.


  ### Desktop Screens
  ![Desktop Responsiveness](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG)


  ### Tablet Screens
  ![Tablet Responsiveness](testing/responsiveness/tablet_responsiveness.gif)


  ### Mobile Screens
  ![Mobile Responsiveness](testing/responsiveness/mobile_responsiveness.gif)


---


## Broswer Compatibility

The website was tested on three different browsers: Brave, Chrome, & Microsoft Edge. It was compatable across all three.

The following elements were tested manually on each of the browsers:
  - Internal links work correctly, & as expected.
  - External links to socials work on the browsers listed & open a new tab for each corresponding link.
  - The contact form works correctly & displays the necessary response page on execution.


  ### Brave
  ![Brave](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG)


  ### Chrome
  ![Chrome](testing/browser/chrome_browser.gif)


  ### Microsoft Edge
  ![Microsoft Edge](testing/browser/browser_microsoft_edge.gif)


---


## Bugs

### Resolved Bugs 

| # | Bug | Troubleshooting Attempts | How I solved the issue | Evidence |
| --- | --- | --- | --- | --- |
| 1 | About app not loading in server: Server Error (500) | - Ensure all file & directory paths are laid out correctly <br> - Compare steps taken with that of the lesson module <br> - Use diffchecker to compare snippets of code <br> - Delete About app & start process again <br> - Consult Google <br> - Consult tutor support | - Create a new database(db) <br> - Update env.py with new db <br> - Ensure all migrations were applied <br> - Delete old db from db manager <br> - Run command 'python3 manage.py loaddata db.json' in terminal | ![About App](static/testing/bugs/about_app.png)  |


### Unresolved Bugs

There are no known bugs at this time.

| # | Bug | Troubleshooting Attempts | How I solved the issue | Evidence |
| --- | --- | --- | --- | --- |
