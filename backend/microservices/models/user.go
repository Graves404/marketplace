package models

import "time"

type User struct {
	ID        int       `json:"id"`
	Name      string    `json:"name"`
	Surname   string    `json:"surname"`
	Email     string    `json:"email"`
	City      string    `json:"city"`
	CreatedAt time.Time `json:"created_at"`
	Phone     string    `json:"phone"`
	Username  string    `json:"username"`
	HashPass  string    `json:"hash_pass"`
	IsActive  bool      `json:"is_active"`
}
