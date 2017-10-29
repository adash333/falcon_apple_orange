<!-- original code from https://www.sejuku.net/blog/26754 and others -->

<?php

$url = "http://localhost:8000/debug";

//cURLセッションを初期化する
$ch = curl_init();

//送信データを指定
$cfile = new CURLFile($_FILES["file"]["tmp_name"],'image/jpeg','test_name');
$data = array('file' => $cfile);

$header = [
    'Content-Type: multipart/form-data'
];

//URLとオプションを指定する
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, $header); // リクエストにヘッダーを含める
curl_setopt($ch, CURLOPT_SAFE_UPLOAD, true);

//URLの情報を取得する
$res =  curl_exec($ch);

//結果を表示する
var_dump($res);

//セッションを終了する
curl_close($ch);

?>
