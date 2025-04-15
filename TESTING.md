# Spill The Beans - Testing

Visit the deployed site: [Spill The Beans](https://spill-the-beans-coffee-blog-8f04f8c6207f.herokuapp.com/)

---

## Validation Testing

<details><summary>Result Key</summary>
| Key | Status |
| :---: | :---: |
| :heavy_check_mark: | Pass |
| :x: | Fail |
| Minor Error | :grey_exclamation: |
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
| **BAG** |
| bag/apps.py | Pass | [apps.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| bag/contexts.py | Pass | [contexts.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| bag/urls.py | Pass | [urls.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| bag/views.py | Pass | [views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| bag/templatetags/bag_tools.py | Pass | [bag_tools.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| bag/test_views.py | Pass | [test_views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **CHECKOUT** |
| checkout/admin.py | Pass | [admin.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/apps.py | Pass | [apps.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/forms.py | Pass | [forms.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/models.py | Pass | [models.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/signals.py | Pass | [signals.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/urls.py | Pass | [urls.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/views.py | Pass | [views.py](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/webhook_handler.py | Pass | [webhook_handler.py](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/webhooks.py | Pass| [webhooks.py](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| checkout/test_forms.py | Pass | [test_forms.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG)|
| checkout/test_views.py | Pass | [test_views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **HOME** |
| home/apps.py | Pass | [apps.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| home/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/home-urls-validation.png)|
| home/views.py | Pass | [views.py validation](documentation/testing/validation/python/home-views-validation.png) |
| home/test_views.py | Pass | [test_views.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| **PRODUCTS** |
| products/admin.py | Pass | [admin.py validation](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
| products/apps.py | Pass | [apps.py validation](documentation/testing/validation/python/products-apps-validation.png) |
| products/forms.py | Pass | [forms.py validation](documentation/testing/validation/python/products-forms-validation.png) |
| products/models.py | Pass | [models.py validation](documentation/testing/validation/python/products-models-validation.png) |
| products/urls.py | Pass | [urls.py validation](documentation/testing/validation/python/products-urls-validation.png) |
| products/views.py | Pass | [views.py validation](documentation/testing/validation/python/products-views-validation.png) |
| products/widgets.py | Pass | [widgets.py validation](documentation/testing/validation/python/products-widgets-validation.png) |
| products/test_models.py | Pass | [test_models.py validation](documentation/testing/validation/python/products-test-models.png) |
| products/test_views.py | Pass | [test_views.py](ENTER_DOCUMENTATION_FILEPATH_HERE.PNG) |
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


## Responsive Testing

## Broswer Compatibility Testing

## Bugs Resolved & Unresolved

| # | Bug | Troubleshooting Attempts | How I solved the issue | Screenshots |
| --- | --- | --- | --- | --- |
| 1 | About app not loading in server: Server Error (500) | - Ensure all file & directory paths are laid out correctly <br> - Compare steps taken with that of the lesson module <br> - Use diffchecker to compare snippets of code <br> - Delete About app & start process again <br> - Consult Google <br> - Consult tutor support | - Create a new database(db) <br> - Update env.py with new db <br> - Ensure all migrations were applied <br> - Delete old db from db manager <br> - Run command 'python3 manage.py loaddata db.json' in terminal | ![About App](static/testing/bugs/about_app.png)  |

## Lighthouse Testing Outcomes

## Code Validation

## User Stories Testing


## Features Testing