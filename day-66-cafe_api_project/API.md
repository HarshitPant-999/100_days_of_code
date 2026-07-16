## API Documentation

### GET /random
Returns a random cafe from the database.

### GET /search?loc=<location>
Returns all cafes matching the given location.
- **Query param:** `loc` (string) — the area to search

### POST /get
Adds a new cafe to the database.
- **Body params:** `name`, `map_url`, `img_url`, `location`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`

### PATCH /update-price/<cafe_id>
Updates the coffee price for a specific cafe.
- **Query param:** `new_price`

### DELETE /report-closed/<cafe_id>
Deletes a cafe from the database.
- **Query param:** `api_key` (string) — required for authorization
