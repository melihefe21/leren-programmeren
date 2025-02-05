<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>products-page</title>
    <link rel="stylesheet" href="{{ asset('css/product.css') }}">
</head>
<body>

<h1>hier zijn alle producten</h1>
@foreach($products as $product)
    @if($product->name != "fanta")
        <p>{{$product->name}}</p>
    @endif

@endforeach
<header>
    <nav>
        <ul>
            <li><a href="http://localhost:8000/welcome" class="">welcome</a></li>
        </ul>
    </nav>
</header>


</body>

</html>
