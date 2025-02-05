<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>product_create</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<form action="/product/store" method="POST">
    @csrf
    <label for="name">name</label>
    <input type="text"name="name">

    <label for="price">prijs van het product</label>
    <input type="number"name="price">

    <label for="amount">hoeveel stukken</label>
    <input type="number"name="amount">
    <input type="submit">
</form>

</body>


