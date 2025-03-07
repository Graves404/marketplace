package models

import "time"

type User struct {
	ID        int       `json:"id"`
	Name      string    `json:"name"`
	Surname   string    `json:"surname"`
	Email     string    `json:"email"`
	City      string    `json:"city"`
	CreatedAt time.Time `json:"-"`
	Phone     string    `json:"phone"`
	Username  string    `json:"username"`
	HashPass  string    `json:"-"`
	IsActive  bool      `json:"is_active"`
}

func (u *User) FixErrorJSON() time.Time {
	return time.Now()
}
