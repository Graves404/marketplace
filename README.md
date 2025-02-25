# Marketplace "kupi.mne" Docs

This repository contains descriptions of the "Kupi.mne" marketplace, including its stack and logic.

## What is "Kupi.mne"

This project provides a convenient platform for buying and selling goods, especially for small shops. Users can create 
an account as either a regular user or a store.

## Core Features
### For "User":
1. User registration
2. Email verification
3. Profile updates
4. Account deletion

### For "Products":
1. Adding of Products
2. Updating product information
3. Deleting products
4. Selling products via API and online payment processing
5. Purchasing products using bank cards

## Tech Stack
### Backend
1. FastAPI
2. Pydantic
3. SQLAlchemy
4. RabbitMQ
5. Temporal
6. FireStore (cloud storage)
7. Stripe (for payments)
8. PyTest
9. Reddis

### Frontend
1. React TSX
2. Ant Component
3. Tailwind CSS
4. FireStore
5. Stripe

### DataBase
1. PostgreSQL
2. YDB


### Code
1. 200 - Completed
2. 201 - Created
3. 204 - Deleted
4. 303 - The user not found
5. 400 - Bad Request (Validation error)
6. 401 - The user not authorized
7. 403 - Incorrect password or email
8. 404 - Not found
9. 409 - Conflict (The user or item already existing)
10. 578 - Difference passwords