# Plus Resources: Django Project Starter

# She Codes News Project - She Codes News Project

## About This Project
This project is a news website developed by She Codes participants. The website allows users to view and create news stories on various topics. Users can also log in and create an account to access additional features.

## How To Run This Code
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Migrate the database using `python manage.py migrate`.
5. Run the development server with `python manage.py runserver`.

## Database Schema
![Entity Relationship Diagram](./relative_path_to_your_entity_relationship_diagram)

## Project Features
- [x] Order stories by date!
![order by date code 1](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 6.23.12 pm.png>)
![orderby date code 2](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 6.25.54 pm.png>)
- [x] Styled "new story" form!
!![new story form styled](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.06.10 pm.png>)
![new story styled](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.07.23 pm.png>)
- ![Alt text](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.41.09 pm.png>)[x] Story images!
![storyCard.html with story.image link](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.12.51 pm.png>)
- [x] Log-in/log-out!
![login/logout code](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.17.21 pm.png>)
- [] "Account view" page!
- [] "Create Account" page!
- [] View stories by author!
- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user is logged in!
![nav.html](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.17.21 pm.png>)
- [x] "Create Story" functionality only available when a user is logged in!
![views.py use of loginrequiredmixin](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.41.09 pm.png>)

## Additional Features
- [ ] Add categories to the stories and allow the user to search for stories by category.
  
- [ ] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).
  
- [ ] Add the ability to “favourite” stories and see a page with your favourite stories.
  
- [ ] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated).
  
- [x] Gracefully handle the error where someone tries to create a new story when they are not logged in.
  ![Alt text](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 7.41.09 pm.png>)

  ![Alt text](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 8.32.42 pm.png>)
  ![Alt text](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 8.33.02 pm.png>)
  ![Alt text](<she_codes_news/news/static/news/images/Screen Shot 2023-07-23 at 8.33.22 pm.png>)