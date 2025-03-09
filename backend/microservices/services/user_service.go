package services

import (
	"log"
	"microservices/models"
	"microservices/repository"
	"os"
	"strconv"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/joho/godotenv"
	"github.com/matthewhartstonge/argon2"
)

func hashPassword(password string) (string, error) {
	argon := argon2.DefaultConfig()
	bytes, err := argon.HashEncoded([]byte(password))
	if err != nil {
		return "", err
	}
	hash := string(bytes)
	return hash, nil
}

func createToken(id_user int) (string, error) {
	err := godotenv.Load()

	if err != nil {
		log.Printf("Error in time upload file .env")
	}

	secret_key := os.Getenv("JWT_SECRET_KEY")

	token := jwt.NewWithClaims(jwt.SigningMethodHS256,
		jwt.MapClaims{
			"sub": strconv.Itoa(id_user),
			"exp": time.Now().Add(time.Hour * 24).Unix(),
		})
	tokenResult, err := token.SignedString([]byte(secret_key))
	if err != nil {
		return "", err
	}
	return tokenResult, nil
}

func CreateUser(user *models.User) string {
	hashPassword, err := hashPassword(user.HashPass)
	if err != nil {
		return ""
	}
	return hashPassword
}

func LoginService(auth models.Auth) string {
	var token string
	storedHash, id, err := repository.GetUserByEmail(auth.Email)
	if err != nil {
		log.Printf("Error getting user: %v", err)
		return ""
	}

	match, err := argon2.VerifyEncoded([]byte(auth.HashPass), []byte(storedHash))
	if err != nil {
		log.Printf("Password comparison failed: %v", err)
		return ""
	}

	if match {
		token, _ = createToken(id)
	}

	return token
}
