package endpoint

import (
	"microservices/models"
	"microservices/repository"
	"microservices/services"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func RegisterationRouter(c *gin.Context) {
	var new_user models.User
	if err := c.ShouldBindJSON(&new_user); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request body"})
		return
	}

	new_user.CreatedAt = time.Now()

	new_user.HashPass = services.CreateUser(&new_user)

	resultChan := make(chan string)

	go func() {
		result := repository.AddNewUser(&new_user)
		resultChan <- result
	}()

	select {
	case result := <-resultChan:
		c.JSON(http.StatusCreated, gin.H{"message": "User registered successfully", "user_id": result})
	case <-time.After(5 * time.Second):
		c.JSON(http.StatusRequestTimeout, gin.H{"error": "Request timed out"})
	}
}

func LoginRouter(C *gin.Context) {

}
