<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>@yield('title', 'Welcome')</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50">
<header>
    <nav class="bg-gray-500 p-4">
        <ul class="flex justify-center space-x-6">
            <li><a href="/welcome" class="text-white text-lg px-4 py-2 rounded-md hover:bg-gray-600">Welcome</a></li>
            <li><a href="/hello" class="text-white text-lg px-4 py-2 rounded-md hover:bg-gray-600">Products</a></li>
            <li><a href="/product/create" class="text-white text-lg px-4 py-2 rounded-md hover:bg-gray-600">New Product</a></li>
        </ul>
    </nav>
</header>
<main class="container mx-auto p-6">
    @yield('content')
</main>

<footer class="text-center p-4 bg-gray-500 text-white mt-6">
    <p>&copy; {{ date('Y') }} webshop</p>
</footer>
</body>
</html>
