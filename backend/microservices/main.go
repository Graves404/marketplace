package main

import (
	"microservices/database_pg"
	"microservices/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/get_user/:id", func(c *gin.Context) {
		id := c.Param("id")
		db := database_pg.Conn()

		var user models.User
		result := db.First(&user, id)
		if result.Error != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": "user not found"})
			return
		}

		c.JSON(http.StatusOK, user)
	})

	router.Run(":9090")
}
