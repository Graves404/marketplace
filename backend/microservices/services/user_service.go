package services

import (
	"microservices/models"

	"github.com/alexedwards/argon2id"
)

func hashPassword(password string) string {
	hash_pass, err := argon2id.CreateHash(password, argon2id.DefaultParams)
	if err != nil {
		panic(err)
	}
	return hash_pass
}

func CreateUser(user *models.User) string {
	hashPassword := hashPassword(user.HashPass)

	return hashPassword
}
