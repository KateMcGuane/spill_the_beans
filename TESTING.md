# Spill The Beans - Testing

Visit the deployed site: [Spill The Beans](//ENTER_DEPLOYED_SITE_HERE)

---

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