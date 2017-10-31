<!-- https://www.sejuku.net/blog/26754 -->

<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>submit</title>
</head>
<body >

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

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

//URLの情報を取得する
$res =  curl_exec($ch);

//結果を表示する
# var_dump(json_decode($res, true));
$array = json_decode($res, true);
print_r($array);

echo "<br />結果：";
echo $array["result"];
echo "<br />確率：";
echo $array["probability"];

//セッションを終了する
curl_close($ch);

?>

</body>
</html>
