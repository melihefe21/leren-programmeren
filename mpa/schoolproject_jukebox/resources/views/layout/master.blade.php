<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    @vite('resources/css/app.css')

    @stack("stylesheet")
</head>
<body>
    <h1></h1>
    <p class="text-7xl text-green-800 text-center text-font-nice"> Products</p>
    @yield("content")
</body>
</html>