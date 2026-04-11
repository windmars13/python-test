<?php
// practice/backend/php/connect.php

// 1. 資料庫設定
$host = 'localhost';     // 通常是 localhost
$db = 'my_practice_db'; // 記得改成你在 MySQL 建立的名稱
$user = 'root';          // XAMPP/MAMP 預設通常是 root
$pass = '';              // XAMPP 預設是空字串，MAMP 可能是 'root'
$charset = 'utf8mb4';    // 建議使用 utf8mb4 支援貼圖或特殊中文字

// 2. 設定 DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// 3. 建立連線選項
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // 錯誤時噴出例外，方便 Debug
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // 取出資料預設用「欄位名稱」關聯陣列
    PDO::ATTR_EMULATE_PREPARES   => false,                  // 關閉模擬以增強安全性
];

try {
    // 嘗試建立連線
    $pdo = new PDO($dsn, $user, $pass, $options);
    // echo "連線成功！"; // 測試用，正式連上後可以註解掉
} catch (\PDOException $e) {
    // 如果連線失敗，噴出錯誤訊息
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
?>
