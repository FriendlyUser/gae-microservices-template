package main

import (
	"os"
	"github.com/gofiber/fiber/v2"
)

func GetPort(key, fallback string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		return fallback
	}
	return ":" + value
}

// add function to check env vars before running
func main() {
	app := fiber.New()
	port := GetPort("PORT", ":8080")
  app.Get("/", func(c *fiber.Ctx) error {
    return c.SendString("Hello, World!")
  })
	app.Listen(port)
}
