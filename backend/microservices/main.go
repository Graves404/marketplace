package main

import (
	"microservices/endpoint"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"http://localhost:5173", "http://127.0.0.1:5173"}

	router.Use(cors.New(config))

	user := router.Group("/user")
	{
		user.POST("/registration", endpoint.RegisterationRouter)
		user.POST("/login", endpoint.LoginRouter)
	}

	router.Run(":9090")
}
