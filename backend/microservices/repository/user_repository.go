package repository

import (
	"microservices/engine"
	"microservices/models"
)

func AddNewUser(user *models.User) string {
	db := engine.Conn()

	result := db.Create(user)

	if result.Error != nil {
		return "Error to server"
	}

	return "User created successfully"
}

func GetUserByID(id int) (*models.User, error) {
	db := engine.Conn()
	user := &models.User{}

	result := db.First(user, id)
	if result.Error != nil {
		return nil, result.Error
	}
	return user, nil
}

func GetUserByEmail(email string) (string, int, error) {
	db := engine.Conn()
	var user models.User
	result := db.Where("email = ?", email).First(&user)
	if result.Error != nil {
		return "", 0, result.Error
	}
	return user.HashPass, user.ID, nil
}
