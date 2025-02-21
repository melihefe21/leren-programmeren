@extends('master.master')
@section('content')
    <div style="background-image: url('/images/background.jpg');">
        <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Nieuw product toevoegen</h2>
        <form action="/product/store" method="POST" enctype="multipart/form-data" class="space-y-4">
            @csrf

            <div>
                <label for="name" class="block text-gray-700 font-medium">Productnaam</label>
                <input type="text" name="name" id="name" class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500">
                @error("name")
                <span class="text-red-600">{{$message}}</span>
                @enderror
            </div>

            <div>
                <label for="price" class="block text-gray-700 font-medium">Prijs (€)</label>
                <input type="number" name="price" id="price" step=".01" class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500">
                @error("price")
                <span class="text-red-600">{{$message}}</span>
                @enderror
            </div>

            <div>
                <label for="amount" class="block text-gray-700 font-medium">Aantal stuks</label>
                <input type="number" name="amount" id="amount" step=".01" class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500">
                @error("amount")
                <span class="text-red-600">{{$message}}</span>
                @enderror
            </div>

            <div>
                <label for="image" class="block text-gray-700 font-medium">Productafbeelding</label>
                <input type="file" name="image" id="image" class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500">

            </div>

            <div class="text-center">
                <input type="submit" value="Product toevoegen" class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 cursor-pointer">
            </div>
        </form>
    </div>
@endsection
