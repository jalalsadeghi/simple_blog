# Simple blog
 
## Models

### Blog article:
   - Contains title, slug (prepopulated from title), content, author (FK to user), publication datetime, and switch to make it online/offline.
   - This model is added to the admin with the possibility to edit all fields.
   - The slug field is prepopulated from the title field. This means that when a new article is created, the slug will be automatically generated based on the title.
   - The publication datetime field is a DateTimeField that stores the date and time when the article was published.
   - The switch field is a BooleanField that determines whether the article is online or offline.

### Contact request:
   - Contains email, name, content, and date.
   - This model is added to the admin without the possibility to add or edit.
   - Only removal of contact requests is possible.

## Admin

### Article model:
   - Registered to admin with the possibility to edit all fields.
   - This means that users can create, update, and delete articles from the admin interface.

### Contact request model:
   - Added to admin without the possibility to add or edit.
   - Only removal of contact requests is possible.
   - This means that users can only delete contact requests from the admin interface.

## Views

### Article list view:
   - Displays 5 entries on one page with a link to a detail view.
   - Pagination links are located at the bottom of the list.
   - This means that users can browse through a large number of articles by clicking on the pagination links.

### Article detail view:
   - Contains slug and id in the URL.
   - Displays article details (title, content, full name of the author, publication datetime).
   - Link to articles list.
   - This means that users can view each article in detail and then navigate back to the list of articles.

### Contact view:
   - Displays a form with email, name, and content.
   - After pressing the "send" button, it stores the entry in the database and sends an email to '' with content, name, and add email address as "Reply-to".
   - This means that users can send contact requests to the website administrator.

## project setup

1- create your env
```
cd simple_blog/src
cp .env.example .env
cd ..
```

2- spin off docker compose
```
docker-compose -f docker-compose.yml up
```


