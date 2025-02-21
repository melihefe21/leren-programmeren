@extends('master.master')


@section('content')
    <h1 class="text-2xl font-bold text-center text-gray-800 bg-gray-200 p-4 rounded-md">
        Hier zijn alle producten
    </h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-4 p-4">
        @foreach($products as $product)
            <div class="bg-white p-4 rounded-lg shadow hover:shadow-md transition">
                <h2 class="text-lg font-semibold text-gray-700">{{ $product->name }}</h2>
                <p class="text-gray-600 mt-1">{{ $product->description }}</p>
                <p class="text-green-700 font-medium mt-2">€{{ number_format($product->price, 2) }}</p>
            </div>
        @endforeach
    </div>


@endsection
