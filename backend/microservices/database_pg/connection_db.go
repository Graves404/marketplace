package database_pg

import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func Conn() *gorm.DB {
	dns := "host=localhost user=postgres password=root dbname=postgres port=5432 sslmode=disable TimeZone=Asia/Shanghai"
	db, err := gorm.Open(postgres.Open(dns), &gorm.Config{})
	if err != nil {
		panic(err)
	}
	return db
}
