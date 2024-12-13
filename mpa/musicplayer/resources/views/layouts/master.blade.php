<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Welcome')</title>
    <link rel="stylesheet" href="{{ asset('css/app.css') }}"> <!-- Main CSS -->
    @stack('styles') <!-- Additional page-specific styles -->
</head>
<body>
<header>
    <nav>
        <ul>
            <li><a href="{{ route('songs.index') }}" class="{{ request()->routeIs('songs.index') ? 'active' : '' }}">Home</a></li>
            <li><a href="{{ route('songs.about') }}" class="{{ request()->routeIs('songs.about') ? 'active' : '' }}">About</a></li>
        </ul>
    </nav>
</header>

<main>
    @yield('content')
</main>

<footer>
    <p>&copy; {{ date('Y') }} Music App</p>
</footer>
</body>
</html>

