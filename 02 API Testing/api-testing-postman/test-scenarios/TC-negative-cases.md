# TC-negative-cases

## Scenarios
1. **Get Invalid Booking**: Request a booking ID that does not exist. Expect `404 Not Found`.
2. **Update without Token**: Try updating a booking without an Auth header/token. Expect `403 Forbidden`.
3. **Create with Invalid Payload**: Send missing required fields in JSON body. Expect `400 Bad Request` or `500`.