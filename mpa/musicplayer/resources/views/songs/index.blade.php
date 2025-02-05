@extends('layouts.master')

@section('content')
<div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-6">Songs</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        @foreach ($songs as $song)
        <div class="bg-white rounded-lg shadow p-6">
            <h2 class="text-xl font-semibold mb-2">{{ $song->name }}</h2>
            <p class="text-gray-600">Artist: {{ $song->artist }}</p>
            <p class="text-gray-600">Duration: {{ gmdate("i:s", $song->duration) }}</p>
            <p class="text-gray-600">Genre: {{ $song->genre->name }}</p>
        </div>
        @endforeach
    </div>
</div>
@endsection
