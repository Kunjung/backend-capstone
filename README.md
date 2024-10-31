## Backend capstone project

### API list implemented as follows


### Homepage

- GET / - loads the homepage with static content

### Menu
- GET /api/menu - returns list of menu items
- POST /api/menu - creates new menu item
- PUT /api/menu/1 - update a single menu item
- DELETE /api/menu/2 - delete a single menu item

### Booking
- GET /api/booking - returns list of booking items
- POST /api/booking - creates new booking item
- PUT /api/booking/1 - update a single booking item
- DELETE /api/booking/2 - delete a single booking item

### Authentication
- POST /api/api-token-auth - returns authentication token after passing username and password in POST request
