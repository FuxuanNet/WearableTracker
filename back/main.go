package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	// 打开数据库（如果不存在会自动创建）
	db, err := sql.Open("sqlite3", "./clothes.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// 创建表
	createTableSQL := `
	CREATE TABLE IF NOT EXISTS clothing (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		imagePath TEXT,
		category TEXT,
		thickness TEXT,
		layer TEXT,
		setInfo TEXT,
		styleLevel INTEGER,
		specialAttributes TEXT,
		remarks TEXT
	);
	`
	_, err = db.Exec(createTableSQL)
	if err != nil {
		log.Fatal(err)
	}

	// 插入数据
	insertData(db)

	// 查询数据
	queryClothing(db, "半袖", "薄款", "外层")
}

func insertData(db *sql.DB) {
	insertSQL := `
	INSERT INTO clothing (name, imagePath, category, thickness, layer, setInfo, styleLevel, specialAttributes, remarks)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
	`
	_, err := db.Exec(insertSQL, "黄灰色长袖", "/images/黄灰色长袖.jpg", "长袖", "薄款", "中层", "不是套装", 3, "无", "无")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("数据插入成功")
}

func queryClothing(db *sql.DB, category, thickness, layer string) {
	querySQL := `
	SELECT id, name, imagePath, category, thickness, layer, setInfo, styleLevel, specialAttributes, remarks
	FROM clothing
	WHERE category LIKE ? AND thickness LIKE ? AND layer LIKE ?;
	`

	rows, err := db.Query(querySQL, "%"+category+"%", "%"+thickness+"%", "%"+layer+"%")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var name, imagePath, category, thickness, layer, setInfo, specialAttributes, remarks string
		var styleLevel int

		err := rows.Scan(&id, &name, &imagePath, &category, &thickness, &layer, &setInfo, &styleLevel, &specialAttributes, &remarks)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("ID: %d, Name: %s, ImagePath: %s, Category: %s, Thickness: %s, Layer: %s, SetInfo: %s, StyleLevel: %d, SpecialAttributes: %s, Remarks: %s\n",
			id, name, imagePath, category, thickness, layer, setInfo, styleLevel, specialAttributes, remarks)
	}
}
