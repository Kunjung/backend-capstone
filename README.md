## Backend capstone project

### API list implemented as follows

1. / -> loads the homepage with static content
2. /api/menu -> returns list of menu items
3. /api/menu/1 -> returns single menu item with the primary key
4. /api/booking -> returns list of bookings
5. /api/booking/1 -> returns single booking with the primary key
6. /api/api-token-auth/ -> returns the authentication token after passing username and password in POST request

### Homepage

- GET / - loads the homepage with static content

### Menu
- GET /api/menu - returns list of menu items
- POST /api/menu - creates new menu item
- PUT /api/menu/<int:pk> - update a single menu item
- DELETE /api/menu/<int:pk> - delete a single menu item

### Booking
- GET /api/booking - returns list of booking items
- POST /api/booking - creates new booking item
- PUT /api/booking/<int:pk> - update a single booking item
- DELETE /api/booking/<int:pk> - delete a single booking item

### Authentication
- POST /api/api-token-auth - returns authentication token after passing username and password in POST request
