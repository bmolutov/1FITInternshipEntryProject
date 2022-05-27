# 1FIT Internship Entry Project

### Used technologies:
   * Django 
   * Django REST Framework
   * DRF Spectacular
   * DRF Token Authentication

APIs implemented by DRF.

### Entities
   * CustomUser(AbstractUser)
      * [default fields]
      * date of birth
   * Company
      * name
      * type
      * logo
      * owner
      * founding date
      * date of last change
   * Review
      * rating
      * content
      * date
      * author
      * company

### Logic
1. Clients can register by entering __username__, __password__, __email__ and __birth date__.
2. After successful registration, the user will be given __token__.
3. Authenticated user can:
   * see info of companies
   * see detail info of specific company
   * leave a review
   * see list of reviews related to specific company
   * see left reviews
4. Entrepreneurs and companies are created in __admin panel__.
   * admin panel <code>http://localhost:8000/admin/</code>
5. Superusers or admins can edit any reviews.
6. Users can see list of companies in sorted order, the order depends on average rating of companies.
7. After sending review by user, owner of the company will be provided message.

## Launch 
   * Go to __back/entryProject__ directory.
   * Open terminal and run 
    on Windows <code>py manage.py runserver</code>
    on Unix <code>python3 manage.py runserver</code>

## Actions related to the user
### Login
   Just logging in into the system.
   You will be given token for auth.
   Simply, enter your __username__ and __password__.
   * Send POST request, <code>http://localhost:8000/api/login/</code>

### Getting the current user info
   If you are logged in you will be given basic info.
   Don't forget to provide you token.
   * Send GET request, <code>http://localhost:8000/api/user/</code>

### Registration
   Just registration by your credentials.
   Provide your __username__, __password__, __email__ and __date of birth__.
   Date of birth should be in the following format: __YYYY-MM-DD__.
   * Send POST request, <code>http://localhost:8000/api/register/</code>

### Logging out
   It will delete you token and log out.
   * Send GET request, <code>http://localhost:8000/api/logout/</code>

## Actions related to Company model
### List of companies
   Getting list of all companies.
   * Send GET request, <code>http://localhost:8000/api/companies/</code> 

### Filtering
   Getting list of companies filtered by __type__.
   * Send GET request, <code>http://localhost:8000/api/filtered/[type]/</code>

### Company details
   Getting detailed info of a company.
   Just choose __id__ firstly.
   * Send GET request, <code>http://localhost:8000/api/companies/[id]/</code>

## Actions related to Review model
### Leaving a review
   Just leaving a review.
   Provide your: __rating__, __review content__, __your id__ and __company id__.
   * Send POST request, <code>http://localhost:8000/api/review/</code>

### Reviews of the company
   Getting all reviews related to this company.
   Provide __id__ of the company.
   * Send GET request, <code>http://localhost:8000/api/review/companies/[id]/</code>

### Reviews filtering
   Getting filtered views related to the company.
   Provide __id__ and __rating__.
   * Send GET request, <code>http://localhost:8000/api/review/companies/[id]/[rating]/</code>

## Extra
### Review editing
   Superusers or admins can edit any reviews.
   Just providing __id__ (pk).
   * Send PUT request, <code>http://localhost:8000/api/review/edit/[pk]/</code>

### Listing companies in sorted order
   Getting companies in specific order, order depends on 
   average of rating: the higher the company's average rating, the higher it will
   appear in the list.
   * Send GET request, <code>http://localhost:8000/api/companies/sorted/</code>

## Auto-documentation
   For this purpose, __drf-spectacular__ is used.
   Getting file:
   * Send GET request, <code>http://localhost:8000/api/schema/</code>
   
   Optional UI:
   * Send GET request, <code>http://localhost:8000/api/schema/swagger-ui/</code>
   * Send GET request, <code>http://localhost:8000/api/schema/redoc/</code>
